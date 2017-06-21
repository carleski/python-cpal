import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-cpal',
    version='1.00',
    author='Rob Carleski',
    author_email='carleski@umich.edu',
    description='Colorized Print and Logger',
    long_description=long_description,
    url='https://github.com/carleski/python-cpal',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
    ],
    zip_safe=False
)
