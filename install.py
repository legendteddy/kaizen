import os
import shutil
import sys


def print_header():
    print("==========================================")
    print("   KAIZEN FRAMEWORK - UNIVERSAL INSTALLER")
    print("==========================================")

def get_user_choice():
    print("\nWhich AI Agent are you configuring?")
    print("1. Cursor (.cursorrules)")
    print("2. Claude Code (CLAUDE.md)")
    print("3. Gemini CLI (.gemini/skills)")
    print("4. Manual / Generic")
    
    while True:
        try:
            choice = input("\nEnter choice (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                return choice
        except KeyboardInterrupt:
            sys.exit(0)

def install_cursor():
    print("\n[Cursor Setup]")
    target = ".cursorrules"
    
    # Read universal prompt
    with open("UNIVERSAL_PROMPT.txt", encoding="utf-8") as f:
        prompt = f.read()
        
    # Append to .cursorrules
    mode = "a" if os.path.exists(target) else "w"
    with open(target, mode, encoding="utf-8") as f:
        f.write("\n\n" + prompt)
        
    print(f"Injected Kaizen activation into {target}")
    print("NOTE: Ensure the 'skills/' folder is in your project root.")

def install_claude():
    print("\n[Claude Code Setup]")
    target = "CLAUDE.md"
    
    with open("UNIVERSAL_PROMPT.txt", encoding="utf-8") as f:
        prompt = f.read()
        
    mode = "a" if os.path.exists(target) else "w"
    with open(target, mode, encoding="utf-8") as f:
        f.write("\n\n" + prompt)
        
    print(f"Injected Kaizen activation into {target}")

def install_gemini():
    print("\n[Gemini CLI Setup]")
    # Detect generic home path
    home = os.path.expanduser("~")
    target_skills = os.path.join(home, ".gemini", "skills")
    
    if not os.path.exists(target_skills):
        try:
            os.makedirs(target_skills)
        except OSError:
            print(f"Error: Could not create {target_skills}")
            return

    print(f"Installing skills to {target_skills}...")
    
    source_skills = "skills"
    
    # Simple copy for now
    count = 0
    for item in os.listdir(source_skills):
        s = os.path.join(source_skills, item)
        d = os.path.join(target_skills, item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
            count += 1
            
    print(f"Installed {count} skills to Gemini CLI.")

def main():
    print_header()
    if not os.path.exists("skills"):
        print("Error: Run this from the kaizen root directory.")
        sys.exit(1)
        
    choice = get_user_choice()
    
    if choice == '1':
        install_cursor()
    elif choice == '2':
        install_claude()
    elif choice == '3':
        install_gemini()
    elif choice == '4':
        print("\n[Manual Setup]")
        print("1. Copy 'skills/' to your agent's context.")
        print("2. Paste content of 'UNIVERSAL_PROMPT.txt' into system prompt.")
        
    print("\nInstallation Complete. Kaizen is active.")

if __name__ == "__main__":
    main()
