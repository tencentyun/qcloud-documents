## Usage Scenarios

If you need to troubleshoot any problems related to configurations or Web applications (for example, turning off to reset password, upgrading service, etc.), and wish to make modifications to the applications without triggering the auto scaling process, you can suspend the scaling group and resume it after the above operations are performed.

## Suspending Scaling Group

### Action

Open the [Console](https://console.cloud.tencent.com/autoscaling/config), select "Scaling Group" in the navigation bar, and click "Disable" at the right side of the scaling group list.

![](https://mc.qcloudimg.com/static/img/ba3bfe7ebc1d21be86f8947b4ed51df9/8.jpg)

When the setting is made, you can see **Disabled** in the **Status** column.

### Note

After the scaling group is disabled, the auto capacity scaling of the scaling group will not be triggered, but the restrictions on the scaling group remain in effect.

The activities that are automatically triggered include:
- Alarm Scaling
- Scheduled Task
- Health Check
- Expected number of instances mismatch due to manual operation

Restrictions on the scaling group include:

- If the number of instances that are removed manually are smaller than the minimum number of instances, the instances are not allowed to be removed;
- If the number of instances that are added manually are larger than the maximum number of instances, the instances are not allowed to be added;
- Increase the minimum or maximum number of instances manually, and do not trigger scaling activity.

## Resuming Scaling Group

If you have finished troubleshooting or performed operations when the scaling group activity is suspended, you can resume the auto scaling configuration for your service.

Open the [Console](https://console.cloud.tencent.com/autoscaling/config), select **Scaling Group** in the navigation bar, and click **Enable** at the right side of the scaling group list.

![](http://mc.qcloudimg.com/static/img/2a2d2d5704b53b4705a39798b53f8425/image.jpg)





