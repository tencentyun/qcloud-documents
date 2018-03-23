
## Switching from Postpaid to Prepaid

To make it possible for you to switch the temporarily used postpaid CVM to the long-lasting and stable prepaid CVM, we launch the Switching from Postpaid to Prepaid service. You can use it at CVM console or via cloud API.

### Switching Rules 
You can switch the billing method at CVM console. Specific rules are as follows:

1. Either one or multiple instances can be switched from postpaid to prepaid.
2. After an instance is switched from postpaid to prepaid, it **cannot** be switched back. Proceed with caution to avoid unnecessary costs.
3. A new order is created when you switch an instance from postpaid to prepaid. The switch takes effect only after you pay this order. If the payment is not settled or has failed, an unpaid order will display at [My Orders](https://console.cloud.tencent.com/deal).
4. After you switch the billing method and pay the order, the instance will be billed on a prepaid basis immediately as of the time when the switch is complete.
5. You cannot switch the billing method of an instance that has been requested for switching but yet paid.
6. If the configuration information of the instance changes (for example, the configuration/bandwidth/disk is adjusted or the system is reinstalled) before payment, you cannot pay the order because the order amount does not match the instance. Cancel the unpaid order at [My Orders](https://console.cloud.tencent.com/deal) before proceeding with the switch again.
7. Switching from Postpaid to Prepaid is only available to instances and disks. The billing method of bandwidth will not be affected.
 


### Service Limits

1. You cannot switch the instance from postpaid to prepaid if the remaining quota of prepaid instances in the availability zone is less than the number of postpaid instances to switch. To increase your quota, check **Apply for Increasing Quota to buy CVMs** and [submit a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7&source=0).
2. The billing method of non-postpaid instances cannot be switched.
3. The network used by an instance is billed by bandwidth usage time and such method cannot be switched. It may be available in the future.
4. The billing method of batch-based instances such as BC1 and BS1 cannot be switched.
5. You cannot switch the billing method of a postpaid instance that has been requested for switching but yet paid.
6. You cannot switch the billing method of a postpaid instance configured with timed termination. To switch it, cancel the timed termination first.


### Switch from Postpaid to Prepaid at Console
	
1.	Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/index).
2.	**Switch a instance:** Check the instance to switch, and click **More -> Switch from Postpaid to Prepaid** at the top of the list or in the right Operation column.
![](https://mc.qcloudimg.com/static/img/cb41b7dc4842af4b6de218a08f531a26/image.jpg)

3.	**Switch multiple instances:** Check the instances to switch, click **More -> Switch from Postpaid to Prepaid** at the top of the list, and then the billing method of the instances are switched in batches. Reasons are given for instances that cannot be switched.
![](https://mc.qcloudimg.com/static/img/6fa0fd33a3c192fd1dc934f9d75b69e4/image.jpg)
4. In the **Switch from Postpaid to Prepaid** popup window,
	- Select the prepaid duration. You can only set the same duration for instances switched in batches.
	- Select **Auto Renewal** if needed.
![](https://mc.qcloudimg.com/static/img/9842518f2dd48137cff679226950dc72/image.jpg)
5. Click **Switch Now**. If the instance does not have an unpaid order for switching, the payment page appears.
![](https://mc.qcloudimg.com/static/img/e42b01f5b0d982f7412651bdaa5f94da/image.jpg)

6. After payment, the switch is complete.


### FAQ

**Q: What to do if the switch failed?**
A: [Submit a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7&source=0).

**Q: Does the switch affect how to bill bandwidth?**
A: No. Switching from Postpaid to Prepaid is only available to instances.

**Q: When does the prepaid billing method take effect after the switch?**
A: Immediately after you pay the order for switching.

**Q: Is the unpaid order for switching still valid when the instance configuration is upgraded?**
A: No. If you need to switch the billing method of the instance, cancel the unpaid order at [Order Center](https://console.cloud.tencent.com/deal) before proceeding with the switch again.
This is because a new order is created when you switch an instance from postpaid to prepaid. If the configuration information of the instance changes before payment, you cannot pay the order because the order amount does not match the instance.


