from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

requires = ["betfairlightweight", "betfairutil[files]>=0.1.1", "ipywidgets"]

setup(
    name="betfairviz",
    version="0.1.0",
    description="Create visualisations of Betfair order books",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Maurice Berk",
    author_email="maurice@mauriceberk.com",
    url="https://github.com/mberk/betfairviz",
    packages=["betfairviz"],
    install_requires=requires,
    tests_require=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)
