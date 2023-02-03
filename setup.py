import setuptools

"""
Author       : PandaWithBeard
Date         : 2023-02-03 02:30:41
LastEditors  : PandaWithBeard
LastEditTime : 2023-02-03 02:30:41
FilePath     : /zhdate/setup.py
Description  : 
"""

with open("README.md", "r", encoding="utf8") as file:
    long_description = file.read()

setuptools.setup(
    name="zh_lunar_date",
    version="0.0.1",
    author="Kylin",
    author_email="l1328076914@gmail.com",
    description="A pachage to convert Chinese Lunar Calendar to datetime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chen-kay/zhdate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
