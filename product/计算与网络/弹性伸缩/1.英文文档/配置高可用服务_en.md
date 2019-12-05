
## Scenario Description

It is relatively cumbersome to build traditional master/slave or active-active HA clusters. You can use health check of Auto Scaling to achieve high availability.

The system will automatically monitor the health status of the active nodes. When the active node does not respond to a ping, the Auto Scaling will automatically replicate a healthy instance to replace any abnormal ones, to ensure healthy and smooth business operation and provide all-round protection for your business.
For example:

![Alt text](https://mc.qcloudimg.com/static/img/b4553279b674477afa12c5109e09bf6f/04+%282%29.gif)

## Tips on Usage

Step 1: Create images of stateless CVMs in a cluster.

Step 2: Create a scaling group, and set the maximum and the minimum scaling group sizes. After that, select **Add CVM** from the list of CVMs in the scaling group to manually add the existing CVM in the cluster. Note: When a CVM that is manually added to a scaling group is replaced, such CVM is not destroyed, but only removed from the scaling group.

Step 3: Create a notification and select to accept the notification on the scaling activities that replace unhealthy instances

![Alt text](https://mc.qcloudimg.com/static/img/ebee2c6fbcae2766d12ca046cdc75317/26.png)



## Benefits of AS

AS can help secure the cluster.

## Applicability
It is strongly recommended that you add the stateless CVM (if any) to the scaling group, as a routine IT deployment.

