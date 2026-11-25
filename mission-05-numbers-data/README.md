# Mission 5 — Numbers and data

## 1. Task / objective

Convert decimal, binary and hexadecimal values by hand, verify those results using Python's built-in functions, build a small Python number converter program, and explain how text is stored using encoding standards.

## 2. Work completed

- Completed all seven manual number conversions with working shown.
- Verified every conversion in the Python interpreter and confirmed results match.
- Created `number_converter.py` and tested it with four positive decimal numbers.
- Wrote notes on ASCII and UTF-8 text encoding.

## 3. Commands / tools used

| Command / function | Purpose |
|-------------------|---------|
| `python3` | Start the Python 3 interpreter |
| `bin(n)` | Convert decimal integer `n` to its binary string (prefix `0b`) |
| `hex(n)` | Convert decimal integer `n` to its hexadecimal string (prefix `0x`) |
| `int(s, 2)` | Convert a binary string `s` to a decimal integer |
| `int(s, 16)` | Convert a hexadecimal string `s` to a decimal integer |
| `ord(c)` | Return the ASCII / Unicode code point of character `c` |
| `input()` | Read a string typed by the user |
| `int()` | Convert a string to an integer |
| `python3 number_converter.py` | Run the converter program from Terminal |

## 4. My understanding

### Task 5.1 — Manual number conversions

**Reminder:** Decimal = base 10, Binary = base 2, Hexadecimal = base 16. In hex: A=10, B=11, C=12, D=13, E=14, F=15.

| Question | Working | Answer |
|----------|---------|--------|
| Convert decimal 13 to binary | 13 ÷ 2 = 6 r **1**, 6 ÷ 2 = 3 r **0**, 3 ÷ 2 = 1 r **1**, 1 ÷ 2 = 0 r **1** → read remainders bottom-up | **1101** |
| Convert decimal 25 to binary | 25 ÷ 2 = 12 r **1**, 12 ÷ 2 = 6 r **0**, 6 ÷ 2 = 3 r **0**, 3 ÷ 2 = 1 r **1**, 1 ÷ 2 = 0 r **1** → bottom-up | **11001** |
| Convert binary 1010 to decimal | 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8 + 0 + 2 + 0 | **10** |
| Convert binary 1101 to decimal | 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 | **13** |
| Convert hexadecimal A to decimal | A = 10 (by definition in hex) | **10** |
| Convert hexadecimal 1F to decimal | 1×16¹ + F×16⁰ = 16 + 15 | **31** |
| Convert binary 1111 to hexadecimal | 1111 in decimal = 1×8+1×4+1×2+1×1 = 15; 15 in hex = F | **F** |

---

### Task 5.2 — Python verification

Verified in the Python interpreter. Every result matches the manual calculation.

| Expression tested | Result | Matches manual? |
|------------------|--------|----------------|
| `bin(13)` | `0b1101` → 1101 | ✓ Yes |
| `bin(25)` | `0b11001` → 11001 | ✓ Yes |
| `int('1010', 2)` | `10` | ✓ Yes |
| `int('1101', 2)` | `13` | ✓ Yes |
| `hex(10)` | `0xa` → A | ✓ Yes |
| `int('A', 16)` | `10` | ✓ Yes |
| `int('1F', 16)` | `31` | ✓ Yes |
| `hex(int('1111', 2))` | `0xf` → F | ✓ Yes |
| `ord('A')` | `65` | ASCII code of uppercase A |
| `ord('a')` | `97` | ASCII code of lowercase a |

Python's `bin()` and `hex()` functions add a prefix (`0b` for binary, `0x` for hexadecimal). The actual digits without the prefix match the hand calculations exactly.

---

### Task 5.3 — Number converter program

The file `number_converter.py` contains:

```python
decimal_input = input("Enter a positive decimal number: ")

try:
    number = int(decimal_input)
    if number == 0:
        print("Zero is not allowed. Please enter a positive whole number greater than 0.")
    elif number < 0:
        print("Negative numbers are not allowed. Please enter a positive whole number greater than 0.")
    else:
        binary_result = bin(number)
        hex_result = hex(number)
        print(f"Decimal    : {number}")
        print(f"Binary     : {binary_result}")
        print(f"Hexadecimal: {hex_result}")
except ValueError:
    print("Invalid input. Please enter a valid positive whole number.")
```

**Test results (actual output from running the program):**

| Input | Behaviour / Output |
|-------|--------------------|
| `13` | `Decimal: 13`, `Binary: 0b1101`, `Hexadecimal: 0xd` |
| `255` | `Decimal: 255`, `Binary: 0b11111111`, `Hexadecimal: 0xff` |
| `42` | `Decimal: 42`, `Binary: 0b101010`, `Hexadecimal: 0x2a` |
| `1000` | `Decimal: 1000`, `Binary: 0b1111101000`, `Hexadecimal: 0x3e8` |
| `0` | Rejected: `Zero is not allowed. Please enter a positive whole number greater than 0.` |
| `-5` | Rejected: `Negative numbers are not allowed. Please enter a positive whole number greater than 0.` |
| `abc` | Handled gracefully: `Invalid input. Please enter a valid positive whole number.` |

The `bin()` function converts a decimal integer to a string of 0s and 1s prefixed with `0b`. The `hex()` function converts a decimal integer to a string of hex digits prefixed with `0x`. The `int()` function converts the user's text input into a proper integer so that the conversion functions can work on it.

---

### Task 5.4 — How is text stored?

Computers can only store numbers (bits). An **encoding standard** assigns a unique number to every character so that the computer knows which number represents which letter, digit or symbol.

**ASCII** (American Standard Code for Information Interchange) is a basic standard that maps 128 characters (letters A–Z, a–z, digits 0–9, punctuation and control characters) to numbers 0–127.

- ASCII code for uppercase **A** = **65**
- ASCII code for lowercase **a** = **97**

Without an encoding standard, different computers might use different numbers for the same character, making it impossible to reliably read a file created on another machine.

**UTF-8** extends ASCII to cover every character in every language — including characters such as `é`, `ñ`, `中`, `ā` and emoji — by using between 1 and 4 bytes per character. The first 128 UTF-8 codes are identical to ASCII, so ASCII files are valid UTF-8.

**Example of a character outside basic ASCII:** The letter `é` (e with an acute accent, used in French). Its UTF-8 encoding is `0xC3 0xA9` (two bytes). It has no ASCII code because basic ASCII only covers unaccented English letters.

## 5. Difficulties faced

No major difficulties. When first reading the Python output for `hex(10)`, the result was `0xa` (lowercase). I confirmed that `a` and `A` represent the same hexadecimal digit (both equal 10), so the answer still matches the manual calculation.

## 6. How I resolved them

Checking that `0xa` == `0xA` == decimal 10 confirmed the result was correct.

## 7. Evidence / files

| File | Description |
|------|-------------|
| `mission-05-numbers-data/number_converter.py` | Python program that converts decimal to binary and hexadecimal |
| `mission-05-numbers-data/README.md` | This file containing manual conversions, Python verification and encoding notes |

## 8. Commit details

**Commit message:** `Build number converter and practise data representation`

Commit pushed to the `main` branch on GitHub. Both `number_converter.py` and this README are visible in the `mission-05-numbers-data/` folder.
