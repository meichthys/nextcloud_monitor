from os import path

import setuptools

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="nextcloudmonitor",
    version="1.6.0",
    description="Python wrapper around nextcloud monitor api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests"],
    py_modules=["nextcloudmonitor"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Networking",
    ],
    url="https://github.com/meichthys/nextcloud_monitor",
)
