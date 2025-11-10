from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    """
    requirement_list:List[str] = []
    try:
        with open('requirements.txt') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except Exception as e:
        print("requirements.txt file not found !!!!!!")
        
    return requirement_list
print(get_requirements())

setup(
    name="trip-agent",
    version="0.1.0",
    author="Sreenav Jajerao",
    author_email="sreenavjajerao@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
                
                