from setuptools import find_packages
from typing import List

def get_requirement(file_path:str)->List[str]:
    '''
    This Function will return list of requirements
    '''
    requirements=[]
    with open('requirement.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n",'')  for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')


setup(
name = 'mlproject',
version='1.0',
author = 'creation',
author_email= 'creation@gmail.com',
packages = find_packages(),
install_requires= get_requirement('requirement.txt')
)