---
title: Minimal Boilerplate for Python Packaging
description: The least necessary boilerplate code to build a modern Python package.
layout: post
---
# Is this for you?

- ✅ Written purely in Python
- 🚫 Includes code another language (e.g., C/C++)

# Project structure

```
.
├── mypackage
│   ├── __init__.py
│   └── module.py
└── pyproject.toml
```

- `mypackage`: a folder for your source code. The name should be the same as your package name.
  - `__init__.py`: An empty file.
  - `module.py`: Your package contents where users will call `from mypackage import module`.
- `pyproject.toml`: Describes your package and other metadata. See [next section](#pyprojecttoml).

## `pyproject.toml`

```toml
[project]
name = "mypackage"
version = "0.0.1"
dependencies = ["cowsay>=6.0"]
```

Other metadata like `author` and `license` are available and you can find more [official documentation](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata).