

## Purchasing Instance

Click and select the instance to purchase in the Tencent Cloud product purchase page. You can purchase up to 10 instances in the page each time. Visit the page again to purchase more.

> Initialization is required for the purchased instances to function normally.

## Upgrading Instance

> This feature is expected to become available in March, 2017. See Tencent Cloud official website for update information.
> Upgrade operation will upgrade current Cloud Database instances to a higher specification. There will be a brief disconnection (several seconds) during the upgrade process, so it is recommended to upgrade your instances during off-peak business hours.
> 
- The upgrade process cannot be aborted once it begins
- Degrade is currently not supported by the console. Submit a ticket if you want to degrade your instance

1.	Go to "Console" -> "Cloud Database" -> "PostgreSQL", select the instance to be upgraded and click "Upgrade" to open the upgrade pop-up window.

2. 	Select the desired specification based on your need and make the payment. Once payment is completed, the system will automatically upgrade instance specification.
 
**Upgrade fee=(target specification unit price - original specification unit price) x remaining usage period**

## Renewing Instance

### 1. Renewal

Renewal means to extend the usage period of a CDB for PostgreSQL instance. You can do this in the following ways:

- Go to "Console" -> "Cloud Database" -> "PostgreSQL" -> "More" -> "Batch Renew", select the instance to be renewed, and click "Renew", "Batch Renew", "Configure Auto Renew".
- Go to "User Center" -> "Renewal Management" -> "Cloud Database (PostgreSQL)", select the instance(s) to be renewed, and click "Renew" or "Batch Renew", as shown below:
![](//mccdn.qcloud.com/static/img/ac67608a62020ce34e84c7e985eafc0a/image.png)

- Go to "User Center" -> "Renewal Management" -> "Cloud Database (PostgreSQL)" and configure Auto Renew.

> The Auto Renew feature will automatically renew instance upon expiration, which requires sufficient balance in your account. Auto renewal will not be automatically reattempted if it fails.

### 2 Renewal Fee

Renewal fee=monthly price of instance x renewal period　(month) + (monthly price of instance/30 x renewal period　(day))

> Note: The renewal fee for a period less than a month is calculated based on monthly price and the number of days to renew. For example, an instance with a monthly price of 60 CNY expires on April 5th. Suppose you want to renew the instance to May 20th, then the expiration date will be adjusted to the 20th day of each month, and the renewal fee is 90 CNY (60+60÷30×15).

