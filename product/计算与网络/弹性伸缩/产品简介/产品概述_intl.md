## What is Auto Scaling (AS)?

Auto Scaling (AS) can automatically adjust CVM computing resources according to your business needs and policies to ensure that you have an appropriate number of CVM instances to handle your application load. For Web applications, intelligent scaling can help control cost and manage resources. When requests increase, more servers are added to handle additional load. When the requests reduce, unnecessary servers are removed.

You only need to set policies for expending and reducing capacity. When the expanding policy is trigger, AS  automatically increase servers to maintain the performance. When the demand decreases, AS reduces servers according to your reducing policy, so as to minimize your cost.

As shown in the figures below, by using AS, your cluster can always keep an appropriate number of resources and stay healthy. You will get rid of the following troubles in the traditional model: 
 - Insufficient machines due to a surge in business or a CC attack, resulting in no response from your service
 - Estimating resources based on peak traffic while the traffic is rarely peaked, causing a waste of resources
 - Personal surveillance and frequent handling of capacity alarms, which require multiple manual changes

**Cluster maintenance in the traditional model:**
![Alt text](https://mc.qcloudimg.com/static/img/92ae76d43c2b490f558490d328b8761a/AS-Product+Introduction%281%29.jpg)

**Effects after using AS:**
![Alt text](https://mc.qcloudimg.com/static/img/953c495c4b950e98fd6e360d871bf891/AS-Product+Introduction%282%29.jpg)


## How AS Works

In common Web application services, your cluster usually runs multiple copies of an application to meet client traffic. For example, the frontend server cluster at the access layer, the application server cluster at the logical layer, and the backend cache server cluster. Every instance can process client requests.

The instances are similar or identical and are usually quantity adjustable. You can add these similar or identical machines to one scaling group for management:

- You can specify the minimum instances in each scaling group, and AS will ensure that the instances in the group will never be less than the minimum number.
- You can specify the maximum instances in each scaling group, and AS will ensure that the instances in the group will never be more than the maximum number.
- You can specify a scaling policy, and AS will start or terminate the instances when the demands for an application increase or decrease. There are two kinds of scaling policies:
   a) Alarm trigger policy: expand capacity dynamically according to specified conditions (for example, when CPU utilization of a server in the scaling group is over than 60%)
   b) Scheduled scaling policy: expand capacity at a specified time (for example, 21:00 every night) 
- After setting the policy, you can also set scaling activity notification. When a scaling activity occurs, AS will inform you via email, SMS and internal message. You only need to check the notifications from AS instead of focusing on the changes of your business request volume all the time.
- You can also specify the number of machines required via one click at any time, or add existing machines to the scaling group for joint management.

## Basic Concepts of AS

**AS products have the following basic concepts:**

- Scaling group
- Scaling configuration
- Scaling policy
- Cooldown period


## 1. Scaling Groups
A scaling group is a collection of CVM instances following the same rules and serving the same scenario. A scaling group defines attributes such as the maximum and minimum numbers of CVM instances, and its associated load balancer instances.

## 2. Scaling Configuration
Scaling configuration is a template for automatic creation of CVM. It contains image ID, CVM instance type, system disk/data disk types and capacities, key pair, security group, etc.

Scaling configuration must be specified when the scaling group is created. Once the scaling configuration is created, its attributes cannot be edited.

## 3. Scaling Policies
A scaling policy defines the conditions for executing a scaling action. The trigger condition can be a time point or an alarm of cloud monitoring, and the action can be removing or adding a CVM.
There are two scaling policies:

- **Scheduled scaling policy**
CVM instances will be automatically increased or reduced at a fixed time point, which can be repeated periodically.

- **Alarm scaling**
CVM instances will be automatically increased or reduced based on cloud monitoring metrics such as CPU, memory and network traffic.

## 4. Cooldown Period
Cooldown period refers to a period of time when the corresponding scaling group is locked after a scaling activity (adding or removing CVM instances) is completed. During this period, no scaling activities are performed with the scaling group. The cooldown period can be specified within 0-999,999 (seconds).

