import pathlib

from setuptools import setup, find_packages

requires = [
    "boto3",
]
test_requires = [
    "moto[s3]",
]
readme = open(pathlib.Path(__file__).parent.resolve() / "README.md").read()

setup(
    name="plone_sync_s3",
    version="0.9.3-alpha2",
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
    s3sync pull = plone_sync_s3.pull:main
    s3sync push = plone_sync_s3.push.main
    """,
)
