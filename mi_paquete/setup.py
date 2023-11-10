from setuptools import setup, find_packages

setup(
    name='mi_paquete',
    version='0.1',
    packages=find_packages(),
    package_data={'mi_paquete': ['entrega1.py', 'modulo2.py']},
)



