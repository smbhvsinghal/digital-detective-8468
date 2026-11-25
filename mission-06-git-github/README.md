# Mission 6 — Git and GitHub

## 1. Task / objective

Understand and practise the Git version control workflow: check status, stage files, create commits and view history. Create a new branch named `update-about`, add a "My Learning" section to the root README, and push the branch to GitHub. Create a Pull Request from `update-about` into `main`. Build a Git command glossary.

## 2. Work completed

- Practised `git status`, `git add`, `git commit` and `git log` and recorded what each does.
- Created the `update-about` branch from `main`.
- Added the "My Learning" section to `README.md` on the new branch.
- Staged the change, committed it with a meaningful message, and pushed the branch to GitHub.
- Created Pull Request #1 from `update-about` into `main` (PR is currently **open and unmerged** — the instructor has not asked for it to be merged).
- Wrote a Git command glossary.

## 3. Commands / tools used

| Git command / operation | Purpose |
|------------------------|---------|
| `git status` | Show which files have been modified, staged or are untracked |
| `git add README.md` | Stage a specific file so it will be included in the next commit |
| `git commit -m "..."` | Record staged changes as a snapshot with a meaningful description |
| `git log --oneline` | Display the commit history with one line per commit |
| `git checkout -b update-about` | Create a new branch named `update-about` and switch to it |
| `git push -u origin update-about` | Push the new branch to GitHub and set the upstream tracking reference |
| `git checkout main` | Switch back to the `main` branch |
| GitHub Pull Request UI / API | Create a PR comparing `update-about` with `main` |

## 4. My understanding

### Task 6.1 — Basic Git workflow

| Git operation | What it does |
|--------------|-------------|
| `git status` | Shows the current state of the working directory and staging area. It tells you which files are modified, which are staged ready for a commit, and which are brand new (untracked). |
| `git add <file>` | Moves selected changes from the working directory into the staging area. Only staged changes go into the next commit, so you choose exactly what to include. |
| `git commit -m "..."` | Takes everything in the staging area and saves it as a permanent snapshot in the repository history with a message explaining what changed. |
| `git log` | Shows the list of past commits — each with its unique hash, author, date and message — so you can see the full history of changes. |

**Staging vs committing:** Staging (`git add`) is a preparation step — you select which changes to include. Committing (`git commit`) is the act of permanently saving those staged changes as a named point in history. This two-step process lets you group only related changes into one commit even when multiple files have been edited.

---

### Task 6.2 — Creating and using the `update-about` branch

```bash
# Starting from main
git checkout -b update-about

# (Edited README.md to add the "My Learning" section)

git status
# On branch update-about
# Changes not staged for commit:
#   modified:   README.md

git add README.md
git commit -m "Add My Learning section to root README"
git push -u origin update-about
```

The "My Learning" section in the root README lists three genuine takeaways from the assignment:
1. The Terminal provides direct, precise control over the file system.
2. Binary and hexadecimal follow clear positional rules (base 2 and base 16).
3. Git branches let you work on new ideas without affecting the main branch.

---

### Task 6.3 — Pull Request

**Pull Request #1** was created on GitHub:

- **Title:** Add My Learning section to root README
- **From:** `update-about` → **Into:** `main`
- **URL:** https://github.com/smbhvsinghal/digital-detective-8468/pull/1
- **Status:** **Open and unmerged**

The PR was reviewed (the changed README.md is visible in the Files Changed tab). It has not been merged because the instructor has not asked for the merge to be completed.

A **branch** is a separate copy of the repository's history where you can make changes without affecting the original. It is useful because it lets one person work on a new feature while another fixes a bug, without their changes clashing.

A **Pull Request** is a request to merge one branch into another. It creates a discussion space where changes can be reviewed and approved before they become part of the main code. This is the standard way teams collaborate on GitHub.

---

### Task 6.4 — Git command glossary

| Operation | Git command | One-line explanation |
|-----------|------------|---------------------|
| Initialise a repository | `git init` | Creates a new empty Git repository in the current folder |
| Check status | `git status` | Shows which files are modified, staged or untracked |
| Stage changes | `git add <file>` | Moves selected file changes into the staging area ready for a commit |
| Commit changes | `git commit -m "..."` | Saves staged changes as a permanent snapshot with a description |
| View history | `git log` | Lists all past commits with their hash, author, date and message |
| Create / list branches | `git branch` / `git checkout -b <name>` | Lists existing branches or creates and switches to a new one |
| Switch branches | `git checkout <name>` | Moves to a different branch, updating the working files |
| Push changes | `git push origin <branch>` | Uploads local commits to the remote repository on GitHub |
| Fetch remote changes | `git fetch` | Downloads new changes from GitHub without merging them into the local branch |
| Pull remote changes | `git pull` | Fetches and immediately merges remote changes into the current local branch |

## 5. Difficulties faced

No major difficulties. When creating the PR via the GitHub API, the response showed that a PR already existed (GitHub had auto-created it from the push). I retrieved the existing PR details instead.

## 6. How I resolved them

Queried the existing pull requests list via the API to get the PR number and URL.

## 7. Evidence / files

| File / item | Description |
|-------------|-------------|
| `mission-06-git-github/README.md` | This file |
| `update-about` branch | Visible on GitHub under the repository's Branches tab |
| Pull Request #1 | Open at https://github.com/smbhvsinghal/digital-detective-8468/pull/1 |
| Root `README.md` on `update-about` | Contains the added "My Learning" section |

## 8. Commit details

**Commit on `update-about` branch:** `Add My Learning section to root README`  
Branch pushed and visible on GitHub. PR #1 is open.

**Commit for this mission README (on `main`):** `Complete Git and GitHub collaboration mission`  
Pushed to `main`. The branch and PR remain untouched on GitHub.
