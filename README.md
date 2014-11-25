# Cob

Cob, yet another yum S3 plugin, provides the way to accessing yum repository hosted on AWS S3. 

What's the difference between Cob and original [yum s3 plugin](https://github.com/henrysher/yum-s3-iam)?

* Support more secure **AWS Signature Version 4** while original one still in __version 2__,
  especially for the new region **eu-central-1** only SigV4 allowed
* Hook on higher layer of Yum built-in library to avoid complicated low-level handlings
* Support static AWS credentials prior to IAM role
* Add retry mechanism to fetch IAM role credentials

## Quick Start

* Installation

  * **./install.sh**
   * plugin conf: **cob.conf** --> /etc/yum/pluginconf.d/cob.conf
   * plugin code: **cob.py**   --> /usr/lib/yum-plugins/cob.py

* Setup minimal IAM Role Policy for Cob

  ```json
  {
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "s3:GetObject"
        ],
        "Resource": "*"
      }
    ]
  }
  ```
* Configure your yum repo conf under **/etc/yum.repos.d/**, like the example below **cob.repo**

  ```ini
  [cob]
  name=cob
  baseurl=https://your-bucket-name-0.s3.amazonaws.com/repo-name/arch/
          https://your-bucket-name-1.s3-eu-west-1.amazonaws.com/repo-name/arch/
          https://your-bucket-name-2.s3-us-west-2.amazonaws.com/repo-name/arch/
  failovermethod=priority
  enabled=1
  gpgcheck=0
  ```
  * add the bucket region name in the baseurl as shown in the example,
    especially for **us-east-1**, like **your-bucket-name-0**, no region name needed there
  * s3 endpoint reference: http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region


* An example from **cob.conf** is taken to indicate its usages:

  ```ini
  [main]
  cachedir=/var/cache/yum/$basearch/$releasever
  keepcache=1
  debuglevel=4
  logfile=/var/log/yum.log
  exactarch=1
  obsoletes=0
  gpgcheck=0
  plugins=1
  distroverpkg=centos-release
  enabled=1

  [aws]
  # access_key = 
  # secret_key =
  timeout = 60
  retries = 5
  metadata_server = http://169.254.169.254
  ```
  * set **main/enabled=1** to enable this yum plugin
  * for static AWS credentials, you could specify via **aws/access_key**, **aws/secret_key**
  * **aws/timeout** and **aws/retries**, used to indicate params in the way of fetching IAM role credentials
  * **metadata_server** used to help testing
