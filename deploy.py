import os
import subprocess
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = "Master-Project-Deployer"

# GitHub API URL
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}"

# ✅ Check repository existence
def check_repository():
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(GITHUB_API_URL, headers=headers)

    if response.status_code == 200:
        print(f"✅ Repository '{REPO_NAME}' exists on GitHub.")
    else:
        print(f"❌ Repository '{REPO_NAME}' not found. Please create it first.")

# ✅ Clone repository if not already present
def clone_repository():
    repo_url = f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
    if os.path.exists(REPO_NAME):
        print(f"📁 Repository already exists locally in '{REPO_NAME}'.")
    else:
        print(f"🔄 Cloning repository: {repo_url}")
        subprocess.run(["git", "clone", repo_url])

# ✅ Pull latest changes from GitHub
def pull_updates():
    print(f"📥 Pulling latest changes for '{REPO_NAME}'...")
    subprocess.run(["git", "-C", REPO_NAME, "pull"])

# ✅ Push local changes to GitHub
def push_changes():
    os.chdir(REPO_NAME)
    try:
        subprocess.run(["git", "add", "."], check=True)
        commit_msg = input("📝 Enter commit message (default = Auto Update): ").strip()
        if not commit_msg:
            commit_msg = "🚀 Auto update from deploy.py"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Project pushed successfully.")
    except subprocess.CalledProcessError:
        print("❌ Push failed. Ensure Git is configured properly.")
    finally:
        os.chdir("..")

# ✅ Check Git status
def show_status():
    subprocess.run(["git", "-C", REPO_NAME, "status"])

# 🔽 Menu
def menu():
    while True:
        print("\n📦 GitHub Deployment Menu")
        print("1. Check GitHub repository status")
        print("2. Clone repository")
        print("3. Pull updates")
        print("4. Push changes")
        print("5. Show Git status")
        print("0. Exit")

        choice = input("👉 Enter your choice: ").strip()

        if choice == "1":
            check_repository()
        elif choice == "2":
            clone_repository()
        elif choice == "3":
            pull_updates()
        elif choice == "4":
            push_changes()
        elif choice == "5":
            show_status()
        elif choice == "0":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()
