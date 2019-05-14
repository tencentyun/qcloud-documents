### What are EIPs used for?
ElPs apply to the following scenarios:
1. Disaster recovery. We strongly recommend that you use EIPs for disaster recovery. For example, when one of your servers fails to provide services, you can unbind the EIP from this server and rebind it to a healthy server to resume service quickly.
2. Retain specific public IP. If you need to retain a specific public IP under your account, you can convert it to an EIP, which then can be used to access public network after being bound/unbound. This EIP is retained under your account until it is "released" by you.
3. Other special scenarios When you need to change an IP in other special cases, you can convert the ordinary public IP to an EIP and then bind/unbind the EIP. With limited EIP resources available, a quota is imposed on the number of EIPs for each region under a single account. Therefore, reasonable planning and use of EIPs are very important.

### How is EIP billed?

1. The fee displayed on the console applies to the EIPs that remain vacant for one hour. EIPs can be billed with an accuracy down to seconds. EIPs that have been bound/unbound many times are billed based on the total duration (in sec) for which they remain unbound.
2. The EIPs that remain unbound for less than 1 hour are billed on a pro rata basis.

### When is an EIP billed?
You can apply for, bind, unbind and release EIPs. With limited EIP resources available, an EIP is only billed for a small usage fee when it is unbound.

### How do I stop the billing of an EIP?
- When you no longer need an EIP, you can release it to stop the billing. Go to the [EIP Console](https://console.cloud.tencent.com/cvm/eip), click **More** -> **Release** in the Operation list, and then click **OK**. The released EIP will no longer be charged.
![](https://main.qcloudimg.com/raw/62aee3210544c2241a49d44c3970eee9.png)
- If you need to retain an EIP but want to stop the billing for it, bind it to a device (CVM, NAT). An EIP in a bound status is not charged.

### How can a CVM without public IP access public network?
If you did not purchase the public IP when you purchased a CVM or have returned the public IP, you can apply for an EIP on the [ElP Console](https://console.cloud.tencent.com/cvm/eip) and bind it to your CVM to allow the access to public network.

### Can I change my public IP?

You can change the public IP of an instance by binding and unbinding an EIP. For more information, please see [Changing Instance's Public IP](https://cloud.tencent.com/document/product/213/16642).

### How to I keep a public IP unchanged?

If you need to retain a specific public IP under your account, you can convert it to an EIP, which is then used to access public network after being bound/unbound. This EIP will be retained under your account until it is **released** by you.

For more information, please see [EIP Operation Guide](https://cloud.tencent.com/document/product/213/16586).

### Can an EIP be converted back to a public IP?

An EIP cannot be converted back to a public IP.

### Can an EIP be recovered?
An EIP cannot be recovered once being released.


