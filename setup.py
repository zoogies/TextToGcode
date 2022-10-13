import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TextToGcode",  # Replace with your own username
    version="1.4.0",
    author="Ryan Zmuda",
    author_email="ryanzmuda@gmail.com",
    description="Convert strings to gcode commands.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yoyolick/TextToGcode",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
