Overview
========

Architecture
------------

The project is organised in independent layers:

.. code-block:: text

   Notebooks
     |-- Simulation/runners.py          <- high-level wiring (D=2, sat=+/-10, t=3s)
          |-- Simulation/simulation.py  <- TFSimulator, HybridSim, NonLinearHybridSim
          |-- Control/                  <- DiscretePID, RSTController
          |-- Models/BallBeam/          <- config, TransferFunctionModel, StateSpace, Nonlinear
          `-- Metrics_Plotting/         <- SimLog, Metrics, Plotting
   Utils/computeRST.py                  <- RST synthesis (no circular dependencies)
   Utils/utils.py                       <- CSV export, utility builders

Plant model
-----------

The **ball-and-beam** system is described by the continuous transfer function:

.. math::

   F(s) = \frac{H}{s^2}, \quad
   H = \frac{m \cdot g \cdot d}{L \cdot (J/R^2 + m)} \approx 0.21 \;\text{m s}^{-2}/\text{rad}

After ZOH discretisation at :math:`T_e = 0.05` s:

.. math::

   F(z) = \frac{0.000263\,(z+1)}{z^2 - 2z + 1}

The two poles at :math:`z = 1` (discrete double integrator) make the system
non-asymptotically stable in open loop.

Common controller interface
----------------------------

Both ``DiscretePID`` and ``RSTController`` share three methods:

* ``reset()`` --- clears the internal state to zero before each simulation run.
* ``setReference(r)`` --- sets the reference setpoint.
* ``step(y) -> float`` --- computes the control command :math:`u[k]` from measurement :math:`y[k]`.

This common interface allows one controller to be substituted for the other in the
runner functions without changing any simulation code.

Hardcoded constants in the runners
------------------------------------

==================== ======= ==================================================
Constant             Value   Role
==================== ======= ==================================================
Disturbance (ampl.)  2.0     Step disturbance injected at the plant input
Disturbance (time)   t >= 3s First 3 s reserved for the reference-tracking transient
Saturation           +/-10   Physical limit of the beam servo actuator
Integration step     1 ms    20x finer than the controller period (50 Hz)
==================== ======= ==================================================

RST synthesis
-------------

Two synthesis functions are available in ``Utils/computeRST.py``:

``Compute_Denominator_Matching_RST(A_m, plant_tf, Integrator, A0)``
   Specify only the dominant poles :math:`A_m`. The polynomial :math:`T = t_0 \cdot A_0`
   enforces unity DC gain and cancels :math:`A_0` from the closed-loop response.

``Compute_Desired_RST(Desired_TF, plant_tf, Integrator, A0)``
   Specify the full desired closed-loop transfer function :math:`B_{cl}/A_m`.
   The numerator :math:`B_{cl}` must be exactly divisible by :math:`B`.

Both functions return ``(S_tf, R_tf, T_tf, H_cl)``.
