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

```python
# Import built-in modules
import os
import sys

print(f"Python version running: {sys.version}")
print(f"Runing here: \t\t{sys.executable}")
```

Use *bang* notation (`!`) to run console commands from a Jupyter Notebook

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

```
