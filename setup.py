import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lego-mp-skeleton",
    version="0.1.8" + os.environ['PACKAGE_BUILD'],
    author="Lee Tzilantonis",
    author_email="LTzilantonis@gmail.com",
    description="Skeleton for the Lego EV3 MicroPython Port",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires="enum34",
    url="https://github.com/klutzybubbles/lego-micropython-skeleton",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
