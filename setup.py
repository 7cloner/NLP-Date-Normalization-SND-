from setuptools import setup, find_packages

setup(
    name='NLP Date Normalization (SND)',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'jdatetime',
    ],
    author='Nasser Khaledi',
    author_email='foray00227@gmail.com',
    description='This library is part of the NLP project which analyzes the Persian text given to it and extracts all'
                ' Jalalian and Gregorian dates and converts them into a standard format in Gregorian date.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='لینک پروژه شما',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
