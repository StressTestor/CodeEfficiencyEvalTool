import time
import sys
import traceback
import os
import ast

# Log file setup
LOG_FILE = os.path.join(os.path.dirname(__file__), "devstral_eval_log.txt")

def log_message(message, error=False):
    """Log a message with timestamp to both console and file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {message}"
    print(formatted)
    try:
        with open(LOG_FILE, "a") as f:
            f.write(formatted + "\n")
    except Exception as e:
        if not error:
            print(f"Failed to write to log: {e}")

def evaluate_complexity(code):
    """Measure code complexity based on AST node count."""
    try:
        tree = ast.parse(code)
        num_nodes = len(list(ast.walk(tree)))
        log_message(f"Code complexity (AST nodes): {num_nodes}")
        return num_nodes
    except Exception as e:
        log_message(f"AST parsing failed: {e}", error=True)
        traceback.print_exc(file=sys.stdout)
        return 0

def safe_exec(code, namespace):
    """Safely execute generated code and return success."""
    try:
        exec(code, namespace)
        log_message("Code executed successfully.")
        return True
    except Exception as e:
        log_message(f"Execution error: {e}", error=True)
        traceback.print_exc(file=sys.stdout)
        return False

def generate_code_snippet(code_template):
    """Generate code from template, measure time, complexity, and validity."""
    start_time = time.perf_counter()
    try:
        compiled_code = compile(code_template, "<string>", "exec")
        log_message("Code generated successfully.")
    except Exception as e:
        log_message(f"Error compiling code: {e}", error=True)
        traceback.print_exc(file=sys.stdout)
        return None, 0

    end_time = time.perf_counter()
    elapsed = end_time - start_time
    log_message(f"Generated code in {elapsed:.4f} seconds")
    complexity = evaluate_complexity(code_template)
    success = safe_exec(compiled_code, {})
    return compiled_code, elapsed, complexity, success

def generate_function():
    """Generate a simple function."""
    code = """
def add(a, b):
    return a + b
"""
    return generate_code_snippet(code)

def generate_class():
    """Generate a simple class."""
    code = """
class Calculator:
    def add(self, a, b):
        return a + b
"""
    return generate_code_snippet(code)

def generate_cli_tool():
    """Generate a CLI tool."""
    code = """
import sys

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
"""
    return generate_code_snippet(code)

def main():
    """Main function to coordinate the evaluation process."""
    try:
        generate_function()
        generate_class()
        generate_cli_tool()
    except Exception as e:
        log_message(f"Error during evaluation process: {e}", error=True)
        traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main()
