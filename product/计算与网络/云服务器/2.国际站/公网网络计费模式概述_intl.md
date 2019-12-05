BGP multi-line access is provided by Tencent Cloud for all ISPs to ensure the link quality. You can choose a billing method based on your business needs.
Choose one of the following billing methods for Tencent Cloud Prepaid and Postpaid CVMs.

### Bill-by-bandwidth

CVMs are billed by the public network outbound bandwidth (in Mbps).
**Feature:** Billing by fixed bandwidth has a lower rate than that of billing by traffic and is suitable for users with consistent usage of network bandwidth.
Distribution of public network inbound bandwidth:
- If the fixed bandwidth purchased by users is larger than 10 Mbps, Tencent Cloud distributes the public network inbound bandwidth that is equal to the purchased bandwidth.
- If the fixed bandwidth purchased by users is less than 10 Mbps, Tencent Cloud distributes 10 Mbps public network inbound bandwidth.

### Bill-by-traffic

CVMs are billed by the public network outbound traffic (in GB).
**Feature:** Billing by traffic is simple on a pay-as-you-go basis and is suitable for customers with fluctuating network requirements to cut cost. To avoid a high cost caused by the traffic surge, you can set a bandwidth cap. If this limit is exceeded, packet loss occurs by default with no cost incurred.



>**Note:**
>If the bandwidth is set to 0 Mbps, the CVM instance is not assigned with a public IP. In this case, the outbound traffic is not supported and the CVM instance cannot be used as public gateway. Please choose with caution.

<!--Now, you can take a further look at [Exclusive Network Billing]() and [Shared Network Billing]() based on the network type of your CVM.-->

