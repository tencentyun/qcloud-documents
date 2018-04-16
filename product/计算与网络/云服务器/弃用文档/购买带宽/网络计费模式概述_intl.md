Tencent Cloud provides BGP multi-line access for all ISPs to ensure the link quality. You can choose based on your business needs.
You can select one of the following billing methods for Tencent Cloud Postpaid servers:

### Bill-by-bandwidth

Tencent Cloud charges users according to the public network outbound bandwidth of their CVMs (in Mbps).
**Feature:** Fees are charged by fixed bandwidth. The price for this method is lower than that of Bill-by-traffic. It is suitable for users consuming stable network bandwidth.
Public network inbound bandwidth:
- If the bandwidth cap is over 10 Mbps, Tencent Cloud assigns the public network inbound bandwidth that is equal to the purchased bandwidth cap.
- If the bandwidth cap is equal to or less than 10 Mbps, Tencent Cloud assigns 10 Mbps public network inbound bandwidth.

### Bill-by-traffic

Tencent Cloud charges users according to the public network outbound traffic of their CVMs (in GB).
**Feature:** The billing rule is simple and the service can be used on a pay-per-use basis, to reduce the network cost incurred due to large network fluctuations. To avoid a high cost caused by the traffic surge, you can choose a capped bandwidth. If this limit is exceeded, package loss occurs by default, and no cost is charged.



>**Note:**
>If the bandwidth is set to 0 Mbps, the public network IP is not distributed to the CVM instance. In this case, outbound traffic is not supported and the CVM instance cannot be used as public gateway. Please select with caution.

<!--Now, you have understood the billing methods, and can take a further look at [Exclusive Network Billing]() and [Shared Network Billing]() based on your CVM network type.-->
