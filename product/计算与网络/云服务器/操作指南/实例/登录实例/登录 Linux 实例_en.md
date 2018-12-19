Once you've purchased and started a Linux instance, you can connect to and log in to it. The login method depends on your local operating system and whether the CVM instance can be accessed by Internet. See the table below for details.
<table><tbody>
<tr><th>Local operating system</th><th> Linux CVM instance with public IP</th><th>Linux CVM instance without public IP</th></tr>
<tr><td>Windows</td><td>VNC Login<br>Remote Login Software<br>Key Login</td><td rowspan="3">VNC Login</td></tr>
<tr><td>Linux</td><td>VNC Login<br>SSH Login<br>Key Login</td></tr>
<tr><td>Mac OS</td><td>VNC Login<br>SSH Login<br>Key Login</td></tr>
</tbody></table>

## Prerequisites
With password login, you need to use the administrator account ID and the corresponding password to log in to the CVM. With key login, you need to create and download a private key to log in to the CVM.

### Prerequisites for login with remote login software and SSH
- Administrator account ID: the administrator account ID varies with the type of Linux instance. See the table below.

|Instance Operating System |Administrator Account ID|
|--|--|
|SUSE/CentOS/Debian| root|
|Ubuntu|ubuntu|

- Password:
  - If you select "Auto Generate Password" when starting the instance, then the initial password will be randomly assigned by the system. You can log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and click the "Internal Message" button on the right. In the "Check and accept the newly purchased server" page, the login account ID and initial password of administrator for CVM will be provided as shown below.
  ![](//mccdn.qcloud.com/img56a20f10a373a.png)
  - If you select "Custom Password" when starting the instance, then the password will be the one you specified when purchasing the CVM instance. To learn more about password, for example, what to do if I forget the login password, refer to [Login Password](/doc/product/213/6093).

### Prerequisites for login with key

To log in with an SSH key, first you need to create an SSH key, download the private key and bind it to Linux CVM. To learn more about key operations, refer to [SSH Key](/doc/product/213/6092).
![](//mccdn.qcloud.com/img56a5d553bddcf.png)

Log in to [Tencent Cloud Console](https://console.cloud.tencent.com), click "Cloud Virtual Machine" - "SSH Key" to enter the key window. Click "Create Key" button, and type a key name to create a new key. After the key is created, click "Download" button to download a private key.

Then right click on the newly created key ID, and select "Bind the Linux server to log in" to bind it. Key login is only available for CVM instances that have been bound with an SSH key.

## Windows system: use remote login software to log in to the Linux instance

On a Windows computer, you can log in to the Linux instance using remote login software. PUTTY is taken as an example in this case. There are also other types of login software for you to choose from.
### Install Windows remote login software
To log in to the Linux CVM from a local Windows computer, you need to use client software to establish a connection. Here PUTTY is taken as an example. Reference download link: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

### Use PUTTY to connect to Linux CVM
Open the Putty client, enter the following information in the "PuTTY Configuration" window:

- Host Name: Public IP of the CVM (Go to the ["Cloud Virtual Machine" page under Tencent Cloud Console](https://console.cloud.tencent.com/cvm), and you can get the public IP of the CVM on the list and detail pages).
- Port: port of the CVM, which must be 22. (Make sure port 22 of the CVM is open. See [Security Group](/doc/product/213/5221) and [Network ACL](/doc/product/215/5132) for details.)
- Connect type: select "SSH".

When all the information is entered, click "Open" to create a new dialog.
![](//mccdn.qcloud.com/img56a5d38a4ffbc.png)

In the Putty dialog window, enter the administrator account ID obtained from the "Prerequisites" step, and press Enter. Enter the login password obtained from the "Prerequisites" step, and press Enter to log in.
![](//mccdn.qcloud.com/img56a5d47b8b5da.png)

If the login fails, check if your CVM instance allows inbound traffic over port 22. Refer to [Security Group](/doc/product/213/5221) to check the Port. If your CVM is in [Virtual Private Cloud/VPC], check related subnet [Network ACL](/doc/product/215/5132) as well. 


## Windows system: log in to the Linux instance with an SSH key
Likewise, you need to use remote login software to log in to the Linux instance from a Windows computer. PUTTY is taken as an example in this case. There are also other types of login software for you to choose from.

### Install Windows remote login software
To log in to the Linux CVM from a local Windows computer, you need to use client software to establish a connection. Here PUTTY is taken as an example. Reference download link: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html. <font color="red">Download putty.exe and puttygen.exe. </font>

### Key format conversion
Open puttygen.exe, and click "Load" button. In the window that pops up, go to the path under which you store the private key downloaded in the Prerequisites step, and then select "All File (\*.\*)", select the downloaded private key (in this case it is file david, which is the name of the key), and click "Open".

![](//mccdn.qcloud.com/img56a5c48fb810a.png)

Enter the key name in the key comment column, enter the password for the private key (optional), and click "Save private key". In the window that pops up, select directory where you store the key, then type key name + ".ppk" in the file name column, and click "Save".
![](//mccdn.qcloud.com/img56a5c4ff657cc.png)

### Log in to Remote Linux CVM
Open putty.exe, and enter into "Auth" configuration page.
![](//mccdn.qcloud.com/img56a5c61c61e42.png)

Click the "Browse" button. In the window that pops up, go to the path where the key is stored, select the key, then click "Open" to return to the configuration page, and go to the "Session" configuration page.
![](//mccdn.qcloud.com/img56a5c67ea3edb.png)

Configure an IP address, port and connection type on the Session configuration page.

- IP: Public IP of the CVM. Go to the ["Cloud Virtual Machine" page under Tencent Cloud Console](https://console.cloud.tencent.com/cvm), and you can get the public IP of the CVM on the list and detail pages.
- Port: port of the CVM, which must be 22. (Make sure port 22 of the CVM is open. See [Security Group](/doc/product/213/5221) and [Network ACL](/doc/product/215/5132) for details.)

Enter a session name in the "Saved Sessions" input box (it is test in this case), then click the "Save" button, and double click the session name or click the "Open" button to issue a login request.
![](//mccdn.qcloud.com/img56a5c6bca781f.png)

If the login fails, check if your CVM instance allows inbound traffic over port 22. Refer to [Security Group](/doc/product/213/5221) to check the Port. If your CVM is in [Virtual Private Cloud/VPC], check related subnet [Network ACL](/doc/product/215/5132) as well. 

## Linux/Mac OS system: log in to the Linux instance with SSH
If you are a Mac OS user, open the Terminal that comes with the system and enter the following command. If you are a Linux user, run the following command directly:

```
ssh <username>@<hostname or ip address>
```
`username` is the administrator account ID obtained from the Prerequisites step, and <hostname or ip address> is the public IP or custom domain name of your Linux instance.

Enter the password obtained from the Prerequisites step (Note that there is only input and no output displays at this time), then press Enter to log in.

If the login fails, check if your CVM instance allows inbound traffic over port 22. Refer to [Security Group](/doc/product/213/5221) to check the Port. If your CVM is in [Virtual Private Cloud/VPC], check related subnet [Network ACL](/doc/product/215/5132) as well. 


## Linux/Mac operating system: log in to the Linux instance with key
If you are a Mac OS user, open the Terminal that comes with the system and enter the following command. If you are a Linux user, run the following command directly to set the private key file to readable only to you.

```
chmod 400 <下载的与云服务器关联的私钥的绝对路径> 
```
 
Run the following remote login command:

```
ssh -i "<下载的与云服务器关联的私钥的绝对路径>" <username>@<hostname or ip address>.
```

`username` is the administrator account ID obtained from the Prerequisites step, and <hostname or ip address> is the public IP or custom domain name of your Linux instance.

For example:

```
ssh -i "Mac/Downloads/shawn_qcloud_stable" ubuntu@119.xxx.xxx.xxx
```

If the login fails, check if your CVM instance allows inbound traffic over port 22. Refer to [Security Group](/doc/product/213/5221) to check the Port. If your CVM is in [Virtual Private Cloud/VPC], check related subnet [Network ACL](/doc/product/215/5132) as well. 

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

