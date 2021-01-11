# pyStaticAnalyzer

![](https://github.com/noname19871/pyStaticAnalyzer/workflows/pyStaticAnalyzer/badge.svg)

Simple static analyzer for small python projects

## System requirements

pyStaticAnalyzer works on Ubuntu, Windows and MacOS

## Installation

run `pip install pyStaticAnalyzer` to install last version

## Documentation

### pyStaticAnalyzer.walker

#### ProjectGraph

Builds graph of some project with respect of its structure.

Arguments:
* **path** — path to the project (string, required)
* **ignored** — set of folders to ignore, venv for example (set of strings, optional, None by default)

Methods:
* **print(indent_count=4)** — prints project structure. Param indent_count defines indents between nesting levels.
* **print_folder(folder_name, indent_count=4)** — prints nested folder structure. Param folder_name defines the path to one of the project folder.

Properties:
* **get_source_codes** — returns dict with sources of project files. Dict keys are paths to files, values — source codes.
* **get_adj_matrix** — returns project graph in format of adjacency matrix.

