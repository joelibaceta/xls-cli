import sys
from setuptools import setup, find_packages

setup(
    name="xls-cli",
    version="1.0.0",
    author="Joel Ibaceta",
    author_email="mail@joelibaceta.com",
    license='MIT',
    description="It is a simple python package to explore xls files in the terminal",
    long_description="A simple tool to open and explore a xls file using ascii characters simulated sheet in terminal",
    url="https://github.com/joelibaceta/xls-cli",
    project_urls={
        'Source': 'https://github.com/joelibaceta/xls-cli',
        'Tracker': 'https://github.com/joelibaceta/xls-cli/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=['xlrd'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='xls terminal excel spreadsheet',
    entry_points={
        "console_scripts": [
            'xls-cli=xls_cli.cli:main'
        ]
    }
)