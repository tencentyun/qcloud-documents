Once you've started a Windows instance, you can connect to and log in to it. The login method depends on your local operating system and whether the CVM instance can be accessed by Internet. See the table below for details.
<table><tbody>
<tr><th>Local operating system</th><th> Windows CVM instance with public IP</th><th> Windows CVM instance without public IP</th></tr>
<tr><td>Windows</td><td>VNC Login<br>Remote Desktop Connection</td><td rowspan="3">VNC Login</td></tr>
<tr><td>Linux</td><td>VNC Login<br>rdesktop Login</td></tr>
<tr><td>Mac OS</td><td>VNC Login<br>rdesktop Login</td></tr>
</tbody></table>

## Prerequisites
You need to use the administrator account ID and the corresponding password to log in to the CVM.

- Administrator account ID: it is ***Administrator*** for all Windows instances 
- Password:
  - If you select "Auto Generate Password" when starting the instance, then the initial password will be randomly assigned by the system. You can log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and click the "Internal Message" button on the right. In the "Check and accept the newly purchased server" page, the login account ID and initial password of administrator for CVM will be provided as shown below.
  ![](//mccdn.qcloud.com/img56a20f10a373a.png)

  - If you select "Custom Password" when starting the instance, then the password will be the one you specified when purchasing the CVM instance. To learn more about password, for example, what to do if I forget the login password, refer to [Login Password](/doc/product/213/6093).

## Windows system: use Remote Desktop Connection to log in to Windows instance
On the local Windows machine, click "Start" - "Run", enter `mstsc` command to open the Remote Desktop Connection dialog box.

In the input box, input the public IP of Windows Server (Log in to [CVM Console](https://console.cloud.tencent.com/cvm) to check the public IP of CVM), as shown below:
![](//mccdn.qcloud.com/img56b1a11a3c31f.png)

Click "Connect", and, in the screen that opens, enter the administrator account ID and corresponding password obtained from the Prerequisites step as shown below:
![](//mccdn.qcloud.com/static/img/878a0e8ef1a0bcc51ad5de2bcce4e353/image.png)
![](//mccdn.qcloud.com/static/img/e140d3151ac8747014313b33e6413568/image.png)

Click "OK" to log in to Windows CVM.

If the login fails, check if your CVM instance allows inbound traffic over port 3389. Refer to [Security Group](/doc/product/213/5221) to check the Port. If your CVM is in [Virtual Private Cloud/VPC], check related subnet [Network ACL](/doc/product/215/5132) as well. 

## Linux system: Use rdesktop to log in to Windows instance
To log in to a remote Windows instance, you need to install an appropriate remote desktop connector, for which rdesktop is recommended. For more information about rdesktop, see [Here](http://www.rdesktop.org/).

1) Install rdesktop
Run the `rdesktop`command to check if it is installed. If not, [download the latest installation package](https://github.com/rdesktop/rdesktop/releases), and run the following command to extract and install it to the appropriate directory.
```
tar xvzf rdesktop-<x.x.x>.tar.gz ## Replace x.x.x with the downloaded version number. 
cd rdesktop-1.8.3
./configure 
make 
make install
```
2) Connect to remote Windows instance
Run the command below (Replace parameters in the example with yours):

```
rdesktop -u Administrator -p <your-password> <hostname or ip address> 
```
"-u" is followed by the username, which is `Administrator`, "-p" is followed by password you obtained from the Prerequisites step and <hostname or ip address> is the public IP or custom domain name of your Windows instance.


If the login fails, check if your CVM instance allows inbound traffic over port 3389. Refer to [Security Group](/doc/product/213/5221) to check the Port. If your CVM is in [Virtual Private Cloud/VPC], check related subnet [Network ACL](/doc/product/215/5132) as well. 

## Mac operating system: Use Microsoft Remote Desktop Connection Client for Mac to log in to Windows instance

Go to the Microsoft official website to download [Remote Desktop Connection Client for Mac OS](https://www.microsoft.com/zh-cn/download/details.aspx?spm=5176.doc25435.2.2.l9afth&id=18140).

After the installation is completed, use the username and password you obtained from the Prerequisites step to log in to the remote Windows instance.

If the login fails, check if your CVM instance allows inbound traffic over port 3389. Refer to [Security Group](/doc/product/213/5221) to check the Port. If your CVM is in [Virtual Private Cloud/VPC], check related subnet [Network ACL](/doc/product/215/5132) as well.  

## Use VNC to log in to instance
VNC login is a way Tencent Cloud provides for users to connect to their CVMs through Web browser. When the remote login client is not installed or cannot be used, you can connect to your CVM using VNC login and check the CVM status. This also allows you to perform basic CVM management operations with the CVM account.

VNC login scenarios include at least the following:

- Check the progress of a CVM startup
- Log in to the server with VNC when client SSH or mstsc login is not available 

In the Action column of CVM list, click "Log In" button to connect to Windows CVM via VNC.

![](//mccdn.qcloud.com/img56b1a6cb7b3e8.png)

By clicking the Ctrl+Alt+Del command at the top left corner, enter the system login screen:

![](//mccdn.qcloud.com/img56b1a6ff2e305.png)

> Note:
> 
>- Ctrl + Alt + Delete is a shortcut key combination for you to log in to Windows or open task manager after the screen is locked.
>- This terminal is exclusive, that is, only one user can log in using VNC at a time.
>- To log in with VNC in the normal way, you need to use modern browsers such as Chrome, Firefox, IE10 or above.
>- Copy and Paste are not supported at the moment.
>- File upload and download are not supported at the moment.