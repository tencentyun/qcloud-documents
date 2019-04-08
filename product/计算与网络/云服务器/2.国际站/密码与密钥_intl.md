### What is the difference between SSH key login and password login?
An SSH key is a way to remotely log into a Linux server by using a key generator to make a pair of keys (public and private). The public key is added to the server, and then the user can use the private key to complete the authentication and login. This method pays more attention to the security of the data, and is different from the manual input of the traditional password login mode, and has higher convenience.
Currently, Linux instance supports both password and SSH key login, however Windows instance supports only password login. Related documentation:
- [Login to Linux instance](https://intl.cloud.tencent.com/document/product/213/5436)
- [Log in to Windows instance](https://intl.cloud.tencent.com/document/product/213/5435)

### If I use SSH key login and password login at the same time?
No. When you log in to the Linux instance using the SSH key pair, the password login is disabled to improve security. 

### What should I do if I forgot my password?
You can log in to the CVM console, reset the password, and then log in to the instance with the new password. For details on how to reset your password, see [Login Password Operation Guide](https://intl.cloud.tencent.com/document/product/213/17008).

### How do I create an SSH key, and what shall I do if I lose it?
For the creation of the key, please see [SSH Key](https://intl.cloud.tencent.com/document/product/213/16691). In case you lose your key, we provide two ways to solve it. :

 - Create a new key through the CVM console and bind the original instance with the new one. For details, please refer to [SSH Key](https://intl.cloud.tencent.com/document/product/213/16691). Once you have created a new key, you can log in to the instance with the new key on the CVM Console > CVMs > Load Key.
 - Reset your password through the CVM console and log in to the instance with your new password. See [Login Password Operation Guide](https://intl.cloud.tencent.com/document/product/213/17008) for details.

### How do I bind/unbind an SSH key to a server?

Please refer to **Binding/Unbinding Key with Server** section in [SSH Key Operation Guide](https://intl.cloud.tencent.com/document/product/213/16691).

### How do I modify the SSH key name/description?

Please refer to the **Modify the SSH Key Name/Description** section in [SSH Key Operation Guide](https://intl.cloud.tencent.com/document/product/213/16691) 

### How do I delete an SSH key?

Please refer to the **Delete SSH Key** section in [SSH Key Operation Guide](https://intl.cloud.tencent.com/document/product/213/16691) .

### What are the usage restrictions for SSH keys?

Please refer to the **Usage Limits** section in [Introduction to SSH Keys](https://intl.cloud.tencent.com/document/product/213/6092) .

### I can't log in to the Linux instance using SSH key

You can refer to the following solutions:

1. In [CVM Console](https://console.cloud.tencent.com/cvm/sshkey), enter the key name to find and key ID, click the ID to see CVMs bound with this key.

2. Cancel or modify the security group policy in [Console](https://intl.console.cloud.tencent.com/cvm/securitygroup). See [Safety Group Operation Guide](https://intl.cloud.tencent.com/document/product/213/12450)

3. In the [Console](https://console.cloud.tencent.com/cvm/sshkey), cancel the key login method, or follow the instructions to correctly set the key to log in to the server. See [SSH Key Operation Guide](https://intl.cloud.tencent.com/document/product/213/16691)

4. Use VNC to log in to the instance to check whether the NIC status and IP configuration information are correct. See [Login Linux Instance Operation Guide](https://cloud.tencent.com/document/product/213/5436)
![](https://main.qcloudimg.com/raw/17fa30409db52577fc8fed99a43264d2.png)

5. Check if the server's SSHD service is running properly and that there are no problems with the configuration files such as ports.
   ![](https://main.qcloudimg.com/raw/32364a0beac01cc63c82d61ebadf89c2.png)

6. Check if the server's iptables firewall is intercepted and check if its policy is OK. ![](https://main.qcloudimg.com/raw/9dbc3baa79c24673e59fb228cc57afad.png)

7. Check if the server's tcp_wrappers has interception control for SSH access.
   ![](https://main.qcloudimg.com/raw/76ac9f09b606cbd7f2121f4306ff3bc8.png)

8. Confirm if the user of the SSH login server is blocked by the PAM module 
   ![](https://main.qcloudimg.com/raw/c7af6184b32867d0eb77cdfe1c362d04.png)

9. Check if the instance is operating correctly in Mode 3 or Mode 5:
   ![](https://main.qcloudimg.com/raw/0371d6b8c5a0b89ac70cff6b56adf3be.png)

