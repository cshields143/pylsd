from setuptools import setup

setup(
    name='py3lsd',
    version='0.1.0',
    description='python bindings for LSD - Line Segment Detector',
    author='Chris Shields',
    author_email='christopher.shields143@gmail.com',
    license='BSD',
    keywords="LSD",
    url='https://github.com/cshields143/pylsd',
    packages=['pylsd', 'pylsd.bindings', 'pylsd.lib'],
    package_dir={'pylsd.lib': 'pylsd/lib'},
    package_data={'pylsd.lib': ['*.so']},
)
