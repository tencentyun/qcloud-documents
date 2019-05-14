MariaDB (TDSQL) provides both private and public network access addresses.

## 1. Obtaining the Private Network Access Address
You can obtain the private network access address of an instance on the Instance Details page. Note that the private network access address refers to the VIP. The database instance is accessed by connecting to the gateway cluster rather than the database instance CPM. Therefore, the private IP does not change during CVM delivery failure or master/slave switch.
![](//mccdn.qcloud.com/img56835cbbbeb73.png)
To access MariaDB (TDSQL) service, you can directly connect the instance's **private network address** in the same CVM as that of MariaDB (TDSQL). Note: you may need to install mysql/MariaDB client first.
![](//mccdn.qcloud.com/img56835e0a9470d.png)

## 2. Obtaining the Public Network Access Address
You can obtain the public network access address of an instance on the Instance Details page.


![](https://mc.qcloudimg.com/static/img/82911c57474269d29cb8a466a6f5a09c/image.png)
> Note:
> 
> Public network access address can only be used for daily database management.
> 
> Public network traffic may be charged. For more information, please see [Product Prices](https://cloud.tencent.com/document/product/237/2034).

