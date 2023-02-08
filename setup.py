import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DiscordUtils",
    version="1.3.9",
    author="Murder",
    description="DiscordUtils is a very useful library made to be used with discord.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MurderWolf/DiscordUtils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.6",
    include_package_data=True,
    install_requires=["discord.py"],
    extras_require={"voice": ["discord.py[voice]", "youtube-dl"]}
)
