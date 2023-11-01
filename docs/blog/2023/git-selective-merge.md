---
date: 2023-11-01 00:00 UK/London
categories: software git merge tips
published: true
title: Selectively merging files across branches
image: /images/2023/git-merge-selective.png
description: "How to selectively merge files from one branch to another"
---

# Selectively merging files from across branches
Recently, I've had the need to merge selective files from one branch into another. This isn't something I recommend doing often, but if you're stuck in a position where you need a few files from another branch, here is one way to do it:

### The process:
Let's say you have a branch named `feature-1` and want the file `example.py` from the `feature-2` branch:

1. First, from the `feature-1` merge the `feature-2` branch with squash option (`git merge --squash feature-2`)
2. Reset the files (or entire folders) that you don't want in `feature-1` (`git reset origin/feature-1 tests/` or `git reset origin/feature-1 tests/test.py`) or remove them completely (`git rm tests/test.py`)
3. Add and commit the file(s) you want in your branch with a new commit message (`git add example.py && git commit -m "merge example.py from feature-2"`)
4. Clean the branch to remove untracked changes (`git clean -xfd`), -f for force, -d to remove the untracked directories, and -x to remove the ignored files. 
5. Restore the tracked changes (`git restore .`)
6. Push the changes to the remote branch (`git push`)