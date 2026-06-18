"""Quick-look plotting utilities for simulation results.

For publication-quality figures, use the inline plotting code in the notebooks
directly; this module is intended for rapid diagnostic checks during development.
"""

import numpy as np
import matplotlib.pyplot as plt


class Plotting:
    """Utility class for visualising simulation results stored in a SimLog."""

    def __init__(self):
        """Initialises the Plotting instance (no state required)."""
        return

    def plotAll(self, Log, title):
        """Plots the output trajectory and control input from a simulation log.

        Opens two separate Matplotlib figures: plant output y(t) and control input u(t),
        both as functions of time.

        Args:
            Log (SimLog): Populated SimLog instance containing t_hist, y_hist, u_hist.
            title (str): Title string applied to both figures.
        """
        plt.figure()
        plt.plot(Log.t_hist, Log.y_hist)
        plt.grid(True)
        plt.xlabel("time [s]")
        plt.ylabel("position")
        plt.title(title)


        plt.figure()
        plt.plot(Log.t_hist, Log.u_hist)
        plt.grid(True)
        plt.xlabel("time [s]")
        plt.ylabel("control input")
        plt.title(title)

        plt.show()
        
        return
    
    