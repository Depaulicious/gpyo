from setuptools import setup

setup(
    name = "gpyo",
    version = "0.1",
    author = "Davide Depau",
    author_email = "davide@depau.eu",
    description = ("Simple script that uses PyWiring to toggle pins on an I2C GPIO board"),
    license = "GPLv2",
    keywords = "wiring i2c gpio io",
    url = "http://github.com/Depaulicious/gpyo",
    packages=['gpyo'],
    install_requires=["pywiring"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Programming Language :: Python",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
)