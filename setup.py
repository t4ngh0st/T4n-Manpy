from setuptools import setup, find_packages

setup(
    name="t4n-manpy",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "t4n = t4n_manpy.main:main"
        ]
    },
    install_requires=[
        # Add dependencies if needed
    ],
)
