from distutils.core import setup

def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except IOError:
        return ''


setup(
    name='jb_test',
    version='0',
    author='sinotec2',
    author_email='sinotec2@gmail.com',
    packages=['jb_test'],
    url='http://github.com/sinotec2/jb_test',
    license='LICENSE',
    description='Python library for the book Modeling and Simulation in Python.',
    long_description=readme(),
)
