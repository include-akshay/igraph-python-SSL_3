import setuptools

# with open("README.md", "r", encoding="utf-8") as fhand:
#     long_description = fhand.read()

setuptools.setup(
    name="igraph",
    version="1.1.3",
    author="Anurag/Akshay/Nitesh",
    author_email="asharma@yaiims.edu",
    description="(Added three functionalities to enhance igraph)",
    url="https://github.com/include-akshay/igraph-python-SSL_3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["Igraph"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True,

)