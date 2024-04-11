from setuptools import setup, find_packages

setup(
    name="chemsource",
    version="1.0.0",
    author="Prajit Rajkumar",
    author_email="prajkumar@ucsd.edu",
    description="Tool to classify novel drugs and other health-related" 
                + "chemicals by origin",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "lxml",
        "openai",
        "requests",
        "wikipedia",
    ],
)