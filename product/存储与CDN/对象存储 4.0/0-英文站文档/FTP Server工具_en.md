COS FTP V4 is used to upload and download files to/from COS via FTP protocol.

## Feature Description

COS FTP V4 is a server end tool which relies on COS 4.X. You can use COS FTP tool to upload and download files to/from COS via FTP protocol.

**Upload mechanism**: Uploaded content are first placed into FTP local disk, and deleted after the content is uploaded to COS, after which a success status is returned to the client. (In later versions, contents are uploaded to COS using stream upload method and are no longer placed into local disk)

**Download mechanism**: Contents are returned to client using stream download method

### Supported FTP Commands

- put
- get
- mput
- mget
- delete
- mkdir
- ls
- cd
- bye
- quit
- size

### Unsupported FTP Command

- append


## Required Environment

### COS Version 

4.x

### System Requirement

Linux (Tencent Cloud Centos series CVMs are recommended)

### Required Library

For systems that are installed using yum (such as Centos), build.sh will download the following required contents automatically. Please install these contents on your own for other systems.

```
cmake
boost
openssl-devel
asio-devel
libidn-devel
```

## How to Use

### Acquire Application Package

Download link: [COS FTP V4 github](https://github.com/tencentyun/cos_ftp_v4)

### Source Code Structure

|    Directory     |              Description               |
| :------: | :---------------------------: |
|   bin    |          Executables generated after compiling          |
|   conf   |            Directory for configuration files             |
|   data   |    Directory for storing temporary data when uploading, the data is deleted when upload succeeds or fails    |
|   dep    | COS 4.X CPP SDK that FTP Server relies on |
| include  |           Directory for header files            |
|   lib    |            Directory for required libraries             |
|   log    |             Directory for logs              |
|  opbin   |        Scripts regarding log cleaning and automatic pulling        |
|   src    |            Directory for FTP source code            |
| build.sh |             Script for compiling              |
| start.sh |        Script for starting FTP server        |
| stop.sh  |            Script for terminating the application            |

### Configuration

The configuration file conf/vsftpd.conf contains relevant configurations for vsftpd. Please refer to the following configuration instructions

```ini
1. COS account information configuration
    #cos, set your app info in cos                                                   
    cos_appid=1000000                                                   
    cos_secretid=xxxxxxxxxxxxxxxxxxxxxxxxx                              
    cos_secretkey=xxxxxxxxxxxxxxxxxx 
    # bucket information, including its name and the region to which it belongs. Currently, available values are South China Guangzhou (gz), East China Shanghai (sh) and North China Tianjin (tj)
    cos_bucket=test                                                     
    cos_region=gz
    # Configuring domain as "cos" means downloading via the COS origin server (recommended for Tencent Cloud CVM users)
    # Configuring domain as "cdn" means downloading via CDN (recommended for non-Tencent Cloud CVM users)
    cos_download_domain=cos                                             
    # No need to configure this item as build.sh script will configure it automatically
    cos_user_home_dir=/home/test/cosftp_data/                                        

2. FTP account configuration (Format - account name:password:read/write privilege. Multiple accounts are separated using semicolons)
    login_users=user1:pass1:RW;user2:pass2:RW  
    
3. Public network IP configuration. Configure public network IP as the public network IP of the server (This is only for users who access FTP service through public network IP. You don't need to configure this item if you access service through private network IP, when both the client and the FTP server are located on Tencent Cloud CVM)
	pasv_address=115.115.115.115
	
4. Control port and data port configuration. You can use the default configuration (It is recommended to use ports from 1025 to 65535 and make sure the ports are not filtered out by firewall iptables)
	listen_port=2121
```
### Compile

1. As FTP will need to use local disk, please place FTP source code applications in a disk with enough storage space. (Data disks purchased with initial Tencent Cloud CVMs need to be formatted and mounted manually. Refer to [https://cloud.tencent.com/doc/product/213/2974](https://cloud.tencent.com/doc/product/213/2974))
2. **Execute build.sh as root** (Because build.sh will call yum to install dependent libraries. It is recommended to use Centos series systems which are commonly used by Tencent Cloud. Please modify opbin/env_init.sh if you use systems of other series, such as ubuntu)

### Run

```
1. Switch to cos_ftp account (which is created in the build.sh script), su cos_ftp
2. sh start.sh (this will start the FTP process and monitor application as well as install the CT script used to automatically clean up logs)
3. Use FTP client to connect to the control port of server (2121 by default). It is recommended to use pasv mode in case the port is restricted by the client.
You can perform a test in advance using FTP command of the server machine (you can install this client application by using yum install ftp).  Test by executing FTP 127.0.0.1 2121.
4. Execute FTP commands such as upload/download
```

### Terminate

```
sh  stop.sh
```

## FAQs

```
1. Cannot connect. Check the account name, password, port number, whether the connection mode is correct, and whether the process has been started on the server (netstat -tulnp | grep vsftpd)
2. During concurrent upload, one of the files failed. FTP does not support concurrent file upload and will lock the files so only one file can be successfully uploaded.
3. Failed to upload large file due to insufficient local disk space. Files uploaded via FTP will be first placed into FTP server disk temporarily (and located in the data directory of the FTP service) before being uploaded to COS. The local files will be deleted when they're successfully uploaded. Downloaded files are not limited by disk space as they will not be placed into local disk. Thus it is recommended to deploy FTP service in a large partition.
4. Failed to upload large files when using clients such as FileZilla. FTP servers of the first version do not support append mode. Clients such as FileZilla will use append operation when uploading certain large files.
5. For other questions, please provide the compressed files under the log directory.
```

 

 
