## Feature Description 
COSFS tool supports mounting COS buckets locally and allows you to operate Tencent Cloud COS directly in the same way as you do with a local file. COSFS has following features:
- Support most of the features of POSIX file system, such as file reading/writing, directory operation, link operation, permission management, uid/gid management.
- Large file transfer.
- Data verification with MD5.

## Service Limits 
This tool supports access to COS V4 and V5 using COS V5 domain name.
## Operating Environment 
### System Environment 
Mainstream Linux system

### Software Environment 
This tool is compiled in C++ compiling environment, and dependent on such software as automake, git, libcurl-devel, libxml2-devel, fuse-devel, make, openssl-devel. For more information on installation method, please see [Environment Installation](#Environment Installation).
<span id="Environment Installation"></span>
### Environment Installation 
#### How to install environment dependency on Ubuntu system
```
sudo apt-get install automake autotools-dev g++ git libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config fuse
```

#### How to install environment dependency on CentOS system
```
sudo yum install automake gcc-c++ git libcurl-devel libxml2-devel fuse-devel make openssl-devel
```

Note: For CentOS 6.5 or below, a message indicating that the fuse version is too low may be returned when you perform "configure" operation during installation.
```
 checking for common_lib_checking... configure: error: Package requirements (fuse >= 2.8.4 libcurl >= 7.0 libxml-2.0 >=    2.6) were not met:
  Requested 'fuse >= 2.8.4' but version of fuse is 2.8.3 
```
In this case, you need to manually install the fuse version by following the procedure below.
```
 # yum remove -y fuse-devel
  # wget https://github.com/libfuse/libfuse/releases/download/fuse_2_9_4/fuse-2.8.4.tar.gz
  # tar -zxvf fuse-2.8.4.tar.gz
  # cd fuse-2.8.4
  # ./configure
  # make
  # make install
  # export PKG_CONFIG_PATH=/usr/lib/pkgconfig:/usr/lib64/pkgconfig/:/usr/local/lib/pkgconfig
  # modprobe fuse
  # echo "/usr/local/lib" >> /etc/ld.so.conf
  # ldconfig
  # pkg-config --modversion fuse   
  2.8.4   //The display of version indicates successful installation.  
```

## How to Use 
### Obtaining Tool 
Link on Github: [COSFS Tool](https://github.com/tencentyun/cosfs-v4.2.1)

### Installing Tool 
You can directly upload the downloaded source code to the specified directory, or download the code to the specified directory using GitHub. The following example shows how to download source code to `/usr/cosfs` with GitHub:
```
git clone https://github.com/tencentyun/cosfs-v4.2.1 /usr/cosfs
```
Go to the directory to compile and install the tool:
```
cd /usr/cosfs
./autogen.sh
./configure
make
sudo make install
```
### Configuration File
In `/etc/passwd-cosfs` file, configure the name of your bucket and the corresponding SecretId and SecretKey. For relevant concepts, please see [Concepts](https://cloud.tencent.com/document/product/436/6225). Parameters are separated with a colon. In addition, set read permission for `/etc/passwd-cosfs`. The command format is as follows:
```
echo <bucketname>:<SecretId>:<SecretKey> > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
```
Where:
The bucketname/SecretId/SecretKey should be replaced with your true information.
#### Example:
```
echo buckettest:AKID8ILGzYjHMG8zhGtnlX7Vi4KOGxRqg1aa:LWVJqIagbFm8IG4sNlrkeSn5DLI3dCYi > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
```
### Running Tool 
Execute the following command to mount the configured bucket to the specified directory:
```
cosfs your-APPID:your-bucketname your mount-point -ourl=cos-domain-name -odbglevel=info
```
Where:
- your-APPID/your-bucketname is replaced with your true information.
- your-mount-point is replaced with the local directory to which the bucket needs to be mounted (such as /mnt).
- cos-domain-name is the domain name of the region to which the bucket belongs in a format of `http://cos.<Region>.myqcloud.com`. Region is the region abbreviation for XML API in [Available Regions](https://cloud.tencent.com/document/product/436/6224), such as `http://cos.ap-guangzhou.myqcloud.com`, `http://cos.eu-frankfurt.myqcloud.com`.
- The -odbglevel parameter indicates the level of information.
#### Example:
```
cosfs 1253972369:buckettest /mnt -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -onoxattr
```
Moreover, if you have a high requirement for the performance, you can use a local disk for file caching. Add -ouse_cache parameter in the command, as shown below:
```
mkdir /local_cache_dir
cosfs 1253972369:buckettest /mnt -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -onoxattr -ouse_cache=/local_cache_dir
```
`/local_cache_dir` is local cache directory, which is not specified if local caching of files is not required, or the capacity of local disk is limited.

Unmount the bucket:
```
fusermount -u /mnt
```
Or

```
umount -l /mnt
```

## Common Mounting Options

1. -omultipart_size=[size]
`multipart_size` is the part size in multipart upload (in MB). Default is 10 MB. Due to a limited number of parts (10,000), for large files larger than 10 MB * 10,000 (100 GB), this parameter should be adjusted as necessary.

2. -oallow_other
Specify the `allow_other` parameter when you run COSFS to allow other users to access the folder to which the bucket is mounted.

3. -odel_cache
By default, COSFS will not clear the data cached locally after the bucket is unmounted for optimal performance. If auto removal of cached data is required when COSFS exits, you can add this option when mounting the bucket.

4. -noxattr
Disable get/setxattr feature which is not supported for the current version of COSFS. If use_xattr is used when you mount the bucket to the disk of the local file, failure may occur when you use mv command to move file to bucket.

## Notes 
- The capabilities and performance provided by COSFS are limited compared to the local file system. For example, randomly writing data or appending data to the file may cause rewrite of the entire file.
- When a COS bucket is mounted to multiple clients, you need to adjust the behaviors of these clients by yourself. For example, to avoid multiple clients from writing data into the same file.
- The hard link is not supported, which is not applicable to scenarios demanding frequent concurrent read/write.
- Do not mount and unmount files in the current directory. You can use cd command to switch to another directory to mount or unmount file.


### FAQs
* How to mount a file to a directory
   You can specify a directory when executing mount command, for example:
   
  `cosfs appid:my-bucket:/my-dir /tmp/cosfs -ourl=http://cn-south.myqcloud.com -odbglevel=info -ouse_cache=/path/to/local_cache`
   Note: my-dir must begin with /.
   
   
* Why can't I write files using the previous version?

   Due to security updates, we highly recommend upgrading to the latest version of COSFS, and try to re-mount.


* For CentOS 6.5 or below, what should I do when I receive a message indicating that the fuse version is too low?

  If the following message is returned when you perform "configure" operation:
  ```
    hecking for common_lib_checking... configure: error: Package requirements (fuse >= 2.8.4 libcurl >= 7.0 libxml-2.0 >=    2.6) were not met:
    Requested 'fuse >= 2.8.4' but version of fuse is 2.8.3 
    ```

   In this case, you need to manually install the fuse version by following the procedure below.

   ```
     # yum remove -y fuse-devel
     # wget https://github.com/libfuse/libfuse/releases/download/fuse_2_9_4/fuse-2.8.4.tar.gz
     # tar -zxvf fuse-2.8.4.tar.gz
     # cd fuse-2.8.4
     # ./configure
     # make
     # make install
     # export PKG_CONFIG_PATH=/usr/lib/pkgconfig:/usr/lib64/pkgconfig/:/usr/local/lib/pkgconfig
     # modprobe fuse
     # echo "/usr/local/lib" >> /etc/ld.so.conf
     # ldconfig
     # pkg-config --modversion fuse   
     2.8.4   //The display of version indicates successful installation.  
   ```

* Why did COSFS exit during its normal operation, and "unable to access MOUNTPOINT /path/to/mountpoint: Transport endpoint is not connected" shows when I remount the tool?

  If COSFS is not killed forcibly, check whether the fuse version is older than 2.9.4. The libfuse below 2.9.4 may cause COSFS to exit abnormally.
  It is recommended to update the fuse version or download COSFS V1.0.2 or above. Download link: https://github.com/tencentyun/cosfs/releases

* Why is the Content-Type of files uploaded via COSFS always "application/octet-stream"?

  
  COSFS automatically sets the Content-Type according to /etc/mime.types and the extension of uploaded file. You should check if the file exists on the machine.

  For Ubuntu, add files through sudo apt-get install mime-support

  For Centos, add files through sudo yum install mailcap

  Or you can add files manually with each file in a separate row, such as image/png png.

