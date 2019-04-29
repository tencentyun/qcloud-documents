WinSCP is an open source graphical SFTP client that uses SSH in Windows environment and supports SCP protocol. Its main function is to copy files between the local and remote computers safely. Instead of using FTP to upload code, you can use the server account and password to access the server directly via WinSCP, without any configuration on the server side. Download address: [Official Download](http://winscp.net/eng/docs/lang:chs).

Start WinSCP after installation. The interface is as follows. Fill in the information as shown and log in.

![](//mccdn.qcloud.com/img56b024e2768ad.png)

> How to fill in the fields:
- Protocol: either SFTP or SCP is OK
- Host Name: Public IP of CVM (Log into [CVM Console](https://console.cloud.tencent.com/cvm) to view the Public IP of CVM)
- Username: the system username for CVM (SUSE/CentOS/Debian: root, Windows: Administrator, Ubuntu: ubuntu)
- Password: the password corresponding to the username of CVM
- Port: 22 by default

Click on Log In after completing the information. The interface is as follows:

![](//mccdn.qcloud.com/img56b0272d4ed3a.png)

After successful login, select a local file and drag it to the remote site on the right, and then you can upload the file to the Linux CVM.

![](//mccdn.qcloud.com/img56b027728e1ec.png)
