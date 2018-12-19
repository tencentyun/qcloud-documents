### What are the restrictions for logging in with an SSH key?

Please see the **Use Limits** section in [SSH Key Overview](https://cloud.tencent.com/document/product/213/6092).

### How do I create an SSH key?

Please see the **Creating an SSH Key** section in the [SSH Key Operation Guide](https://cloud.tencent.com/document/product/213/16691).

### How do I bind/unbind an SSH key to/from the server?

Please see the **Binding/Unbinding Key to/from Server** section in the [SSH Key Operation Guide](https://cloud.tencent.com/document/product/213/16691).

### How do I modify the SSH key name/description?

Please see the **Modifying SSH Key Name/Description** section in the [SSH Key Operation Guide](https://cloud.tencent.com/document/product/213/16691).

### How do I delete an SSH key?

Please see the **Deleting an SSH Key** section in the [SSH Key Operation Guide](https://cloud.tencent.com/document/product/213/16691).

### How do I troubleshoot the failure to log in to a Linux instance using an SSH key?

The solutions are as follows:

1. Cancel or modify the security group policy on the [Console](https://console.cloud.tencent.com/cvm/securitygroup). See [Security Group Operation Guide](https://cloud.tencent.com/document/product/213/12450)

2. Cancel "login by key" on the [Console](https://console.cloud.tencent.com/cvm/sshkey) or set "login through key authentication" as instructed. See [SSH Key Operation Guide](https://cloud.tencent.com/document/product/213/16691)

3. Log in to the instance via VNC to check whether the ENI status and IP configuration information are correct. See [Logging in to a Linux Instance](https://cloud.tencent.com/document/product/213/5436)

   ![](https://main.qcloudimg.com/raw/17fa30409db52577fc8fed99a43264d2.png)

4. Verify whether the instance is running normally in Mode 3 or Mode 5:
   ![](https://main.qcloudimg.com/raw/0371d6b8c5a0b89ac70cff6b56adf3be.png)

5. Verify whether the sshd service of the server is running normally and there is no problem with the configuration such as port.
   ![](https://main.qcloudimg.com/raw/32364a0beac01cc63c82d61ebadf89c2.png)

6. Verify whether the server's iptables firewall has blocked the access and whether its policy is OK.![](https://main.qcloudimg.com/raw/9dbc3baa79c24673e59fb228cc57afad.png)

7. Verify whether the tcp_wrappers of the server has blocked SSH access.
   ![](https://main.qcloudimg.com/raw/76ac9f09b606cbd7f2121f4306ff3bc8.png)

8. Verify whether the user who wants to log in to the server via SSH is blocked by the PAM module (this is a rare case):
   ![](https://main.qcloudimg.com/raw/c7af6184b32867d0eb77cdfe1c362d04.png)
