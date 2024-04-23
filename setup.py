from setuptools import setup, find_packages

setup(
    name="chemsource",
    version="1.0.0",
    author="Prajit Rajkumar",
    author_email="prajkumar@ucsd.edu",
    description="Tool to classify novel drugs and other health-related" 
                + "chemicals by origin",
    package_dir={"": "chemsource"},
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "lxml",
        "openai",
        "requests",
        "wikipedia",
    ],
)