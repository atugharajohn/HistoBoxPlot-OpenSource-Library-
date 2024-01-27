from setuptools import setup, find_packages

setup(
    name='HistoBoxPlot',
    version='0.1',
    author="John Atughara",
    author_email="atugharajohn@gmail.com",
    packages=find_packages(),
    description='A Python package to create combined histogram and boxplot visualization',
    install_requires=[
        'matplotlib>=3.1.1',
        'seaborn>=0.9.0'
    ],
    python_requires='>=3.6',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/atugharajohn/HistoBoxPlot'
)

