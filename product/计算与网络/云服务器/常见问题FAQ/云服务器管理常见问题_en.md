## FAQ on configuration adjustment
### 1. Where can I check the history of my configuration changes? 
You can view the record of the adjustments you've made to CVM configuration in the Operation Logs at the upper right corner of the console. For CVMs with an annual or monthly plan, an order will be generated in the transaction statement for both upgrading and degrading of configuration.
![](//mccdn.qcloud.com/static/img/b759463ebe8f1e988902456f2aed07c8/image.png)

### 2. How does the annual or monthly plan work for degrading of configuration and extension of expiry time? 
The refundable difference between the unexpended part of you've paid and the unexpended part for the target configuration by the time the configuration of your CVM needs to be degraded is calculated. If the difference is larger than zero, that difference will be converted into the length of time supported by the target configuration and the expiry time of the server will be extended accordingly. If the difference is less than zero, the expiry time of your server will not be adjusted.

### 3. Is there a possibility that the configuration of the server with an annual or monthly plan is degraded but an extended expiry time is not offered? 
Yes. 
For example, the price for your configuration A is 100CNY/month as shown on the official website before you degrade it, whereas you purchased it at the price of 50 yuan/month with a 50% promotion discount. After ten days of use, you need to degrade the configuration to B, which is priced 60 yuan/month on the official website. In this case, the difference between the paid price (50 yuan/month) and the official website price (60 yuan/month) is less than zero, so the expiry time of your server will not be adjusted.  
This may also happen when vouchers or other non-cash payment methods are used to make the purchase. In this case, you will be prompted with the following when degrading the configuration:

```
You have three chances to degrade your configuration, and you have two left; 
The original configuration is 2-core 8GB and the target one is 1-core 2GB; 
For degraded configuration, a price difference in the amount of ＊＊ yuan will refunded based on the paid amount and the price shown on the official website; 
As the difference to refund is less than zero, the expiry time of your server will not be adjusted.
```

### 4. How does the charge-by-quantity work after an adjustment is made? 
It will apply immediately upon completion of the adjustment, with the time accurate to the second. 
For example, if the original configuration 1-core 2G is successfully upgraded to 2-core 4G at 1:23:21, by 2:00 o'clock you will be charged on the basis of 1-core 2G for the first 23 minutes and 21 seconds, and 2-core 4G for the remaining 36 minutes and 39 seconds, with the time accurate to the second.

## Questions on network adjustment
### 1. What is the Bandwidth Package mode?
Bandwidth Package is a billing mode for CVMs sharing public network bandwidth. The mode works based on pre-purchased Bandwidth Package and payment for the excess part (if any) by month. You can purchase a Bandwidth Package for the next few months in the current month:
No extra fee will apply if the bytes used in the next month are less than the package limit. If the bytes used in the next month are larger than the package limit, you will be charged for the excess part by the end of that month.
The rates are as follows:

| | Bandwidth Package (CNY/Mbps) |Exceeding Package (CNY/Mbps) |
| --------- | --------- | --------- |
| Mainland China | 100 | 108 |
| Hong Kong | 100 | 108 |
| North America | 200 | 216 |
