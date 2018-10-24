Once you've purchased and started a Linux instance, you can connect to and log in to it. The login method depends on your local operating system and whether the CVM instance can be accessed by Internet. See the table below for details.
<table><tbody>
<tr><th>Local operating system</th><th> Linux CVM instance with public IP</th><th>Linux CVM instance without public IP</th></tr>
<tr><td>Windows</td><td><br>Login via WebShell<br>Login via remote login software<br>Login by key</td><td rowspan="3">Login via VNC</td></tr>
<tr><td>Linux</td><td>Login via WebShell<br>Login via VNC<br>Login via SSH<br>Login by key</td></tr>
<tr><td>Mac OS</td><td>Login via WebShell<br>Login via VNC<br>Login via SSH<br>Login by key</td></tr>
</tbody></table>

## Prerequisites
### Prerequisites for login by password
**Administrator account and password are required for login by password**
- Administrator account: The administrator account varies with different types of Linux instances, as shown below.

| Instance Operating System | Administrator Account |
| ------------------ | ------ |
| SUSE/CentOS/Debian | root   |
| Ubuntu             | ubuntu |

- Password:
  - If **Auto Generate Password** is selected when you start an instance, the initial password is randomly assigned by the system. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com), and click the **Internal Message** button on the right. In the **Check the new CVM you purchased** page, the administrator account and initial password for logging in to CVM are provided as shown below.
    ![](//mc.qcloudimg.com/static/img/d2d6900e58fc4f7b141b770de23cd3d8/image.png)

  - If **Custom Password** is selected when you start a CVM instance, the password is the one you specified when purchasing the instance. For more information about password (for example, what to do if you forget the login password), please see [Login Password](/doc/product/213/6093).

### Prerequisites for login by key
**To log in to a CVM using a private key, you need to create and download the key.**
First, you need to create an SSH key, download the private key and bind it to the Linux CVM. For more information about operations on the key, please see [SSH Key](/doc/product/213/6092).

## Login from Local Windows PC by Password
### Login tool
Log in to a Linux instance by password using **remote login software** (in this case, PuTTY is used. You can also choose another login software).
### Procedure
1. Download and install the Windows remote login software from, for example: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html.

2. Connect to the Linux CVM using PuTTY. Open the PuTTY client, enter the following information in the PuTTY Configuration window:
  >- Host Name: Public IP of the CVM (log in to the [CVM Console](https://console.cloud.tencent.com) to obtain the public IP of the CVM in the list and details pages).
  >- Port: Port of the CVM, which must be 22. (Make sure port 22 of the CVM is open. For more information, please see [Security Group](/doc/product/213/5221) and [Network ACL](/doc/product/215/5132).)
  >- Connect type: Select "SSH".

3. When all the information is entered, click **Open** to create a new session.
  ![](//mccdn.qcloud.com/img56a5d38a4ffbc.png)

4. In the PuTTY session window, enter the administrator account obtained in the "Prerequisites" step, and then press Enter. Enter the login password obtained in the "Prerequisites" step, and then press Enter to log in to the instance.
  ![](//mccdn.qcloud.com/img56a5d47b8b5da.png)

>**Note:**
>If the login fails, check if your CVM instance allows inbound traffic over port 22. Check the port by referring to [Security Group](/doc/product/213/5221). If your CVM is in a [VPC](/doc/product/213/5227), also check the related subnet's [network ACL](/doc/product/215/5132). 

## Login from Local Windows PC by SSH Key
### Login tool
Log in to a Linux instance by SSH key using **remote login software** (in this case, PuTTY is used. You can also choose another login software).

### Procedure
1. Download and install the Windows remote login software from, for example: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html (two files are downloaded: putty.exe and puttygen.exe).

2. Select a private key. Open puttygen.exe, and click **Load** button. In the window that pops up, go to the path under which you store the private key downloaded in the "Prerequisites" step, and then select **All Files (\*.\*)**. Select the downloaded private key (in this case it is file david, which is the name of the key), and click **Open**.
  ![](//mccdn.qcloud.com/img56a5c48fb810a.png)

3. Convert the key. Enter the key name in the **key comment** column, enter the password for the encrypted private key, and then click **Save private key**. In the window that pops up, select the directory where you store the key, enter key name + ".ppk" in the file name column, and then click **Save**.
  ![](//mccdn.qcloud.com/img56a5c4ff657cc.png)

4. Open putty.exe to enter the **Auth** configuration page.
  ![](//mccdn.qcloud.com/img56a5c61c61e42.png)

5. Click the **Browse** button. In the window that pops up, go to the path where the key is stored, select the key, click **Open** to return to the configuration page, and then go to the **Session** configuration page.
  ![](//mccdn.qcloud.com/img56a5c67ea3edb.png)

6. Configure the IP, port and connection type for the server on the **Session** configuration page.
 - IP: Public IP of the CVM. Log in to the [CVM Console](https://console.cloud.tencent.com) to obtain the public IP of the CVM in the list and details pages.
 - Port: Port of the CVM, which must be 22. (Make sure port 22 of the CVM is open. For more information, please see "Security Group" and "Network ACL".)

6. Enter a session name in the **Saved Sessions** input box (enter "test" in this case), click **Save**, and then double click the session name or click **Open** to initiate a login request.
  ![](//mccdn.qcloud.com/img56a5c6bca781f.png)

>**Note:**
>If the login fails, check if your CVM instance allows inbound traffic over port 22. Check the port by referring to [Security Group](/doc/product/213/5221). If your CVM is in a [VPC](/doc/product/213/5227), also check the related subnet's [network ACL](/doc/product/215/5132). 

## Login from Local Linux/Mac OS PC by Password
### Login tool
Log in to the instance with SSH using the Terminal supplied with Mac OS system.

### Procedure
1. If you are a Mac OS user, open the Terminal supplied with the system and enter the following command. If you are a Linux user, run the following command directly: 	`ssh <username>@<hostname or ip address>` 
  (`username` is the administrator account obtained in the "Prerequisites" step, and `hostname or ip address` is the public IP or custom domain name of your Linux instance.)

2. Enter the password obtained in the "Prerequisites" step (there is only input and no output at this point), then press Enter to log in to the instance.

>**Note:**
>If the login fails, check if your CVM instance allows inbound traffic over port 22. Check the port by referring to [Security Group](/doc/product/213/5221). If your CVM is in a [VPC](/doc/product/213/5227), also check the related subnet's [network ACL](/doc/product/215/5132). 


## Login from Local Linux/Mac OS PC by Key
### Login tool
Log in to the instance using the Terminal supplied with Mac OS system.

### Procedure
1. If you are a Mac OS user, open the Terminal supplied with the system and enter the following command. If you are a Linux user, run the following command directly to set the private key file to be read only by you. `chmod 400 <absolute path of the private key downloaded to be associated with the CVM>'

2. Run the following remote login command: `ssh -i "<absolute path of the private key downloaded to be associated with the CVM>" <username>@<hostname or ip address>. `
  (`username` is the administrator account obtained in the "Prerequisites" step, and `hostname or ip address` is the public IP or custom domain name of your Linux instance. For example: `ssh -i "Mac/Downloads/shawn_qcloud_stable" ubuntu@119.xxx.xxx.xxx`).

>**Note:**
>If the login fails, check if your CVM instance allows inbound traffic over port 22. Check the port by referring to [Security Group](/doc/product/213/5221). If your CVM is in a [VPC](/doc/product/213/5227), also check the related subnet's [network ACL](/doc/product/215/5132). 

## Login via WebShell (recommended)
### Login tool
Login via WebShell is a method Tencent Cloud provides for you to connect to your CVMs through Web browser. Compared with login via VNC, login via WebShell provides a user experience more similar to login using PuTTY, SSH and other clients. If the CVM has a public IP and its login port is open, using WebShell can give you a better remote access experience.

**Advantages:**
- Supports copy and paste operations with shortcut keys.
- Supports scrolling with mouse wheel.
- Supports Chinese input.
- Features a high security (password or key is required for each login).

### Procedure
1. Log in to the [CVM Console](https://console.cloud.tencent.com). Select **Cloud Products** -> **Cloud Compute & Network** -> **Cloud Virtual Machine** from the top menu.
2. Go to the CVM list, as shown below, and then click the **Log In** button for the Linux CVM to which you want to log in.
  ![](https://mc.qcloudimg.com/static/img/0c9dd598a6b9405e43e54dd412fc7ffd/Snipaste_2018-02-02_18-32-54.png)
	
3. A new tab page appears, as shown below, where you can select **Login By Password** or **Login by Key**.
![](https://mc.qcloudimg.com/static/img/ed96f4638ad6b343ff38fc19452b8188/Snipaste_2018-02-02_18-20-17.png)

4. If the password or key is correct, it will pass the verification of system, and you'll log in to the Linux CVM successfully with WebShell.
![](https://mc.qcloudimg.com/static/img/31b25c56a1e6afdd39533436589ceb04/Snipaste_2018-02-02_18-21-02.png)

>**Note:**
>- The CVM is required to have a public IP.
>- SSH remote login port (default is 22) needs to be open on the CVM.


## Login via VNC
### Login tool
Login via VNC is a method Tencent Cloud provides for you to connect to your CVMs through Web browser. If the remote login client is not installed or cannot be used, you can connect to your CVM via VNC to check the CVM status and perform basic CVM management operations with your CVM account.

"Login via VNC" scenarios include at least the following: 
- Check the progress of a CVM startup
- When login with client SSH or mstsc failed


### Procedure
1. Log in to the [CVM Console](https://console.cloud.tencent.com). Select **Cloud Products** -> **Cloud Compute & Network** -> **Cloud Virtual Machine** from the top menu.

2. Go to the CVM list, as shown below, and then click the **Log In** button for the Linux CVM to which you want to log in.
  ![](https://mc.qcloudimg.com/static/img/0c9dd598a6b9405e43e54dd412fc7ffd/Snipaste_2018-02-02_18-32-54.png)
	
3. A new tab page appears, as shown below. The white window in the middle is used for login via WebShell, so you need to click the **x** button in the upper right corner to switch the login method (as shown below).
![](https://mc.qcloudimg.com/static/img/1ea9873436a2a0fbe6741a56b3f59a78/Snipaste_2018-02-02_18-44-59.png)

4. Click **Other Login Methods** in the upper right corner of the page.
  ![](https://mc.qcloudimg.com/static/img/1113ca3bde85dbc223a99f5a250d3088/%5E6AAAB397B29FEF3319E3BBD6157AB6D86C902D693A752276A2%5Epimgpsh_mobile_save_distr.jpg)

5. A new white window pops up. Locate the **Login via VNC using Browser** column, at the bottom, and then click **Log In Now**.
  ![](https://mc.qcloudimg.com/static/img/cbf20e70e6c24f2348b4aa7e12c9225e/Snipaste_2018-02-02_18-47-05.png)
	
6. Now, you can successfully log in to the Linux CVM via VNC.
   ![](https://mc.qcloudimg.com/static/img/079533e90ee16b95a63e19064a742a64/%5EDD57BACBDC8B333FCD0FFD6CA385F54D9D9CD790697DEB8847%5Epimgpsh_mobile_save_distr.jpg) 


>**Note:**
>- This terminal is exclusive, that is, only one user can log in to CVM via VNC at a time.
>- A successful login via VNC requires mainstream browsers such as Chrome, Firefox, IE10 or above.
>- File upload and download are not supported.

