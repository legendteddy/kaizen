
import pytest

from kaizen_core.tools import SecurityError, ToolManager


@pytest.fixture
def workspace(tmp_path):
    return tmp_path

@pytest.fixture
def tools(workspace):
    return ToolManager(workspace)

def test_read_write_file(tools, workspace):
    file_path = "test.txt"
    content = "Hello, Kaizen!"
    
    # Write
    result = tools.write_file(file_path, content)
    assert "Success" in result
    assert (workspace / file_path).read_text(encoding='utf-8') == content
    
    # Read
    read_content = tools.read_file(file_path)
    assert read_content == content

def test_security_jail_break(tools):
    # Try to access parent directory
    with pytest.raises(SecurityError):
        tools._validate_path("../secret.txt")
        
    with pytest.raises(SecurityError):
        tools._validate_path("/etc/passwd")

def test_command_whitelist(tools):
    # Allowed
    assert "STDOUT" in tools.run_shell("echo 'test'")
    
    # Blocked (not in whitelist)
    assert "SECURITY ALERT" in tools.run_shell("rm -rf /")
    
    # Blocked (chaining)
    assert "SECURITY ALERT" in tools.run_shell("ls && rm test")
