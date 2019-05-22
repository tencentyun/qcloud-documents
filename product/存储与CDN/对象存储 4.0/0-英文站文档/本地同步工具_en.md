## Feature Description

Synchronize sub files and sub directories in local directories to COS. **Only applicable to COS 4.0**
Implementation mechanism: The COS local synchronization tool will acquire the user's local file list, upload the files and log the result of the upload operation locally. The tool will re-acquire local file list each time is it executed, and perform comparison and synchronization operations with the local database (upload or delete).

## Operating Environment

### System Environment

Linux/Windows system

### Required Software

JDK 1.7 or 1.8

## How to Use
### Acquire the Tool Package
Download Link: [Tool Package cos_sync.zip](https://mc.qcloudimg.com/static/archive/769a1592b2ee429e8e82a78b99700bcc/cos_sync.zip)

Decompress the package and go to the path containing the tool:

```shell
unzip cos_sync.zip && cd cos_sync
```

### Configuration Instructions

Configuration file is located at /conf/config.json in the tool package directory:

```json
{
    "appid"            : "xxxxxx",
    "secret_id"        : "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "secret_key"       : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "bucket"           : "xxxxxx",
    "timeout"          : "60",
    "thread_num"       : "20",
    "delete_sync"      : "1", 
    "daemon_mode"      : "0",
    "daemon_interval"  : "60", 
    "enable_https"     : "0",
    "region"           : "gz",

    "local_path"       : "/home/test/data",
    "cos_path"         : "/mysyncfolder"
}
```

| Name              | Description                                       | Valid Value      |
| --------------- | ---------------------------------------- | -------- |
| app_id          | APPID that needs to perform the operation (you can acquire it from the console)                     | APPID number |
| secret_id       | The private key ID that corresponds to the APPID (you can acquire it from the console)                    | String      |
| secret_key      | The private key that corresponds to the APPID (you can acquire it from the console)                  | String      |
| bucket          | Name of the bucket to be synchronized. You need to create the bucket in the console beforehand. Refer to [Create Bucket](/doc/api/436/6232).  | String      |
| timeout         | Timeout for COS connections. You can increase this value when the network is poor. <br />Unit: second | Number       |
| thread_num      | Number of concurrent threads. Increase this value for a higher concurrent level and upload speed. Lowering this value will reduce upload speed.  | Number       |
| delete_sync     | Delete COS file in sync when deleting local file.  <br />1: Delete remote file when deleting local file; 0: Ignore deleted local file | Number       |
| daemon_mode     | Run in daemon mode. <br />1: Run the synchronization tool in cycles; 0: Exit the tool after one execution.   | Number       |
| daemon_interval | (In daemon mode) Time interval for checking local file changes. <br />Unit: second         | Number       |
| enable_https    | Enable HTTPS for transmission. <br />1: Use HTTPS &verbar; 0: Use HTTP | Number       |
| region          | Region in which the bucket resides. For example: Tianjin, North China (tj),  Shanghai, East China (sh),  Guangzhou, South China (gz) | String      |
| local_path      | The absolute local path to be synchronized. In Windows, paths are separated using double backslashes "\\". <br />Linux example: /home/user/dir<br /> Windows example: C:\\\document\\\dir | String      |
| cos_path        | Target COS path to which the files are to be synchronized. The path needs to end with "/" to indicate that it's a directory. The root directory is "/".       | String      |

### Use the Software

Execute the synchronization tool (For Windows, double click start_cos_sync.bat)

```shell
sh start_cos_sync.sh 
```

When the execution is completed, the tool will display the statistical information of successful/failed file creation/deletion operations as well as how long they took.

## Q&A

### FAQs

**I accidentally deleted files on COS after synchronization is completed. Will the files be uploaded again if I run the tool again?**

No. The tool keeps the list of synchronized files locally. It does not acquire file list from COS.

**Where is the database for storing synchronization records located? What will happen if I delete the records and then execute the tool again?**

Synchronization result records are stored in the data file under the db directory. If you execute the tool again after deleting the records, the tool will try to upload all local files onto COS, and existing files on the COS will be overwritten.

**Does it support Chinese file names or directories?**

Yes. Currently, all paths and files in UTF-8 encoding are supported.

### Common Errors

If synchronization fails, check the error log under the log directory first. Common error codes are shown below.

**code: -3, connection timeout**

The connection to COS service has timed out, please check whether resolution and port are normal.

*How to check DNS: Suppose your region is "sh", execute "dig sh.file.myqcloud.com" locally and see if the IP received is an IP from Tencent Cloud. You can verify this by using external ping tools, such as [chinaz - Ping](http://ping.chinaz.com). An IP from Tencent Cloud data center should be resolved as 10.\*.\*.\*. The same can be applied for other regions *

*How to check port: If IP is resolved correctly, execute `telnet sh.file.myqcloud.com 80` and see if `Escape character is '^]'.` is returned. If there is no return, check your local firewall configuration, and whether your network functions normally.*

**code:-133, ERROR_CMD_BUCKET_NOTEXIST**

Check if "region" is configured correctly in your configuration file. Refer to configuration instruction for detailed relationships between regions and configurations. 

### Other Errors

Please submit a ticket. Tell us the relevant configurations of the config.json for your synchronization tool (private key is not required) as well as your packaged log directory

## Version History

- 2016.11.17  4.x JAVA synchronization tool became available

