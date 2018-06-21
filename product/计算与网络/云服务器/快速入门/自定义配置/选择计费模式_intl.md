Tencent Cloud CVM instances support the following billing methods:

- **Prepaid**: This method requires customers to pay off the fees of a CVM instance for a period of one or multiple months/years in advance. It is cheaper than postpaid plan and is suitable for scenarios where device demands are estimated in advance.
-  **Postpaid**: It is a flexible billing method for CVM instances. A CVM can be activated/terminated at any time and is billed by the actual usage, with a time granularity down to second. Fees are charged every hour on the hour with no need to pay in advance. This billing method is suitable for the scenarios where the demand for devices fluctuates dramatically, such as snap-up campaign on an e-commerce site, with the unit price 3-4 times higher than that of Prepaid billing method.

Prepaid and Postpaid billing methods are provided to satisfy user requirements in different scenarios. Comparison between these two methods is shown below. For more information, please see [Billing Methods](https://cloud.tencent.com/document/product/213/2180).


| Billing method of CVM | Prepaid | Postpaid |
|---------|:---------:|:---------:|
| Payment method | Pay in advance | Fees are frozen at the time of purchase and billed on an hourly basis |
| Billing unit | CNY/month | CNY/sec |
| Unit price | Unit price is low | Original unit price is high and reduced on a tiered basis</br>The unit price of a postpaid CVM that is used for more than 15 consecutive days is basically the same as that of a prepaid CVM.
| Minimum usage period | At least one month | Fees are calculated per second and settled per hour, and the resources are released whenever you purchase the service. |
| Adjustment of instance configuration | Configuration can be upgraded/downgraded at any time. There is no limit on the number of times a CVM can be upgraded, but downgrade can only be performed once. | Configuration can be upgraded/downgraded at any time without limitation. |
| Application scenario | Suitable for mature businesses with stable and long-term device demands | Suitable for scenarios where the demand for devices fluctuates dramatically, such as snap-up campaign on an e-commerce site |



