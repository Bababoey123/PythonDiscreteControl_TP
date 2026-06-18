"""Nonlinear dynamics of the ball-and-beam system.

The state is X = [[r], [ṙ]] where r is the ball position [m] and ṙ its velocity [m/s].
The control input u is the servo beam angle [rad]. The nonlinear ODE is:

    ṙ = ṙ
    r̈ = −m·g·sin(α) / (J/R² + m),   α = (d/L)·u
"""

import numpy as np

from Models.base import BaseNonlinearModel


class NonlinearBallBeamModel(BaseNonlinearModel):
    """Nonlinear model of the ball-and-beam plant.

    Implements the exact (non-linearised) equations of motion using sin(α) instead
    of the small-angle approximation sin(α) ≈ α used by the linear models.
    For small inputs the nonlinear and linear responses are nearly identical;
    differences become visible when ``abs(u) > ~0.1 rad``.
    """

    def __init__(self, config_file):
        """Stores all physical parameters from the configuration module.

        Args:
            config_file: Plant configuration module exposing m, g, J, R, d, L.
        """
        self.m = config_file.m
        self.g = config_file.g
        self.J = config_file.J
        self.R = config_file.R
        self.d = config_file.d
        self.L = config_file.L
        self.config_file = config_file

        # Output matrix: y = C @ X extracts ball position
        self.C = np.array([[1.0, 0.0]])

    def f(self, X: np.ndarray, u: float) -> np.ndarray:
        """Evaluates the nonlinear state derivative Ẋ = f(X, u).

        Args:
            X (np.ndarray): State vector [[r], [ṙ]], shape (2, 1).
                r  — ball position along the beam [m].
                ṙ  — ball velocity [m/s].
            u (float): Servo beam angle [rad].

        Returns:
            np.ndarray: State derivative [[ṙ], [r̈]], shape (2, 1).
        """
        r_dot = X[1, 0]
        alpha = (self.d / self.L) * u                               # beam tilt angle [rad]
        r_ddot = -self.m * self.g * np.sin(alpha) / (self.J / self.R**2 + self.m)
        return np.array([[r_dot], [r_ddot]])
