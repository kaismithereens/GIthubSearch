# GITHUB SEARCH

This project interacts with the GitHub API to search for repositories and users, and displays the relevant data in a table format. It uses two distinct API endpoints provided by GitHub's REST API.

## Features

### 1. GitHub REST API Search
- **Search Repositories:** This feature allows searching for repositories based on various criteria, similar to how you might search on Google. The API can return up to 100 results per page, but this project limits the displayed results to 10 for clarity and efficiency.

### 2. GitHub REST API Repository Management
- **List User Repositories:** This feature lists public repositories owned by a specified user. If a username is provided, the project fetches and displays all public repositories for that user. If the user does not exist, it will handle that case gracefully.

## Project Structure

The project is structured as follows:
- **README.md:** Documentation file explaining the project.
- **project.py:** The main Python script that interacts with the GitHub API, fetches data, and displays the search results.
- **requirements.txt:** Lists the dependencies required to run the project.
- **test_project.py:** Contains unit tests to ensure the project functions correctly.
- **Locally saved files:**
  - `harvard_repos_data.json`
  - `kaismithereens.json`
  - `python_repos_data.json`
 
These files store locally saved search results after using one of the three project's functions.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/kaismithereens/GithubSearch
   cd GithubSearch
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project:
   ```bash
   python project.py
   ```

## Usage

- **Search for Repositories:** The project provides a simple interface to search for repositories based on different criteria such as language, topics, or keywords. 

There are three different functions used to showcase sample criteria, 
i) displays ten most popular Python repositories,
ii) displays ten most popular Harvard repositories, 
iii) prompts the end user for the search term and displays repositories that match the search term.


- **List Repositories of a User:** 

There are two different functions used to showcase this functionality:
i) displays all repositories owned by me,
ii) prompts the end user to enter a GitHub username to retrieve a list of all their public repositories.

- **Save the search results:**

There are three different functions used to showcase this functionality:
i) saves the most popular Harvard repositories locally
ii) saves the most popular Python repositories locally
iii) saves my user profile information locally

## Testing

Run the following command to execute the unit tests:
```bash
pytest test_project.py
```
