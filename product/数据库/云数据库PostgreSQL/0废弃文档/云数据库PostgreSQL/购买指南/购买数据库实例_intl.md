
1. Log in to the Tencent Cloud [console]().

2. In the console page, click **Create**.

3. Specify database instance information according to your demand and click **Purchase Now**.

- Billing method: Postpaid. That is, pay by the usage duration of the storage space.
- Region: The region to which the instance is actually deployed. It is recommended to choose the same region as the CVM to be connected in order to minimize delay.
- Availability zone: Physical IDCs whose electric power facilities and networks are independent from each other within the same region. It is recommended to choose the same availability zone as the CVM to be connected in order to minimize delay.
- Network type: Network in which the instance resides. This cannot be changed once specified. It is recommended to choose the same network as the CVM to be connected in order to minimize delay.
- Database kernel version: There are feature differences between different PostgreSQL database kernel versions. For more information, see [9.3.5](https://www.postgresql.org/docs/9.3/static/index.html), [9.5.4](https://www.postgresql.org/docs/9.5/static/index.html) and [10.4](https://www.postgresql.org/docs/10/static/index.html).
- Instance specification: Instance performance and base price depend on its specification.
- Disk: Default disk is SSD (local disk). More disk types will become available in the future.
- Project: If you wish that different databases are managed by different teams, you can specify projects that belong to different teams for the databases.
- Purchase quantity: Number of instances to be purchased each time. We configured a limit on how many instances can be purchased at a time in order to prevent misoperation. You can make additional purchase attempts if you wish to purchase more.
- Usage period: Postpaid adopts a 3-tier billing mode. Longer usage duration means lower unit price.

4. You will be redirected to the payment page upon purchase. After payment is successfully made, you can view your purchased instances from the database instance list page in the Tencent Cloud console.






