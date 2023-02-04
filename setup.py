from setuptools import setup, find_packages

setup(
    name='pythonScrapeWithRequest',
    packages=find_packages(),
    version='2.0.0',
    install_requires=[
        'pandas',
        'orjson',
        'fake-useragent',
        'requests',
        'bs4',
        'urllib3'
    ]
)
