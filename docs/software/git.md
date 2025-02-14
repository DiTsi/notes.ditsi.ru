# git

## Commands

Examples:

```bash
# Restore a file from one of the past commits
git checkout aa9463b853dc removed-file.txt

# Git rebase - this is a BASE (commit) change for a branch commit
<changes>: git rebase master # the base change for the changes branch to the commit pointed to by the master branch

# git show
git show <commit>

# Differences in STAGE
git diff --cached

# Show log with differences
git log -p

# Show all git files
git ls-tree -r master --name-only

# Show commits with branches
git log --graph --all

# See which commits changed the contents of file.txt
git blame file.txt

# Delete remote branches
git push origin --delete feature/remotebranch

# Squash commits (top 5 into 1)
git rebase -i HEAD~5

# Delete large files in history (must be installed https://github.com/newren/git-filter-repo)
git filter-repo --path files/ --invert-paths # in this case, everything in the files/ folder is deleted
```

#### How to delete unnecessary things in history and push everything again in GitLab

```yaml
- git clone
- git filter-repo --path files/ --invert-paths
- rm -Rf .git/logs .git/refs/original
- git gc --prune=all --aggressive
- deactivate Protected Branch
- in Push Rules we deactivate everything that prevents unregistered users from pushing
- git push origin --all --force
- if there are tags, more needs to be done "git push origin --tags --force"
```

#### git log
```bash
# The command shows commits issued branches in chronological order

# Find any commit that added or removed the string password
git log -S password
```

#### git log --graph

The command shows commits in chronological order within only one branch. Commits on neighboring branches can (and often will) be <span style="color: #ff0000;">NOT IN CHRONOLOGICAL</span> order. To see the correct order, use the `--date-order` option

#### git blame

If you need to find who wrote a specific code
