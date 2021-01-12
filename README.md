# pyStaticAnalyzer

![](https://github.com/noname19871/pyStaticAnalyzer/workflows/pyStaticAnalyzer/badge.svg)

Simple static analyzer for small python projects

## System requirements

pyStaticAnalyzer works on Ubuntu, Windows and MacOS

Compatible with Python 3.6+

## Installation

run `pip install pyStaticAnalyzer` to install last version

## Examples

Run test_ubuntu.py (for Linux and MacOS) or test_windows.py (for Windows) to play with minimal working example.

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

Represents Node in Call Graph structure.

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

Represents Static Analyzer kernel for single file.

Arguments:
* **path** — path to the file (string, required).

Properties:
* **get_path** — returns string path to the analyzed file.
* **get_all_tree** — returns dict with kernel structure. Keys represent names of files/functions/classes, values — FolderNodes.
* **get_source_codes** — returns dict with sources of project files. Dict keys are paths to files, values — source codes.
* **get_structure** — returns project graph in format of adjacency matrix. (This property duplicates behavior of the similar ProjectKernel property and it is not really useful here).

Methods:
* **get_source_code(filename)** — returns source code of the file (in FileKernel it works only for source file).
* **get_file_ast(filename)** — return abstract syntax tree of the file (in Filekernel it also works only for source file).
* **get_file_classes_and_functions(filename)** — returns all classes and function defined in file in format of dict with string keys (functions and classes names) and FolderNode values.
* **find_function_ast(file, name)** — returns abstract syntax tree of function "name" from file with name "file".
* **find_class_ast(file, name)** — returns abstract syntax tree of class "name" from file with name "file".
* **print_file_ast(filename)** — pretty prints abstract syntax tree of the file (in FileKernel it works only for source file).
* **print_all_asts()** — pretty prints abstract syntax trees of all files in the project.
* **print_structure()** — print project structure (in FileKernel — only source file name).
* **build_call_graph()** — returns call graph of given file. Call graph returns as CallNode with type main, which contains children — functions and classes called in the global scope of the file (reptresented by CallNodes). Each of them also contains children and so on. Call graph recognizes imports from other files (and give imported functions type "imported_function"), class initialisation (with type "class), class method calls (with type "method") and common function (with type "function"). At this moment graph construction does not continue in class initializations and imports.
* **print_call_graph(indent_count=4)** — builds and prints call graph. Param indent_count defines indents between nesting levels.

#### Class ProjectKernel

Represents Static Analyzer kernel for python project.

Arguments:
* **path** — path to the file (string, required).
* **ignored** - set of folders to be skipped (set of strings, optional, None by default).

Properties:
* **get_path** — returns string path to the analyzed file.
* **get_all_tree** — returns dict with kernel structure. Keys represent names of files/functions/classes, values — FolderNodes.
* **get_source_codes** — returns dict with sources of project files. Dict keys are paths to files, values — source codes.
* **get_structure** — returns project graph in format of adjacency matrix.

Methods:
* **get_source_code(filename)** — returns source code of the file.
* **get_file_ast(filename)** — return abstract syntax tree of the file.
* **get_file_classes_and_functions(filename)** returns all classes and function defined in file in format of dict with string keys (functions and classes names) and FolderNode values.
* **find_function_ast(file, name)** — returns abstract syntax tree of function "name" from file with name "file".
* **find_class_ast(file, name)** — returns abstract syntax tree of class "name" from file with name "file".
* **print_file_ast(filename)** — pretty prints abstract syntax tree of the file.
* **print_folder_asts(folder)** — pretty prints all files abstract syntax trees from subfolder of the project.
* **print_all_asts()** — pretty prints abstract syntax trees of all files in the project.
* **print_structure(indent_count=4)** — prints project structure. Param indent_count defines indents between nesting levels.
* **print_folder(folder_name, indent_count=4)** — prints subfolder structure. Param indent_count defines indents between nesting levels.
* **build_call_graph()** — returns call graph of given file. Call graph returns as CallNode with type main, which contains children — functions and classes called in the global scope of the file (reptresented by CallNodes). Each of them also contains children and so on. Call graph recognizes imports from other files (and give imported functions type "imported_function"), class initialisation (with type "class), class method calls (with type "method") and common function (with type "function"). At this moment graph construction does not continue in class initializations and imports.
* **print_call_graph(indent_count=4)** — builds and prints call graph. Param indent_count defines indents between nesting levels.

#### Function print_ast

Pretty prints given abstract syntax tree.

Arguments:
* **ast** — abstract syntax tree

#### Function get_class_methods

Returns all class methods in format of dict with string keys — methods names and corresponding FolderNode values.

Arguments:
* **class_node** — FolderNode of the class.

#### Function get_nested_classes

Returns all nested classes from class in format of dict with string keys — classes names and corresponding FolderNode values.

Arguments:
* **class_node** — FolderNode of the class.

#### Function get_nested_functions

Returns all nested functions from function in format of dict with string keys — function names and corresponding FolderNode values.

Arguments:
* **func_node** — FolderNode of the function.

#### Function get_classes_from_function

Returns all classes from function in format of dict with string keys — classes names and corresponding FolderNode values.

Arguments:
* **func_node** — FolderNode of the function.

#### Function find_imports

returns names of imported modules and functions import from it in format of dict with string keys — function names and string values — modules names.

Arguments:
* **node** — abstract syntax tree of the file.

### pyStaticAnalyzer.checker

#### Class Checker

Represents class-aggregator for all checks

Methods:
* **get_all_checks()** — returns names of all checks added to this class.
* **run_checks(name, \*args)** — run single check by name with given args.
* **run_all_checks(name, args=None)** — run all checks added to this class. Param args optional, if specified it must be list of lists — one list of params for one check.

#### Decorator add_method

Usage — @add_method(Checker). Must be added to every check function (only to the main check function — additional functions should not be specified with this decorator). NOTE! All main check functions names must be started with "check" prefix.

#### Function check_bad_names

Check function similar to Pylint C0102. Check names in the code to be "good".

Arguments:
* **k** — kernel to be analyzed (ProjectKernel or FileKernel, required).
* **bad_names_list** — list of bad names (list of strings, optional, `["foo", "bar", "baz", "toto", "tutu", "tata"]` by default).

#### Function check_invalid_names

Check function similar to Pylint C0103. Check names of different types to be valid (by regexps).

Arguments:
* **k** — kernel to be analyzed (ProjectKernel or FileKernel, required).
* **good_names_list** — list of names which always be accepted (list of strings, optional, None by default).
* **regexs** — dict of regexs to change default regexs. By default this check has 6 regexs:
    1. `'argument-rgx' : '[a-z_][a-z0-9_]{2,30}$'`
    2. `'attr-rgx' : '[a-z_][a-z0-9_]{2,30}$'`
    3. `'class-rgx' : '[A-Z_][a-zA-Z0-9]+$'`
    4. `'function-rgx' : '[a-z_][a-z0-9_]{2,30}$'`
    5. `'module-rgx' : '(([a-z_][a-z0-9_]*)|([A-Z][a-zA-Z0-9]+))$'`
    6. `'variable-rgx' : '[a-z_][a-z0-9_]{2,30}$'`
 
 every single regex (or more) can be changed by adding {key:value} pair to regexs param.

 ## Command line 
 
 Some of the pyStaticAnalyzer functionality can be used with command line.
 
 ### Usage example
 
 `python -m pyStaticAnalyzer --file-ast <YOUR_FILENAME>`
 
 ### Possible arguments
 
* `--file-ast <YOUR_FILENAME>` — prints abstract syntax tree of file with name YOUR_FILENAME.
* `--folder-asts <YOUR_FOLDERNAME>` — prints abstract syntax trees of all files from folder with name YOUR_FOLDERNAME.
* `--structure <YOUR_FOLDERNAME>` — prints structure of folder with name YOUR_FOLDERNAME.
* `--call-graph <YOUR_FILENAME>` — prints call graph of the file with name YOUR_FILENAME.
* `--function-ast <YOUR_FUNCTIONNAME> --file <YOUR_FILENAME>` — prints abstract syntax tree of the function with name YOUR_FUNCTIONNAME from file YOUR_FILENAME.
* `--class-ast <YOUR_CLASSNAME> --file <YOUR_FILENAME>` — prints abstract syntax tree of the class with name YOUR_CLASSNAME from file YOUR_FILENAME.
* `--check-file <YOUR_FILENAME>` — runs all checks fof file with name YOUR_FILENAME.
* `--check-folder <YOUR_FOLDERNAME>` — runs all checks for folder with name YOUR_FOLDERNAME.
