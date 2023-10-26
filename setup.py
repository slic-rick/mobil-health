from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mobile_clinic/__init__.py
from mobile_clinic import __version__ as version

setup(
	name="mobile_clinic",
	version=version,
	description="An ERP for managing a clinic",
	author="Wellness Warriors",
	author_email="erickabraham63@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
