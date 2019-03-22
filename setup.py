from setuptools import setup, find_packages

setup(
    name='firstpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='package containing recursive and sorting functions',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/MbusoMthimkhul/firstpackage',
    author='Mbuso mthimkhulu',
    author_email='mthimkhulu.mbuso15@gmail.com'
)
