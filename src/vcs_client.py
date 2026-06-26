import requests

GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789"
GITHUB_API_URL = "https://api.github.com"


def list_repositories(owner: str) -> list:
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    url = f"{GITHUB_API_URL}/users/{owner}/repos"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def create_issue(owner: str, repo: str, title: str, body: str) -> dict:
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"
    payload = {"title": title, "body": body}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()


def get_commit_history(owner: str, repo: str) -> list:
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/commits"
    response = requests.get(url, headers=headers)
    return response.json()
