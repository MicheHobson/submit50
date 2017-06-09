from setuptools import setup

setup(
    author="CS50",
    author_email="sysadmins@cs50.harvard.edu",
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Utilities"
    ],
    description="This is submit50, with which you can submit solutions to problems for CS50.",
    install_requires=["backports.shutil_get_terminal_size", "pexpect>=4.0", "requests", "six", "termcolor"],
    keywords=["submit", "submit50"],
    name="submit50",
    scripts=["submit50"],
    url="https://github.com/cs50/submit50",
    version="2.2.0"
)
