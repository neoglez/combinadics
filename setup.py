
"""
Created on Wed Jun 02 13:30:10 2021
@author: neoglez
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='combinadics',  
     version='0.0.1',
     author="Yansel Gonzalez Tejeda",
     author_email="neoglez@gmail.com",
     description="Combinatorial system of degree k ranking and unranking.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/neoglez/combinadics",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2",
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     

 )
