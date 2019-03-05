Once you've started a Windows instance, you can connect to and log in to it. The login method depends on your local operating system and whether the CVM instance can be accessed by Internet. See the table below for details.
<table><tbody>
<tr><th>Local operating system</th><th> Instance with public IP</th><th>Instance without public IP</th></tr>
<tr><td>Windows</td><td>Login via VNC<br>Remote Desktop Connector</td><td rowspan="3">Login via VNC</td></tr>
<tr><td>Linux</td><td>Login via VNC<br>Login via rdesktop</td></tr>
<tr><td>Mac OS</td><td>Login via VNC<br>Login via rdesktop</td></tr>
</tbody></table>

## Prerequisites
Administrator account and password are required for logging in to a CVM.

- Administrator account: It is **Administrator** for all Windows instances. 
- Password:
  - If **Auto Generate Password** is selected when you start an instance, the initial password is randomly assigned by the system. Log in to [Tencent Cloud Console](https://cloud.tencent.com/login), and click the **Internal Message** button on the right. In the **Check the new CVM you purchased** page, the administrator account and initial password for logging in to CVM are provided as shown below.
![](https://main.qcloudimg.com/raw/9cd945cd28f842bae2af1a1cc07fce41.png)

  - If **Custom Password** is selected when you start a CVM instance, the password is the one you specified when purchasing the instance. For more information about password, please see [Login Password](/doc/product/213/6093).

## Login from Local Windows PC
### Login tool
**On a local Windows machine, log in to the Windows instance using Remote Desktop Connection.**

### Procedure
1. On the local Windows machine, click **Start** -> **Run**, enter `mstsc` command to open the Remote Desktop Connection dialog box.

2. Enter the public IP of the Windows server in the input box (log in to [CVM Console](https://console.cloud.tencent.com) to check the public IP of the CVM), as shown below:
![](https://main.qcloudimg.com/raw/adf42c508c505f0259ea1f841148972c.png)

3. Click **Connect**, and enter the administrator account and password obtained in the "Prerequisites" step in the new page that appears, as shown below:
![](https://main.qcloudimg.com/raw/0dca776e824d8ed669bf3915f88dadaa.png)
![](https://main.qcloudimg.com/raw/5cad03de2650757d56264b6817e0345e.png)

4. Click **OK** to log in to the Windows CVM instance.

>**Note:**
>If the login fails, check if your CVM instance allows inbound traffic over port 3389. Check the port by referring to [Security Group](/doc/product/213/5221). If your CVM is in a [VPC](/doc/product/213/5227), also check the related subnet's [network ACL](/doc/product/215/5132). 

## Login from Local Linux PC
### Login tool
**Use rdesktop for logging in to a Windows instance from a local Linux PC.**
You need to install the applicable Remote Desktop Connector (rdesktop is recommended). For more information about rdesktop, please see [rdesktop official instructions](http://www.rdesktop.org/).

### Procedure
1. Install rdesktop.
 	Run the `rdesktop` command to check if the system has been installed. If not, [go to github to download the latest installer package >>](https://github.com/rdesktop/rdesktop/releases)
 	Or click the link below to download the v1.8.3 version directly:
 	[rdesktop-1.8.3.tar.gz](https://mc.qcloudimg.com/static/archive/06483121ce067b537342687dd6a909d8/rdesktop-1.8.3.tar.gz)
 	[rdesktop-1.8.3.zip](https://mc.qcloudimg.com/static/archive/24adfd7586f55bd96cd6714a6078a4df/rdesktop-1.8.3.zip)

 		And run the following command in the relevant directory to decompress and install it.
	```
	tar xvzf rdesktop-<x.x.x>.tar.gz ##Replace x.x.x with the downloaded version number 
	cd rdesktop-1.8.3
	./configure 
	make 
	make install
	```
2. Connect to remote Windows instance
	Run the command below (Replace parameters in the example with yours):

	```
	rdesktop -u Administrator -p <your-password> <hostname or ip address> 
	```
	"-u" is followed by the username, which is `Administrator`; "-p" is followed by the password obtained in the "Prerequisites" step; <hostname or ip address> is the public IP or custom domain name of your Windows instance.

>**Note:**
>If the login fails, check if your CVM instance allows inbound traffic over port 3389. Check the port by referring to [Security Group](/doc/product/213/5221). If your CVM is in a [VPC](/doc/product/213/5227), also check the related subnet's [network ACL](/doc/product/215/5132). 

## Login from Mac OS PC
### Login tool
**If you are a Mac OS user, log in to the Windows instance using Microsoft Remote Desktop for Mac.**
For more information on how to download Microsoft Remote Desktop for Mac, please see [Instructions for Downloading Remote Login Client for Mac OS](/document/product/213/12444).

### Procedure
1. Open the client tool.

2. Enter the public IP of the Windows server in the input box.

3. Click **Connect**, and enter the administrator account and password obtained in the "Prerequisites" step in the new page that appears.

>**Note:**
>If the login fails, check if your CVM instance allows inbound traffic over port 3389. Check the port by referring to [Security Group](/doc/product/213/5221). If your CVM is in a [VPC](/doc/product/213/5227), also check the related subnet's [network ACL](/doc/product/215/5132).  

## Login via VNC
### Login tool
Login via VNC is a method Tencent Cloud provides for you to connect to your CVMs through Web browser. If the remote login client is not installed or cannot be used, you can connect to your CVM from VNC to check the CVM status and perform basic CVM management operations with your CVM account.

"Login via VNC" scenarios include at least the following:
- Check the progress of a CVM startup
- When login with client SSH or mstsc failed 

### Procedure
1. Log in to the [CVM Console](https://console.cloud.tencent.com).

2. In the **Operation** column of CVM list, click **Log In** button to connect to the Windows CVM via VNC.
![](https://main.qcloudimg.com/raw/f94280c97ed049b5887b40ec398cb98b.png)

3. Press Ctrl+Alt+Del at the top left corner to go to the system login page:
![](https://main.qcloudimg.com/raw/2d290cc6b0da50c033260d241e239537.png)

>**Note:**
>- This terminal is exclusive, that is, only one user can log in using VNC at a time.
>- A successful login via VNC requires mainstream browsers such as Chrome, Firefox, IE10 or above.
>- File upload and download are not supported.

