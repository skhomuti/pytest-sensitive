from setuptools import setup, find_packages

PACKAGE = "pytest-sensitive"

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Framework :: Pytest",
    "Intended Audience :: Developers",
    'License :: OSI Approved :: Apache Software License',
    "Operating System :: POSIX",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS :: MacOS X",
    "Topic :: Software Development :: Testing",
    "Topic :: Software Development :: Quality Assurance",
    "Topic :: Utilities",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",

]

setup_requires = [
    "setuptools_scm"
]

install_requires = [
]


if __name__ == '__main__':
    setup(
        name=PACKAGE,
        version="0.0.1",
        description="Hide pytest sensitive information easily",
        license="Apache-2.0",
        install_requires=install_requires,
        setup_requires=setup_requires,
        keywords="pytest pytest-plugin sensitive testing",
        packages=find_packages(where="src"),
        entry_points={"pytest11": ["pytest_sensitive = src.plugin"]},
        package_dir={"": "src"},
        url="https://github.com/skhomuti/pytest-sensitive",
        author="Sergey Khomutinin",
        author_email="skhomuti@gmail.com",
        classifiers=classifiers,
    )
