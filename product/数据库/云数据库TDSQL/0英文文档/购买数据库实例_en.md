1. Log in to Tencent Cloud Console and open the Console via the URL [https://console.cloud.tencent.com/tdsql](https://console.cloud.tencent.com/tdsql)

2. Click "New" in the upper-right corner of the console or visit the purchase page [https://buy.cloud.tencent.com/tdsql](https://buy.cloud.tencent.com/tdsql)
![](//mccdn.qcloud.com/static/img/a85919abd21ca9c765f0d6f23833d59b/image.png)


3. On the purchase page, specify database instance information according to your demand and click "Purchase Now";
> Take note of the following configurations when purchasing instance:
>
>- Billing method: Prepaid, which means you need to pay the charges before you can use the instances.
>- Region: The region to which the instance is actually deployed. It is recommended to choose the same region as the CVM to be connected in order to minimize delay.
>- Availability zone: Physical IDCs whose electric power facilities and networks are independent from each other within the same region. It is recommended to choose the same availability zone as the CVM to be connected in order to minimize delay.
>- Network type: Network in which the instance resides. This cannot be changed once specified. It is recommended to choose the same network as the CVM to be connected in order to minimize delay.
>- Instance version: Select desired [Instance Version](https://cloud.tencent.com/doc/product/237/6918) based on your demand. In general, more slaves means higher availability.
>- Database version: MariaDB (TDSQL) database kernel version. There are differences between the features of [10.0.10](https://mariadb.com/kb/en/mariadb/mariadb-10010-changelog/) and [10.1.9](https://mariadb.com/kb/en/mariadb/mariadb-1019-changelog/), for more information, please see [MariaDB Official Instructions](https://mariadb.org/).
>- Instance specification: Instance performance and base price depend on its specification. For more information, please see [Product Prices](https://cloud.tencent.com/document/product/237/2034).
>- Disk: Default disk is SSD (local disk). More disk types will become available in the future.
>- Project: If you wish that different databases are managed by different teams, you can specify projects that belong to different teams for the databases.
>- Purchase quantity: Number of instances to be purchased each time. *We configured a limit on how many instances can be purchased at a time in order to prevent misoperation. You can make additional purchase attempts if you wish to purchase more*.
>- Purchased usage period: Since our database service is billed in a prepaid method, you need to estimate your expected database usage period. *Currently Tencent Cloud provides a discount with which you can purchase the service at a lower price if you purchase for a longer usage period*.



![](https://mc.qcloudimg.com/static/img/542a4db8a351d436bbb207ca2cdd4b2e/image.png)



4. Upon purchase, you will be taken to the payment page where you can finish the payment. Once payment is successful, you will see your purchased instance from the TDSQL Instance List page in the Tencent Cloud Console.






