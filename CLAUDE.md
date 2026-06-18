# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Educational Python project for discrete-time control systems. The plant studied is a **ball-and-beam** modelled as a double integrator H/s². Two controllers are compared: a discrete PID and a polynomial RST synthesised via a Diophantine equation. Three Jupyter notebooks drive the pedagogy; the Python packages provide the underlying simulation and synthesis infrastructure.

## Running tests

There is no test runner configuration. Tests are plain Python scripts with `if __name__ == '__main__'` guards.

```bash
# Model tests — run from the project root
python Models/tests/test_models.py

# RST synthesis tests — must be run from Utils/ (uses bare `import computeRST`)
cd Utils && python test_computeRST.py
```

To run a single test function, import and call it directly:
```bash
python -c "import sys; sys.path.insert(0,'..'); import computeRST; from test_computeRST import test_compute_denominator_matching_rst_with_integrator; test_compute_denominator_matching_rst_with_integrator()"
```

## Running notebooks

```bash
jupyter notebook
```

Open notebooks in order: `DoubleIntégrateurAnalyse.ipynb` → `CommandeDoubleIntégrateur_PID.ipynb` → `CommandeDoubleIntégrateur_RST.ipynb`. Cells must be executed top-to-bottom; restarting the kernel clears all state.

## Architecture

### Layered dependency flow

```
Notebooks
  └─ Simulation/runners.py          # high-level wiring (hardcoded D=2, sat=±10, t_disturb=3s)
       ├─ Simulation/simulation.py  # TFSimulator · HybridSim · NonLinearHybridSim
       ├─ Control/                  # DiscretePID · RSTController (same interface)
       ├─ Models/BallBeam/          # config + TransferFunctionModel + StateSpace + Nonlinear
       └─ Metrics_Plotting/         # SimLog · Metrics · Plotting
Utils/computeRST.py                 # RST polynomial synthesis (standalone, no circular deps)
Utils/utils.py                      # CSV export · helper builders (Place_real_radius, poles_to_denominator)
```

### Key design contracts

**Config modules** (`Models/BallBeam/ballbeam_config.py`) act as mutable parameter objects — `ballbeam_config.dt` and `ballbeam_config.T` are mutated by notebooks before instantiating simulators. Any new plant needs its own config module exposing `num_cont`, `den_cont`, `dt`, `T`, and the state-space matrices `A_mat`, `B_mat`, `C_mat`, `D_mat`.

**Controller interface** — both `DiscretePID` and `RSTController` expose the same three methods: `reset()`, `setReference(r: float)`, `step(y: float) -> float`. Runner functions depend only on this interface, so a new controller is a drop-in replacement.

**Plant base classes** (`Models/base.py`) — `BaseLinearStateSpaceModel` (no abstract methods, relies on attribute convention) and `BaseNonlinearModel` (abstract `f(X, u)`). `HybridSim` accepts any `BaseLinearStateSpaceModel`; `NonLinearHybridSim` accepts any `BaseNonlinearModel`.

**TFSimulator** is used for *both* the plant (open-loop discrete TF) and internally by `DiscretePID` and `RSTController` for their difference-equation recursion. Its `step()` implements a direct-form II difference equation.

**RST synthesis** (`Utils/computeRST.py`) has two entry points:
- `Compute_Denominator_Matching_RST(A_m, plant_tf, Integrator, A0)` — specify dominant poles only; T = t₀·A₀ enforces unity DC gain.
- `Compute_Desired_RST(Desired_TF, plant_tf, Integrator, A0)` — specify the full desired closed-loop TF; B_cl must be divisible by B.

Both return `(S_tf, R_tf, T_tf, H_cl)`. The `Integrator=True` flag forces `(z−1)` into S, giving exact rejection of constant input disturbances (`S(1) = 0`).

### Hardcoded simulation constants (in `Simulation/runners.py`)

| Constant | Value | Reason |
|---|---|---|
| Disturbance magnitude | 2.0 | Step input disturbance injected at plant input |
| Disturbance onset | t ≥ 3.0 s | First 3 s reserved for reference-tracking transient |
| Saturation limits | ±10 | Approximates physical servo actuator range |
| Plant integration step | 1 ms | 20× finer than 50 Hz controller; keeps RK4 error negligible |

## Dependencies

```
numpy  scipy  matplotlib  control  jupyter
```

Install with `pip install numpy scipy matplotlib control jupyter` or from `requirements.txt` (note: `requirements.txt` omits `scipy` and `jupyter` — add them if recreating the environment).
