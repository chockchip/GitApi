import GitApi as git

# Example for get user from open pr with specific repo
owner = "octocat"
repo = "hello-world"
full_name = owner + "/" + repo

list_user = git.get_user_openpr(owner, repo, full_name)
print(list_user)

print()
print("***********************************************************")
print()

# Example for get repos from topic
feature = "docker"
query = f'q={feature}+is:featured'

list_repo = git.get_repos(query)
print(list_repo)