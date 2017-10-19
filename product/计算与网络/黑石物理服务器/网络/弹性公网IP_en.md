
Elastic IP (EIP) address is a static IP address designed for dynamic cloud computing. Unlike traditional static IP, EIP can be bound to any CPM - CPM A or CPM B. In case of a failure of a CPM or availability zone, you can remap the IP to a healthy CPM so that you can deal with the CPM problem while offering service.

Note: A BM EIP can ONLY be bound to CPM or NAT gateway of a CPM VPC, and CANNOT be used together with CVM Elastic Public IPs

## Range of Application

A BM EIP address can be bound to CPM and NAT gateway of a CPM VPC, but you can only bind it to resources within the same region and VPC.


## Billing
The charges for using BM EIP include "IP Idle Fee" and "public network egress fee"
<li>IP inactivity fee: A BM EIP is essentially a public IP of IPv4. Such IP resources are precious and limited. If the IP is not bound, an inactivity fee will be charged as penalty, thus you should release the EIP when it is not used</li>
<li>Public network egress fee: A BM EIP that has been bound to CPM can be used for public network access. The resulting public network traffic or bandwidth will be accounted into the public network egress fee for using this EIP.

### IP Idle Fee
A BM EIP, if it's not bound to any CPM, it's charged at 0.20 CNY/hour as the IP Idle fee. Usage period less than 1 hour is be counted as 1 hour.

### Public Network Egress Fee
There are two billing modes for public network egress charges: "Bill by Traffic" and "Bill by Fixed Bandwidth"
<li>Bill by traffic: Unit price: 0.8 CNY/GB, without cap on peak bandwidth (no speed limit). Pay by actual traffic on an hourly basis (post-paid).</li>
<li>Bill by fixed bandwidth: Pay by the purchased peak bandwidth. Public network egress speed is limited to the specified peak bandwidth. Tiered prices are adopted:</li>
<table>
<tr>
<th>Tier</th>
<th>Price</th>
</tr>
<tr>
<td>≤ 5 M</td>
<td>0.0625 CNY/M/Hour</td>
</tr>
<tr>
<td>> 5 M</td>
<td>0.25 CNY/M/Hour</td>
</tr>
</table>
Charge is billed on an hourly basis with a post-paid mode. Usage period less than 1 hour will be counted as 1 hour.</br>

*You may change the public network egress billing mode of BM EIP. The change will take effect in the next hour.</br>*
*Within the same hour and under the same billing mode, changes to the peak bandwidth will take effect immediately. The public network egress fee for the current billing period depends on the last modified peak bandwidth*

### Bills
BM EIP uses three types of bills based on billing items and billing modes:
<li>BM EIP public network egress - Bill by public network traffic - Charges for Month X. This records the total public network traffic generated from using BM EIP and the charges billed within the selected time range</li>
![](http://mc.qcloudimg.com/static/img/00a241310bde9875abc00112b1651ac9/image.png)
<li>BM EIP public network egress - Bill by fixed bandwidth - Charges for Month X. This records the details of peak bandwidth purchased and charges billed for BM ElPs within the selected time range</li>
![](http://mc.qcloudimg.com/static/img/84562d836f248f54a93fbf811176ac42/image.png)
<li>BM ElP - Charges for Month X: This records the details of idleness and charges billed for all the BM EIPs within the selected time range</li>
![](http://mc.qcloudimg.com/static/img/21e4a12a3e18993d87d9360dfaca2fb3/image.png)

## Binding

1) Log in to CPM console and locate the "EIP" option.

![](http://mc.qcloudimg.com/static/img/9123cee39932385deb3ea5beef3416cf/image.png)

2) Locate the IP to be bound and click **Bind** button. The button will be unavailable if the IP has already been bound to a CPM or NAT gateway. You need to unbind it from the original resource first.


3) Select the CPM or NAT gateway to which the EIP is to be bound, and click "Bind" button to complete the process. Public network egress fee will be charged from this point of time.</br>
![](http://mc.qcloudimg.com/static/img/b2658106b9895bd396a7d813a2c9f8d9/image.png)

*Note: BM EIP with the billing mode of "bill by fixed bandwidth" cannot be bound to NAT gateway*</br>

## Unbinding

1) Log in to CPM console and select **EIP** from the left pane.

![](http://mc.qcloudimg.com/static/img/9123cee39932385deb3ea5beef3416cf/image.png)

2) Select an EIP and click **Unbind**. Confirm the unbinding to complete the operation. The IP Idle Fee is charged from this point of time.


## Releasing EIP

1) Log in to CPM console and select **EIP** from the left pane.

![](http://mc.qcloudimg.com/static/img/9123cee39932385deb3ea5beef3416cf/image.png)

2) Select an EIP and click **Release**. The idle EIP stops charging from this point of time.