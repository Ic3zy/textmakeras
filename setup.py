from setuptools import setup, find_packages

setup(
    name="textmaker",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "Pillow",
        "requests",
    ],
    author="Ic3zy",
    author_email="abdullah51dundar51@gmail.com",
    description="Textmaker Api",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/abdullah5151/textmaker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
