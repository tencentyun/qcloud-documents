## Obtaining the Address on the Console

1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
2. The CVM list displays the instances under your account. Move the mouse cursor over the public IP of the CVM, and the "Copy" button will appear. Click the button to copy this IP address.
   ![](F:/mc.qcloudimg.com/static/img/be0c50402332ca78c347f372f7c54eef/image.png)

> **Note:**
> The public IP address is mapped to the private IP address through NAT. Therefore, if you view the attributes of a network interface within the instance (for example, by using the commands such as `ifconfig (Linux)` or `ipconfig (Windows)`), the public IP address is not displayed. To obtain the public IP address of an instance from within the instance, please see [Obtain the Public IP Address of an Instance Using Instance Metadata](#jump).

## Obtaining the Address Using API

&Nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For more information, please see [DescribeInstances API](/doc/product/213/9388).

<span id = "jump">  </span>

## Obtaining the Address Using Instance Metadata

1. Log in to the CVM instance. For more information, please see [Log in to Linux Instance](/doc/product/213/5436) and [Log in to Windows Instance](/doc/product/213/5435).
2. Enter the command:

```
curl http://metadata.tencentyun.com/meta-data/public-ipv4
```

If the returned value is in the following structure, you can see the public IP address:
![]()
For more information, please see [Instance Metadata](/doc/product/213/4934).

