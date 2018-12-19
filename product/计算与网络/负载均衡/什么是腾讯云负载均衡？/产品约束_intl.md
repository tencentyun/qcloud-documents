
﻿In addition to general usage restrictions, Tencent cloud load balancer instances are also subject to specific usage restrictions depending on their types.  For more information on types of cloud load balancer instances, refer to [Public Network Cloud Load Balancer](http://intl.cloud.tencent.com/document/product/214/6147) and [Private Network Cloud Load Balancer](http://intl.cloud.tencent.com/document/product/214/6148).


<table>
<tbody>
<tr><th></th><th>Specific Use Limits</th><th>General Use Limits</th></tr>
<tr>
  <td>Application CLB instance</td>
  <td>A frontend port only corresponds to one protocol within one CLB instance <br>A frontend port corresponds to multiple backend ports within one CLB instance <br>A maximum of 50 forwarding rules can be created in one listener <br>A maximum of 100 forwarding groups (deviceId + port, i.e. CVM + port) can be added in one forwarding rule</td>
  <td rowspan="4">A maximum of 100 CLB instances can be purchased for each type <br>A maximum of 100 CVMs can be associated with each CLB instance <br>A maximum of 50 listeners can be created for each CLB instance <br>The number of ports can only be an integer within 1-65535</td>
 </tr>
<tr>
  <td>Conventional CLB instance</td>
  <td>A frontend port only corresponds to one protocol within one CLB instance <br>A frontend port corresponds to multiple backend ports within one CLB instance</td>
 </tr>
 <tr>
  <td>Private network CLB instance</td>
  <td></td>
 </tr>
</tbody>
</table>

If a CLB-associated CVM is isolated (put into the recycle bin, or removed according to the postpaid plan) due to arrears, the CLB still binds this CVM.
