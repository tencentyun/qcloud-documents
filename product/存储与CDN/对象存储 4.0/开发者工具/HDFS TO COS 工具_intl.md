## Feature Description
HDFS TO COS is used to copy the data on HDFS to Tencent Cloud COS.

## Operating Environment
### System Environment
Linux/Windows system
### Software Dependencies
JDK 1.7/1.8 
#### Installation and Configuration
For more information on the installation and configuration of environment, please see [Install and Configure Java](https://cloud.tencent.com/document/product/436/10865).
## Configuration and Usage
### How to Configure
1. For more information on how to install Hadoop-2.7.2 or later, please see [Install and Test Hadoop](/doc/product/436/10867).
2. Download HDFS TO COS at [here](https://github.com/tencentyun/hdfs_to_cos_tools) and decompress it.
3. Copy core-site.xml in the HDFS cluster to be synchronized to the conf folder. core-site.xml contains the configuration information of NameNode.
4. Edit the configuration file `cos_info.conf`, bucket, region, and API key. The provided name of "bucket" should be the full name including the appid provided by Tencent. E.g. "mybucket-125000000".
5. Specify a location for the configuration file in the command line parameter. By default, it is located at `conf/cos_info.conf`.
> <font color="#0000cc">**Note: ** </font>
If the command line parameter conflicts with the configuration file, the command line parameter prevails.

### How to Use
(Take Linux as an example)
#### View Help
```
./hdfs_to_cos_cmd -h
```
The execution result is as follows:
![WeChat Image_20170807163035](//mc.qcloudimg.com/static/img/dcff34d37928c0d8b9c4b45c25ac116e/image.png)

#### Copying File
- If the file you copy from HDFS to COS has the same name with a file originally stored in COS, the latter will be overwritten.
```
./hdfs_to_cos_cmd --hdfs_path=/tmp/hive --cos_path=/hdfs/20170224/
```
-  If the file you copy from HDFS to COS has the same name and length with a file originally stored in COS, the copy will be ignored.
```
./hdfs_to_cos_cmd --hdfs_path=/tmp/hive --cos_path=/hdfs/20170224/ -skip_if_len_match
```
Only file length is used as a metric, because calculating file summaries of Hadoop takes too much work.

#### Directories
```
conf: Configuration file, which stores core-site.xml and cos_info.conf
log: log directory
src: Java source program
dep: Runnable JAR package generated after compilation
```
## Q&A
#### About Configuration Information
Make sure you enter the correct configuration information, including bucket, region and API key. The provided name of "bucket" should be the full name including the appid provided by Tencent. E.g. "mybucket-125000000". Make sure the time difference between the server and Beijing time does not exceed 1 minute. Otherwise, reset the server time.
#### About DateNode
Make sure DateNode can be connected with the server that contains the replication program. NameNode can be connected because it has a public IP. But the DateNode server that contains the obtained block only has a private IP, it cannot be connected directly. It is recommended to execute the synchronization program at a Hadoop node, so that both NameNode and DateNode can be accessed.
#### About Permissions
Use Hadoop command to download and check files, and then use synchronization tools to synchronize data on Hadoop.
#### About File Overwriting
If the file you copy from HDFS to COS has the same name with a file originally stored in COS, the latter will be overwritten by default. If a user specifies `-skip_if_len_match`, the copy will be skipped when the file you copy from HDFS to COS has the same name and length with a file originally stored in COS.
#### About COS path
 COS path is a directory by default, and all the files copied from HDFS are stored in the directory.

