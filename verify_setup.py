#!/usr/bin/env python3
"""
ReCom - Setup Verification Script
==================================

This script checks if your development environment is properly configured.

Run this after installing requirements.txt to verify everything works.

Usage:
    python verify_setup.py
"""

import sys
import platform


def check_python_version():
    """
    Verify Python version meets requirements.
    
    ReCom requires Python 3.13.0, but will work with 3.9+
    We check if the version is at least 3.9
    """
    print("=" * 70)
    print("CHECKING PYTHON VERSION")
    print("=" * 70)
    
    version = sys.version_info
    current_version = f"{version.major}.{version.minor}.{version.micro}"
    
    print(f"Current Python version: {current_version}")
    print(f"Running on: {platform.system()} {platform.release()}")
    
    # Check if Python version is at least 3.9
    if version.major >= 3 and version.minor >= 9:
        print("✅ Python version is compatible!")
        return True
    else:
        print("❌ Python version is too old. Please upgrade to Python 3.9 or higher.")
        return False


def check_required_packages():
    """
    Try importing all Phase 0 required packages.
    
    This verifies that requirements.txt was installed correctly.
    """
    print("\n" + "=" * 70)
    print("CHECKING REQUIRED PACKAGES (Phase 0)")
    print("=" * 70)
    
    # List of (package_name, import_name) tuples
    # Some packages have different import names than pip package names
    packages = [
        ("numpy", "numpy"),
        ("pandas", "pandas"),
        ("scipy", "scipy"),
        ("matplotlib", "matplotlib"),
        ("seaborn", "seaborn"),
        ("jupyter", "jupyter"),
        ("ipython", "IPython"),
    ]
    
    all_ok = True
    
    for package_name, import_name in packages:
        try:
            # Dynamically import the package
            module = __import__(import_name)
            
            # Try to get version if available
            version = getattr(module, "__version__", "unknown")
            
            print(f"✅ {package_name:20s} (version: {version})")
            
        except ImportError:
            print(f"❌ {package_name:20s} NOT FOUND")
            all_ok = False
    
    return all_ok


def check_directory_structure():
    """
    Verify the project directory structure exists.
    
    Checks for key directories that should be present.
    """
    print("\n" + "=" * 70)
    print("CHECKING DIRECTORY STRUCTURE")
    print("=" * 70)
    
    import os
    
    # Expected directories
    directories = [
        "data",
        "data/raw",
        "data/processed",
        "notebooks",
        "src",
        "models",
        "tests",
        "docs",
    ]
    
    all_ok = True
    
    for directory in directories:
        if os.path.isdir(directory):
            print(f"✅ {directory}/")
        else:
            print(f"⚠️  {directory}/ NOT FOUND (will be created when needed)")
            # Note: We don't mark this as failure since some dirs are created later
    
    return all_ok


def check_git_setup():
    """
    Check if git is initialized and configured.
    
    Verifies git repository exists and has basic config.
    """
    print("\n" + "=" * 70)
    print("CHECKING GIT SETUP")
    print("=" * 70)
    
    import os
    import subprocess
    
    # Check if .git directory exists
    if not os.path.isdir(".git"):
        print("⚠️  Git repository not initialized")
        print("   Run: git init")
        return False
    
    print("✅ Git repository initialized")
    
    # Check git config
    try:
        # Check if user.name is configured
        result = subprocess.run(
            ["git", "config", "user.name"],
            capture_output=True,
            text=True,
            check=True
        )
        username = result.stdout.strip()
        print(f"✅ Git user.name: {username}")
        
        # Check if user.email is configured
        result = subprocess.run(
            ["git", "config", "user.email"],
            capture_output=True,
            text=True,
            check=True
        )
        email = result.stdout.strip()
        print(f"✅ Git user.email: {email}")
        
        return True
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️  Git not configured or not in PATH")
        print("   Configure with:")
        print("   git config --global user.name \"Your Name\"")
        print("   git config --global user.email \"your.email@example.com\"")
        return False


def print_next_steps():
    """
    Print helpful next steps after verification.
    """
    print("\n" + "=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    print("""
1. ✅ Environment setup complete!

2. Start Jupyter Notebook:
   jupyter notebook

3. Create your first notebook in the notebooks/ directory

4. Begin Phase 0: Data Acquisition and Exploration
   - Choose a dataset (Last.fm, Million Song, or synthetic)
   - Perform exploratory data analysis
   - Understand the data characteristics

5. Commit your initial setup to git:
   git add .
   git commit -m "Initial project setup"
   git remote add origin https://github.com/YOUR_USERNAME/ReCom.git
   git push -u origin main

Happy coding! 🎵
""")


def main():
    """
    Main function - runs all verification checks.
    """
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "ReCom Setup Verification" + " " * 29 + "║")
    print("╚" + "=" * 68 + "╝")
    print("\n")
    
    # Run all checks
    checks = [
        check_python_version(),
        check_required_packages(),
        check_directory_structure(),
        check_git_setup(),
    ]
    
    # Print summary
    print("\n" + "=" * 70)
    print("VERIFICATION SUMMARY")
    print("=" * 70)
    
    if all(checks):
        print("✅ All checks passed! Your environment is ready.")
        print_next_steps()
        return 0
    else:
        print("⚠️  Some checks failed. Please review the output above.")
        print("\nCommon fixes:")
        print("- Install packages: pip install -r requirements.txt")
        print("- Initialize git: git init")
        print("- Create directories: mkdir -p data/raw data/processed notebooks src models tests docs")
        return 1


if __name__ == "__main__":
    # Exit with proper code (0 = success, 1 = failure)
    sys.exit(main())
