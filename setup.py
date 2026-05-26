#this will help to build ur ml model as package and use it
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
#func to install package
def get_requirements(file_path:str)->list[str]:
    "this func will return the list of requiremnets"
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requiremennts=[req.replace("\n","  ") for req in requirements ]
        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT)
            
setup(
    name="Ml_project",
    version="0.0.1",
    author="Rajveer",
    author_email="rajveersinghvs2004@gmail.com",
    packages=find_packages(),
    # install_requires=["pandas","numpy","seaborn"]
    install_requires=get_requirements("requirements.txt")
    

)