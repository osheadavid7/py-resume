from github import Github

from secrets import secret

def get_github_user(secret):
    g = Github(secret['GU'],secret['GP'])
    user = g.get_user()
    repos = user.get_repos()
    pub_repos = []
    #Only include public repos
    for r in repos:
        if r.private==False:
            #print r.name
            pub_repos.append(r)

    return user,pub_repos

def get_repo_details(user,repo):
    repo_el ={}
    repo_el['name'] = repo.name.replace('_','\_')
    repo_el['desc'] = repo.description.replace('_','\_')
    pcs = user.html_url.split('/')
    repo_el['html_url'] = repo.html_url.replace('_','\_')

    branches = repo.get_branches()
    bnames = [b.name for b in branches]
    if 'gh-pages' in bnames:
        ghpage=True
        temp= 'https://'+pcs[-1]+'.github.io/'+repo.name
        repo_el['ghpage'] = temp.replace('_','\_')
    else:
        ghpage=False

    return repo_el

def return_tidy_gh_data():
    user,repos = get_github_user(secret)
    repo_list = []
    for repo in repos:
        repo_el = get_repo_details(user,repo)
        repo_list.append(repo_el)
    return user,repo_list
