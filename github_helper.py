import requests
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = os.getenv("GITHUB_REPO_OWNER")
REPO = os.getenv("GITHUB_REPO_NAME")

def get_repo_info():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_open_issues():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()
