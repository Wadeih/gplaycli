from setuptools import setup
import os
import sys

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(name='gplaycli',
		version='3.30',
		description='GPlayCli, a Google play downloader command line interface',
		long_description=long_description,
		long_description_content_type="text/markdown",
		author="Matlink",
		author_email="matlink@matlink.fr",
		url="https://github.com/Wadeih/gplaycli",
		license="AGPLv3",
		entry_points={
			'console_scripts': [
				'gplaycli = gplaycli.gplaycli:main',
			],
		},
		packages=[
			'gplaycli',
		],
		package_dir={
			'gplaycli': 'gplaycli',
		},
		data_files=[
			['etc/gplaycli', ['gplaycli.conf']],
		],
		install_requires=[
				'gpapi-auth-fixed @ git+https://github.com/Wadeih/googleplay-api@master#egg=gpapi-auth-fixed',
				'pyaxmlparser',
		],

)
