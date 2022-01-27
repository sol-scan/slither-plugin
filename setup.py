from setuptools import setup, find_packages

setup(
    name="slither-plugin",
    description="This is a slither plugin",
    url = "https://github.com/sol-scan/slither-plugin",
    author="rtm",
    version="0.0.1",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=["slither-analyzer==0.8.2"],
    entry_points={
        "slither_analyzer.plugin": "slither my-plugin=plugin.execute:make_plugin",
    },
)