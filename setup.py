import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csv_to_xlsx",
    version="0.0.5",
    author="Russ Lamb",
    author_email="revoltingrobot@gmail.com",
    description="Convert CSV and TSV to XLSX files using openpyxl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/russlamb/file_convert",
    packages=setuptools.find_packages(),
    install_requires=['openpyxl'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
