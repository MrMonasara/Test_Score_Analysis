from setuptools import find_packages,setup
from typing import List

HYPNE_E_DOT = '-e.'
def get_requirements(file_path:str) ->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("\n", " ") for req in requirements]

        if HYPNE_E_DOT in requirements:
            requirements.remove(HYPNE_E_DOT)

        return requirements
setup(
    name='MLProject',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'seaborn',
    ],
    # Additional metadata about your project
)