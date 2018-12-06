### How do I upgrade/degrade the configuration of a CVM?

Only the instances **whose system disk and data disk are both cloud disks** support adjusting configuration. 

For more information about how to upgrade/degrade instance configuration, please see [Adjusting Instance Configuration](https://cloud.tencent.com/document/product/213/2178).

For more information about how to adjust bandwidth/network configuration, please see [Adjusting Network Configuration](https://cloud.tencent.com/document/product/213/15517).

If your configuration adjustment does not take effect, [submit a ticket](https://console.cloud.tencent.com/workorder/category) to contact us.

### How do I check the records of configuration adjustments?

The records of configuration adjustments can be found in the operation log in the upper right corner of the [Console](https://console.cloud.tencent.com/cvm/index). For a prepaid instance, an order will be generated in the income & expense statement each time the instance is upgraded or degraded.
![](https://main.qcloudimg.com/raw/276e7199bedf1c6d4745d6dd18003f67.png)

### Can bandwidth be adjusted when the CVM is renewed in Recycle Bin?
No. Adjustment to bandwidth configuration can only be made after the instance is successfully renewed in Recycle Bin.

### Does a postpaid instance support adjusting configuration?
The instances whose data disk and system disk are both cloud disks support adjusting configuration. The configuration of a postpaid instance can be upgraded or degraded for unlimited times; the configuration of a prepaid instance can be upgraded for unlimited times, but can **only be degraded once**.

### How many times can the configuration of a CVM be degraded at most?
Each instance can only be degraded once.

### Will the usage period of a prepaid instance be extended after the instance is degraded?
It may not be extended. This depends on whether the remaining amount of your actual payment at the time of purchase after the deduction of fees for the used resources is greater than the amount to be paid for the degraded configuration. If so, the usage period is extended, otherwise it remains unchanged.
#### Example:
An instance with a configuration of "Standard, 2-core, 4-GB local disk, without bandwidth" is priced at 102 CNY/month. You purchased the instance for a usage period of one year with a 400 CNY voucher at a discount of 83% off. When the instance has been used for 2 months, its configuration is degraded to "Standard, 1-Core, 2-GB local disk, without bandwidth", which is priced at 51 CNY/month.
Discounted price: 102  \* 12 \* 0.83 = 1015.92 CNY
Actual paid amount: 1015.92 - 400 = 615.92 CNY
Remaining amount after deduction of fees for used resources: 615.92 - 102 \* 2 = 411.92 CNY
The amount to be paid for the degraded instance (1-core CPU, 2-GB local disk) for a usage period of 10 months is 51 \* 10 = 510 CNY
**Conclusion:** Because 411.92 < 510, the usage period remains unchanged.
> The above prices are only used as examples, and are not actual prices listed on the official website.

