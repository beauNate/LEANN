"""
Test Python 3.9 compatibility for type hints.

This test ensures that all modules using PEP 604 syntax (dict[str, Any], list[str])
have the proper `from __future__ import annotations` import for Python 3.9 compatibility.
"""

import ast
import sys
from pathlib import Path


def test_python39_type_hint_compatibility():
    """
    Verify that all Python files using modern type hints have future annotations.

    PEP 604 (dict[str, Any], list[str] syntax) was added in Python 3.10.
    For Python 3.9 compatibility, files must use `from __future__ import annotations`.
    """
    leann_core_src = Path(__file__).parent.parent / "packages" / "leann-core" / "src" / "leann"
    
    if not leann_core_src.exists():
        # Skip test if path doesn't exist (e.g., in installed package)
        return
    
    files_needing_future_import = []
    files_with_issue = []
    
    for py_file in leann_core_src.glob("*.py"):
        if py_file.name == "__init__.py":
            continue
            
        content = py_file.read_text(encoding="utf-8")
        
        # Check if file uses PEP 604 syntax (dict[...] or list[...] in type hints)
        # Simple heuristic: look for these patterns in the file
        uses_modern_hints = ("dict[" in content or "list[" in content)
        
        if not uses_modern_hints:
            continue
            
        files_needing_future_import.append(py_file.name)
        
        # Parse the file to check for future annotations import
        try:
            tree = ast.parse(content, filename=str(py_file))
            has_future_import = False
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    if node.module == "__future__":
                        for alias in node.names:
                            if alias.name == "annotations":
                                has_future_import = True
                                break
            
            if not has_future_import:
                files_with_issue.append(py_file.name)
                
        except SyntaxError as e:
            # If we can't parse the file, it's already broken
            files_with_issue.append(f"{py_file.name} (syntax error: {e})")
    
    # Report findings
    if files_with_issue:
        error_msg = (
            f"The following files use PEP 604 type hints (dict[...], list[...]) "
            f"but lack 'from __future__ import annotations' for Python 3.9 compatibility:\n"
            f"{chr(10).join('  - ' + f for f in files_with_issue)}\n\n"
            f"Files checked: {len(files_needing_future_import)}\n"
            f"Files with issues: {len(files_with_issue)}\n"
            f"Python version: {sys.version}"
        )
        raise AssertionError(error_msg)


def test_import_leann_on_python39():
    """
    Test that core LEANN modules can be imported on Python 3.9.
    
    This is a basic smoke test to ensure type hint syntax doesn't break imports.
    """
    try:
        # These imports should work on Python 3.9 with proper future annotations
        from leann import LeannBuilder, LeannSearcher  # noqa: F401
        from leann.api import compute_embeddings  # noqa: F401
        
        # If we get here without errors, type hints are properly handled
        assert True
        
    except TypeError as e:
        if "is not subscriptable" in str(e):
            raise AssertionError(
                f"Type hint compatibility issue on Python {sys.version}: {e}\n"
                "This likely means a file is missing 'from __future__ import annotations'"
            )
        raise
