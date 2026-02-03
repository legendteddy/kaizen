import ast
import os
import re
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT_DIR, "skills")
PATTERNS_DIR = os.path.join(ROOT_DIR, "patterns")
SCAN_DIRS = [SKILLS_DIR, PATTERNS_DIR]

def get_anchors(file_path):
    """Extracts all headers as slugified anchors from a markdown file."""
    anchors = set()
    if not os.path.exists(file_path):
        return anchors
    
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            if line.startswith("#"):
                # Clean header to slug: "## My Header!" -> "my-header"
                text = line.lstrip("#").strip().lower()
                slug = re.sub(r'[^a-z0-9\s-]', '', text).replace(' ', '-')
                anchors.add(slug)
    return anchors

def check_link(url, source_file):
    """
    Returns (Valid: bool, Error: str)
    """
    # 1. Local Paths
    if not url.startswith("http"):
        source_dir = os.path.dirname(source_file)
        
        # Split path and anchor
        parts = url.split('#')
        path_part = parts[0]
        anchor_part = parts[1] if len(parts) > 1 else None
        
        # Empty path means "same file"
        if not path_part:
            target_path = source_file
        else:
            target_path = os.path.abspath(os.path.join(source_dir, path_part))
        
        if not os.path.exists(target_path):
            return False, "File not found"
            
        # Check Anchor if present
        if anchor_part:
            valid_anchors = get_anchors(target_path)
            if anchor_part not in valid_anchors:
                # Fuzzy match try (sometimes Github does wierd things)
                return False, f"Anchor '#{anchor_part}' not found in {os.path.basename(target_path)}"
                
        return True, None

    return True, None # Skip online

def check_python_syntax(code_block):
    """Returns (True, None) or (False, ErrorMessage)"""
    try:
        ast.parse(code_block)
        return True, None
    except SyntaxError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def check_gremlins(content):
    """Returns list of gremlins found"""
    gremlins = []
    patterns = ["TODO", "FIXME", "XXX", "placeholder", "insert text"]
    for p in patterns:
        if p.lower() in content.lower():
            gremlins.append(p)
    return gremlins

def run():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🧪 Starting Deep Inspection (v2.0)...")
    
    failures = []
    total_checks = 0
    passed_checks = 0
    
    link_regex = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    code_regex = re.compile(r'```python(.*?)```', re.DOTALL)
    
    for scan_dir in SCAN_DIRS:
        if not os.path.exists(scan_dir):
            continue
        
        for sk in os.listdir(scan_dir):
            path = os.path.join(scan_dir, sk)
            if not os.path.isfile(path):
                # Handle subdirectories like in skills/, but patterns/ might be flat files
                 path = os.path.join(scan_dir, sk, "SKILL.md")
            
            if not os.path.exists(path): 
                # Fallback for patterns which are .py files or .md files directly
                path = os.path.join(scan_dir, sk)
                if not os.path.isfile(path):
                    continue
            
            # Skip non-markdown/python text files
            if not path.endswith('.md') and not path.endswith('.py'):
                continue

            with open(path, encoding='utf-8') as f:
                content = f.read()
            
            # Special check for .py files: The whole file is code
            if path.endswith('.py'):
                total_checks += 1
                valid, err = check_python_syntax(content)
                if valid:
                    passed_checks += 1
                else:
                    failures.append(f"[BAD SYNTAX] {sk}: {err}")
                continue
                
            # 1. Check Links & Anchors
            for match in link_regex.finditer(content):
                total_checks += 1
                text, url = match.groups()
                valid, err = check_link(url, path)
                if valid:
                    passed_checks += 1
                else:
                    failures.append(f"[BROKEN LINK] {sk}: {text} -> {url} ({err})")
                    
            # 2. Check Code Logic
            for match in code_regex.finditer(content):
                total_checks += 1
                code = match.group(1).strip()
                if "..." in code and len(code) < 20:
                    continue 
                
                valid, err = check_python_syntax(code)
                if valid:
                    passed_checks += 1
                else:
                    failures.append(f"[BAD SYNTAX] {sk}: {err}")
    
            # 3. Check Gremlins
            found_gremlins = check_gremlins(content)
            if found_gremlins:
                total_checks += 1
                failures.append(f"[GREMLIN] {sk}: Found {found_gremlins}")
            else:
                total_checks += 1
                passed_checks += 1
                
    score = (passed_checks / total_checks * 100) if total_checks > 0 else 0
    
    print("\nRESULTS:")
    print(f"Total Deep Checks: {total_checks}")
    print(f"Failures Found: {len(failures)}")
    
    if len(failures) > 0:
        print("\n❌ FAILED INSPECTION:")
        for f in failures:
            print(f"  - {f}")
    
    print(f"\n🔮 Reality Score: {score:.1f}%")

if __name__ == "__main__":
    run()
