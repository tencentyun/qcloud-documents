<table><tbody>
<th width=15%>Date</th>
<th>Updates</th>
<tr>
<td> Jan 19, 2016 </td>
<td> 
1. The API key module went online <br>
2. The users who purchased CVMs could adjust the system disk size. Users needed to contact customer service personnel to activate this service.<br>
3. Redis module was added.<br>
4. Cmem module was added.<br>
<tr>
<td> Dec 21, 2015 </td>
<td> 
1. Core-sharing CVMs were removed from the Guangzhou Zone 1, and API disabled renewal and automatic renewal operations. For details, please check the announcement and the internal message: [Tencent Cloud] Notice on Upgrading Tencent Cloud Core-sharing CVMs to 1 Core 1G For Free.<br>
2. The users who purchased CVM with an annual or monthly plan could choose whether an external network is needed by setting wanIp = 1 (enable) or wanIp = 0 (do not enable). The default setting is 1 (enable). For details, please check RunInstances API.<br>
3. The problem was solved that users with a Bandwidth Package plan could not purchase Charge-by-Quantity machines through the RunInstancesHour API.<br>
4. [EIP] module was added to provide elastic IP service.
</td>
</tr>
<tr>
<td> Dec 3, 2015 </td>
<td> 1. Users with a Bandwidth Package plan were supported by UpdateInstanceBandwidth for an upgrade. <br>2. A uniform resource ID unInstanceIdUsers would be returned with the purchase of CVMs with an annual or monthly plan.  </td>
</tr>
<tr>
<td> Nov 10, 2015 
<td> The DFW security group went online.
</tr>
<tr>
<td> Nov 5, 2015 </td>
<td>  1. A unique ID (unInstanceId) was added for CVMs, which can be obtained from DescribeInstances API. It is recommended to use unInstanceId instead of instanceId to identify CVMs. <br>1. A unique ID (unImgId) was added for images, which can be obtained from DescribeImages API. It is recommended to use unImgId instead of imageId to identify Images. <br>3. RenewInstance API canceled passing parameter instanceType <br> 4. DescribeDeals API allowed the unique ID unInstanceId to be returned with the purchase of CVMs with a monthly plan.</td>
</tr>
<tr>
<td> Sept 2, 2015 </td>
<td> 1. Passing projectID was allowed during the query/creation of CVMs.< br > 2. The API to copy custom images was added. <br>3. The API to modify the project to which a CVM belongs was added. <br>4. JAVA SDK was modified.</td>
</tr>
<tr>
<td> July 24, 2015 </td>
<td> The agent console supported logging in from North America.</td>
</tr>
<tr>
<td> July 8, 2015</td>
<td> 1. Service marketplace images (except North American region) and full-volume public images were allowed for the purchase, reinstallation and renewal of CVMs. <br>2. DescribeImages API was modified and the query for service marketplace images was added. <br>3. Public image list page was canceled. DescribeImages API was enabled for querying imageID.</td>
</tr>
<tr>
<td> May 29, 2015</td>
<td> 1. DescribeInstances API returned the image's operating system type. <br>2. Cloud API was available in North American DC.</td>
</tr>
</tbody></table>

