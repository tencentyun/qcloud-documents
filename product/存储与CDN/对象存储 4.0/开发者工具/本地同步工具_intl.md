## Feature Description
This tool is used to synchronize sub-files and sub-directories under a local directory to COS.
### How It Works
COS local synchronization tool obtains a user's local file list, upload files and record the upload results locally. The local file list is re-obtained every time you use the tool and is compared with the record of the uploaded local files under db directory. Then, the following policies are used:
  1. Upload new local files to COS.
  2. Replace existing files in COS with modified local files. 
  3. Skip and do not process unchanged files.
  
## Service Limits
Only applicable to COS V4/V5
## Operating Environment
### System Environment
Linux/Windows system
### Software Dependencies
JDK 1.7/1.8  
#### Installation and Configuration
For more information on installation and configuration, please see [Install and Configure Java](/doc/product/436/10865).
## How to Use
### Obtaining Toolkit
Download link: [Local Synchronization Tool](https://github.com/tencentyun/cos_sync_tools_v5)

Decompress the package and go to the path to the toolkit:
- **Windows:** 
Decompress and save it to a directory, such as `C:\Users\Administrator\Downloads\cos_sync`
- **Linux:**
```
unzip cos_sync_tools_v5-master.zip && cd cos_sync_tools_v5-master
```

<span id="Configuration Instructions"></span>
### Configuration Instructions
The configuration file is under `conf/config.ini`. Modify configurations as needed based on the following example.
```
# secret_id of a user's key (which can be seen at https://console.cloud.tencent.com/capi)
secret_id=XXXXXXXXXXXXXXXXXXXXXXXX
# secret_key of a user's key (which can be seen at https://console.cloud.tencent.com/capi)
secret_key=YYYYYYYYYYYYYYYYYYYYYYYYY
# Bucket is named in a format of {name}-{appid}, which means a bucket name must contain appid, such as movie-1251000000
bucket=mybucket-1251000000
# Region where a bucket resides. Enter the region corresponding to XML API. The abbreviation for xml api region in COS can be found at https://cloud.tencent.com/document/product/436/6224
region=ap-beijing-1
# Storage standard: standard, standard_ia, and nearline
storage_class=standard
# Local path
local_path=/mydata/
# COS path
cos_path=/mycospath
# Whether to transfer via HTTPS (low speed, applicable to transfer scenarios that demand high security). 1: Yes; 0: No
enable_https=0
```
Configurations:

| Name | Description | Valid Value |
| --------------- | ---------------------------------------- | -------- |
| secret_id | Key ID corresponding to APPID, which can be obtained from the console. For more information, please see [Concepts](/doc/product/436/6225) | String |
| secret_key | Key corresponding to APPID, which can be obtained from the console. For more information, please see [Concepts](/doc/product/436/6225) | String |
| bucket | Name of the bucket to synchronize, which must be created in the console in advance. For more information, please see [Create Bucket](/doc/api/436/6232) | String |
| enable_https    | Whether to transfer via HTTPS. 1: Yes; 0: Use http instead | Number |
| region | Region where a bucket resides. Available values are region abbreviations for XML API in [Available Regions](/doc/product/436/6224), such as ap-beijing. | String |
| local_path | Local absolute path to synchronize. Paths on Windows need to be separated by "\\\". <br>Sample path on Linux: /home/user/dir. Sample path on Windows: C:\\\document\\\dir | String |
| cos_path | Target path in COS to store synchronized files, which needs to end with "/" to indicate a directory. A root directory ends with "/". | String |
> <font color="#0000cc">**Note: ** </font>
Paths on Windows need to be separated by "\\\". If "\" is used, some special characters may be regarded as escape characters in configuration files.

### Use of Software
Execute the synchronization tool:
 **Windows:** Double click [start_cos_sync.bat].
**Linux:**
```
sh start_cos_sync.sh
```
After the tool is executed successfully, statistics of the upload results (successful, failed, skipped) and the execution time are output.

## Q&A
### FAQs
**If I accidentally delete a synchronized file in COS, will the file be re-uploaded to COS when I run the synchronization tool again?**
No, because the list of synchronized files is recorded locally rather than in COS.

**Where is the list of synchronized files saved? What if I delete the list and run the synchronization tool?**
The list of synchronized files is saved in the data file under db directory. If you delete the list and run the synchronization tool, all the local files will be re-uploaded to COS and overwrite the existing ones.

**Are Chinese file names or directories supported?**
Yes. All paths and files encoded with UTF-8 are supported.

In case of a failure, re-run the synchronization tool. The uploaded files will not be re-uploaded.

### Other Errors
[Submit a ticket](https://console.cloud.tencent.com/workorder/category) and provide config.json related configurations (without key) of the synchronization tool and the packaged log directory.

