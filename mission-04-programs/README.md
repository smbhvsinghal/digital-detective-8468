# Mission 4 — How programs run

## 1. Task / objective

Create and run a simple Python program. Compare how a compiler and an interpreter translate and execute source code, using a table and a written explanation.

## 2. Work completed

- Created `hello.py` in this mission folder with a single `print()` statement.
- Ran `hello.py` using Python 3 from Terminal and recorded the actual output.
- Completed a compiler vs interpreter comparison table.
- Wrote a plain-language explanation of the difference between the two approaches.

## 3. Commands / tools used

| Command / tool | Purpose |
|----------------|---------|
| `python3 hello.py` | Run the Python file using the Python 3 interpreter |
| `print()` | Python built-in function that displays text to the screen |

## 4. My understanding

### Task 4.1 — Creating and running hello.py

The file `hello.py` contains one line:

```python
print("Hello from Python")
```

Running it from Terminal:

```bash
python3 hello.py
```

**Actual output:**
```
Hello from Python
```

The program ran successfully. The Python interpreter read the source file, understood the `print()` function call, and displayed the text to the screen.

---

### Task 4.2 — Compiler vs interpreter

| Point | Compiler | Interpreter |
|-------|----------|-------------|
| **When translation / execution happens** | Translates the entire source code into machine code before the program runs. The compiled file is then executed separately. | Reads and executes the source code line by line at runtime. Translation and execution happen at the same time. |
| **Typical output** | A standalone executable file (e.g. `.exe` on Windows or a binary on macOS/Linux) that can run without the original source code or compiler. | The result of running the source code directly — no separate executable is produced by default. |
| **One example** | C and C++ are typically compiled. The `gcc` or `clang` compiler translates C source code into a binary before it is run. | Python is typically interpreted. The `python3` command reads and runs `.py` source files directly. |
| **One advantage** | Compiled programs usually run faster because all translation is done before execution, so no translation work is needed at runtime. | Interpreted programs are easier to test and develop because you can run a file immediately after editing it, without a separate compile step. |

**Written explanation:**

A compiler reads the entire source code once and converts it into machine code, producing an output file. That output file can then be run as many times as needed without the compiler being present. An interpreter, by contrast, reads the source code and carries out each instruction as it goes, without producing a separate output file. Python uses an interpreter, which is why running `python3 hello.py` immediately executes the file without any extra compile step. Compiled languages tend to run faster at execution time, while interpreted languages tend to be quicker to test and modify during development.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

| File | Description |
|------|-------------|
| `mission-04-programs/hello.py` | Simple Python program that prints `Hello from Python` |
| `mission-04-programs/README.md` | This file containing the comparison table and explanation |

## 8. Commit details

**Commit message:** `Compare compilers and interpreters`

Commit pushed to the `main` branch on GitHub. Both `hello.py` and this README are visible in the `mission-04-programs/` folder.
