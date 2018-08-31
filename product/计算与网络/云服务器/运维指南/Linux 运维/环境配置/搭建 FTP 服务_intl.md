This document describes how to build FTP service on Linux CVM. In this example, CentOS 7.2 64-bit system is used for illustration. vsftpd is used as FTP server and FileZilla as the client.

## Step 1: Install vsftpd
 1. Log in to the CVM.
 
 2. Install the software. Enter the command:
``` 
yum install vsftpd -y
```
 
 3. If "Complete !" is displayed, the installation is completed.

## Step 2: Start vsftpd service
1. Start the service. Enter the command:
```
systemctl start vsftpd
```

2. Confirm whether it is started with a command. Enter the following command. If the result is displayed as shown below, the service has been started.
```
netstat -tunlp
```
![](//mc.qcloudimg.com/static/img/6cc74de5689106ce763be98bfe7f5d24/image.png)

3. Confirm whether it is started through public network access.
 1. Install telnet service with the following command.
```
yum -y install  telnet
```
 2. Test with a command on another computer connected to the Internet:
```
telnet + CVM public network IP + 21
```
If the following is displayed, the service has been started.
![](https://main.qcloudimg.com/raw/47ad66d7be133b6d69d60c3e5b719dbd.png)

<span id = "jump">  </span>
## Step 3: Edit vsftpd configuration file
 1. In CVM, enter the command: `vi /etc/vsftpd/vsftpd.conf`
 
 2. Edit the content. Change the status to "anonymous login is not allowed". Press "a" on the keyboard to start editing. Change `anonymous_enable=YES` in the file to `anonymous_enable=NO`. After the modification, press "Esc" on the keyboard, and enter `:write` anywhere to save the changes. Enter `:quit` to quit the editing.
 ![](//mc.qcloudimg.com/static/img/4e7770981eae42e7b16a2a5a7866a6a6/image.png)

## Step 4: Add FTP users
 1. Add users. In this example, a user named ftpuser1 is added. Enter the command: ` useradd -m -d /home/ftpuser1 -s /sbin/nologin ftpuser1 `

 2. Set user login password. In this example, login password is set for user ftpuser1. Enter the command: `passwd ftpuser1`. Enter the password and confirm it.
![](//mc.qcloudimg.com/static/img/f8912544914d11dfc1dd7e0a6db16f11/image.png)

## FAQ
### Problem description
Some users may encounter such problem as connection timeout and failure to read the directory list when using FTP client connections locally, as shown below.
![](//mc.qcloudimg.com/static/img/eb7beaf8c5a6e683257e94dd754e3f25/image.jpg)
The problem occurs at the PASV command. The reason is that FTP protocol is incompatible with Tencent Cloud network architecture. FTP client transmits data in passive mode by default. Therefore, it searches for the server's IP address to connect during the communication process. However, public IP of Tencent Cloud is not directly configured on ENI, so the client cannot find a valid IP in passive mode (it can only find private IP of CVM. The private IP cannot communicate directly with the public network). Therefore, the connection cannot be established.

### Solution
 - Change the transmission mode on the client to active.
 - If the client network environment requires passive mode, then add the following statements to the configuration file of the server [Step 3](#jump):
 ```
 pasv_address=XXX.XXX.XXX.XXX     // (Public IP)
 pasv_enable=YES
 pasv_min_port=1024
 pasv_max_port=2048
 ```

