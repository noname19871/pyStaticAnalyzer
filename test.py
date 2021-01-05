from kernel import ProjectKernel, get_class_methods, get_classes_from_function, get_nested_classes, get_nested_functions, FileKernel
from checker import Checker

# we use global paths to files, so change it according to absolute path to test project
dir = '/Users/empire/Desktop/pyStaticAnalyzer/test_linter/'

kernel = ProjectKernel(dir, ignored={'venv', '.idea', '__pycache__'})

# Tests for project kernel
kernel.print_structure(indent_count=8)
kernel.print_folder(dir + '1')
kernel.print_all_asts()
kernel.print_folder_asts(dir + '1')
kernel.print_file_ast(dir + '1/11/111/first.py')
tree = kernel.get_all_tree
tree = kernel.get_structure
tree = kernel.get_source_codes
tree = kernel.get_source_code(dir + '1/11/111/first.py')
tree = kernel.get_file_classes_and_function(dir + '1/11/111/first.py')
methods = get_class_methods(tree.children['A'])
nested_classes = get_nested_classes(tree.children['A'])
nested_functions = get_nested_functions(tree.children['ctx'])
cl_from_func = get_classes_from_function(tree.children['ctx'])
tree = kernel.find_function_ast(dir + '1/11/111/first.py', 'bar')
tree = kernel.find_class_ast(dir + '1/11/111/first.py', 'a')
graph = kernel.build_call_graph(dir + '1/11/111/first.py')
kernel.print_call_graph(dir + '1/11/111/first.py')

# test checker for project kernel
c = Checker()
c.run_check("check_invalid_names", kernel)
c.run_all_checks([[kernel, ["tmp"]], [kernel, ["b"]]])

kernel = FileKernel(dir + '1/11/111/first.py')

# Tests for project kernel
kernel.print_structure()
kernel.print_all_asts()
kernel.print_file_ast(dir + '1/11/111/first.py')
tree = kernel.get_all_tree
tree = kernel.get_structure
tree = kernel.get_source_codes
tree = kernel.get_source_code(dir + '1/11/111/first.py')
tree = kernel.get_file_classes_and_function(dir + '1/11/111/first.py')
methods = get_class_methods(tree.children['A'])
nested_classes = get_nested_classes(tree.children['A'])
nested_functions = get_nested_functions(tree.children['ctx'])
cl_from_func = get_classes_from_function(tree.children['ctx'])
tree = kernel.find_function_ast(dir + '1/11/111/first.py', 'bar')
tree = kernel.find_class_ast(dir + '1/11/111/first.py', 'A')
graph = kernel.build_call_graph()
kernel.print_call_graph()

# test checker for project kernel
c = Checker()
c.run_check("check_invalid_names", kernel)
c.run_all_checks([[kernel, ["tmp"]], [kernel, ["b"]]])

