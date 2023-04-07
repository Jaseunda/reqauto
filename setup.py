from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open("docs/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="reauto",
    version="0.1.1",
    author="Jaseunda",
    author_email="opensource@jaseunda.com",
    description="A Python package to automatically generate and install requirements.txt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/piply",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "setuptools",
    ],
    entry_points={
        "console_scripts": [
            "piply=piply:main",
        ],
    },
    python_requires=">=3.6",
)
