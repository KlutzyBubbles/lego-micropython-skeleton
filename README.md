# lego-micropython-skeleton

![Downloads](https://img.shields.io/pypi/dm/lego-mp-skeleton) ![License](https://img.shields.io/pypi/l/lego-mp-skeleton) ![Version](https://img.shields.io/pypi/v/lego-mp-skeleton) ![Python Version](https://img.shields.io/pypi/pyversions/lego-mp-skeleton)

Branch | Build Status | Test Status | Test Coverage | Code Grade
------ | ------------ | ----------- | ------------- | ----------
Master | ![Build Status](https://img.shields.io/azure-devops/build/leetzilantonisibmcom/e89ff3b5-d86a-4bb3-bcef-40f7255e5d10/3/master) | ![Test Status](https://img.shields.io/azure-devops/tests/leetzilantonisibmcom/LegoExtension/3/master?compact_message) | ![Test Coverage](https://img.shields.io/azure-devops/coverage/leetzilantonisibmcom/legoextension/3/master) | ![Code Grade](https://img.shields.io/codacy/grade/cf0f96b46c484bf9ae6851088780e50e/master)
Dev | ![Build Status](https://img.shields.io/azure-devops/build/leetzilantonisibmcom/e89ff3b5-d86a-4bb3-bcef-40f7255e5d10/3/dev) | ![Test Status](https://img.shields.io/azure-devops/tests/leetzilantonisibmcom/LegoExtension/3/dev?compact_message) | ![Test Coverage](https://img.shields.io/azure-devops/coverage/leetzilantonisibmcom/legoextension/3/dev) | ![Code Grade](https://img.shields.io/codacy/grade/cf0f96b46c484bf9ae6851088780e50e/dev)

NOTE: We have recently dropped support for python 2.7, please make sure you are developing on a machine with python >3.4

## Documentation

We have recently merged out previous repo `lego-micropython-docs` with this repo to simplify the updating process. You can find the docs hosted at <https://klutzybubbles.github.io/lego-micropython-skeleton/>

## About

Skeleton to help with linting programs using the MicroPython functions built for Lego EV3 Mindstorms

Master branch is the branch that has been tested from python 3.4 to 3.7 based off of the functions that are listed in the documentation for lego ev3 python.

Dev branch is for development to tests or updates in the ev3 python docs that need to be tested, although this package doesn't have any working code it is highly reccomended that you stick with the master branch so you dont get confused during development

This package contains NO WORKING CODE! all functions return

### Versions

Version spec MAJOR.MINOR.PATCH.(dev)YYYYMMDDBB with BB being the build number for that day (1-1000)

### Installation

Because this project has no working code, there is no need to include it on the EV3 brick itself. Doing so will break the functionality of the project on the EV3.

So to install the skeleton, on the development machine type `pip install --upgrade lego-mp-skeleton`, Generally development builds are not needed but if you would like to use them just add `--pre` to the installation command.

### PyPi

You can find this project hosted on PyPi here: <https://pypi.org/project/lego-mp-skeleton/>

## Contributing

Contributing is easy :D

1. Fork the dev branch
2. Make your changes
3. Make a pull request into dev

## License

I am in no way affiliated with Lego nor do i have any affiliation with the EV3 or EV3Dev platforms, this is a standalone package to help aid in developing Lego EV3 MicroPython programs.
