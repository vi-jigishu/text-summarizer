import os
from pathlib import Path    
import logging

logging.basicConfig(level=logging.INFO, format='[%(ascitime)s]:%(message)s:')


#CREATING THE PROJECT STRUCTURE. projectname will contain the whole structure.
project_name= "textSummarizer"    #textSummarizer is the name for the project

list_of_files=[
    ".github/workflows/.gitkeep",    #will be used for ci/cd deployment
    f"src/{project_name}/__init__.py",   #init.py is a of constructor file
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging//__int__.py",
    f"src/{project_name}/config/__int__.py",
    f"src/{project_name}/pipeline/__int__.py",
    f"src/{project_name}/entity/__int__.py",
    f"src/{project_name}/constants/__int__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py"
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    #THE PACKAGE WILL  CONTAIN ALL THESE FILES. we may even need extra files later on, which we will create manually there.
]


#LOGIC FOR THE CREATION OF THE ABOVE FILES

for filepath in list_of_files:    #assigns each file path to the variable 'filepath'
    filepath= Path(filepath)      #will assign the path according to the operating system by using pathlib libbrary
    filedir, filename= os.path.split(filepath)     #split function return file direcory and file name of filepah variable.
    
    if filedir != "":     #creating folders when filedir is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating direcory: {filedir} for the file{filename}")
    
    
    #creating files inside the folder
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):            #checking that the file doesnt exist or if it exists but has length 0: then only create the file.
        with open(filepath, "w") as f:   #opening the file path in write mode
            pass              #we dont want to make any chnages right now so will just pass the file
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} already exists.")
                
   
