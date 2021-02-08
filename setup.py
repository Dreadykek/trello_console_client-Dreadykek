import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="trello_client-Dreadykek", version="0.0.1", author="Danil",
    author_email="zdanil2000@gmail.com", description="small app for create, move or read lists on boards in trello",
    long_description=long_description, long_description_content_type="text/markdown",
    url="https://github.com/Dreadykek/trello_client", packages=setuptools.find_packages(),
    classifiers=[ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ],
    python_requires='>=3.6',
)