import numpy as np
import control as ct

from Models.base import BaseLinearStateSpaceModel


class LinearStateSpaceModel(BaseLinearStateSpaceModel):
    """Linearised continuous and ZOH-discrete state-space model for a generic plant.

    Populates both the continuous attributes (A, B, C, D) defined by
    ``BaseLinearStateSpaceModel`` and the discrete attributes (Ad, Bd, Cd, Dd)
    obtained by ZOH sampling at ``config_file.dt``.

    The config must expose:
        ``A_mat``, ``B_mat``, ``C_mat``, ``D_mat`` — continuous system matrices
        ``dt`` — sampling period [s]
    """

    def __init__(self, config_file):
        """Builds continuous and ZOH-discrete state-space matrices from a config module.

        Args:
            config_file: Plant configuration module exposing ``A_mat``, ``B_mat``,
                ``C_mat``, ``D_mat``, and ``dt``.
        """
        self.A = np.array(config_file.A_mat, dtype=float)
        self.B = np.array(config_file.B_mat, dtype=float)
        self.C = np.array(config_file.C_mat, dtype=float)
        self.D = np.array(config_file.D_mat, dtype=float)

        ss_cont = ct.StateSpace(self.A, self.B, self.C, self.D)
        ss_disc = ss_cont.sample(config_file.dt, 'zoh')

        self.Ad = np.array(ss_disc.A)
        self.Bd = np.array(ss_disc.B)
        self.Cd = np.array(ss_disc.C)
        self.Dd = np.array(ss_disc.D)
