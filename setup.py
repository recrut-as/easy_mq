import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy_mq",
    version="0.0.3",
    author="Halvor Bø",
    author_email="halvor@recrut.no",
    description="Currently internal. Package to simplefy the using pika.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/recrut-as/easy_mq",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)