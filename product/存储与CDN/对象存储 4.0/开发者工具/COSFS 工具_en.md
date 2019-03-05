
## Feature Description

COSFS is a user-mode file system based on libfuse, which is used to mount remote Tencent Cloud COS onto user machine and access Tencent Cloud COS in a similar manner as accessing a local disk. For users or applications, performing operations to the local file system is equivalent to performing operations to Tencent Cloud COS. Currently, only file read operations are supported. **Only applicable to COS 4.0**

## Operating Environment

### System Environment

Linux


### Required Dynamic Library

dl z ssl crypto stdc++ pthread


### Static Library (Application Package Included)

cossdk fuse curl jsoncpp


## How to Use

### Acquire Application Package

Current version: COSFS-v4.2.0 [Click to Download](https://github.com/tencentyun/cosfs-v4.2.0) 


### Compile

```
cmake .
make
```


### Configuration File cosfs_config.json

COS SDK usage that cosfs relies on. Parameter description:

```c++
"AppID":1251668577,
"SecretID":"AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO",
"SecretKey":"FZjRSu0mJ9YJijVXXY57MAdCl4uylaA7",
"Region":"sh",                    //COS region. URLs in upload and download operations are all related to this parameter
"SignExpiredTime":360,            //Signature timeout. Unit: second
"CurlConnectTimeoutInms":10000,   //CURL connection timeout. Unit: millisecond
"CurlGlobalConnectTimeoutInms":360000, //CURL connection maximum execution time. Unit: millisecond
"UploadSliceSize":1048576,        //Part size. Unit: byte. Available options: 512k, 1M, 2M, 3M (need to be converted into corresponding number of bytes)
"IsUploadTakeSha":0,              //Whether sha value is required to be included when uploading file
"DownloadDomainType":2,           //Type of download domain: 1: cdn, 2: cos, 3: innercos, 4: self domain
"SelfDomain":"",                  //Custom domain
"UploadThreadPoolSize":5          //Thread pool size for uploading a single file in multipart
"AsynThreadPoolSize":2            //Thread pool size for asynchronous upload and download
"LogoutType":0                    //Printout. 0: No output, 1: Output to screen, 2: Print syslog
```

**Usually, you only need to modify the following COS information parameters**
AppID, SecretID, SecretKey, Region, DownloadDomainType

### Run

(1) Mount bucket to local

```c++
./cosfs bucket /mnt/mointpoint/ -o cfgfile=cos_config.json  

//[/mnt/mointpoint/] is the user's local path (specified by user)
//[bucket] is the name of the user bucket on COS (specified by user)
```

(2) Mount a certain directory under the bucket to local

```c++
./cosfs bucket:/folder /mnt/mointpoint/ -o cfgfile=cosfs_config.json 

//[/mnt/mointpoint/] is the user's local path (specified by user)
//[bucket:/folder] are the names of the user bucket on COS and the directory under this bucket (specified by user)
```

### Unmount

This is only available when you have already installed fuse (yum install fuse)

``` 
fusermount -u /mnt/mointpoint/
```

If you receive "device busy", you need to exit /mnt/mointpoint/. If you still cannot unmount it, execute:

```
umount -l /mnt/mointpoint/
```


**Note:**
Currently, only read operations are supported, write operations are not supported:
linux command: cd, ls, ll, cat, more, cp
System API: open(), read(), stat(), close(), lseek()



