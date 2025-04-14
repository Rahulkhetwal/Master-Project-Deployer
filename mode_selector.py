import subprocess

def select_mode():
    print("🎯 Welcome to Code Editor Launcher")
    print("1. Basic Mode")
    print("2. Advanced Mode")
    print("3. Cold Email Generator")
    print("4. Exit")
    
    choice = input("Select your option (1/2/3/4): ").strip()

    if choice == '1':
        print("🚀 Launching Basic Editor...\n")
        subprocess.run(["python", "basic_editor.py"])
    elif choice == '2':
        print("🚀 Launching Advanced Editor...\n")
        subprocess.run(["python", "advanced_editor.py"])
    elif choice == '3':
        print("📧 Launching Cold Email Generator...\n")
        subprocess.run(["python", "cold_email_generator.py"])
    elif choice == '4':
        print("👋 Exiting Project Launcher.")
    else:
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    select_mode()
