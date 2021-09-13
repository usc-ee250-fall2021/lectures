import requests
import json

r = requests.get('https://api.github.com/orgs/usc-ee250-fall2021/repos')
print("Headers:\n" + str(r.headers))

if r.status_code == 200:
    repos = r.json()
    for repo in repos:
        print("\n\n")
        print(repo['name'])
        
#        for k,v in repo.items():
#            print("\t",k,":",v)

elif r.status_code == 404:
    print("URI not found")


