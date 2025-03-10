import os
import time
import subprocess

# Constants
OWNER_PASSWORD = "masterrahul9731@#"
BASE_PATH = "D:/Master_Project_Deployer/guest_projects/"
UPI_ID = "itzrahul9548437@oksbi"

def clear_screen():
    """Clears the terminal screen for better visibility."""
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_screen():
    """Displays the welcome message and user options."""
    clear_screen()
    print("="*50)
    print("🚀 Welcome to Master Project Deployer 🚀")
    print("="*50)
    print("\n1️⃣ Owner (Rahul) - Full Access")
    print("2️⃣ Guest - Limited or Paid Access")
    print("\nEnter 'exit' to quit.")
    print("-"*50)

def get_user_choice():
    """Gets user choice and validates input."""
    while True:
        choice = input("👉 Select your role (1/2): ").strip().lower()
        if choice in ['1', '2', 'exit']:
            return choice
        print("❌ Invalid choice! Please enter 1 (Owner), 2 (Guest), or 'exit'.")

def owner_login():
    """Handles owner login verification with 3 attempts."""
    attempts = 3
    while attempts > 0:
        password = input(f"🔑 Enter Owner Password ({attempts} attempts left): ")
        if password == OWNER_PASSWORD:
            print("✅ Access Granted! Welcome, Rahul!")
            return True
        else:
            attempts -= 1
            print("❌ Incorrect Password! Try again.")

    print("\n⚠️ Too many incorrect attempts! Access BLOCKED.")
    print("🔄 Switching to Guest Mode...\n")
    time.sleep(2)
    return False  # Redirect to Guest Mode

def guest_mode():
    """Handles guest user choices."""
    print("\nGuest Mode Selected:")
    print("1️⃣ Basic Mode - Free (Manual Project Creation)")
    print("2️⃣ Advanced Mode - Paid (Auto-Code + GitHub Push)")

    while True:
        mode = input("👉 Choose mode (1/2): ").strip()
        if mode in ['1', '2']:
            return mode
        print("❌ Invalid choice! Please enter 1 (Basic) or 2 (Advanced).")

def create_guest_project():
    """Allows guest users to manually create a project folder and open in VS Code."""
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

    # Ask user if they want to open in VS Code
    open_code = input("\n🖥️ Open project in VS Code? (yes/no): ").strip().lower()
    if open_code == 'yes':
        print("🚀 Opening VS Code...")
        subprocess.run(["code", project_path], shell=True)

def process_payment(amount):
    """Handles guest user payment and cashback."""
    print(f"\n💰 Payment Required: ₹{amount}")
    print(f"📲 Pay via UPI: {UPI_ID}")
    input("\n💳 Press Enter after completing the payment...")

    cashback = amount // 10  # ₹1 cashback for every ₹10 spent
    print(f"🎉 Payment Successful! You will receive ₹{cashback} cashback.")

def generate_auto_code(project_name):
    """Automatically generates basic project structure and code."""
    project_path = os.path.join(BASE_PATH, project_name)
    os.makedirs(project_path, exist_ok=True)

    main_file = os.path.join(project_path, "main.py")
    with open(main_file, "w") as f:
        f.write('print("Hello, this is your automated project!")')

    print(f"✅ Auto-generated code saved in {main_file}")
    return project_path  # Return project path for preview

def preview_project(project_path):
    """Displays the generated code for user approval before pushing to GitHub."""
    print("\n🔍 Project Preview:")
    print("="*50)
    
    for file in os.listdir(project_path):
        file_path = os.path.join(project_path, file)
        print(f"\n📄 {file}")
        print("-"*50)
        with open(file_path, "r") as f:
            print(f.read())

    print("="*50)

    while True:
        approval = input("\n✅ Approve project for GitHub push? (yes/no): ").strip().lower()
        if approval in ['yes', 'no']:
            return approval == 'yes'
        print("❌ Invalid input! Please enter 'yes' or 'no'.")

def push_to_github(project_name, guest_github_url):
    """Pushes project to guest's GitHub repository."""
    project_path = os.path.join(BASE_PATH, project_name)

    os.system(f'cd "{project_path}" && git init')
    os.system(f'cd "{project_path}" && git add .')
    os.system(f'cd "{project_path}" && git commit -m "Initial Commit"')
    os.system(f'cd "{project_path}" && git branch -M main')
    os.system(f'cd "{project_path}" && git remote add origin {guest_github_url}')
    os.system(f'cd "{project_path}" && git push -u origin main')

    print(f"🚀 Project successfully pushed to {guest_github_url}")

def advanced_mode():
    """Handles guest users in Advanced Mode with payment, auto-code, preview, and GitHub push."""
    print("\n🔹 Advanced Mode Selected")
    project_name = input("📝 Enter project name: ").strip()

    if not project_name:
        print("❌ Project name cannot be empty!")
        return

    project_complexity = int(input("\n🔢 Choose complexity (1 - Simple, 2 - Medium, 3 - Complex): "))
    
    price_mapping = {1: 10, 2: 30, 3: 50}
    amount = price_mapping.get(project_complexity, 10)  # Default to ₹10 if invalid choice

    process_payment(amount)
    project_path = generate_auto_code(project_name)

    if preview_project(project_path):
        guest_github_url = input("\n🔗 Enter your GitHub repo URL: ").strip()
        if guest_github_url:
            push_to_github(project_name, guest_github_url)
    else:
        print("❌ Project rejected by the user. Modifications needed before push.")

def main():
    """Main function to handle user roles."""
    while True:
        welcome_screen()
        choice = get_user_choice()

        if choice == '1':  # Owner (Rahul)
            if owner_login():
                print("\n✅ Owner Mode Activated - Full Access Granted!")
                break
            else:
                choice = '2'  # Redirect to Guest Mode if owner login fails

        if choice == '2':  # Guest
            mode = guest_mode()
            if mode == '1':  # Basic Mode
                create_guest_project()
            elif mode == '2':  # Advanced Mode
                advanced_mode()

        elif choice == 'exit':
            print("\n👋 Exiting... Goodbye!")
            break

        input("\nPress Enter to continue...")  # Pause before clearing screen

if __name__ == "__main__":
    main()
