import unittest
import os
import yaml

class TestKaizenIntegrity(unittest.TestCase):
    
    def setUp(self):
        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.skills_dir = os.path.join(self.root, "skills")
        
    def test_skills_have_frontmatter(self):
        """Ensure every SKILL.md has valid YAML frontmatter"""
        for skill_name in os.listdir(self.skills_dir):
            skill_path = os.path.join(self.skills_dir, skill_name)
            if not os.path.isdir(skill_path):
                continue
                
            readme = os.path.join(skill_path, "SKILL.md")
            self.assertTrue(os.path.exists(readme), f"Missing SKILL.md in {skill_name}")
            
            with open(readme, 'r', encoding='utf-8') as f:
                content = f.read()
                
            self.assertTrue(content.startswith("---"), f"{skill_name} missing frontmatter start")
            self.assertIn("\n---", content[3:], f"{skill_name} missing frontmatter end")

    def test_universal_prompt_exists(self):
        """Critical activation file must exist"""
        path = os.path.join(self.root, "UNIVERSAL_PROMPT.txt")
        self.assertTrue(os.path.exists(path))

if __name__ == '__main__':
    unittest.main()

