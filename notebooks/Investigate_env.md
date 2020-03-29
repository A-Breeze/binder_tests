---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Investigate environment
Commands to check that the environment has correctly activated.


## Python executable and package managers

```python
# Import built-in modules
import sys

print(f"Python version running: {sys.version}")
print(f"Runing here: \t\t{sys.executable}")
```

Use *bang* notation (`!`) to run console commands from a Jupyter Notebook

```python
print("Jupyter packages and versions installed:")
!jupyter --version
```

```python
print("Jupyter is running from here:")
!which jupyter-notebook
```

```python
# This is a Git repo that can push to the following remote
!git remote -v
```

```python
# The notebook is running in an environment called "notebook"
# This is *irrespective* of the name given in the environment.yml file
!conda env list
```

```python
# Get a list of all conda packages installed:
# !conda list

# We'll just examine a few in the below
```

```python
import pip

print(f"pip version:\t{pip.__version__}")
print("Running here:")
!which pip
```

```python
import jupytext

print(f"jupytext version:\t{jupytext.__version__}")
print("Running here:")
!which jupytext
```
```python
# Show all warnings when running the notebook
import warnings
warnings.filterwarnings('always')
```

## Loaded packages

```python
# Import other built-in modules
from functools import partial

# Import external modules
import numpy as np
import pandas as pd
from sklearn import __version__ as skl_version
from matplotlib import __version__ as mpl_version
import matplotlib.pyplot as plt
from IPython.display import Image

# Allow imports relative to the project root folder
import pyprojroot
proj_root_dir_path = pyprojroot.here()
if sys.path[0] != str(proj_root_dir_path):
    sys.path.insert(0, str(proj_root_dir_path))

# Import project modules
import config_public as proj_config
from proj_utils import __version__ as pru_version
import proj_utils.io

print(f"numpy version:\t\t{np.__version__}")
print(f"pandas version:\t\t{pd.__version__}")
print(f"sklearn version:\t{skl_version}")
print(f"matplotlib version:\t{mpl_version}")

print(f"Project root folder is here:\t{proj_config.proj_root_dir_path}")
print(f"Project utils package version:\t{pru_version}")
```

### Use `matplotlib`
Simple plot example from here: <https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html>

```python
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()
# plt.show()  # Could use this, but actually save and reload as below

# Save the plot
output_file_location = proj_config.exhibits_dir_path / "test.png"
if proj_utils.io.save_with_check(
    # Using functools.partial to call fig.savefig with arguement dpi=200
    partial(fig.savefig, dpi=200),
    output_file_location):
    print(f"Plot saved here:\t{output_file_location}")
plt.close()  # Do not show the plot produced above
    
# Reload the plot
Image(output_file_location)
```

```python

```
