"""
Package config for scrape tumblr
"""
import setuptools

setuptools.setup(
    name='scrape_tumblr',
    version='1.0.0',
    description='Scrape posts from tumblr\'s search page',
    url='https://github.com/Deafjams/scrape_tumblr',
    author='Emma Foster',
    license='MIT',
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    package_dir={
        'scrape_tumblr': 'scrape_tumblr'
    },
    packages=setuptools.find_packages(),
    classifiers=(
        "Development Status :: 5 - Production",
        "License :: Public Domain",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7"
    )
)
