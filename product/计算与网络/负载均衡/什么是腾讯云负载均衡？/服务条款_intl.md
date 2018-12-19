## Service Availability
We guarantee a 99.95% service availability for Cloud Load Balance, which means Cloud Load Balance will be available for service for at least 99.95% of the time, or 30(d)×24(h)×60(min)×99.95%=43,178.4 minutes, and be unavailable for service for 21.6 minutes at most each month. Such service availability is also applicable to Layer4/7 cloud load balancing VIP.

When a CVM fails, the cloud load balancer will automatically eliminate the failed CVM and order other CVMs to handle the traffic of this CVM, whose downtime will not be included in the unavailable time of Cloud Load Balance.

If a cloud load balancer recovers from the failure within 5 minutes, its downtime will also not be included in the unavailable time of Cloud Load Balance. The unavailable time refers to the period from failure to recovery from failure, including maintenance.

## Network Access Capability

The self-adaptive network access capability enables the cloud load balancer to adjust network access traffic in accordance with the bandwidth of CVM associated with the user, whose public network-ingress bandwidth is determined by the public network bandwidth of the associated CVM. Supported by BGP multi-line access in ingress, Tencent Cloud Load Balance is capable of providing good network access quality.

## Resource Allocation Capability

Tencent Cloud cluster-based load balancer system provides auto-scaling capacity to adapt to different user service scales. Users can achieve auto-scaling allocation by simply increasing or decreasing CVMs on the cloud load balancer in accordance with their business scales.

## Audit of Data

In accordance with the applicable laws and regulations and on condition of compliance with relevant process and availability of all necessary documents, Tencent Cloud may disclose information on cloud load balancer system, including operation log of key components, operation records of operation & maintenance personnel and operation records of users, if required by the regulatory authorities or it is necessary to do so for other reasons such as collection of evidences during investigation into safety accidents.

## Failure Recovery Capability

With a professional team that provides 7x24 maintenance service and technical support by means of tickets, telephone or other channels, Tencent Cloud boasts a series of excellent emergency response mechanisms covering efficient failure monitoring, automatic alarm, fast positioning and rapid recovery.

