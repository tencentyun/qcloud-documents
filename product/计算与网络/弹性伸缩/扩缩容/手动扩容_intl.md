AS not only supports the capacity scaling based on business load, but also allows you to intervene manually, so as to achieve manual capacity scaling in a fast way. Manual scale-up can be achieved using the following two methods:

- Add existing CVM instances to the scaling group
- Modify the expected number of instances in the scaling group to enable one-click scale-up

## Adding Existing CVM Instances to the Scaling Group

The scaling group offers an option: you can add one or more CVM instances to the existing scaling group, and perform load observation and management operations on such instance(s) along with other instances in this scaling group.

### - Conditions for Adding Instances

- The instance is in the running status
- The instance is in the same region as the scaling group
- The network attribute of the instance must be exactly the same as that of the scaling group, which means that they both belong to the same basic network or VPC.

### - Operations after Adding Instances Manually

- AS will add the required capacity of the group to the number of instances to be added. For example, if the currently expected number of instance in your scaling group is 5, after 3 instances are added manually, the expected number of instance in your scaling group will be 5 + 3 = 8. (If the sum of the number of instances to be added and required capacity exceeds the maximum capacity of the group, the request will fail)

- If the scaling group is associated with one or more CLBs, the manually-added instances will be automatically registered into all the CLBs of the scaling group.

- The scaling group will remove the automatically created machines first during scale-down. If there is no automatically-created machine, then the manually added machines will be removed. For those manually added instances that are removed by the scaling group, the instances are not destroyed, but only removed from the scaling group and CLB and no longer under the control of the scaling group.

### - Example of Adding an Instance in Console

Click the ID of the scaling group to be managed, or click **Management** beside it, to enter the details page of scaling group. In the lower half of the page, click "Add CVM" in CVM list, and check the corresponding CVM in the dialog box, then click "OK".

![](https://mc.qcloudimg.com/static/img/7fab080a771cd36a18cd669a6e6cf78b/1.jpg)


## Modifying the Expected Number of Instances to Enable One-click Scale-up

If the following requirements are met, you are suggested to use AS to achieve one-click scale-up:

- Though it is hard to predict the peaks and troughs of the service, you are not willing to use the system for performing capacity scaling exclusively; (if peaks and troughs are predictable, we suggest that you use scheduled task for capacity scaling)
- Your computing needs are based on projects, and the CVMs to be used every time are similar (for example, collection of social conditions and public opinions, gene sequencing and weather prediction)
In such case, you can set the scaling configuration of CVM template, and configure the corresponding scaling group. If you want to scale up later, you can directly modify the required capacity of scaling group.


### Performing One-click Scale-up in the Console

1. Create a custom image.
An instance that is scaled up subsequently will deploy the environment based on this image.
Suggested steps to create a custom image: You can deploy your services on an existing CVM or a newly-created CVM, set the services to be activated upon the boot of operating system, and export the services as a custom image.
For any question, refer to [Create Custom Images](https://intl.cloud.tencent.com/document/product/213/4942).

2. Create a scaling configuration based on the custom image.
For more information about creating scaling configuration, refer to [Create Scaling Configuration](https://intl.cloud.tencent.com/document/product/377/8544).

3. Create a scaling group.
During the creation process, select the created scaling configurations. For the minimum group size, maximum group size and initial number of instances, you should fill in these fields based on the upper and lower limits of the required number of servers as well as the current number. After finishing this step, you can scale up at any time.

4. Scale up.
If the service needs to be scaled up (for example, starting a gene sequencing task or enabling a request-specific server for data collection), you can directly modify the configuration of scaling group to increase the minimum group size, maximum group size and the expected number of instances, and then AS will quickly perform the scale-up operation for you.

**Summary:** With such operations as CLB forwarding rules, machine configuration and service deployment performed in advance, you can complete scale-up by simply modifying the parameters of scaling group, ensuring the agility of service.
