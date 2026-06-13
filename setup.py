'''
The setup.py file is an essentila part of packagnig and distributing Python projects.
It is used by setuptools (or distutils in older Python versions) to define the configurations
of yor projects, such as metadata, depencies, and more.
'''

from setuptools import find_packages, setup 

# find_packages -> Looks through each folder and search for __init__.py
# wherever it finds then its consider its immediate parent as a pacakage.

from typing import List

def get_requirements()-> List[str]:
    """
    This fuction returns list of requirements.
    """

    requirement_list:List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # Ignore the empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print('Requirements.txt Not Found')

    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Aftabalam Makandar",
    author_email = "aftabalam.makandar81@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)
