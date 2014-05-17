from github import Github

from secrets import secret

def get_github_user(secret):
    g = Github(secret['GU'],secret['GP'])
    user = g.get_user()
    repos = user.get_repos()

    return user,repos

def get_repo_details(user,repo,ghpage=False):
    repo_el ={}
    repo_el['name'] = repo.name
    repo_el['desc'] = repo.description
    pcs = user.html_url.split('/')
    repo_el['html_url'] = repo.html_url
    if ghpage==True:
        repo_el['ghpage'] = pcs[-1]+'.github.io/'+repo1.name
    else:
        repo_el['ghpage'] = ''
    
    return repo_el

user,repos = get_github_user(secret)
repo1 = repos[4] #py-resume

repo_el = get_repo_details(user,repo1,ghpage=True)
