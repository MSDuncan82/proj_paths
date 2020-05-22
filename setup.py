from setuptools import find_namespace_packages, find_packages, setup

setup(
    name="proj_path",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    version="0.1.0",
    description="A way to easily access directories and files in a project",
    author="Michael Duncan",
    license="MIT",
)
