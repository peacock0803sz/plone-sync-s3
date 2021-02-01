import pathlib

from setuptools import setup, find_packages  # type: ignore

requires = [
    "click",
    "boto3",
    "boto3-stubs[s3]",
]
test_requires = [
    "pytest",
    "moto",
]
readme = open(pathlib.Path(__file__).parent.resolve() / "README.md").read()

setup(
    name="plone_sync_s3",
    version="1.0.0a1",
    description="Scripts for syncing Plone data between local and AWS S3",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Framework :: Plone",
    ],
    author="Peacock",
    author_email="contact@peacock0803sz.com",
    url="https://github.com/peacock0803sz/plone-sync-s3",
    keywords="Plone Python AWS",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={"tests": test_requires},
    entry_points="""\
    [console_scripts]
    s3sync = plone_sync_s3.router:cli
    """,
)
