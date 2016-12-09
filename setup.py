from setuptools import setup, find_packages
from helga_quip import __version__ as version


setup(
    name='helga-quip',
    version=version,
    description=('Match quips and other witticisms'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat :: Internet Relay Chat'],
    keywords='irc bot quip joke jokes',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/helga-quip',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=['helga', 'requests'],
    test_suite='tests',
    entry_points=dict(
        helga_plugins=[
            'quip = helga_quip.plugin:quip',
        ],
    ),
)
