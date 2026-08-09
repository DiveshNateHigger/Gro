#!/usr/bin/env python
"""
Verification script for Plant Disease Detection Application
This script checks the environment, dependencies, and file structure
"""

import os
import sys
import importlib
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    print(f"Python version: {sys.version}")
    if sys.version_info < (3, 8):
        print("❌ Python version should be 3.8 or higher")
        return False
    print("✅ Python version OK")
    return True

def check_dependencies():
    """Check if all required packages are installed"""
    required_imports = {
        "flask": "flask",
        "flask_sqlalchemy": "flask_sqlalchemy",
        "pillow": "PIL",
        "torch": "torch",
        "torchvision": "torchvision",
        "pandas": "pandas",
        "numpy": "numpy",
        "python-dotenv": "dotenv"
    }
    
    all_installed = True
    for display_name, import_name in required_imports.items():
        try:
            importlib.import_module(import_name)
            print(f"✅ {display_name} is installed")
        except ImportError:
            print(f"❌ {display_name} is not installed")
            all_installed = False
    
    return all_installed

def check_file_structure():
    """Check if all required files and directories exist"""
    required_files = [
        "run.py",
        "requirements.txt",
        "README.md",
        "data/disease_info.csv",
        "data/supplement_info.csv",
        "models/plant_disease_model_1.pt"
    ]
    
    required_dirs = [
        "app",
        "data",
        "models",
        "static",
        "static/css",
        "static/js",
        "static/uploads",
        "templates"
    ]
    
    all_files_exist = True
    all_dirs_exist = True
    
    # Check files
    for file_path in required_files:
        if not os.path.isfile(file_path):
            print(f"❌ File missing: {file_path}")
            all_files_exist = False
        else:
            print(f"✅ File exists: {file_path}")
    
    # Check directories
    for dir_path in required_dirs:
        if not os.path.isdir(dir_path):
            print(f"❌ Directory missing: {dir_path}")
            all_dirs_exist = False
        else:
            print(f"✅ Directory exists: {dir_path}")
    
    return all_files_exist and all_dirs_exist

def check_model_compatibility():
    """Check if the model file is compatible with installed torch version"""
    if not os.path.isfile("models/plant_disease_model_1.pt"):
        print("❌ Model file is missing")
        return False
        
    try:
        import torch
        # Attempt to load model - this will fail if incompatible
        print("Testing model loading...")
        model = torch.load("models/plant_disease_model_1.pt", map_location=torch.device('cpu'))
        print(f"✅ Model can be loaded with torch {torch.__version__}")
        return True
    except Exception as e:
        print(f"❌ Model loading failed: {str(e)}")
        return False

def main():
    """Main verification function"""
    print("\n" + "="*50)
    print("Plant Disease Detection Application - Verification")
    print("="*50 + "\n")
    
    # Path checks
    print("Current directory:", os.getcwd())
    print("\n" + "-"*50)
    print("CHECKING PYTHON ENVIRONMENT")
    print("-"*50)
    python_ok = check_python_version()
    
    print("\n" + "-"*50)
    print("CHECKING DEPENDENCIES")
    print("-"*50)
    deps_ok = check_dependencies()
    
    print("\n" + "-"*50)
    print("CHECKING FILE STRUCTURE")
    print("-"*50)
    files_ok = check_file_structure()
    
    print("\n" + "-"*50)
    print("CHECKING MODEL COMPATIBILITY")
    print("-"*50)
    model_ok = check_model_compatibility()
    
    # Summary
    print("\n" + "="*50)
    print("VERIFICATION SUMMARY")
    print("="*50)
    print(f"Python environment: {'✅ OK' if python_ok else '❌ Issues found'}")
    print(f"Dependencies: {'✅ OK' if deps_ok else '❌ Issues found'}")
    print(f"File structure: {'✅ OK' if files_ok else '❌ Issues found'}")
    print(f"Model compatibility: {'✅ OK' if model_ok else '❌ Issues found'}")
    
    if all([python_ok, deps_ok, files_ok, model_ok]):
        print("\n✅ All checks passed! The application should run correctly.")
        print("Run 'python run.py' to start the application.")
    else:
        print("\n❌ Some checks failed. Please fix the issues before running the application.")
        print("See the HELP.md file for troubleshooting information.")
    
if __name__ == "__main__":
    main() 