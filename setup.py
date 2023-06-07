from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()
setup(
    name="cars_solution",
    version="1.0.0",
    packages=["cars"],
    package_data={"": ["data/*.json"]},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "cars-solution = cars.main:exit_handle",
        ],
    },
    install_requires=required,
)
