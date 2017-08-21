This document provides several methods on how to log in to a Linux CVM locally. For more login methods, refer to "Linux Cloud Service Operation Manual" - "Log in to a Linux CVM".

2) You can log in to the CVM from console whether you have purchased public bandwidth/traffic or not and regardless of the local operating system. In the Action column of CVM list, click "Log In" button to connect to Linux CVM via VNC.

![](//mccdn.qcloud.com/img56b1a6cb7b3e8.png)

Enter the account ID ("ubuntu" for Ubuntu system users and "root" for all other systems) and the initial password in the internal message (or the password modified by you) to log in.

> NOTE: This terminal is exclusive, that is, only one user can log in using the console at a time.


2) For the Linux CVM for which you have purchased public bandwidth/traffic, the following shows how to log in to Linux CVM from local Windows with password:

After you have purchased CVM successfully, log in to [Tencent Cloud Console](https://console.qcloud.com/), click the "Internal Message" button on the right. In the "Check and accept the newly purchased server" page, the login account ID and initial password of administrator for CVM will be provided as shown below.
![](//mccdn.qcloud.com/img56a20f10a373a.png)

Download remote link software Putty by referring to the download link: http://www.putty.nl/download.html

Open the Putty client, enter the following information in the "PuTTY Configuration" window:
- Host Name: Public IP of the Linux CVM.
- Port: port of the CVM, which must be 22. (Make sure port 22 of the CVM is open)
- Connect type: select "SSH".

When all the information is entered, click "Open" to create a new dialog.
![](//mccdn.qcloud.com/img56a5d38a4ffbc.png)

In the Putty dialog window, enter the administrator account ID and press Enter.
>Administrator account ID:
SUSE/CentOS/Debian: root
ubuntu: ubuntu 

And then enter the initial password and press Enter to complete login.
![](//mccdn.qcloud.com/img56a5d47b8b5da.png)

3) When trying to log in to the Linux CVM from a local Linux or Mac OS Linux system, you can simply use the SSH command, e.g. ssh root @public IP of the Linux CVM, to connect, and then enter the root user's initial password to complete the login.