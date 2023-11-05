#couldnt understand what the projecttools in setuptools.setup() is doing

import setuptools

with open("README.md", "r", encoding="utf-8") as f:          #all the guideline will be stored in README.md
    long_description=f.read()


__version__="0.0.0"

REPO_NAME = "text-summarizer"
AUTHOR_USER_NAME= "vijigishu"
SRC_REPO= "textSummarizer"
AUTHOR_EMAIL= "priyanshubhusan07@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },    #additional project related urls
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")   #to automatically discover and list all packages wihin specified "src" directory  
)
