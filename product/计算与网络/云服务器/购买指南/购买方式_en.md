The CVM supports two purchase modes: official website purchase and API purchase. This section will detail these two purchase modes.
## Official website purchase

All users can purchase CVMs on the official website of Tencent Cloud. By billing mode, users can purchase two types of CVMs: prepaid (monthly/annual purchase) and postpaid (billing in seconds, settled every hour). For details, see [Billing Instructions](https://cloud.tencent.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E).
For official website purchase of CVMs, click [here](https://cloud.tencent.com/doc/product/213/6998). In the following section, we will introduce official website purchase of two kinds of CVMs.

### Prepaid Package

1) Log in to [Tencent Cloud Service Purchase page](http://manage.qcloud.com/shoppingcart/shop.php?tab=cvm)

2) For the billing mode on the Purchase page, you can choose "Prepaid".

3) Choose the region, availability zone, CVM type, and select hardware, bandwidth or traffic as needed. Then you can confirm the order.

- Pay by Bandwidth is recommended for those users with stable network conditions. If you select fixed bandwidth, there is no limit on traffic, and the billing mode is "Hardware + Bandwidth" (Annual/Monthly Package).
- Pay by Traffic is recommended for those users with highly fluctuating network conditions. If you select pay-by-traffic, you are free to choose the peak bandwidth, and the billing mode is "Hardware (Annual/Monthly Package) + Traffic (according to the actual traffic consumed)".

4) You can pay for orders via the account balance and credit cards.
  
5) The CVM is activated after you pay for the order. 1-5 minutes later you can see the IP address, through which you can perform login management.


 
### Postpaid
 
1) Log in to [Tencent Cloud Service Purchase page](http://manage.qcloud.com/shoppingcart/shop.php?tab=cvm)
 
2) For the billing mode on the Purchase page, you can choose "Postpaid".

3) Choose the region, CVM type, and select hardware, bandwidth or traffic as needed. Then you can confirm the order.

- Pay by Bandwidth is recommended for those users with stable network conditions. If you select fixed bandwidth, there is no limit on traffic, and the billing mode is "Hardware + Bandwidth" (fixed fee, settled every hour).

- Pay by Traffic is recommended for those users with highly fluctuating network conditions. If you select pay-by-traffic, you are free to choose the peak bandwidth, and the billing mode is "Hardware (fixed fee, settled every hour) + Traffic (according to the actual traffic consumed)".

4) You can pay for orders via the account balance and credit cards.

5) The CVM is activated after you pay for the order. 10 minutes later you can see the IP address, through which you can perform login management. (After activating postpaid CVMs, make sure that your account has sufficient balance)

## Purchase via API
For API purchase of CVMs, see the API document [Create Prepaid Instances](https://cloud.tencent.com/doc/api/229/%E5%88%9B%E5%BB%BA%E5%AE%9E%E4%BE%8B%EF%BC%88%E5%8C%85%E5%B9%B4%E5%8C%85%E6%9C%88%EF%BC%89) and [Create Postpaid Instances](https://cloud.tencent.com/doc/api/229/%E5%88%9B%E5%BB%BA%E5%AE%9E%E4%BE%8B%EF%BC%88%E6%8C%89%E9%87%8F%E8%AE%A1%E8%B4%B9%EF%BC%89)

