import pytest
import os
import responses
from options import search_by_username, store_most_popular_python_repos, most_popular_harvard_repos, store_most_popular_harvard_repos
from welcome import welcome_screen
import json

def test_welcome():
    assert welcome_screen() == 'This program allows users to search through GitHub repositories.\nTo exit the program at any time, press "CTRL" + "D"\n'

@pytest.fixture
def user_data():
    with open('username_repos.json', 'r') as repos_file:
        repos_json = json.load(repos_file)
        return repos_json

@responses.activate
def test_username_search(user_data):
    USERNAME = "octocat"
    responses.add(responses.GET, f"https://api.github.com/users/{USERNAME}/repos", json=user_data)
    assert search_by_username(USERNAME) == [{"name": "Hello-World", "description": "This your first repo!", "url": "https://api.github.com/repos/octocat/Hello-World"}]


def harvard_data():

    with open("harvard_repos_data.json", "r") as harvard_fr:
        harvard_json = json.load(harvard_fr)
    return harvard_json

@responses.activate
def test_Harvard_repos():

    responses.get(
        "https://api.github.com/search/repositories",
        json=harvard_data())
    assert most_popular_harvard_repos()[0]['name'] == 'd2l-en'

def test_store_repos():
    if os.path.exists('python_repos_data.json') == False:
        store_most_popular_python_repos()
    assert os.path.exists('python_repos_data.json') == True

