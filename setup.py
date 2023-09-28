import setuptools

__version__ = "0.0.1"

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

REPO_NAME = "CNNClassifier"

AUTHOR_NAME = "Yipu Lerina"
SRC_REPO = "cnnclassifier"
AUTHOR_EMAIL = "yipulerina29@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="This is my CNN Classification project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    )