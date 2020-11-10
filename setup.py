import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gaming-functions-DobbyK", # Replace with your own username
    version="0.1.3",
    author="Dobby King",
    author_email="dobbyk@techie.com",
    description="A small package not really meant for production, learning mostly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DobbyK/Heartlife",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
