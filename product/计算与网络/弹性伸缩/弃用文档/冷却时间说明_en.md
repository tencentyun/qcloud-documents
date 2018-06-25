## Cooldown Period

The AS cooldown period is a configurable setting for your scaling group that helps to ensure that AS doesn't launch or terminate other instances before the previous scaling activity takes effect. After the scaling group dynamically scales using a simple scaling policy, AS waits for the cooldown period to complete before resuming scaling activities.

When you manually scale your scaling group, the default is not to wait for the cooldown period, but you can overwrite the default by setting a new cooldown period. Note that if an instance becomes unhealthy, AS does not wait for the cooldown period to complete before replacing the unhealthy instance. 

## Importance of Cooldown Period

After an instance is added to the scaling group, it will take some time to decrease the load. If there is no cooldown period, the system will keep scaling in before the load decreases. After the newly added instance takes over the service, it has to scale out due to low load.

These instances use a configuration script to install and configure software before the instance is put into service. As a result, it takes around two or three minutes for the instances to be put into service after they are enabled. (The actual time, of course, depends on several factors, such as the size of the instance and whether there are startup scripts to complete.)

**Scenario Example:**

A spike in traffic occurs, which triggers the alarm policy. When it does, AS enables an instance to help with the increase in demand. However, there's a problem: the instance takes a couple of minutes to enable, and it will also take some time for the enabled instance to receive requests from CLB. During that time, the monitor alarm could continue to be triggered, causing AS to enable another instance each time the alarm is triggered.

However, with a cooldown period in place, AS enables an instance and then suspends scaling activities due to simple scaling policies or manual scaling until the specified time elapses (the default is 60 seconds). This gives newly-enabled instances time to start handling application traffic.

After the cooldown period expires, any suspended scaling actions resume. If the alarm is triggered again, AS enables another instance, and the cooldown period takes effect again. If, however, the additional instance was enough to bring the CPU utilization back down, then the group remains at its current size. 

## How to Configure the Cooldown Period

Cooldown period is 60 seconds by default.

Use the following steps if you need to modify the cooldown period:

- Open the details page of the scaling group;

- Click **Alarm Trigger Policy**, select an appropriate alarm scaling policy, and then select **Modify** to specify the cooldown duration below the modification box (value range: 0-999,999 seconds)

