from setuptools import setup

setup(
    name="wpm",
    scripts=["src/scripts/wpm"],
    version="1.9",
    description="Console app for measuring typing speed in words per minute (WPM)",
    author="Christian Stigen Larsen",
    author_email="csl@csl.name",
    packages=["wpm"],
    package_dir={"wpm": "src/wpm"},
    package_data={"wpm": ["data/examples.json"]},
    include_package_data=True,
    install_requires=["urwid"],
    url="https://github.com/cslarsen/wpm",
    download_url="https://github.com/cslarsen/wpm/tarball/v1.9",
    license="https://www.gnu.org/licenses/agpl-3.0.html",
    long_description=open("README.rst").read(),
    zip_safe=True,
    keywords=["wpm", "typing", "typist"],
    platforms=["unix", "linux", "osx", "cygwin", "win32"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
