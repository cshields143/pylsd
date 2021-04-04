from setuptools import setup

setup(
    name='pylsd',
    version='0.0.1',
    description='pylsd is the python bindings for LSD - Line Segment Detector',
    author='Gefu Tang',
    author_email='tanggefu@gmail.com',
    license='BSD',
    keywords="LSD",
    url='https://github.com/primetang/pylsd',
    packages=['pylsd', 'pylsd.bindings', 'pylsd.lib'],
    package_dir={'pylsd.lib': 'pylsd/lib'},
    package_data={'pylsd.lib': [
        'darwin/*.dylib', 'win32/x86/*.dll', 'win32/x64/*.dll', 'linux/*.so']},
)
