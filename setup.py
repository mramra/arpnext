from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in arpnext/__init__.py
from arpnext import __version__ as version


setup(
	name="arpnext",
	version=version,
	description="arpnext",
	author="arpnext",
	author_email="e@f.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
