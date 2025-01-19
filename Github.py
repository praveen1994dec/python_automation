import requests
import json

# Define the repository information
owner = "your-username"  # replace with the repo owner's GitHub username
repo = "your-repo"       # replace with the repository name

# GitHub API URL for fetching branches
url = f"https://api.github.com/repos/{owner}/{repo}/branches"

# Optional: Provide a GitHub token for higher rate limits
headers = {
    "Authorization": "token your-github-token"  # replace with your GitHub token if needed
}

# Function to get branches from GitHub repository
def get_branches(owner, repo, headers=None):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/branches", headers=headers)
    if response.status_code == 200:
        branches_data = response.json()
        return branches_data
    else:
        print(f"Error fetching branches: {response.status_code}")
        return None

# Fetch branches
branches_data = get_branches(owner, repo, headers)

# Manipulating the branch data
if branches_data:
    branch_names = []
    for branch in branches_data:
        branch_name = branch['name']  # Extracting branch name
        commit_sha = branch['commit']['sha']  # Extracting the commit SHA for the branch
        protected = branch.get('protected', False)  # Check if branch is protected
        branch_names.append({
            'branch_name': branch_name,
            'commit_sha': commit_sha,
            'protected': protected
        })
    
    # Example: Print out all branch names and their statuses
    print("Branch Information:")
    for branch in branch_names:
        print(f"Branch: {branch['branch_name']}, SHA: {branch['commit_sha']}, Protected: {branch['protected']}")
    
    # Example: Filter branches with a specific pattern in the name
    filtered_branches = [branch for branch in branch_names if 'feature' in branch['branch_name'].lower()]
    print("\nFiltered Branches (contain 'feature'):")
    for branch in filtered_branches:
        print(f"Branch: {branch['branch_name']}, SHA: {branch['commit_sha']}, Protected: {branch['protected']}")
    
    # Example: Sorting branches alphabetically by name
    sorted_branches = sorted(branch_names, key=lambda x: x['branch_name'])
    print("\nSorted Branches:")
    for branch in sorted_branches:
        print(f"Branch: {branch['branch_name']}, SHA: {branch['commit_sha']}, Protected: {branch['protected']}")
else:
    print("No data available.")
