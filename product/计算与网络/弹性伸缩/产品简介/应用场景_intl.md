## 1. Deploying Capacity Scaling in Advance

If the user knows when capacity scaling is needed, he/she can configure Auto Scaling schedule policy in advance. By the configured time, the system will automatically increase or decrease the number of CVM instances without the need to wait.

## 2. Coping with Business Volume Surge with Low Cost

When the customer is faced with access peak, he/she will need to prepare servers in advance and prevent server overload caused by the sudden surge in CPU usage. The customer may decrease the number of servers according to the situation when the surge has passed. The user can configure Auto Scaling monitor policy in advance and the system will automatically determine whether CVM scale-out is needed according to the business monitoring metrics that are already configured. The system will automatically increase or decrease the number of CVM instances and complete load balancer configurations when the monitoring metric reaches certain thresholds. For customers, this not only saves cost, but also saves the effort to be constantly prepared for manual capacity scaling.

## 3. Replacing Unhealthy CVMs Automatically

Users need to constantly monitor the operation statuses of CVMs and take actions on unhealthy CVMs in time to prevent them from affecting their business. With Auto Scaling, the system will regularly perform health check on CVMs. When the system detects an abnormal instance, it will automatically create a new instance as replacement. This operation will be logged for users to view later.
