from setuptools import find_packages, setup

setup(
    name="py3dbp",
    version="1.1.0",
    packages=find_packages(),
    install_requires=["numpy", "matplotlib"],
    author="Boxme",
    author_email="",
    description="A 3D bin packing problem solver",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Boxme-Global/py3dbp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
