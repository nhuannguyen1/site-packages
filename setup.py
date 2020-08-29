from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="appnvn",
    version="0.0.1",
    description="A Python package to get weather reports for any location.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nhuannguyen1/site-packages.git",
    author="Nikhil Kumar Singh",
    author_email="nikhilksingh97@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["appnvn"],
    include_package_data=True,
    install_requires=["requests"],
)