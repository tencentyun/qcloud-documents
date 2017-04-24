## Feature Description

This migration tool is used to migrate files from services such as AWS S3, Aliyun OSS, Qiniu, to COS. It can also migrate file lists, which means migrating files to COS based on given URLs. **Only applicable to COS 4.0**

## Operating Environment

### System Environment

Linux, Mac OS

### Required Software

Operation platform for this tool is \*nix. An environment of Python2.6 or above is required, and pip, gcc, python-dev should be installed on the machine. You may use the package manager (included in the system) to install relevant depended resources.

In centos, use the following command to install:
```bash
sudo yum install python-pip python-devel gcc
```

In ubuntu/debian, use the following command to install:
```bash
sudo apt-get install python-pip python-dev gcc
```
## How to Use

### Acquire the Tool

Github project: https://github.com/tencentyun/cos_migrate_tool

### How to Install

It is recommended to use pip for installation. Refer to the [Official Site](https://pip.pypa.io/en/latest/installing/) to learn about how to install pip, or use package managers (such as apt, yum) to install python-pip package.

```bash
 pip install -U cos_migrate_tool
    
```
After executing the command above, you can check whether the installation is successful by using the following command.
```bash
cos_migrate_tool -h
```

### Configuration File

Configure file template. "common" section is for basic configurations, "workspace" is the workspace directory mentioned above. "source" section is for configuring data source information. Configure oss attributes if you wish to migrate oss to cos. "destination" section is for configuring cos attributes.

**Please delete the annotation texts in configuration files (`# Annotation`). Refer to [Link](https://github.com/tencentyun/cos_migrate_tool/tree/master/conf) for a blank template**

```bash
[common]
workspace=/tmp/tmp6   # Workspace directory
threads=20            # Number of working threads. 10 threads if not configured

[source]
type=oss
accesskeyid=
accesskeysecret=
bucket=
endpoint=

[destination]
type=cosv4
region=shanghai
accesskeyid=
appid=
accesskeysecret=
bucket=sdktest
```

#### Migrate Files in OSS

```bash
[common]
workspace=/tmp/tmp6

[source]
type=oss
accesskeyid=         # oss accesskey id
accesskeysecret=     # oss accesskey secret
bucket=              # Name of the bucket to be migrated
endpoint=            # endpoint of oss, for example: oss-cn-beijing.aliyuncs.com

[destination]
type=cosv4
region=shanghai            # region of cos, such as shanghai, guangzhou
accesskeyid=               # accesskeyid of cos
appid=                     # appid of cos
accesskeysecret=           # accesskeysecret of cos
bucket=sdktest             # bucket of cos
prefix_dir=/dir21          # Directory of cos. Migrated files will be placed under this directory (root directory if not configured)
```

#### Migrate Files in Qiniu

```bash
[common]
workspace=/tmp/tmp11
       

[source]
type=qiniu
accesskeyid=               # accesskeyid of qiniu
accesskeysecret=           # accesskeysecret of qiniu
bucket=                    # qiniu bucket to be migrated
domain_url=                # Download domain of qiniu

[destination]
type=cosv4
region=shanghai            # region of cos, such as shanghai, guangzhou
accesskeyid=               # accesskeyid of cos
appid=                     # appid of cos
accesskeysecret=           # accesskeysecret of cos
bucket=sdktest             # bucket of cos
prefix_dir=/dir21          # Directory of cos. Migrated files will be placed under this directory (root directory if not configured)
```

#### Migrate Files is S3

```bash
[common]
workspace=/tmp/tmp21

[source]
type=s3
accesskeyid=               # accesskey id of s3
accesskeysecret=           # accesskey secret of s3
bucket=                    # Name of the s3 bucket to be migrated

[destination]
type=cosv4
region=shanghai
accesskeyid=
appid=
accesskeysecret=
bucket=

```

#### Migrate Lists of Files

```bash
[common]
workspace=

[source]
type=url
url_list_file=/tmp/urllist.txt   # The list file containing the URLs of files to be migrated. Each line in the file contains a complete URL
timeout=3                        # Timeout for HTTP requests 

[destination]
type=cosv4
region=
accesskeyid=
appid=
accesskeysecret=
bucket=
```

### Run the Tool

Once installed, there will be an executable command `cos_migrate_tool` in the system, which will be used for all subsequent migration operations. How to execute this command:

```bash
cos_migrate_tool -c /path/to/your/conf
```

Modify the configuration file according to the templates mentioned above. You need to configure a workspace directory in the configuration file. Temporary files generated in migration operations will be stored in this directory, so please make sure there is enough storage space for this directory. It is recommended to use different directories if there are multiple concurrent migration tasks.

During the migration process, you can check the fail_file.txt (located in the workspace directory you configured) to view the list of files that weren't migrated successfully.

### How to Uninstall

Run the following command:

```
pip uninstall cos_migrate_tool
```

## FAQs
1. pip command does not exist.  Use "apt install python-pip" or "yum install python-pip" to install pip.
2. Failed to use pip to install migration tool. Try executing "sudo pip install cos_migrate_tool".


