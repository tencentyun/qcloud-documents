
This section describes how to log in to a CPM after an EIP is bound.

## Acquiring Login Password
If the purchased CPM is displayed as "Running" on the CPM console, it means the operating system has been installed and the CPM delivered to you.
Please go to [Tencent Cloud Message Center](https://console.cloud.tencent.com/message/index/all/104 "Message Center") to view your CPM password.</br>
![](http://mc.qcloudimg.com/static/img/9e1593f7340a55f489fd6971fd862d33/image.png))


## Acquiring Public IP
From the CPM console, locate the CPM you just purchased and the public IP.
![](http://mc.qcloudimg.com/static/img/b13303aefb6aca569a898416746c64c7/image.png)

*If there is no public IP, please verify whether an EIP is bound*

## Remote Login
Download the remote connection software Putty. Reference download link: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

Open the Putty client, enter the following information in the "PuTTY Configuration" window:

<li>Host Name: Public IP address of the CPM</li>
<li>Port: Port of the CPM, which must be 22.</li>
<li>Connect type: Select "SSH".</li>
When all the information is entered, click "Open" to create a new session.</br>
![](http://mc.qcloudimg.com/static/img/2ddbfe58c5fd6e2a783bb92fa51124b8/image.png)

In the Putty session window, enter the administrator account ID and press Enter.
>Administrator account ID:</br>
SUSE/CentOS/Debian: root</br>
ubuntu: ubuntu

Then enter the initial password and press Enter to complete login process.</br>
![](https://mccdn.qcloud.com/img56a5d47b8b5da.png)

When trying to log in to the Linux CVM from a local Linux or Mac OS, you can simply use the SSH command. For example: ssh root @<public IP of the Linux CVM>. Then enter the root user's initial password to complete the login process.

*Please use an SSH password to log in ASAP, in order to prevent a weak password from being cracked*
