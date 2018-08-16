## Billing Items
The charges for Cloud Load Balancer service include instance rental fee and bandwidth traffic fee of backend servers. For example, if 3 CVMs are associated with a CLB instance, then the actual charges will include the cost for the CLB instance and the cost for the 3 CVM instances associated with it (cost for instances will be accounted into network charges).

## Postpaid
The price for CLB has been reduced in June, 2017. The service is billed flexibly on a postpaid basis and supports hourly billing. You can activate or terminate CLB instance at any time, which is billed by the actually usage. Billing method is adjusted as follows:

1. The billing method for public network-based load balancer is adjusted from prepaid 4.41 USD (0.147 USD/day) to postpaid 0.003 USD/hour. The price is reduced by more than 50%.
2. For new load balancer customers, the postpaid billing method is applied.
3. For existing customers, the fees for previous month have been liquidated in the early morning of July 31, 2017, and the new billing policy has been applied. Please make sure your account balance is sufficient.
4. The private network-based load balancer is still free of charge.

For hourly billing, all fees are charged on the hour with no need to pay in advance.

After the postpaid mode is activated for a load balancer instance, the system freezes configuration fee of an hour for the instance, and settles the service fees on the hour (Beijing time). The frozen fees for CLB instance will be unfrozen after you delete the instance.
Load balancer instances are billed on hour basis, and are settled based on actual numbers of hours. The billing for a CLB instance starts upon its successful creation, and ends when you initiate the termination operation. Use of less than one hour will be billed for one hour.

> **Note:**
>When you create a postpaid load balancer instance, the system freezes the fee of one hour. Please make sure your account balance is sufficient.
After the load balancer is purchased, the configuration fee will continue to be charged at 0.003 USD/hour even it is idle (there is no access and backend CVM is not bound).

## Arrear Isolation Policy

- In case of arrears, the instance service will be suspended 24 hours later, and you will be reminded within 24 hours upon arrear via SMS message/email. Please top up within 24 hours to avoid service suspension.
- If you do not renew within 24 hours upon, the instance service will be suspended and **isolated**. After the instance is isolated, the service will be suspended and the billing for your load balancer instance will be stopped. Configuration data of the instance will be retained for seven days. If you top up within seven days, the service will be automatically enabled for you. Otherwise, it is regarded as giving up the CLB service, and the relevant configuration data will be released.
- Tencent Cloud will send you an SMS message/email one day before the release of isolated instance. Relevant configuration data will be permanently deleted after the instance is released, and cannot be restored.

>**Note: **
>Tencent Cloud will not be unbind a load balancer from CVM, unless the **CVM** is isolated (prepaid CVM that is put into recycle bin; postpaid CVM that has been in arrears for more than two hours).

## FAQ

1. How often will a deduction be performed for hourly billing?
A: Once per hour.
2. Is the price reduced by more than 50% after adjustment?
A: It is 0.147 USD/day for the old billing method and you need to pay 30 × 0.147 = 4.41 USD for consecutive 30-day use.
It is 0.003 USD/hour for the new billing method and you need to pay 0.003 × 24 × 30 = 2.16 USD for consecutive 30-day use. Therefore, you save (4.41 - 2.16) / 4.41 × 100% = 51%.
3. Why is the billing method changed?
A: The postpaid method is more flexible, and do not need to freeze the cost in advance. You can release instances at any time when you do not need them, and save cost in this billing method.

## Billing for Cross-region Binding

CLB's cross-region binding feature allows you to modify the region attribute of your backend CVM. For example, you can bind LBs in [Beijing], [Shanghai] and other cities to the backend cluster in [Guangzhou]. This feature is in beta test for now. Submit a
[Ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=163&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB) for application.

Its billing method is as follows:
1. Intra-region binding: free.
2. Cross-region binding (private network-based cross-region binding & basic network-based cross-region binding)
 - Postpaid on a daily basis.
 - Calculated as the peak bandwidth of the day multiplied by the applicable tiered price.
 - Peak bandwidth of the current day is calculated as follows: Inbound/outbound bandwidth is captured every 5 minutes, and the maximum is taken as the peak bandwidth.
For more information, please see the following table:

<table>
        <tbody>
                <tr>
            <th style="width: 10%;" rowspan="2">Feature</th>
            <th style="width: 25%;" rowspan="2">Billing Method</th>
                        <th style="width: 25%;" rowspan="2">Bandwidth</th>
            <th style="width: 40%;" colspan="4">Price</th>
        </tr>
        <tr>
            <th>Beijing<br>Chengdu<br>Shanghai<br>Shanghai Finance Zone<br>Guangzhou<br>Shenzhen Finance Zone</th>
                        <th>Hong Kong</th>
                        <th>Singapore<br>Silicon Valley<br>Frankfurt</th>
            <th>Toronto</th>
        </tr>
                <tr>
        <td>Intra-region binding</td>
                <td colspan="6" >Free</td>
                <tr>
                <tr>
            <td rowspan="5">Cross-region binding</td>
                        <td rowspan="5">Peak bandwidth of the day<br><br>Charged on a daily basis (USD/Mbps/day)<br><br>Peak bandwidth is calculated using the average bandwidth per 5 minutes<br></td>
                        <td>(0 , 20] Mbps</td>
                        <td>2.941</td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
        </tr>
           <tr>
                <td>(20 , 100] Mbps</td>
                        <td>1.765</td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                </tr>
                <tr>
                <td>(100 , 500] Mbps</td>
                <td colspan="4" rowspan="4">Please contact business department<br>
                </tr>
                <tr>
                <td>(500 , 2000] Mbps</td>
                </tr>
             <tr>
                <td >> 2,000 Mbps</td>
                </tr>
                    <tr>
</tbody></table>

>**Note: **
> Contact business department to inquire more about the prices.

**Example:**
If the load balancer is in Shanghai and the backend CVM is in Guangzhou, and the peak outbound bandwidth of the day is 20 Mbps and the peak inbound bandwidth is 30 Mbps, the cost of the day is: 30 * 1.765 = 52.95 USD, which is charged by cloud load balancer side.
