## Obtaining the private IP address of an instance

### Obtaining the Address on the Console

 1. Log in to the [CVM Console](https:https://console.cloud.tencent.com/cvm/).

 2. The CVM list displays the instances under your account. Move the mouse cursor over the private IP of the CVM, and the "Copy" button will appear; click the button to copy the private IP.

![](https://mc.qcloudimg.com/static/img/2663aabcbe44c2ad372b5b8ba2bb6a1f/image.png)

### Obtaining the Address Using API
&Nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For more information, please see [DescribeInstances API](/doc/product/213/9388).

### Obtaining the Address Using Instance Metadata

 1. Log in to the CVM instance. For more information, please see [Log in to Linux Instance](/doc/product/213/5436) and [Log in to Windows Instance](/doc/product/213/5435).

 2. Enter the command:
```
curl http:https://metadata.tencentyun.com/meta-data/local-ipv4
```
If the returned value is in the following structure, you can see the private IP address:
![](https://mc.qcloudimg.com/static/img/14a13eccebc7eee6f83bc026adb30902/image.png)
For more information, please see [Instance Metadata](/doc/product/213/4934).

## Private Network DNS Settings

When a network resolution error occurs, users can set the private network DNS manually. The private network DNS can be set as follows:

- **For Linux users**. CVM DNS can be modified by editing the `/etc/resolv.conf` file on the CVM.
  Run the command `vi /etc/resolv.conf`, and edit the DNS IP according to the above table.
  ![](https://mc.qcloudimg.com/static/img/9c46100760f1049454b076a3c83c7f8a/image.png)
- **For Windows users**. On the CVM, open **Control Panel** -> **Network and Sharing Center** -> **Change Adapter Settings**, right-click the **Property** of the ENI, and double-click **IPv4** to modify the DNS server IP.
  ![](https://mc.qcloudimg.com/static/img/93b7bda1075530ff6e7ba5ece4ab71f4/image.png)