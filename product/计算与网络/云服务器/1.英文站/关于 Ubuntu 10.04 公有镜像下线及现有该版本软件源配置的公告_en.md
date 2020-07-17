Ubuntu has officially stopped the maintenance for Ubuntu 10.04 LTS, so Tencent Cloud has also stopped offering the public images of Ubuntu 10.04.

The directory trees for Ubuntu10.04 LTS have been deleted from the latest official source warehouse. To ensure the consistency with the official source warehouse, Tencent Cloud software warehouse will no longer provide support for Ubuntu 10.04 LTS under the official source directory tree. It is recommended to change the images to a higher version.

If existing users hope to continue to use the software source of Ubuntu 10.04, we provide support in two ways:

## Method 1: Manually update configuration file
To improve the user experience, the Tencent Cloud software warehouse pulls the official archive source of Ubuntu 10.04 LTS (http://old-releases.ubuntu.com/ubuntu/) for users. Users can use the warehouse as usual by manually modifying the configuration file:

Open the apt source configuration file` vi /etc/apt/sources.list`, and modify the following codes:

```
deb-src http://mirrors.tencentyun.com/old-archives/ubuntu lucid main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/old-archives/ubuntu lucid-updates main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/old-archives/ubuntu lucid-security main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/old-archives/ubuntu lucid-backports main restricted universe multiverse
deb http://mirrors.tencentyun.com/old-archives/ubuntu lucid main restricted universe multiverse
deb http://mirrors.tencentyun.com/old-archives/ubuntu lucid-updates main restricted universe multiverse
deb http://mirrors.tencentyun.com/old-archives/ubuntu lucid-security main restricted universe multiverse
deb http://mirrors.tencentyun.com/old-archives/ubuntu lucid-backports main restricted universe multiverse
```

## Method 2: Run the automated script
Make the configuration using the script provided by Tencent Cloud ([old-archive.run])(http://ubuntu10-10016717.cos.myqcloud.com/old-archive.run). Download the file to Ubuntu 10.04 CVM and run the following commands:

```
chmod +x old-archive.run
./old-archive.run
```