To enhance users' software installation efficiency on CVM and reduce the costs for downloading and installing software, Tencent Cloud provides you with Apt-get download source. Users of CVM on the operating system of Ubuntu12.04 can quickly install software through Apt-get.

For apt-get download source, software package can be installed directly without adding software source. In order to speed up software installation, the system has already configured mirror of Ubuntu for private network. The mirror is a full image of official x86_64 and is in line with the source of official website. 

## 1. Installation steps
1) Log into the CVM on the operating system of Ubuntu12.04

2) Use the following command to install the software:

```
sudo apt-get install
```
Examples are as follows:

```
sudo apt-get install nginx php5-cli php5-cgi php5-fpm php5-mcrypt php5-mysql mysql-client-core-5.5 mysql-server-core-5.5
```

Result:

![](//mccdn.qcloud.com/img56af4dfeb631a.png)

3) Input "Y" to confirm and start the installation until the software is installed.

##  2. View the information of the installed software
After the software has been installed, you can view the installation directory of the software package and all the files within the package using the following command:

```
sudo dpkg -L 
```

The following command can be used to view the version information of the software package:

```
sudo dpkg -l 
```

Examples are as follows:

```
sudo dpkg -L nginx 
sudo dpkg -l nginx
```

The results are as follows (The actual version may be different from this one; please refer to the version actually queried):
![](//mccdn.qcloud.com/img56af4f1d9e433.png)
![](//mccdn.qcloud.com/img56af4f7f57949.png)
