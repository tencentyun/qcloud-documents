## 1. Regions

Tencent Cloud hosted data centers are distributed in different locations across the globe. Within China, they cover South China, East China and North China. The Hong Kong node covers Southeast Asia and the data center node in Toronto covers North America. We will gradually increase available nodes to cover more regions. All nodes consist of regions and availability zones.

Currently, the following available regions are offered by Tencent Cloud: 
China: South China (Guangzhou), East China (Shanghai), North China (Beijing). 
Outside China: Southeast Asia (Hong Kong) and North America (Toronto).


Notes: 
1) Cloud products in the same region can communicate with each other through private network
2) Cloud products in different regions cannot communicate with each other through private network 

-  Tencent Cloud resources in different regions cannot access each other through private network

3) When purchasing cloud service, it is recommended to select the region that is closest to your customers to minimize access latency;

4) The name of regional availability zone is the most straightforward representation of the coverage range of a data center. To make it easier for clients to understand the name of regional availability zone, the "coverage range + city where the data center is located" structure is used when naming regions. The first half represents the coverage capability of the data center, and the second half indicates the city where the data center is located, or is near. Availability zone names are in the "city + number" structure.

> Note:
- The "connection through private network" mentioned above refers to the interconnection among resources under the same account. Private resource networks of different accounts are completely isolated from each other 
- Some Tencent Cloud resources may be unavailable in certain regions or availability zones. Before deploying your application, make sure you can create the required resources in that region or availability zone

## 2. Availability Zone
 
Availability zones refer to Tencent Cloud physical data centers in a certain region where power and network equipment are independent from each other. They are designed to ensure that failures within an availability zone can be isolated (except for large-scale disaster or major power failure) without spreading to other zones in order to keep user business constantly up and running.
[South China]  Guangzhou Zone 1 (out of stock), Guangzhou Zone 2, Guangzhou Zone 3
[East China]  Shanghai Zone 1
[North China]  Beijing Zone 1
[Southeast Asia]  Hong Kong Zone 1
[North America]  Toronto Zone 1


Availability zones in the same region can communicate with each other via private network, and network latency is shorter for products within the same availability zone.

> Notes:
- If there is only one availability zone to choose in a region, it means the region has only one availability zone at the moment.
- You cannot change availability zone for cloud service resources already purchased.




