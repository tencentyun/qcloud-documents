The Tencent Cloud instances' hardware devices can be adjusted easily. This is an important feature of cloud virtual servers that makes them more usable than physical servers. This document describes how to upgrade and degrade instance configuration and important considerations.

## Prerequisites and Considerations
### Instance status
You can adjust an instance's configuration when the instance has been either started up or shut down, and the change takes effect after the instance is forced to shut down and restarted.
> **Note:**
>- When the instance has been **shut down**, you can make changes in the console directly.
-  When the instance has been **started up**, you can make changes online, and confirm forced shutdown after changes are made. The changes to configuration take effect after the instance is restarted.
- You can adjust configuration **in batch** online for multiple instances. If there is a server that has been **started up** in the batch of instances, you need to confirm the forced shutdown individually, and the changes take effect after the servers are restarted.

### Limit of configuration adjustment
- Upgrading configuration
No limit is imposed on the number of times configuration upgrade can be performed. The upgrade takes effect immediately.
- Degrading configuration
 - Postpaid instances can be degraded at any time and for unlimited times.

### Hardware 
The instances **whose system disk and data disk are both cloud disks** support adjusting configuration.

### Change of private IP
For a very small number of instances, their private IPs will change after the configuration adjustment.

## Upgrading Configuration
You can upgrade the configuration of CVMs to adapt to you growing business. For all CVM types, the upgraded configuration takes effect immediately. That is, after you upgrade the configuration and pay the additional fees, the CVM will run with the new configuration immediately.

### Upgrading via console

1. Log in to the [console](https://console.cloud.tencent.com/), and then click the **CVM** tab on the left to go to the CVM list.

2. Locate the Operation column next to the instance to be adjusted, and click **More** -> **CVM Configuration** -> **Adjust Configuration**.

3. In the popup box, select the configuration you want to upgrade to, and then click **OK**.


 - **Popup box for postpaid instances:**
![](https://main.qcloudimg.com/raw/83c89f2a8d2fa39c875a7e4ffce2d38b.png)

### Upgrading via API
You can upgrade instance configuration using the APIs ResizeInstance and ResizeInstanceHour. For more information, please see [APIs for adjusting instance configuration](/doc/product/213/9394).

## Degrading Configuration
You can also degrade the configuration of CVM instances in console to adapt to your shrinking business.
The degrade method varies with different CVM types.


### Degrading postpaid instances
1. Log in to the [console](https://console.cloud.tencent.com/), and then click the **CVM** tab on the left to go to the CVM list.

2. Locate the Operation column next to the **postpaid** instance to be adjusted, and click **More** -> **CVM Configuration** -> **Adjust Configuration**.

3. In the popup box, select the configuration you want to degrade to, and then click **OK**.
![](https://main.qcloudimg.com/raw/4898656c35e6b28e52eeb3db03f105ab.png)
