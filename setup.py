from setuptools import setup, find_packages
from typing import List
import os

def get_requirements(file_path: str = 'requirements.txt') -> List[str]:
    """
    Safely reads requirements from a file, handling various edge cases.
    Returns empty list if file doesn't exist or has parsing errors.
    """
    requirements = []
    
    # Check if file exists
    if not os.path.exists(file_path):
        return requirements
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file_obj:
            for line in file_obj:
                line = line.strip()
                
                # Skip empty lines, comments, and editable installs
                if not line or line.startswith('#') or line == '-e .':
                    continue
                
                # Handle cases where requirements might have comments after them
                requirement = line.split('#')[0].strip()
                if requirement:
                    requirements.append(requirement)
    
    except Exception as e:
        print(f"Warning: Error reading requirements file: {e}")
        return []
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Apoorva',
    author_email='apoorvadhume@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires='>=3.6',
)


