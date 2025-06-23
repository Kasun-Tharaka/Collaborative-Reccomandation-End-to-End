# to make this project as a local package for import different componets in development

# find_package is nothing but, search for init.py and if it is there it will conside as a local package(able to import anywhere)

from setuptools import setup, find_packages

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

REPO_NAME = "Machine Learning Book Recommendation System"
AUTHOR_NAME = "KASUN THARAKA"
SRC_REPO = 'Book_Recommendor'
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version="0.0.1",
    author="KASUN THARAKA",
    description="Machine Learning Recommendation pakcage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kasun-Tharaka/Collaborative-Reccomandation-End-to-End",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)