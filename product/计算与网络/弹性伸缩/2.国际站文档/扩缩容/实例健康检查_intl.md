If you specify the "initial number of instances" when creating a new scaling group, after the scaling configuration and scaling group are created, the scaling group will create the CVM instances whose number is equal to the initial number of instances. Meanwhile, the scaling group will ensure the instances whose number is larger than "minimum group size" and smaller than "maximum group size" are running.
> Note:
> 
> - Minimum group size: Minimum number of instances that can be in a scaling group. If the number of CVMs in the scaling group is smaller than the minimum group size, AS will add the instances till the number of current instances in the scaling group reaches the minimum group size.
> 
> - Initial number of instances: Initial number of CVMs when the scaling group is created.
> - Maximum group size: Maximum number of instances that can be in a scaling group. If the number of CVMs in the scaling group is greater than the maximum group size, AS will remove some instances till the number of current instances in the scaling group is limited to the maximum group size.

AS periodically performs health checks on the instances in your scaling group to ensure normal operation. If an instance is found unhealthy, AS will terminate and replace it with a new CVM.

- **Instance Health check**

AS periodically performs health checks on the instances in your scaling group to determine whether each instance is healthy by checking whether it is able to respond to a ping for one minute. If not, AS will mark it as unhealthy.

- **Replacing unhealthy instances**

If an instance is marked as unhealthy, the scaling group will immediately replace it with a new instance, unless it is under "removal protection".

