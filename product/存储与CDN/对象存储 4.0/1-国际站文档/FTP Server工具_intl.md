The COS FTP Server tool can be used to directly operate objects and directories in COS via the FTP protocol, including uploading/downloading/deleting files and creating folders. This tool is developed with Python, which makes the installation easier.
## Operating Environment
### System Environment
OS: Linux. It is recommended to use the CVM of Tencent Cloud CentOS 7 series. Windows systems are not supported for now.

Python interpreter version: Python 2.7. For more information on how to install and configure it, please see [Python Installation and Configuration](https://cloud.tencent.com/document/product/436/10866).

Dependent libraries:
- requests
- argparse

### Download and Installation
GitHub link: [COS FTP Server Tool](https://github.com/tencentyun/cos-ftp-server-V5).

After the download is completed, simply run `setup.py` under the `cos ftp server` directory. You need to install dependent libraries online.
```
python setup.py install   # sudo or root permissions may be required here.
```

### Special Notes
This tool is developed with the COS XML API.

## Feature Description
#### Upload Mechanism
The stream upload is adopted and the uploaded file is not saved locally. It works only if the working directory is configured according to the standard FTP protocol, and no disk storage space is occupied actually.

#### Download Mechanism
The downloaded file is directly returned to the client in the stream download mode.

#### Directory Mechanism
Bucket serves as the root directory of the entire FTP Server, and multiple subdirectories can be created under Bucket.

#### Notes
- Now, only one Bucket can be operated each time. But simultaneous operation on multiple Buckets may be supported in the future.
- The FTP Server tool does not support resuming upload from the breakpoint for now.
- An empty file (0B) cannot be uploaded. The maximum file size is 200 GB.

## Supported FTP Commands
- put
- mput
- get
- rename
- delete
- mkdir
- ls
- cd
- bye
- quite
- size

## Unsupported FTP Commands
- append
- mget (The native mget command is not supported, but on certain Windows clients, such as FileZilla, the files can still be downloaded in batches.)


## Configuration File
`conf/vsftpd.conf` is the configuration file of the FTP Server tool. The relevant configuration items are described as follows:
```conf
[COS_ACCOUNT]
cos_secretid = XXXXXX
cos_secretkey = XXXXXX
# SecretId and SecretKey can be obtained at https://console.cloud.tencent.com/cam/capi.
cos_bucket = BucketName-appid
# The bucket to be operated. Its format is bucektname-appid, such as cos_bucket = mybucket-125888888888.
cos_region = ap-xxx
# Bucket's region. For more information on supported regions, please see [Available Regions - Applicable to the XML API Section]:https://cloud.tencent.com/document/product/436/6224
cos_user_home_dir = /home/cos_ftp/data
# The working directory of the FTP Server.
[FTP_ACCOUNT]
login_users = user1:pass1:RW;user2:pass2:RW
# FTP account configuration. The configuration format is <User name: Password: Read and write permissions>, and multiple accounts are separated by a semicolon.

[NETWORK]
masquerade_address = XXX.XXX.XXX.XXX
# For FTP server located behind a gateway or NAT, you can assign the gateway's IP or domain name to the FTP Server through this configuration item. In general, this configuration item needs not to be configured.
listen_port = 2121
# The listening port (default: 2121) of the Ftp Server. Please note that the firewall needs this port opened.
passive_ports = 60000,65535             
# passive_port can be used to set the port range for the passive mode. Default is (60000, 65535).

[FILE_OPTION]
single_file_max_size = 21474836480
# By default, the maximum size of a single file is 200 GB. Too large files are not recommended.

[OPTIONAL]
# For the following settings, take the defaults if there is no special requirements, or fill in an appropriate integer if necessary.
min_part_size       = default
upload_thread_num   = default
max_connection_num  = 512
max_list_file       = 10000                # The maximum number of files to be listed by ls command. It is recommended not to set it too big. Otherwise, high delay of ls command may occur.
log_level           = INFO                 # Set the log output level
log_dir             = log                  # Set the directory to store logs. Default is the log directory under the ftp server directory.
```
The OPTIONAL part in the configuration is used to adjust the upload performance. In general, it will be fine to take the default values. You can obtain an optimal uploading speed by reasonably adjusting the multipart size and the number of concurrent upload threads based on the server performance. max_connection_num is the limit option for the maximum number of connections, which can be adjusted based on the server condition. If it is set to 0, there is no limit on the maximum number of connections. 
## Running FTP Server
After the configuration is completed, you can directly run `ftp_server.py` in the root directory via Python to start the FTP Server. You can also use the screen command to make the FTP Server run in the backend.
```
python ftp_server.py
```
After the command is executed, if the result is shown as below, it indicates that the FTP Server service is successfully enabled. And you can access the configured IP and port through the FTP client.
![](//mc.qcloudimg.com/static/img/7bbb20b2ba2c6cf9678a47d8753499cc/image.png)

## Stopping FTP Server
The FTP Server (running directly or in the backend with the screen command) can be easily stopped via `Ctrl + C`.
## FAQ

### What does the masquerade_address option in the configuration file do and when to configure it?
If the FTP Server runs in PASSIVE mode (PASSIVE mode is generally enabled for the FTP client located behind a NAT gateway) on a Server with multiple ENIs, you need to use the masquerade_address option to bind an IP for reply in PASSIVE mode. For example, the FTP Server has multiple IPs (private IP: 10.XXX.XXX.XXX, public IP: 123.XXX.XXX.XXX), and the client adopts PASSIVE mode for transmission. If the public IP is not bound via the masquerade_address option, the private IP may be used when the Server makes a reply in PASSIVE mode. That is, the client can connect to the FTP Server but cannot get any reply data from the Server.

If necessary, it is recommended to set masquerade_address to the IP used by the client to connect with the Server.

#### If a large file in uploading is cancelled, why does it remain on COS as an uploaded file?
The FTP Server applicable to COS V5 provides the full stream upload capability, and cancelling of file upload or connection break can trigger the completion of large file upload. Then, COS will regard the user's data stream as uploaded completely, and then generate a complete file using the uploaded data. If you want to upload the file again, you can directly upload it with the original file name and overwrite the previous one, or delete the incomplete file and then upload the file again.

#### Why does the maximum size of uploaded file need to be set in FTP Server configuration?
The maximum number of multiparts to be uploaded to COS is 10,000, and the size of each multipart is limited to 1 MB-5 G. The upper limit on uploaded files is set to calculate the size of a multipart.
The FTP Server supports uploading a single file less than 200 GB by default. However, it is recommended not to set the upper limit to a too big value, because the bigger the set file size, the larger the multipart buffer for uploading. This may increase the consumption of your memory resource. Therefore, it is recommended to set the upper limit on the size of a single file appropriately according to the actual situation.

#### What will happen if the size of an uploaded file exceeds the upper limit?
If the size of a single uploaded file exceeds the upper limit specified in the configuration file, the system will return an IOError exception and record the error message in the log.

#### If you have any other questions, please [submit a ticket](https://console.cloud.tencent.com/workorder/category) and attach the complete `cos_v5.log` log for troubleshooting.

