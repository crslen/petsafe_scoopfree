import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="petsafe_scoopfree",
    version="1.0",
    author="Chris Lennon",
    license="MIT",
    author_email="lennonc@gmail.com",
    description="Provides ability to connect and control a PetSafe Scoopfree device using the PetSafe-Scoopfree API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crslen/petsafe_scoopfree",
    packages=setuptools.find_packages(),
    install_requires=["requests", "boto3"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
