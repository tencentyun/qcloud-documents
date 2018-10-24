To enhance users' software installation efficiency on CVM and reduce the costs for downloading and installing software, Tencent Cloud provides you with Yum download source. In CentOS environment, users can quickly install software through YUM.

For Yum download source, software package can be installed directly without adding software source.

## 1. Installation steps
1) After logging into the CVM on a CentOS operating system, root permission is granted by default:

>Note: The execution of password command is forbidden, and the root password cannot be modified by default. 

2) Run the following command as root to install the software:
```
yum install [nginx][php][php-fpm][mariadb][mariadb-server][mysql][mysql-server]...
```

>Note: Since CentOS 7, MariaDB has become the default database installer in yum source. MySQL will be unusable when installed in a system higher than CentOS 7 via Yum. You can choose to use MariaDB that is fully compatible, or refer to [here](https://www.linode.com/docs/databases/mysql/how-to-install-mysql-on-centos-7) to install MySQL of a lower version.


3) System will automatically search relevant software packages and dependencies, and prompt users to verify whether the software package is suitable in the interface as shown below:
![](//mccdn.qcloud.com/static/img/f61a066066619f09fed1be6fa4a8a4b0/image.png)

4) Input "y" to confirm and start the installation. When the installation is done, it will display "Complete" as shown below:
![](//mccdn.qcloud.com/static/img/e36f74f325c00814c3c840aeda9c26a6/image.png)

## 2. View the information of the installed software
After the software has been installed, you can view the installation directory of the software package using the following command:

```
 rpm -ql 
```
Taking the installation directory of nginx as an example:
![](//mccdn.qcloud.com/img56a61fa482658.png)

The following command can be used to view the version information of the software package:
```
 rpm -q 
```
Taking the version of nginx as an example (The actual version may be different from this one; please refer to the version actually queried):
![](//mccdn.qcloud.com/img56a621c372e23.png)