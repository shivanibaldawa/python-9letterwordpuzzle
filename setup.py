import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wordpuzzle",
    version="0.1.0",
    author="Shivani Baldawa",
    author_email="shivani.baldawa@marlo.com.au",
    description="Word Puzzle Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=
    "https://gitlab.com/theMarloGroup/training/students/sbaldawa/python-9letterwordpuzzle",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL 3",
        "Operating System :: OS Independent",
    ])
