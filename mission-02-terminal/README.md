# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective

Use the command-line interface (CLI) to practise navigating directories, creating and managing files, understand command flags and pipes, and explain what a package manager does.

## 2. Work completed

- Practised nine core Terminal operations and recorded the command, purpose and observation for each.
- Created `terminal-practice/notes.txt`, added two lines of text, made a backup copy, and renamed the backup to `notes-backup-renamed.txt`.
- Demonstrated `ls`, `ls -la`, `ls -lah`, and a piped command (`ls -lah | head -n 5`).
- Checked Homebrew (the macOS package manager), noted its version and listed some managed packages.
- Wrote explanations for replacing vs appending, copying vs moving, `pwd` and `ls`.

## 3. Commands / tools used

| Command | Purpose | What I observed |
|---------|---------|----------------|
| `pwd` | Display the full path of the current working directory | Showed `/Users/[redacted]/.gemini/antigravity/scratch/digital-detective-8468` |
| `ls` | List files and folders in the current directory | Listed all nine mission folders |
| `ls -la` | Detailed listing including hidden files, permissions, owner, size and date | Showed `.gitignore` and all mission folders with permissions such as `drwxr-xr-x` |
| `cd ..` | Move to the parent folder | The prompt changed to show the parent directory |
| `mkdir -p terminal-practice` | Create a new directory (the `-p` flag creates parent directories if needed) | Created the `terminal-practice` folder inside `mission-02-terminal/` |
| `touch notes.txt` | Create an empty file | Created `notes.txt` with zero bytes |
| `printf '...\n' > notes.txt` | Write text into a file, replacing existing contents | The first line appeared when displayed with `cat` |
| `printf '...\n' >> notes.txt` | Append text to a file without removing existing contents | Both lines appeared when displayed with `cat` |
| `cat notes.txt` | Display the contents of a file | Showed both lines of text |
| `cp notes.txt notes-backup.txt` | Copy a file to a new name | Created `notes-backup.txt` with the same contents |
| `mv notes-backup.txt notes-backup-renamed.txt` | Rename or move a file | The backup was renamed; the original name disappeared |
| `ls -lah` | Detailed listing with human-readable file sizes | Showed file sizes as `150B` instead of raw bytes |
| `ls -lah \| head -n 5` | Send listing output to `head`, which shows only the first five lines | Only the first five lines of the listing appeared |
| `brew --version` | Check the installed Homebrew version | Returned `Homebrew 7.0.9` |
| `brew list` | List all packages managed by Homebrew | Showed packages including `ffmpeg`, `openssl@4`, `ca-certificates` |

## 4. My understanding

### Task 2.2 — File changes inside `terminal-practice/`

The practice files were created and managed with these commands:

```bash
cd mission-02-terminal/terminal-practice
touch notes.txt
printf 'First line: Terminal practice file for the Digital Detective assignment.\n' > notes.txt
printf 'Second line: Learning how to append text without overwriting the first line.\n' >> notes.txt
cat notes.txt
cp notes.txt notes-backup.txt
mv notes-backup.txt notes-backup-renamed.txt
ls -lah
```

**Actual output of `cat notes.txt`:**
```
First line: Terminal practice file for the Digital Detective assignment.
Second line: Learning how to append text without overwriting the first line.
```

**Actual output of `ls -lah` in `terminal-practice/`:**
```
total 16
drwxr-xr-x@ 4 [redacted]  staff   128B Nov 25 23:13 .
drwxr-xr-x@ 3 [redacted]  staff    96B Nov 25 23:12 ..
-rw-r--r--@ 1 [redacted]  staff   150B Nov 25 23:13 notes-backup-renamed.txt
-rw-r--r--@ 1 [redacted]  staff   150B Nov 25 23:13 notes.txt
```

**Answers to questions:**

- **Replacing vs appending:** Using `>` replaces everything already in the file — the old content is lost. Using `>>` adds new text at the end without deleting the existing content. This matters because using `>` by mistake will delete work that cannot easily be recovered.
- **Copying vs moving:** Copying (`cp`) creates a second copy while keeping the original. Moving (`mv`) moves the file to a new location or renames it; the original no longer exists at the old path.
- **What `pwd` provides:** `pwd` shows the full absolute path of the current directory. This tells you exactly where you are in the file system so you can avoid running commands in the wrong folder.
- **Why `ls` is useful:** `ls` shows the contents of a directory so you can see which files and folders exist before running commands that might affect them.

### Task 2.3 — Flags and pipes

A **flag** (or option) changes how a command behaves. For example:
- `ls` — simple list of names.
- `ls -l` — detailed listing (permissions, owner, size, date).
- `ls -a` — includes hidden files (names starting with `.`).
- `ls -h` — shows sizes in human-readable form (`128B`, `4K`).
- `ls -lah` — combines all three flags: detailed, hidden, human-readable.

A **pipe** (`|`) connects two commands by sending the output of the first as the input to the second.

```bash
ls -lah | head -n 5
```

The left side of the pipe (`ls -lah`) produces the full detailed listing. The right side (`head -n 5`) reads that output and shows only the first five lines. This is useful when output is long and you only want to see the beginning.

### Task 2.4 — Package managers

Homebrew is installed on this Mac. Version check:

```bash
brew --version
# Homebrew 7.0.9
```

Some packages managed by Homebrew on this system: `ca-certificates`, `ffmpeg`, `openssl@4`, `opus`, `x264`.

A **package manager** is a tool that automatically handles downloading, installing, updating and removing software. Instead of manually finding a website, downloading an installer and placing files in the right location, the package manager does all of this with a single command. It also tracks which software depends on which other software, so removing one package does not break another.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

| File | Description |
|------|-------------|
| `mission-02-terminal/terminal-practice/notes.txt` | Practice text file with two lines of content |
| `mission-02-terminal/terminal-practice/notes-backup-renamed.txt` | Renamed copy of `notes.txt` with identical contents |
| `mission-02-terminal/README.md` | This file |

## 8. Commit details

**Commit message:** `Complete Terminal and file management mission`

Commit pushed to the `main` branch on GitHub. Both practice files and this README are visible in the repository.
