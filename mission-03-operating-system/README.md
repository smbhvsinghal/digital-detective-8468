# Mission 3 — Understand the operating system

## 1. Task / objective

Explore the operating system environment using Terminal commands. Observe system information, running processes, storage usage, file paths and file permissions. Explain the six main responsibilities of an operating system.

## 2. Work completed

- Recorded OS details, storage usage and a system activity snapshot from Terminal.
- Explained what a process is, what PID means, and identified two real running processes.
- Explained absolute and relative paths with examples from this project.
- Read the permission string from a file listing and explained read, write and execute.
- Wrote explanations for all six OS responsibilities in my own words.

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `sw_vers` | Display the macOS version and build number |
| `whoami` | Show the current logged-in account name |
| `df -h /` | Show disk usage for the main volume in human-readable form |
| `top -l 1 -n 5` | Take one snapshot of system activity and show the top five processes |
| `ps -eo pid,comm` | List all running processes with their PID and command name |
| `ls -la` | Show a detailed listing including permission strings |
| `pwd` | Show the current working directory (absolute path) |
| `cd mission-02-terminal` | Navigate into a sub-folder using a relative path |

## 4. My understanding

### Task 3.1 — System information

| Information explored | What it tells you | Observation (privacy-safe) |
|---------------------|------------------|---------------------------|
| Operating system | Which OS and version is running | macOS 27.2.1 (Build 26B131) |
| Current account | Which user account is active | [redacted — personal account name] |
| Available and used storage | How much disk space is free and in use | Total: 926 GiB, Used: 13 GiB, Available: 802 GiB (2% used) |
| System activity snapshot | CPU usage, memory and running processes | 933 processes total (4 running, 929 sleeping). CPU: ~14% user, ~15% sys, ~71% idle. RAM: 15 GiB used out of available physical memory. |

The commands used to gather this information:

```bash
sw_vers
# ProductName: macOS
# ProductVersion: 27.2.1
# BuildVersion: 26B131

df -h /
# /dev/disk3s1s1   926Gi  13Gi  802Gi  2%  ...  /

top -l 1 -n 5
# (snapshot of CPU, memory and top processes — usernames redacted)
```

---

### Task 3.2 — Processes

A **process** is a program that is currently running on the computer. When you open an application, the operating system creates a process for it. The process gets its own section of memory and a turn on the CPU.

The **PID** (Process Identifier) is a unique number the operating system assigns to every running process. It is used to identify and manage that process — for example, to stop it or check its resource use. PIDs are assigned in increasing order and may be reused after a process ends.

**Two examples of running processes observed using `ps -eo pid,comm`:**

1. **PID 1 — `/sbin/launchd`**: This is the first process started when the Mac boots. It is the parent of all other processes and manages system services and daemons.
2. **PID 6306 — `Google Chrome Helper`**: A helper process for the Chrome browser. Chrome runs several helper processes to handle separate browser tabs and extensions safely.

---

### Task 3.3 — Paths and permissions

**Absolute path:** A path that starts from the root of the file system (`/`). It always refers to the same location regardless of where you currently are.

Example from this project:
```
/Users/[redacted]/.gemini/antigravity/scratch/digital-detective-8468/mission-02-terminal/terminal-practice/notes.txt
```

**Relative path:** A path that is measured from the current working directory. It changes meaning depending on where you are.

Example: If the current directory is `digital-detective-8468/`, then:
```
mission-02-terminal/terminal-practice/notes.txt
```
refers to the same file using a relative path.

**File permissions:**

Running `ls -la mission-02-terminal/terminal-practice/notes.txt` produced:
```
-rw-r--r--@ 1 [redacted]  staff  150 Nov 25 23:13 notes.txt
```

The permission string `-rw-r--r--` is read as:

| Characters | Who | Permissions |
|-----------|-----|------------|
| `rw-` | Owner | Can read and write; cannot execute |
| `r--` | Group | Can read only |
| `r--` | Others | Can read only |

| Permission | Meaning | Example |
|-----------|---------|---------|
| `r` — Read | Allows the file's contents to be read | Opening a text file in a text editor |
| `w` — Write | Allows the file to be edited or overwritten | Saving changes to a text file |
| `x` — Execute | Allows the file to be run as a program; on a directory, allows entering or traversing it | Running a `.py` Python script |

The owner of `notes.txt` can read and write it but cannot execute it (which is correct — it is a text file, not a script).

---

### Task 3.4 — Operating system responsibilities

| OS responsibility | Explanation | Example |
|------------------|------------|---------|
| **Process management** | The OS starts, pauses, resumes and stops programs. It decides which process gets CPU time and for how long, so that multiple programs can appear to run at the same time. | Opening Chrome and a text editor at the same time — the OS switches the CPU between them so quickly that both seem to run simultaneously. |
| **Memory management** | The OS allocates RAM to each running program and makes sure programs do not access memory belonging to another program. When RAM is full it may move some data to disk temporarily (virtual memory). | When many browser tabs are open, the OS manages how much RAM each tab gets and may suspend background tabs to free memory. |
| **Device management** | The OS uses drivers to communicate with hardware devices such as keyboards, printers and USB drives, so applications do not need to know the details of each device. | Plugging in a USB drive: the OS detects it, loads the correct driver and makes the drive available in the file manager. |
| **File management** | The OS organises files into a hierarchical folder structure, controls who can read or write each file, and handles reading from and writing to storage devices. | Saving a document creates a file at a specific path; the OS writes the data to the SSD and updates the directory listing. |
| **User interface / shell** | The OS provides a way for users to interact with the computer — either through a graphical user interface (GUI) with windows and icons, or through a command-line shell such as zsh on macOS. | Typing `ls` in Terminal — the shell reads the command, asks the OS to list the directory, and shows the result as text. |
| **Security and permissions** | The OS enforces who can access which files and programs, checks passwords, and separates processes so that one program cannot read another's private data. | A file owned by one user account cannot be read by another account unless the permissions allow it — this is enforced by the OS. |

## 5. Difficulties faced

No major difficulties. Reading the permission string (`-rw-r--r--`) required care to separate the owner, group and others sections correctly.

## 6. How I resolved them

Remembering that the nine characters after the file-type character are split into three groups of three (owner | group | others) made the permission string straightforward to interpret.

## 7. Evidence / files

| File | Description |
|------|-------------|
| `mission-03-operating-system/README.md` | This file containing system information, process observations, path examples and OS responsibility table |

## 8. Commit details

**Commit message:** `Document operating system and file management`

Commit pushed to the `main` branch on GitHub. The file is visible in the `mission-03-operating-system/` folder.
