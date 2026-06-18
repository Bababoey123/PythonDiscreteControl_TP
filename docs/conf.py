"""Sphinx configuration for PythonDiscreteControl_TP."""

import sys
import os

# Make the project root importable so autodoc can find the packages.
sys.path.insert(0, os.path.abspath('..'))

# ---------------------------------------------------------------------------
# Project metadata
# ---------------------------------------------------------------------------
project = 'PythonDiscreteControl_TP'
author = 'Adam Caulier'
release = '1.0'
language = 'en'

# ---------------------------------------------------------------------------
# Extensions
# ---------------------------------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',    # Google-style and NumPy-style docstrings
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
]

autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'show-inheritance': True,
    'member-order': 'bysource',
}

napoleon_google_docstring = True
napoleon_numpy_docstring = False

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable', None),
}

# ---------------------------------------------------------------------------
# HTML output
# ---------------------------------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = []

# ---------------------------------------------------------------------------
# Rinoh (PDF) output
# ---------------------------------------------------------------------------
rinoh_documents = [
    {
        'doc': 'index',
        'target': 'PythonDiscreteControl_TP',
        'title': 'PythonDiscreteControl — Documentation',
        'author': author,
        'template': 'article',
    }
]
