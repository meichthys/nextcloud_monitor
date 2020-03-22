import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="nextcloudmonitor",
    version="0.0.4",
    description="Python wrapper around nextcloud monitor api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests"],
    py_modules=["nextcloudmonitor"],
)
