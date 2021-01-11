from pyStaticAnalyzer import kernel, checker

dir = 'test_linter/'

k = kernel.ProjectKernel(dir, ignored={'venv', '.idea', '__pycache__'})

# Tests for project kernel
k.print_structure(indent_count=8)
k.print_folder(dir + '1')
k.print_all_asts()
k.print_folder_asts(dir + '1')
k.print_file_ast(dir + '1/11/111/first.py')
tree = k.get_all_tree
tree = k.get_structure
tree = k.get_source_codes
tree = k.get_source_code(dir + '1/11/111/first.py')
tree = k.get_file_classes_and_function(dir + '1/11/111/first.py')
methods = kernel.get_class_methods(tree.children['A'])
nested_classes = kernel.get_nested_classes(tree.children['A'])
nested_functions = kernel.get_nested_functions(tree.children['ctx'])
cl_from_func = kernel.get_classes_from_function(tree.children['ctx'])
tree = k.find_function_ast(dir + '1/11/111/first.py', 'bar')
tree = k.find_class_ast(dir + '1/11/111/first.py', 'a')
graph = k.build_call_graph(dir + '1/11/111/first.py')
k.print_call_graph(dir + '1/11/111/first.py')

# test checker for project kernel
c = checker.Checker()
c.run_check("check_invalid_names", k)
c.run_all_checks([[k, ["tmp"]], [k, ["b"]]])

k = kernel.FileKernel(dir + '1/11/111/first.py')

# Tests for project kernel
k.print_structure()
k.print_all_asts()
k.print_file_ast(dir + '1/11/111/first.py')
tree = k.get_all_tree
tree = k.get_structure
tree = k.get_source_codes
tree = k.get_source_code(dir + '1/11/111/first.py')
tree = k.get_file_classes_and_function(dir + '1/11/111/first.py')
methods = kernel.get_class_methods(tree.children['A'])
nested_classes = kernel.get_nested_classes(tree.children['A'])
nested_functions = kernel.get_nested_functions(tree.children['ctx'])
cl_from_func = kernel.get_classes_from_function(tree.children['ctx'])
tree = k.find_function_ast(dir + '1/11/111/first.py', 'bar')
tree = k.find_class_ast(dir + '1/11/111/first.py', 'A')
graph = k.build_call_graph()
k.print_call_graph()

# test checker for project kernel
c = checker.Checker()
c.run_check("check_invalid_names", k)
c.run_all_checks([[k, ["tmp"]], [k, ["b"]]])
