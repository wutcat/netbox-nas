from setuptools import find_packages, setup

setup(
    name='netbox-nas',
    version='1.0.4',
    description='Add NAS entities to NetBox',
    long_description_content_type='text/markdown',
    long_description=open('README.md', 'r').read(),
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
