
PostgreSQL provides both private and public network access addresses.

## 1. Obtaining the Private Network Access Address
You can obtain the private network access address of an instance on the Instance Details page. Note that the private network access address refers to the VIP. The database instance is accessed by connecting to the gateway cluster rather than the database instance CPM. Therefore, the private IP does not change during CVM delivery failure or master/slave switch.

From a CVM that **resides in the same network** as PostgreSQL, you can directly connect to the instance's **private network address** to access PostgreSQL services. (Note: you may need to install the client first)

## 2. Obtaining the Public Network Access Address
You can obtain the public network access address of an instance on the Instance Details page.

![](https://mc.qcloudimg.com/static/img/4b234c3c28d06d00631ee071e77b2d7d/image.png)

> Note:
>
> Public network access address can only be used for daily database management. Public network traffic may incur a fee. For more information, please see [Product Prices](https://cloud.tencent.com/document/product/409/4993).

