from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(filepath : str) -> List[str]:
    """Get requirements from a file."""

    requirements = []

    with open(filepath) as file_obj : 
        requirements = file_obj.readlines()

        requirements = [req.replace('\'n' , "") for req in requirements]
        requirements 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
 # metadata
name= "TrackVision" ,
version= '0.0.0' , 
author= 'Sultanahmed-99' , 
author_email='sultanworker@gmail.com' , 
packages= find_packages() , 
install_requires = get_requirements('requirements.txt') , 

)

# This code block sets up the metadata
#  for the project, including the project name,
#   version number, author, author email,
#   and required packages. The 'find_packages' 
#   function is used to automatically detect and 
#   include all project packages. 
#   The 'install_requires'
#    argument specifies 
#    the required packages that need to be installed 
#    in order to run the project successfully.