from setuptools import setup, find_namespace_packages

setup(name='car_price',
    version='1.0.1',
    description='car cost calculation',
    url='https://github.com/Koallla/goit-python/tree/main/lesson7/clean_folder',
    author='Mihail Zmiiov',
    author_email='zmiyov2422@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['car = car_price.price_car:tax_auction']})