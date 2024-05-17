from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "APS_ML_project"
AUTHOR_USER_NAME = "param-unik"
SRC_REPO = "sensor"
AUTHOR_EMAIL = "param.unik@gmail.com"


def read_requirements(file_path="requirements.txt"):
    """
    Read the requirements.txt file and return a list of dependencies,
    excluding lines with '-e .'.
    """
    requirements = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#") and line != "-e .":
                requirements.append(line)
    return requirements


install_requires = read_requirements()

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=find_packages(),
    install_requires=install_requires,
)
