from setuptools import setup, find_packages

setup(
    name="Document Structure Automation",
    version="0.1.0",
    author="Ankur Mishra",
    author_email="ankurmishra1jan@gmail.com",
    description="A short description of your project",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        # "numpy>=1.23",
        # "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
