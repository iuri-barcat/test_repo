import json

# Define the Git commands as a dictionary
git_commands = {
    "Basic Git Commands": {
        "git clone": "Clone a remote repository to your local machine.",
        "git status": "Check the status of your working directory and staged changes.",
        "git add": "Stage changes for the next commit.",
        "git commit": "Commit staged changes with a message.",
        "git push": "Push local commits to the remote repository.",
        "git pull": "Fetch and merge changes from the remote repository."
    },
    "Branching": {
        "git branch": "List all local branches.",
        "git branch <branch-name>": "Create a new branch.",
        "git switch <branch-name>": "Switch to an existing branch.",
        "git switch -c <new-branch-name>": "Create and switch to a new branch.",
        "git branch -d <branch-name>": "Delete a local branch.",
        "git push -u origin <branch-name>": "Push a local branch to the remote and set it as upstream."
    },
    "Merging": {
        "git merge <branch-name>": "Merge a branch into the current branch.",
        "git merge --squash <branch-name>": "Squash all commits from a branch into a single commit.",
        "git rebase <branch-name>": "Reapply commits from the current branch onto another branch."
    },
    "Pull Requests (GitHub CLI)": {
        "gh pr create": "Create a pull request.",
        "gh pr list": "List open pull requests.",
        "gh pr view <pr-number>": "View details of a specific pull request.",
        "gh pr checkout <pr-number>": "Checkout a pull request locally.",
        "gh pr merge <pr-number>": "Merge a pull request."
    },
    "Conflict Resolution": {
        "git mergetool": "Open a merge tool to resolve conflicts.",
        "git add <conflicted-file>": "Mark a conflicted file as resolved.",
        "git commit": "Complete the merge after resolving conflicts."
    },
    "Syncing After Remote Changes": {
        "git fetch": "Fetch changes from the remote repository.",
        "git pull origin <branch-name>": "Fetch and merge changes from a remote branch.",
        "git switch <branch-name> + git pull": "Sync a local branch with the remote."
    },
    "Undoing Changes": {
        "git restore <file>": "Discard changes in the working directory.",
        "git restore --staged <file>": "Unstage a file.",
        "git reset --hard": "Discard all local changes and reset to the last commit."
    },
    "Submodules": {
        "git submodule init": "Initialize submodules.",
        "git submodule update": "Update submodules to the latest commit.",
        "git rm --cached <submodule-path>": "Remove a submodule from Git’s tracking."
    },
    "Configuration": {
        "git config --global user.name": "Set your Git username.",
        "git config --global user.email": "Set your Git email.",
        "git config --global push.autoSetupRemote true": "Automatically set upstream when pushing new branches."
    },
    "Miscellaneous": {
        "git log --oneline": "View a concise commit history.",
        "git diff": "View changes between commits, branches, or the working directory.",
        "git clean -fd": "Remove untracked files and directories."
    }
}

# Save the dictionary as a JSON file
with open('git_commands.json', 'w') as json_file:
    json.dump(git_commands, json_file, indent=4)