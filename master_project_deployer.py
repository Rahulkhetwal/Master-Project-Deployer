import os
import time
import subprocess

# Constants
OWNER_PASSWORD = "masterrahul9731@#"
BASE_PATH = "D:/Master_Project_Deployer/guest_projects/"
UPI_ID = "itzrahul9548437@oksbi"
GITHUB_USERNAME = "your-github-username"  # Replace with your GitHub username

def clear_screen():
    """Clears the terminal screen for better visibility."""
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_screen():
    """Displays the welcome message and user options (only once)."""
    clear_screen()
    print("\n1️⃣ Owner (Rahul) - Full Access")
    print("2️⃣ Guest - Limited or Paid Access")
    print("\nEnter 'exit' to quit.")
    print("-" * 50)

def get_user_choice():
    """Gets user choice and validates input without reprinting the menu."""
    while True:
        choice = input("\n👉 Press 1 for Owner, 2 for Guest, or type 'exit': ").strip().lower()
        if choice in ['1', '2', 'exit']:
            return choice
        print("❌ Invalid choice! Please enter 1 (Owner), 2 (Guest), or 'exit'.")

def owner_login():
    """Handles owner login verification with 3 attempts."""
    attempts = 3
    while attempts > 0:
        password = input(f"🔑 Enter Owner Password ({attempts} attempts left): ")
        if password == OWNER_PASSWORD:
            print("\n✅ Access Granted! Welcome, Rahul!")
            return True
        else:
            attempts -= 1
            print("❌ Incorrect Password! Try again.")

    print("\n⚠️ Too many incorrect attempts! Access BLOCKED.")
    print("🔄 Switching to Guest Mode...\n")
    time.sleep(2)
    return False  # Redirect to Guest Mode

def list_guest_projects():
    """Lists existing guest projects before creating a new one."""
    print("\n📂 Available Guest Projects:")
    
    if os.path.exists(BASE_PATH):
        existing_projects = os.listdir(BASE_PATH)
        if existing_projects:
            for project in existing_projects:
                print(f"  📁 {project}")
        else:
            print("  ❌ No projects found. Be the first to create one!")
    else:
        os.makedirs(BASE_PATH)
        print("  ❌ No projects found. Be the first to create one!")

def create_guest_project():
    """Allows guest users to manually create a project folder and open it in VS Code."""
    list_guest_projects()

    print("\n📂 Create a New Project")
    project_name = input("📝 Enter your project name: ").strip()

    if not project_name:
        print("❌ Project name cannot be empty!")
        return

    project_path = os.path.join(BASE_PATH, project_name)

    if os.path.exists(project_path):
        print("⚠️ Project already exists! Choose a different name.")
        return

    os.makedirs(project_path)
    print(f"✅ Project '{project_name}' created successfully at {project_path}")

    # Create a README.md file with project details
    readme_path = os.path.join(project_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {project_name}\n\nThis is a new guest project created using Master Project Deployer.")

    print(f"📄 README.md file created inside {project_name}")

    # Ask user if they want to open in VS Code
    open_code = input("\n🖥️ Open project in VS Code? (yes/no): ").strip().lower()
    if open_code == 'yes':
        print("🚀 Opening VS Code...")
        subprocess.run(["code", project_path], shell=True)

def create_github_repo(project_name, project_path):
    """Creates a new GitHub repository and pushes the project automatically."""
    print("\n🌍 Creating GitHub Repository...")
    subprocess.run([f"gh repo create {GITHUB_USERNAME}/{project_name} --public --source={project_path} --remote=origin"], shell=True)
    
    # Git Initialization and First Commit
    print("🔧 Initializing Git...")
    subprocess.run(["git", "init"], cwd=project_path)
    subprocess.run(["git", "add", "--all"], cwd=project_path)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=project_path)
    
    # Pushing to GitHub
    print("🚀 Pushing to GitHub...")
    subprocess.run(["git", "branch", "-M", "main"], cwd=project_path)
    subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{GITHUB_USERNAME}/{project_name}.git"], cwd=project_path)
    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=project_path)
    
    print("✅ Project successfully pushed to GitHub!")

def guest_mode():
    """Handles guest user choices and ensures no loopback issue."""
    print("\nGuest Mode Selected:")
    print("1️⃣ Basic Mode - Free (Manual Project Creation)")
    print("2️⃣ Advanced Mode - Paid (Auto-Code + GitHub Push)")

    while True:
        mode = input("👉 Choose mode (1/2): ").strip()
        if mode == '1':
            print("\n📂 Entering Basic Mode (Manual Project Creation)...")
            create_guest_project()
            return  # Exit the function properly
        elif mode == '2':
            print("\n🚀 Entering Advanced Mode (Auto-Code + GitHub Push)...")
            project_name = input("📝 Enter your project name: ").strip()
            project_path = os.path.join(BASE_PATH, project_name)
            os.makedirs(project_path, exist_ok=True)
            create_github_repo(project_name, project_path)
            return  # Exit the function properly
        else:
            print("❌ Invalid choice! Please enter 1 (Basic) or 2 (Advanced).")

def main():
    """Main function to handle user roles without looping back."""
    welcome_screen()  # Show the menu only once

    choice = get_user_choice()

    if choice == '1':  # Owner (Rahul)
        if owner_login():
            print("\n✅ Owner Mode Activated - Full Access Granted!")
            return  # Exit after successful login
        else:
            choice = '2'  # Automatically switch to Guest Mode if owner login fails

    if choice == '2':  # Guest Mode (manual or forced due to login failure)
        guest_mode()  # Ensures once a mode is chosen, no loopback

    elif choice == 'exit':
        print("\n👋 Exiting... Goodbye!")

if __name__ == "__main__":
    main()
