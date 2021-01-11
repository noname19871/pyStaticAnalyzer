# pyStaticAnalyzer

![](https://github.com/noname19871/pyStaticAnalyzer/workflows/pyStaticAnalyzer/badge.svg)

Simple static analyzer for small python projects

## System requirements

pyStaticAnalyzer works on Ubuntu, Windows and MacOS

## Installation

run `pip install pyStaticAnalyzer` to install last version

## Documentation

### pyStaticAnalyzer.walker

#### Class ProjectGraph

Builds graph of some project with respect of its structure.

Arguments:
* **path** — path to the project (string, required).
* **ignored** — set of folders to ignore, venv for example (set of strings, optional, None by default).

Methods:
* **print(indent_count=4)** — prints project structure. Param indent_count defines indents between nesting levels.
* **print_folder(folder_name, indent_count=4)** — prints nested folder structure. Param folder_name defines the path to one of the project folder.

Properties:
* **get_source_codes** — returns dict with sources of project files. Dict keys are paths to files, values — source codes.
* **get_adj_matrix** — returns project graph in format of adjacency matrix.

### pyStaticAnalyzer.kernel

#### Class FolderNode

Represents Node in Kernel structure.

Arguments:
* **name** — name of the node (path to the file, function or class name) (string, required).
* **type** — type of the node (file, class, function) (string, required).
* **ast** — Abstract Syntax Tree related to the node (AST node, required).

Attributes:
* **name** — string name of the node
* **type** — string type of the node
* **ast** — AST node
* **children** — dict with next FolderNodes. Dict keys are names of the next nodes, values — FolderNodes.

#### Class CallNode

Arguments:
* **id** — integer id of the node (integer, required).
* **name** — string name of the function or class (string, required).
* **type** — type of the node (function, class, method) (string, required).
* **imported_from** — source file of the function or class (string, optional, None by default).

Attributes:
* **id** — integer id of the node.
* **name** — string name of the function or class.
* **type** — string (function, class, method).
* **imported_from** — string name of source file of class (possible None).
* **children** — list of children CallNodes.

#### Class FileKernel

Represents Static Analyzer kernel for single File
