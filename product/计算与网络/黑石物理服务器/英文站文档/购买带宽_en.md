This chapter describes how to configure CPMs to provide public network service for external access and how to purchase egress bandwidth of public network.

## Achieving Public Network Access
CPM offers two ways of public network access: Elastic Public IP (EIP) and BM load balancer.</br>

<li>EIP</li> 
It is a static IP address designed for dynamic cloud computing. Unlike traditional static IP, EIP can be bound to any CPM - CPM A or CPM B. In case of a failure of a CPM or availability zone, you can remap the IP to a healthy CPM so that you can deal with the CPM problem while offering service.  
*For more information, please see [Elastic Public IP](/doc/product/386/7144)*

<li>BM Load Balancer</li> 
BM load balancer can automatically spread access traffic of applications among multiple CPMs. It improves the fault tolerance of applications, and continuously provides the load balance capacity needed for responding to the incoming traffic of applications. BM load balancer can detect any unhealthy CPM in the cluster and automatically shift the route to a healthy CPM until the unhealthy one recovers. You can enable the BM load balancer in a single availability zone or multiple availability zones to achieve a more consistent application performance.

## Public Network Egress Charges
Public network egress fee can be billed by **traffic**, **bandwidth cap** and **actual bandwidth**.

Note: 
1. You can change the public outboud fee billing mode. The new billing mode takes effect by the next clock hour.</br>
2. For bandwidth cap changes within one clock hour (in the same billing mode), the changes take effect immediately, and the latest bandwidth cap is used for billing of public outbound fee. 

### Bill by traffic: 
Unit price: 0.8 CNY/GB, without cap on peak bandwidth (no speed limit). Pay by actual traffic on an hourly basis (post-paid) </li>
### Bill by bandwidth cap: 
Pay by the bandwidth cap you set. Public network egress speed is limited to the specified peak bandwidth. Tiered prices are adopted.</li>
<table>
<tr>
<th>Tier</th>
<th>Price</th>
</tr>
<tr>
<td>≤5 M</td>
<td>0.0625 CNY/M/Hour</td>
</tr>
<tr>
<td>>5 M</td>
<td>0.25 CNY/M/Hour</td>
</tr>
</table>
Charge is billed on an hourly basis with a post-paid mode. Usage period less than 1 hour will be counted as 1 hour.</br>

*You're allowed to change the billing mode for public network egress. The change will take effect in the next hour.</br>*
*Within the same hour and under the same billing mode, changes to the peak bandwidth will take effect immediately. The public network egress charge for the current billing period depends on the last modified peak bandwidth*

## How to configure public network service

- Binding BM EIP

Please select the billing mode for public network egress when purchasing BM EIP. Please select the billing mode commensurate with your business needs and bind to the CPM.

![](http://mc.qcloudimg.com/static/img/f99e8be2dbb895a8e0cbdc53942c15a4/image.png)


- Binding BM load balancer

Please select the billing mode for public network egress when purchasing BM load balancer instance.

![](http://mc.qcloudimg.com/static/img/fad1dd8905c67a727bdec95a4ffc712b/image.png)

The billing mode for public network egress of the listener is same as that of BM load balancer instance. Please select the appropriate billing mode for public network egress when creating the listener.

![](http://mc.qcloudimg.com/static/img/e109f9d8503abf2b034cc50037238f4a/image.png)

## Statement of public network egress charges

### Statement of public network egress charges for BM EIP

Take "Bill by Fixed Bandwidth" as an example.

<li>BM EIP public network egress - Bill by fixed bandwidth - Charges for Month X: This records the details of peak bandwidth purchased and charges billed for BM EIPs within the selected time range</li>
![](http://mc.qcloudimg.com/static/img/84562d836f248f54a93fbf811176ac42/image.png)

<li>BM EIP - Charges for Month X: This records the details of idleness and charges billed for all the BM EIPs within the selected time range</li>
![](http://mc.qcloudimg.com/static/img/21e4a12a3e18993d87d9360dfaca2fb3/image.png)

### Statement of public network egress charges for BM load balancer

Take "Bill by Fixed Bandwidth" as an example.

<li>Public network egress for BM load balancer - Bill by fixed bandwidth - Charges for Month X: This records the details of peak bandwidths purchased and charges billed for all the BM load balancer listeners within the selected time range</li>
![](http://mc.qcloudimg.com/static/img/bd39ae2719bdb598e2de1199d92ede18/image.png)

<li>Public network egress for BM load balancer - Charges for Month X: This records the details of charges billed for the public network egress for all the BM load balancer listeners with a bill mode of "Bill by Fixed Bandwidth" within the selected time range.</li>
![](http://mc.qcloudimg.com/static/img/ec571b3bab983b62f6ff1b867abcaec7/image.png)


