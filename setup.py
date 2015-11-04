from setuptools import setup

setup(
    name='cloudify-diamond-plugin',
    version='1.3rc1',
    author='Cloudify',
    author_email='cosmo-admin@gigaspaces.com',
    description='Cloudify Diamond monitoring plugin',
    packages=['diamond_agent', 'cloudify_handler'],
    install_requires=['cloudify-plugins-common>=3.3rc1',
                      'ConfigObj==5.0.6',
                      'psutil==2.1.1'],
)
