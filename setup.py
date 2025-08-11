from setuptools import setup, find_packages

setup(
    name="github-activity",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "github-activity=github_activity.cli:main",
        ],
    },
    install_requires=[
        "requests",  # якщо будеш використовувати
    ],
    python_requires=">=3.7",
)
