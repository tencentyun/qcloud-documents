Elastic IP, is referred to as ElP for short. It is a static IP designed for dynamic cloud computing, and a fixed public IP in a certain region. In case of an instance failure, the EIP can be remapped to another instance in your account (or [NAT gateway instance](/doc/product/215/%E7%BD%91%E5%85%B3#2.-nat.E7.BD.91.E5.85.B3)) quickly to block the failure.


## Common Operations
The following describes how to use EIPs.

### Applying for EIPs 

 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).
	
 2. In the left navigation pane, click **EIP**.

 3. Click the **Apply** button, enter a region and the number of EIPs you want to apply for, and then click **OK**.

 4. After this, you can see in the list the new EIP(s) you just applied for, which have/has an unbound status.

<span id = "jump2">  </span>
### Binding EIPs to cloud products

 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).

 2. In the left navigation pane, click **EIP**.

 3. In the EIP list, click the **Bind** button next to the EIP to be bound to a cloud product. (If the EIP is already bound to an instance, this button is unavailable. Please unbind it first.)
	
 4. In the popup box, select the cloud product type that you want to bind, and then select the cloud product instance ID. Click the **Bind** button to complete the binding.

### Unbinding EIPs from cloud products

 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).

 2. In the left navigation pane, click **EIP**.

 3. In the EIP list, click the **Unbind** button next to the EIP that is already bound to a cloud product.

 4. Click **OK**.
 
>**Note:**
> After unbinding, the cloud product instance may be assigned a new public IP, which may be different from the one before binding.

<span id = "jump">  </span>
### Releasing EIPs
 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).

 2. In the left navigation pane, click **EIP**.

 3. In the EIP list, click **More** -> **Release** button next to the EIP to be released.

 4. Click **OK**.


#### Adjusting bandwidth
 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).

 2. In the left navigation pane, click **EIP**.

 3. In the EIP list, click the **Change Bandwidth** button next to the EIP for which you want to adjust bandwidth.

 4. Adjust the target bandwidth value in the Adjust Bandwidth page.
 
 5. Click **OK**.

### Converting public IP to EIP
The public IP purchased along with the CVM instance is an ordinary public IP. It does not have elasticity and cannot be mounted and unmounted. Tencent Cloud allows you to convert an ordinary public IP to an EIP by following the steps below:

 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).

 2. Click the Convert icon.
![](https://main.qcloudimg.com/raw/7ccc4a036037b497feecb29d1725b54b.png)
 3. Click **Confirm Conversion**.
![](https://main.qcloudimg.com/raw/3d20c058c66975f847e68e42ae944d6f.png)


## Troubleshooting
Network inaccessibility may occur with an EIP. This is generally caused by the following reasons: 

- The EIP is not bound to any cloud product. For more information about how to bind an EIP to cloud products, please see [Binding EIP to Cloud Products](#jump2).

- Security policy is invalid. Check if there is a valid security policy (security group or network ACL). If the bound cloud product has a security group policy, for example: access to 8080 port is denied, the port 8080 of the EIP is also inaccessible.

