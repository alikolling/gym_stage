import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gym_stage",
    version="0.1.0",
    author="Alisson H. Kolling",
    author_email="alikolling@gmail.com",
    description="Gym environment for stage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alikolling/stage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['gym']
)
