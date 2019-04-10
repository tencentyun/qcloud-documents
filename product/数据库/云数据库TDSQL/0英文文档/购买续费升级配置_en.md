## Purchasing Instance

Click and select the instance to purchase in the Tencent Cloud Product Purchase page. You can purchase up to 10 instances in the page each time. Visit the page again to purchase more.

> Initialization is required for the purchased instances to function normally.

## Upgrading Instance

> Upgrade operation will upgrade current MariaDB (TDSQL) instances to a higher specification. There will be a brief disconnection (several seconds) during the upgrade process, so it is recommended to upgrade your instances during off-peak business hours.
- The upgrade process cannot be aborted once it begins
- Degrade is currently not supported by the console. Submit a ticket if you wish to degrade your instance

1.	Go to "Console" -> "Cloud Database" -> "MariaDB (TDSQL)", select the instance to be upgraded, and then click "Upgrade" to open the upgrade pop-up window.

2. In the pop-up window, select the target specification based on your need and make the payment. After the successful payment, the system will automatically upgrade the instance to the specified specification.
Upgrade interface:
![](//mccdn.qcloud.com/static/img/d5916ce64bd27d051a305476c0191449/image.png)
 
**Upgrade fee=(price of target specification - price of original specification) x remaining usage period**

## Renewing Instance

### 1. Renewal

Renewal means extending the usage period of a CDB for MariaDB (TDSQL) instance. The following operations are supported:

- Go to "Console" -> "Cloud Database" -> "MariaDB (TDSQL)" -> "More" -> "Batch Renew", select the instance to be renewed, and then click "Renew", "Batch Renew" or "Configure Auto Renew"
- Go to "User Center" -> "Renewal Management" -> "Cloud Database MariaDB (TDSQL)", select the instance to be renewed, and then click "Renewal " or "Batch Renewal", as shown below:
![](//mccdn.qcloud.com/static/img/ac67608a62020ce34e84c7e985eafc0a/image.png)

- Go to "User Center" -> "Renewal Management" -> "Cloud Database MariaDB (TDSQL)" and configure auto renew.

> Auto renew feature will automatically renew instance upon its expiration, which requires sufficient balance in your account. Auto renew will not be automatically retried if it fails.

### 2 Renewal Fee

Renewal fee=monthly price of instance x renewal period　(month) + (monthly price of instance/30 x renewal period　(day))

> Note: The renewal fee for a period less than a month is calculated based on monthly price and the number of days to renew. For example, an instance priced at 60 CNY per month expires on April 5. Suppose you want to renew the instance to May 20, then the expiration date will be adjust to the 20th day of each month, and the renewal fee is 90 CNY (60+60÷30×15).

