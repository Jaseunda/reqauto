from setuptools import setup, find_packages
from setuptools.command.install import install
import os

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        os.system('python3 post_install.py')

# Read the contents of your README file
with open("docs/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    cmdclass={'install': PostInstallCommand},
)

setup(
    name="reqauto",
    version="0.1.3",
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
