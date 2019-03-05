## CDB for MariaDB (TDSQL) Instance Upgrade

> Upgrade operation will upgrade current TDSQL instances to a higher specification. There will be a brief disconnection (lasts several seconds) during the upgrade process, so it is recommended to upgrade your instances during off-peak business hours.
- The upgrade process cannot be aborted
- Degrade is currently not supported by the console. Submit a ticket if you wish to degrade your instance

1.	Go to "Console" -> "Cloud Database" -> "TDSQL", select the instance to be upgraded and click "Upgrade" to open the upgrade pop-up window.
2. In the pop-up window, select the target specification based on your need and make the payment. After the successful payment, the system will automatically upgrade the instance to the specified specification.
Upgrade interface:
![](//mccdn.qcloud.com/static/img/d5916ce64bd27d051a305476c0191449/image.png)
 
Upgrade fee=(price of target specification - price of original specification) x remaining usage period


## DCDB for TDSQL Instance Upgrade

> Upgrade operation will upgrade current TDSQL instances to a higher specification. Since distributed database is composed of multiple parts, instance upgrade solutions include "Add Part" and "Upgrade Part". The service does not stop during the upgrade process, but some of the parts may become read-only for several seconds, so it is recommended to upgrade your instances during off-peak business hours. For more information, please see "Auto Re-Balancing"

### Adding Part
Go to "Console" -> "Distributed Cloud Database" and click "Add Part". Select the number of new parts to be added and their specifications to complete the upgrade process.
![](//mccdn.qcloud.com/static/img/b9cff4d43c31ffac56b2296945ac2337/image.png)
![](//mccdn.qcloud.com/static/img/6742591dcd12c8f56e6a11cdf0670e79/image.png)

### Upgrading Part
This operation upgrades the specification of a single part to a higher level without adding new parts. **The feature is not supported for the current version and will become available in the future.**

1.	Go to "Console" -> "Distributed Cloud Database", click "Management" to enter the management page, choose "Part Management" and click on the part to be upgraded to complete the upgrade process.
![](//mccdn.qcloud.com/static/img/d77ef38bc7becc785decbd51fd285b84/image.png)
![](//mccdn.qcloud.com/static/img/0bb016e4be65e8865a86cd4f4eb20c59/image.png)

 

 

