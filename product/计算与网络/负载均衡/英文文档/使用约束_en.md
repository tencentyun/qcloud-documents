In addition to general usage restrictions, Tencent cloud load balancer instances are also subject to specific usage restrictions depending on their types.  For more information on types of cloud load balancer instances, refer to [Public Network Cloud Load Balancer](/doc/product/214/6147) and [Private Network Cloud Load Balancer](/doc/product/214/6148).

<table>
<tbody>
<tr><th></th><th>Specific Restrictions </th><th> General Restrictions</th></tr>
<tr>
  <td>Public network application-based cloud load balancer instance</td>
  <td>A front-end port can only correspond to one protocol type within one cloud load balancer instance<br>A front-end port can correspond to multiple back-end ports within one cloud load balancer instance<br>The number of forwarding rules created in one listener shall not exceed 50<br>The number of forwarding groups (deviceId+port, or CVM+port) added in one forwarding rule shall not exceed 100</td>
  <td rowspan="4">The number of CLBs which can be purchased for each type shall not exceed 100<br>The number of CVMs associated with each CLB instance shall not exceed 100<br> The number of listeners created for each CLB instance shall not exceed 50<br> The number of ports listened by each CLB instance shall not exceed 20<br> The number of ports can only be an integer of 1-65535</td>
 </tr>
<tr>
  <td>Public network (with static IP) cloud load balancer instance</td>
  <td>A front-end port can only correspond to one protocol type within one cloud load balancer instance<br>A front-end port can correspond to multiple back-end ports within one cloud load balancer instance</td>
 </tr>
 <tr>
  <td>Public network (without static IP) cloud load balancer instance</td>
  <td>Service IP (VIP) not supported<br>Layer-4 forwarding (UDP, TCP) not supported<br>Layer-7 forwarding (HTTP) supported<br>Session persistence supported<br>Health check supported <br>Port 843 not supported<br>Back-end ports shall be different each other, and be consistent with the front-end ports within one cloud load balancer</td>
 </tr>
 <tr>
  <td>Private network cloud load balancer instance</td>
  <td></td>
 </tr>
</tbody>
</table>

If the CLB-associated CVM is isolated (put into recycle bin, or canceled in accordanc with Bill-by-Traffic) for arrears , the CLB still binds this CVM.
