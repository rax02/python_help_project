"""
Setup script for the Python package.

This script is used to build, package, and distribute the Python package. It includes
metadata about the package such as its name, version, author, and dependencies.

Attributes:
    NAME (str): The name of the package.
    VERSION (str): The version of the package.
    DESCRIPTION (str): A brief description of the package.
    LONG_DESCRIPTION (str): A detailed description of the package, typically read from a README file.
    AUTHOR (str): The name of the package author.
    AUTHOR_EMAIL (str): The email address of the package author.
    URL (str): The URL for the package's homepage.
    PACKAGES (list): A list of all Python import packages that should be included in the distribution package.
    INSTALL_REQUIRES (list): A list of dependencies required for the package to run.
    CLASSIFIERS (list): A list of classifiers that provide some additional metadata about the package.
    PYTHON_REQUIRES (str): The Python version requirement for the package.

Functions:
    setup(): The main function that sets up the package using the provided metadata.
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """Reads the requirements file and returns the list of dependencies."""
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt') as f:
            lines=f.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement !='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('Requirements file not found.')
    except Exception as e:
        print('An error occurred while reading the requirements file.')
    return requirement_lst
    
setup(
    name='python-package-template',
    version='0.0.1',
    description='A template for creating Python packages.',
    long_description='A template for creating Python packages.',
    author_email='0001rkm@gmail.com',
    author='Ravi Maurya',
    packages=find_packages(),
    install_requires=get_requirements()

)