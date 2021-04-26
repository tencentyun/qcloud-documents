1. Log in to Tencent Cloud Console and open the Console via the URL [https://console.cloud.tencent.com/pgsql](https://console.cloud.tencent.com/pgsql)

2. On the upper-right corner of the console, click "New Instance" and choose from the pop-up window.
>**According to product operation strategy, you can apply to use PostgreSQL for free before December 31, 2016. There's no need to purchase in the purchase page.**

3. On the purchase page, specify database instance information according to your demand and click "Purchase Now";
> Take note of the following configurations when purchasing instance:
>
>- Billing method: Prepaid, which means you need to pay the charges before you can use the instances.
>- Region: The region to which the instance is actually deployed. It is recommended to choose the same region as the CVM to be connected in order to minimize delay.
>- Availability zone: Physical IDCs whose electric power facilities and networks are independent from each other within the same region. It is recommended to choose the same availability zone as the CVM to be connected in order to minimize delay.
>- Network type: Network in which the instance resides. This cannot be changed once specified. It is recommended to choose the same network as the CVM to be connected in order to minimize delay.
>- Database kernel version: PostgreSQL database kernel version. There are differences between the features of [9.3.5](https://www.postgresql.org/docs/9.3/static/index.html) and [9.5.4](https://www.postgresql.org/docs/9.5/static/index.html), for more information, please see [PostgreSQL Official Instructions](https://mariadb.org/).
>- Instance specification: Instance performance and base price depend on its specification.
>- Disk: Default disk is SSD (local disk). More disk types will become available in the future.
>- Project: If you want different databases to be managed by different teams, you can specify projects that belong to different teams for the databases.
>- Purchase quantity: Number of instances to be purchased each time. *We configured a limit on how many instances can be purchased at a time in order to prevent misoperation. You can make additional purchase attempts if you want to purchase more*.
>- Purchased usage period: Since our database service is billed in a prepaid method, you need to estimate your expected database usage period. *Currently Tencent Cloud provides a discount with which you can purchase the service at a lower price if you purchase for a longer usage period*.

4. You will be redirected to the payment page upon purchase. After payment is successfully made, you can view your purchased instance from the cloud database instance list page in the Tencent Cloud console.






