You can launch instances in a placement group which determines how the instances are placed on underlying hardware. When creating a placement group, you can distribute the instances in the group to different underlying hardware.
> The feature is under internal trial. Click [here](https://cloud.tencent.com/act/apply/PlacementSet) to apply for a trial use.

## Spread Placement Groups
In a spread placement group, the instances are placed on different underlying hardware.

For applications of important instances that need to be placed separately, such as master/slave databases, high-availability clusters, a spread placement group is recommend. By launching instances in a spread placement group, you can reduce the risk of simultaneous failure that occurs when the instances are placed on the same underlying hardware.

A spread placement group has geographical attributes and it can span multiple availability zones. There is a limit on the number of instances in a group. For more information, please see the Console page on the official website.

When you launch instances in a spread placement group, the request fails if there is not enough hardware to meet the request. We provide more different hardware so that you can retry your request.

## Spread Placement Group Rules and Limits
Before using a spread placement group, you should pay attention to the following rules:
1. Placement groups cannot be merged.
2. An instance can be launched in a placement group at a time.
3. An instance cannot span multiple placement groups.
4. You cannot place existing instances into a placement group on your own.
5. Spread placement layers can be selected, including physical machine, exchange, and rack.
6. The maximum numbers of instances in groups on different placement layers are different. For more information, please see the official website.
7. The disaster recovery group policy you have specified is strictly complied with. Note that if there is not enough hardware to distribute instances, the creation of some instances fails.
8. Instances on CDH don't support spread placement groups.

## Operation Instructions
For more information on how to operate spread placement groups, please see [Spread Placement Group Operation Instructions](/document/product/213/17020).

