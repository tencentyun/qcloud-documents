## Feature Description
This migration tool is used to migrate files from services such as AWS S3, Alibaba Cloud OSS and Qiniu Cloud to COS. It also allows migration of a list of files from given URLs to COS.
## Service Limits
Only applicable to COS V4. Not available in Chongqing (ap-chongqing), Seoul (ap-seoul), and Mumbai (ap-mumbai).

## Operating Environment
### System Environment
Linux or Mac system
### Software Dependencies
Python 2.7.x, pip, gcc and python-dev.
#### Installation and Configuration
1. For more information on how to install Python 2.7.x, please see [Install and Configure Python](https://cloud.tencent.com/document/product/436/10866).
2. Install pip, gcc and python-dev:
```
sudo yum install python-pip python-devel gcc g++
```

## How to Use
### Obtaining Tool
[Link to Github](https://github.com/tencentyun/cos_migrate_tool) 
### Installation Method
Installation using pip is recommended. For more information on how to install pip, please see [pip official website](https://pip.pypa.io/en/latest/installing/). Alternatively, you can use apt/yum and other package management tools to install python-pip package.
```
 pip install -U cos_migrate_tool
```
![Migration tool 1](//mc.qcloudimg.com/static/img/1b576204b2d16c368be9a6bca908b014/image.png)
After the above command is executed, check whether the tool has been installed using the following command:
```
cos_migrate_tool -h
```
The following returned result indicates a successful installation:
![Migration tool 2](//mc.qcloudimg.com/static/img/04495932eebaae7e5099830cbe73f2e1/image.png)
<span id="Configuration file"></span>
### Configuration File
Configuration file template is located in `./cos_migrate_tool-master/conf`. The following shows an example of configuration:
Assume that the data is migrated from OSS to COS, configure the basic information in "common" section (workspace is a working directory), the data source information (OSS attributes) in "source" section, and the COS attributes in "destination" section.

**Delete notes (`# note`) from configuration file. Blank template can be found on [GitHub page](https://github.com/tencentyun/cos_migrate_tool/tree/master/conf).**
#### Migration from OSS
```
[common]
workspace=/tmp/tmp6
threads=20           # Number of threads. Default is 10.
 
[source]
type=oss
accesskeyid=         # oss accesskey id
accesskeysecret=     # oss accesskey secret
bucket=              # Name of bucket to be migrated
endpoint=            # The endpoint of OSS, such as oss-cn-beijing.aliyuncs.com

[destination]
type=cosv4
region=sh                  # The region of COS, such as sh, gz
accesskeyid=               # The accesskeyid of COS
appid=                     # The appid of COS
accesskeysecret=           # The accesskeysecret of COS
bucket=sdktest             # COS bucket
prefix_dir=/dir21          # The COS directory to which all files are migrated. If it is not configured, files are migrated to the root directory.
```
#### Migration from Qiniu Cloud
```
[common]
workspace=/tmp/tmp11


[source]
type=qiniu
accesskeyid=               # The accesskeyid of Qiniu
accesskeysecret=           # The accesskeysecret of Qiniu
bucket=                    # Qiniu bucket to be migrated
domain_url=                # The download domain name of Qiniu

[destination]
type=cosv4
region=sh                  # The region of COS, such as sh, gz
accesskeyid=               # The accesskeyid of COS
appid=                     # The appid of COS
accesskeysecret=           # The accesskeysecret of COS
bucket=sdktest             # COS bucket
prefix_dir=/dir21          # The COS directory to which all files are migrated. If it is not configured, files are migrated to the root directory.
```
#### Migration from S3
```
[common]
workspace=/tmp/tmp21

[source]
type=s3
accesskeyid=               # The accesskey id of S3
accesskeysecret=           # The accesskey secret of S3
bucket=                    # Name of S3 bucket to be migrated
region=                    # Required for S3 in China

[destination]
type=cosv4
region=shanghai
accesskeyid=
appid=
accesskeysecret=
bucket=
```
#### Migrating List File
```
[common]
workspace=

[source]
type=url
url_list_file=/tmp/urllist.txt   # The list file containing URLs of files to be migrated, with each complete URL in a separate row
timeout=3                        # The timeout of HTTP request

[destination]
type=cosv4
region=
accesskeyid=
appid=
accesskeysecret=
bucket=
```
### Running Tool
After the tool has been installed, an executable command `cos_migrate_tool` is provided for all the subsequent migration processes. The command is executed as follows:
```
cos_migrate_tool -c /path/to/your/conf
```
Write a configuration file by referring to the [Configuration File](#Configuration File) section. In the configuration file, you need to configure a working directory to store all the temporary files generated during the migration process. Make sure that the directory has sufficient space. Use different directories for multiple migration tasks performed in parallel.
During the migration process, you can view the fail_file.txt in your working directory to obtain the list of files failed to be migrated.
### How to Uninstall
Run the following command:
```
pip uninstall cos_migrate_tool
```
## FAQs
1. The pip command does not exist. 
Use the command `apt install python-pip` or `yum install python-pip` to install PIP.
2. Failed to install the migration tool using pip.
Execute `sudo pip install cos_migrate_tool`.

