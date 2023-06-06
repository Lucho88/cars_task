from setuptools import setup

with open('cars/requirements.txt') as f:
    required = f.read().splitlines()
setup(
    name="cars_task_solution",
    version="1.0.0",
    packages=["cars"],
    entry_points={
        "console_scripts": [
            "cars-solution = cars.main:exit_handle",
        ],
    },
    install_requires=required
)