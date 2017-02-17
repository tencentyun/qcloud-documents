To enhance users' software installation efficiency on CVM and reduce the costs for downloading and installing software, Tencent Cloud provides you with YaST download source. Users of CVM on the operating system of SUSE10 can quickly install software through YaST.

## 1. Installation steps
After logging into the CVM on a SUSE operating system, the root permission is granted by default. Run the following command as root to list the software sources:

```
service-list 
```
Or

```
sl
```
Example of returned results:
![](//mccdn.qcloud.com/img56a624f424c9b.png)

If the two software sources shown in the figure above are displayed, you can directly go with step 3 to download and install the software; 

If not, please follow step 2 to add a software source;

> Note: To avoid the error describing "Please insert media [Failed to mount iso:///?iso=/data/SLES-10-SP1-DVD]#1. Retry [y/n]:", if there's ISO CD source "suse-linux-enterprise-server", please delete it using "suse-linux-enterprise-sd".

## 2. Add software source
If there's no software source listed in the previous step, you need to manually add a software source by running the following command as root:

```
service-add
```
Or
```
sa
```
Examples are as follows:

```
sa -t YaST http://mirrors.tencentyun.com/suse suse 
sa -t YaST http://mirrors.tencentyun.com/suse/update update
```

## 3. Search for software packages
Use the following command to search for software packages:

```
search
```
Or

```
se
```
Examples are as follows:

```
se nginx
```
Result:
![](//mccdn.qcloud.com/img56af4b0fab73a.png)

## 4. Install software package
Install the software according to the name of software package searched.  If you want to install multiple software, separate them by space.

> Note: During the software installation, a dependent package will be downloaded and installed automatically if needed, and users do not need to install it by themselves.

Using the following command to install software packages:

```
install
```
Or
```
in
```
Examples are as follows:

```
in nginx
```

The results are:

![](//mccdn.qcloud.com/img56af4be96d4b4.png)

Please install php and php-fpm software in the same way:

```
in MySQL-server-community php5-mysql php5 php5-fpm
```

## 5. View the information of the installed software
After the software has been installed, you can view the installation directory of the software package using the following command:

```
rpm -ql 
```

The following command can be used to view the version information of the software package:

```
rpm -q
```

Example:

```
rpm -ql nginx
rpm -q nginx
```
The results are as follows (The actual version may be different from this one; please refer to the version actually queried):
![](//mccdn.qcloud.com/img56af4cc4d0c52.png)
![](//mccdn.qcloud.com/img56af4ccb0d033.png)