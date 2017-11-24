## Billing
<table>
<tr>
<th> Billing Items </th>
<th>Discount</th>
<th>Unit Price<br>(Unit:USD/day) </th>
<th> Billing Cycle</th>
<th>Billing Method</th>
</tr>
<tr>
<td>China Mainland</td>
<td  rowspan="4">null</td>
<td> 0.072</td>
<td  rowspan="4" >day </td>
<td  rowspan="4">postpaid/perday</td>
</tr>
<tr>
<td>Singapore<br>Frankfurt<br>Toronto</td>
<td>0.144</td>
</tr>
<tr>
<td> Silicon Valley </td>
<td> 0.120 </td>
</tr>
<tr>
<td>Hong Kong<br>Korea</td>
<td>0.216</td>
</tr>
</table>

The charges for cloud load balance service include instance rental fee and bandwidth traffic fee of backend servers. For example, if there is a CLB instance managing 3 CVMs, then the actual charges will include cost for the CLB instance and the cost for the 3 CVM instances (cost for instances will be accounted into network charges).

Cloud load balance is postpaid product. As long as the account is not in arrears, the system will not cancel cloud load balancer instances unless the user returns (deletes) them. When the account is in appears, cloud load balancer instances will be isolated by the system on 21st of the month, and reclaimed on 28th if the user does not renew the service. Once reclaimed, all binding relationships with backend servers will be disconnected. 

>Note: When a CVM is isolated (Go into recycle bin for CVMs of annual or monthly plan, or be in arrears for more than two hours for CVMs of Bill-by-Traffic plan), its binding relationship with the LB will be terminated. 
