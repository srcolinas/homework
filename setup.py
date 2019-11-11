import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="homework",
    version="0.0.1",
    author="Sebastian Rodriguez Colina",
    author_email="srcolinas@gmail.com",
    description="A package to create programming assignments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/srcolinas/homework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'cryptography'
    ]
)