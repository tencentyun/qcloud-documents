To make the applications deployed on CVM instances publicly available, data must be transferred over the Internet and an Internet IP address (also known as public IP address) is required. Tencent Cloud provides Internet access via high-speed connected networks of Tencent Cloud IDC. The domestic multi-line BGP network covers more than 20 network operators and public network egress achieves cross-region switchover in a matter of seconds. This ensures that your users can enjoy high-speed and secure network no matter which network they use.



## Public IP Address
 - **Overview:** Public IP addresses are non-reserved addresses on the Internet. A CVM with a public IP address can access other computers on the Internet and can be accessed by other computers.
 - **How to obtain:** When you create a CVM, set the bandwidth to a value greater than 0 Mbps in the network. Then Tencent Cloud system automatically assigns a public IP address to the instance from Tencent Cloud public IP address pool. This address cannot be changed and it is not associated with your Tencent Cloud account.
 - **Configuration:** You can log in to a CVM instance with a public IP address on the Internet and configure it accordingly. For more information, please see [Log in to Linux Instance](/doc/product/213/5436) and [Log in to Windows Instance](/doc/product/213/5435).
 - **Translation:** The public IP address is mapped to the [private IP address](/doc/product/213/5225) of the instance through Network Address Translation (NAT).
 - **Maintenance:** All the public network interfaces of Tencent Cloud are managed by Tencent Gateway (TGW). Public network ENIs of Tencent CVM instances are configured on the API layer TGW, with CVMs unaffected. Therefore, when you use such commands as `ifconfig (Linux)` or `ipconfig (Windows)` in the CVM to view the network interface information, only the information of [private network](/doc/product/213/5225) is displayed. To view public network information, log in to [CVM Console](https://console.cloud.tencent.com/cvm) and go to CVM List/Details page.
 - **Fees:** Fees are charged on instances providing services through a public IP address. For more information, please see [Purchase Network Bandwidth](/doc/product/213/509#2.1.-.E5.B8.A6.E5.AE.BD.E5.8C.85.E8.AE.A1.E8.B4.B9).

## Public IP Address Release
You cannot actively associate or release the public IP address associated with an instance.
In the following cases, the public IP address is released or reallocated:
- **The instance is terminated.** When you actively terminate a postpaid instance or a prepaid instance is terminated upon expiry, Tencent Cloud will release the public IP address of the instance.
- **An [EIP address](/doc/product/213/5733) is associated or dissociated with the instance.** When an instance is associated with an EIP address, Tencent Cloud will release the original public IP address of the instance. When the instance is dissociated with the EIP address, the instance is automatically assigned a new public IP address. The previously released public IP address is returned to the public IP address pool and you cannot reuse it.

If you need a permanent public IP address, use an [EIP address](/doc/product/213/5733).
