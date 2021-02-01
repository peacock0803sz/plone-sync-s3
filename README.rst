plone-sync-s3
=============

Scripts syncing Plone data between local and AWS S3

Installation
------------

Just run ``pip install plone_sync_s3``

Uses
----

`
$ s3sync push path/to/datadir
$ s3sync pull path/to/datadir
`

Features
--------

- Compress blobstorage and filestorage as tar, and upload to S3
- Download them from S3, and extract to specific directory

Dependences
-----------

- boto3 https://github.com/boto/boto3
- click https://github.com/pallets/click

