## What is Spot Instance
Spot instances are a new mode of CVM instances that featured by spot prices at substantial discounts and an interruption mechanism (available at certain discounts and can be automatically interrupted and reclaimed by the system). After you purchase a spot instance, you can use it the same way as you use a postpaid CVM instance, including console operations, remote login, service deployment, associating with VPC, etc.

* Related document: [FAQ About Spot Instances](document/product/213/17817)
* Related document: [How to purchase Spot Instances](/document/product/213/17926)

## Special Policies During Public Trial
* Application: During the public trial, you need to submit an application before you can use a spot instance. Tencent Cloud technical engineers will review and reply to your application. [Application Page >>](https://cloud.tencent.com/act/apply/spot)
* Fixed discount: Spot instances of all specifications are available at a fixed discount. Any spot instance is sold at a discount of 20% off compared to the postpaid instance of the same specification. The prices of a small number of instances may be adjusted slightly.
* Interruption by system: The interruption will not be caused by the reason that the market price is higher than the price paid by user, but will be caused by insufficient stock of spot instance pool. In case of insufficient resources, the system will reclaim some allocated spot instances at random.
* Increasing coverage: At the early stage of public trial, spot instances are only available for some availability zones and instance types. More availability zones and instance types will be supported later as the public trial progresses. For the up-to-date list of supported regions and instance types, please see [FAQ About Spot Instances - Supported Regions and Instances>>](/document/product/213/17817).

## Product Features
### 1. Greatly reduced cost
![](https://main.qcloudimg.com/raw/9ff933a9f597d0df46f44437980fb13b.png)
Spot instances are sold at a discount of up to 90% off compared to the postpaid instances.
* **Discount range**: Spot instances are priced at a discount ranging from 10% to 100% off based on the prices of postpaid instances of the same specifications.
* **What are covered by discount**: The discount only involves CVM vCPU and memory. Other CVM-related billed items such as system disk, data disk, bandwidth, and paid images are not affected by the discount.
* **Price fluctuation**: The discount is stable for a period of time, but when there are bulk purchases in an availability zone, the price will fluctuate (during the public trial, the discount is fixed at 80%).

### 2. Interruption by system
![](https://main.qcloudimg.com/raw/6f6c1f65cbecf508a97a5172720ab53a.png)
Unlike postpaid and prepaid instances that can only be released by users, spot instances are interrupted by the backend of system, which determines whether to interrupt the allocated spot instances based on the current price and the stock of resource pool.
![](https://main.qcloudimg.com/raw/a1dab91390022aa00be10b5bcea7b05a.png)
* **Interruption due to price**: When the market price is higher than your highest bid, the spot instance will be reclaimed (during the public trial, the market price is fixed).
* **Interruption due to insufficient stock**: In case of insufficient stock of resource pool of your spot instance, the system reclaims the spot instance based on the stock shortage; when the pool is fully stocked, you can apply for spot instances again.

## Scenarios To Which Spot Instances Do Not Apply
Due to the interruption by system, you cannot bring the lifecycle of a spot instance under your control. Therefore, it is not recommended to run services that require high stability on a spot instance, for example:
* Database services
* Online and website services without load balancer
* Master control nodes in a distributed architecture
* Long-time (over 10 hours) big data computing tasks

## Scenarios and Industries To Which Spot Instances Apply
### Scenarios
* Big data computing
* Online and website services with load balancer
* Web crawler service
* Other computing scenarios with fine granularity or support for checkpoint restart

### Industries
* Gene sequencing and analysis
* Drug crystal form analysis
* Video transcoding and rendering
* Finance and transaction data analysis
* Image and multimedia processing
* Scientific calculations (geography, hydromechanics...)

## Limits
* Quota limit: Unlike the quantity quota of non-spot instances, the quota of spot instances depends on the total number of vCPU cores of all spot instances you own in the availability zone. During the public trial period, the number of spot instances in each availability zone under an account should be limited such that the number of vCPU cores is not more than 30 (you can submit a ticket to apply for a bigger quota).
* Operation limit 1: Upgrading/degrading configuration is not supported for spot instances.
* Operation limit 2: Spot instances cannot be changed to prepaid instances.

## Best Practices
### 1. Splitting high-granularity tasks
* Split a long-time task into fine-grained subtasks to reduce the possibility of interruption;
* Use a big data suite like EMR that comes with splitting mechanism.

### 2. Ensure the stability of online and website services with load balancer
* Use load balancer, such as CLB, for the access layer;
* Use a small proportion of postpaid instances + a large proportion of spot instances for backend resources;
* Listen on the interruptions of spot instances and remove from the CLB the instances that are about to be interrupted.

### 3. Computing scheduling mode supporting checkpoint restart
* Store the intermediate results of computation on the permanent storage products such as COS/CFS/NAS;
* Keep aware of instances that are about to be interrupted through Metadata and store the computing results for the retention period of 5 minutes;
* When the spot instance is started again, resume the last computation.

