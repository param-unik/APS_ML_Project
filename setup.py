from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list: List[str] = []
    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    with open('requirements.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#') and line != '-e .':
                requirement_list.append(line)
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Paramjit",
    author_email="param.unik@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(), 
)