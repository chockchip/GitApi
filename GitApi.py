import requests
import json

def get_user_openpr(owner, repo, full_name):
    # url = ""
    # if (owner == "" or repo == ""):
    #     url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
    # elif(full_name != ""):
    url = f'https://api.github.com/repos/{full_name}/pulls'
    result = requests.get(url)
    result_json = json.loads(result.text)

    list_user = []

    for i in range(0, len(result_json)):
        list_user.append(result_json[i]["user"]["login"])
    
    return(list_user)

def get_repos(query):
    # example quert: q=ruby+is:featured'
    url = 'https://api.github.com/search/repositories?'

    url = url + query

    # Have to add header because API during its preview
    head = {
        'Accept': 'application/vnd.github.mercy-preview+json',
    }

    result = requests.get(url, headers=head)
    result_json = json.loads(result.text)

    repos = []
    list_item = result_json["items"]

    for i in range(0, len(list_item)):
        repos.append(list_item[i]["full_name"])
    
    return(repos)