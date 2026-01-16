## Key Topics
- Writing Python code in files (`.py`) allows programs to be saved, edited, and executed multiple times.
- Scripts: Python programs executed directly from the command line.
- Modules: Python files designed to be imported by other programs.

## Executing Programs
- Use `python filename.py` to run a script.
- `input()` requires explicit conversion (e.g., `int()`, `float()`).
- Add comments with `#` for clarity.
- Scripts can include logic to detect number properties (even, odd, divisible by 10, etc.).

## Command Line Arguments
- Values can be passed to a program via the command line: `python total.py 10 20 30`.
- Accessed in Python using `sys.argv` (first element is always the program name).
- Convert string arguments to numbers for processing.
- Can compute sums, averages, and handle the case of no arguments.

## Writing and Using Modules
- Any `.py` file can act as a module containing functions, variables, or classes.
- Modules are imported with `import module_name`.
- Functions can be accessed with `module_name.func()` or imported directly.
- Use aliases to shorten names: `import math as m` or `from math import sqrt as root`.
- Avoid `from module import *` in production code to prevent namespace clashes.
- Use `dir()` to inspect names in the current symbol table or module.

## Module Search Path
- Python searches for modules in:
  1. Standard Library
  2. Current directory
  3. Directories in `sys.path`
- Can modify `sys.path` or use `PYTHONPATH` environment variable for custom module locations.

## Scripts vs Modules
- `__name__` variable determines how a file is executed:
  - `__name__ == "__main__"` → file is executed as a script
  - Otherwise → file is imported as a module
- Allows files to act as both reusable modules and standalone programs.

## Key Terminology
- **IDE**: Integrated Development Environment, a tool for writing, running, and debugging code (e.g., PyCharm, IDLE).
- **Module**: Python file containing reusable code (functions, classes, variables).
- **Command Line Arguments**: Values passed to a program at execution.
- **Symbol-table**: A record of all names (variables, functions) in the current scope.
- **Search path**: Locations Python searches to find modules for importing.
