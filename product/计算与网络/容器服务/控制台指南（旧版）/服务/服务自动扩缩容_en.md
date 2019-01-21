## Overview
Horizontal Pod Autoscaling (HPA) for services can automatically scales the number of pods for services according to the CPU utilization of pods and other metrics.
Note that Horizontal Pod Autoscaling is available to a backend HPA component of the version v2alpha1 and does not support a Kubernetes cluster of the version 1.4.6.

## Procedures
You can set HPA for services via the following three entries:
- Set when creating/updating a service:
![createserviceas][1]
- Set when updating the number of pods for a service:
![setserviceas][2]

- Maximum number of pods, minimum number of pods: the range of the number of pods that HPA can adjust.
- Triggering policy metric: the policy metric that HPA depends on.
- CPU utilization: the ratio of the CPU usage of the container to the request value of CPU.
- Memory utilization: the ratio of the memory usage of the container to the request value of the memory.
- Inbound bandwidth: pod inbound bandwidth (in MB).
- Outbound bandwidth: pod outbound bandwidth (in MB).

The CPU utilization and the memory utilization correspond to metrics of the Kubernetes resource type. The inbound bandwidth and the outbound bandwidth correspond to metrics of the Kubernetes custom pod type.
If you need to use resource-type metrics as the autoscaling policy, set the request value for the container when creating a service. Otherwise, resource-type metrics are not supported.

## Scaling Algorithm
The HPA backend component for services periodically (every 30s) pulls the monitoring metric of the container and pods from Tencent Cloud's Cloud Monitor, and then calculates the target number of replicas based on the current value of this metric, the current number of replicas and the target value of this metric. The target number of replicas is used as the expected number of replicas for services to achieve autoscaling. For example, for 2 pods with an average CPU utilization of 90%, if the target CPU utilization is set to 60% for autoscaling for services, the number of pods will be adjusted automatically to: 90%\*2 / 60% = 3.
If you set multiple auto scaling metrics, HPA will calculate the target numbers of replicas respectively according to each metric, and then take the maximum number as the final target number of replicas.


## Notes

- Set CPU Request for the container;
- Set a reasonable target for the policy metric, For example, 70% for the container and application, and 30% remained.
- Keep pods and nodes healthy and avoid frequently recreating pods.
- Ensure that the loads you request are balanced.
- The target number of replicas calculated by HPA is allowed to fluctuate within 10%, under which HPA will not adjust the number of replicas.
- If the value of deployment.spec.replicas corresponding to the service is 0, auto scaling will not take effect.
 
[1]:https://mc.qcloudimg.com/static/img/47f9a1ab386056eb4d217067844d89b1/image.png
[2]:https://mc.qcloudimg.com/static/img/699bdb8be1075dceeaef657f590b4f92/image.png

