import requests
import json

# Search for all GitHub's repositories owned by me
def search_by_username(USERNAME):

    response_user = requests.get(f"https://api.github.com/users/{USERNAME}/repos",
    params={"q": "user:{USERNAME}"},
    )
    json_user = response_user.json()

    my_list = []
    for repo in json_user:
        my_dict = {}
        my_dict['name'] = repo['name']
        description = repo['description']
        my_dict['description'] = description if description != None else ''
        my_dict['url'] = repo['url']
        my_list.append(my_dict)
    return my_list


def search_for_term():
    # Search GitHub's repositories for word supplied by a user in the file name or in the path

    search_term = ""
    while search_term == "":
        try:
            search_term = input("Search for files which contain the word: ")
            response = requests.get(
                "https://api.github.com/search/repositories",
                params={"q": "{search_term} in:file,path" ,"sort": "stars", "order": "desc"},
            )

            # Inspect some attributes of the first ten repositories
            json_response = response.json()
            search_repositories = json_response["items"]
            my_list = []
            for repo in search_repositories[:10]:
                my_dict = {}
                my_dict['name'] = repo['name']
                my_dict['description'] = repo['description']
                my_dict['url'] = repo['url']
                my_list.append(my_dict)
        except ValueError:
            break
        finally:
            return my_list


#List all repositories owned by an owner. End user provides the owner's username.
def search_for_owner():

    USERNAME = ""
    while (USERNAME == ""):

        try:

            my_list = []
            USERNAME = input("Username: ")
            response_user = requests.get(f"https://api.github.com/users/{USERNAME}/repos",
            params={"q": "user:{USERNAME}"},
            )
            json_user = response_user.json()

            for repo in json_user[:10]:
                my_dict = {}
                my_dict['name'] = repo['name']
                description = repo['description']
                my_dict['description'] = description if description != None else ''
                my_dict['url'] = repo['url']
                my_list.append(my_dict)

        except ValueError:
            break

        finally:
            return my_list


#Query the most popular Python repos. Sort the answer by the number of stars.
def most_popular_python_repos():
    # Search GitHub's repositories for popular Python projects
    response = requests.get(
        "https://api.github.com/search/repositories",
        params={"q": "language:python", "sort": "stars", "order": "desc"},
    )

    # Inspect selected attributes of the first ten repositories
    json_response = response.json()
    popular_repositories = json_response["items"]

    my_list = []
    for repo in popular_repositories[:10]:
        my_dict = {}
        my_dict['name'] = repo['name']
        my_dict['description'] = repo['description']
        my_dict['url'] = repo['html_url']
        my_list.append(my_dict)
    return my_list


#Save the response from querying the most popular Python repos locally.
def store_most_popular_python_repos():
    # Search GitHub's repositories for most popular Python repositories

    response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python", "sort": "stars", "order": "desc"},
    )

    if response.status_code == 200:
        new_data = response.json()

        try:
            with open("python_repos_data.json", "r") as json_file:
                existing_data = json.load(json_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            existing_data = []

        existing_data.append(new_data)

        with open("python_repos_data.json", "w") as json_file:
            json.dump(existing_data, json_file, indent=4)
            print("Data appended to python_repos_data.json file.")

        return existing_data

    else:
        print("Failed to retrieve data from the API. Status code:", response.status_code)

def most_popular_harvard_repos():

    # Search GitHub's repositories for word Harvard in the file name or in the path
    response = requests.get(
        "https://api.github.com/search/repositories",
        params={"q": "Harvard in:file,path" ,"sort": "stars", "order": "desc"},
    )

    # Inspect some attributes of the first ten repositories
    json_response = response.json()
    popular_repositories = json_response["items"]

    my_list = []
    for repo in popular_repositories[:10]:
        my_dict = {}
        my_dict['name'] = repo['name']
        my_dict['description'] = repo['description']
        my_dict['url'] = repo['url']
        my_list.append(my_dict)
    return my_list


#Save the response from querying the most popular Harvard repositories locally.
def store_most_popular_harvard_repos():
    # Search GitHub's repositories for word Harvard in the file name or in the path

    response = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": "Harvard in:file,path" ,"sort": "stars", "order": "desc"},
        )

    if response.status_code == 200:
        new_data = response.json()

        with open("harvard_repos_data.json", "w") as json_file:
            json.dump(new_data, json_file, indent=4)
            print("Data appended to harvard_repos_data.json file.")

        return new_data

    else:
        print("Failed to retrieve data from the API. Status code:", response.status_code)


#Save the owner's profile picture locally. In this example the owner's name is set to my username.
def write_img_to_local():

    username = "kaismithereens"
    url = "https://api.github.com/users/{}".format(username)

    response = requests.get(url)
    output = json.loads(response.text)
    response_img = requests.get(output["avatar_url"])

    fp = open("{}.json".format(username), "wb")
    fp.write(response.content)
    fp.close()

    return response_img



