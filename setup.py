import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="partial_transform",
    version="0.1.0",
    author="cm-hirano-shigetoshi",
    author_email="hirano.shigetoshi@classmethod.jp",
    description="This command allows you to apply text transform command to a part of each line.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cm-hirano-shigetoshi/partial_transform",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['partial_transform = partial_transform.partial_transform:main']
    },
    python_requires='>=3.7',
)