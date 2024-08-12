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
    long_description=open('README.md').read(),  # README dosyasından uzun açıklama alır
    long_description_content_type='text/markdown',  # README dosyasının formatı (Markdown)
    url="https://github.com/yourusername/textmakerapi",  # Proje URL'si
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
