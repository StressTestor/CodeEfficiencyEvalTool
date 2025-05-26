
# Code Efficiency Self-Eval Tool

A self-contained Python utility designed to evaluate the performance of code generation by any language model or automated system.

This script:
- Generates simple Python code snippets (function, class, CLI)
- Measures generation time
- Analyzes structural complexity using AST
- Executes and validates the code
- Logs results to a timestamped file

## 📁 Project Structure

| File | Description |
|------|-------------|
| `code_efficiency.py` | Core script for generating, timing, validating, and analyzing code |
| `run_code_eval.bat` | Launchable from any folder. Verifies Python availability, then runs the script |
| `devstral_eval_log.txt` | Sample log file from an initial evaluation session |

## 🚀 How to Use

### 🔹 Requirements
- Python 3.8+
- OS with command prompt or shell access (tested on Windows 11)

### 🔹 Running It

1. Extract the ZIP folder to any directory.
2. Double-click the `run_code_eval.bat` file.
3. A terminal window will open and execute the Python evaluation script.
4. Results will be logged in `devstral_eval_log.txt`.

### 🔹 Sample Output
```text
[YYYY-MM-DD HH:MM:SS] Code generated successfully.
[YYYY-MM-DD HH:MM:SS] Generated code in 0.0005 seconds
[YYYY-MM-DD HH:MM:SS] Code complexity (AST nodes): 12
[YYYY-MM-DD HH:MM:SS] Code executed successfully.
```

## 🔍 Features

- 📏 Measures runtime performance
- 🌳 AST-based complexity analysis
- ✅ Syntax + execution validation
- 📓 Auto-logging with timestamps
- 💡 Modular design for easy expansion (e.g., CSV output, refactoring)

## 🔧 Future Ideas

- Add token estimation (for cost-awareness)
- Integrate test case pass/fail scoring
- Export results to CSV or JSON
- Challenge the model to improve/refactor its own output

---

_This project showcases recursive tool-use, LLM meta-evaluation, and code introspection via AST. Designed to test code reliability and performance across models._
