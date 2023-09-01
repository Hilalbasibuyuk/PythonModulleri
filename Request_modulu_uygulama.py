import requests

class GitHub:
    def __init__(self):
        self.api_url = ("https://api.github.com")
        self.token = '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'

    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    
    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username + "/repos")
        return response.json()
    
    def createRepositories(self,name):
        response = requests.post(self.api_url +'user/repos?access_token='+ self.token ,json={ 
            "name" : name ,
            "description": "This is your first repository",
            "homepage" : "https://hilalbasibuyuk.com"
            })
        return response.json()
    
github = GitHub()

while True:
    secim = input("1-Find User\n2-Get Repositories\n3-Create Repositories\n4-Exit\nSeçim: ")

    if secim == "4":
        break
    else:
        if secim=="1":
            username = input("Username: ")
            result = github.getUser(username)
            print(f"name: {result['name']} public repos : {result['public_repos']} follower: {result['followers']}")
        elif secim == "2":
            username = input("Username: ")
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim == "3":
            name = input("repository name: ")
            result = github.createRepositories(name)
            print(result)
        else:
            print("Yanlış bir rakam girdiniz!")
