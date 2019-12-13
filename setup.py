# MK-Img2fig: Markdown Img to Figure
#
# Copyright (c) 2019 Mandaris Moore
#
# GNU License

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    author="Mandaris Moore",
    author_email="MK-Img2fig@MandarisMoore.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Topic :: Documentation",
        "Topic :: Text Processing :: Markup",
    ],
    description="Figure and figcaption generator markdown extension",
    entry_points={
        "markdown.extensions":
        ["MK-Img2fig = MK-Img2fig:MK-Img2FigExtension"]
    },
    install_requires=requirements,
    keywords="markdown image figure caption html a11y",
    license="GPLv3+",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="Mandaris Moore",
    maintainer_email="MK-Img2fig@MandarisMoore.com",
    name="MK-Img2fig",
    packages=setuptools.find_packages(),
    python_requires=">=3.5.*, <4",
    url="https://github.com/mandaris/MK-Img2fig",
    version="0.1",
)
