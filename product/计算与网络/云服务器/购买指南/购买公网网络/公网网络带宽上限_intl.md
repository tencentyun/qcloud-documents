### Upper Limit of the Outbound Bandwidth (Downstream Bandwidth)
The upper limit of public network bandwidth is the upper limit of outbound bandwidth by default, that is, the bandwidth that flows out of CVM. The upper limit of public network bandwidth varies with different network billing methods. Details are as follows:
<table border="3">
    <tr>
       <th rowspan="2"><b>Network Billing Method</b></th> 
       <th colspan="2" ><b>CVM</b></th>
       <th rowspan="2"><b>Available range of the upper limit of bandwidth (Mbps)</b></th>	
   </tr>
    <tr>
       <th><b>CVM Billing Method</b></th> 
       <th><b>CVM Configuration</b></th> 
    </tr>
	<tr>
	      <td rowspan="4">Bill-by-Traffic</td> 
        <td >Postpaid CVM</td> 
        <td >ALL</td> 
				<td>0-100</td>    
   </tr>
	  <tr>
        <td rowspan="3">Prepaid CVM</td> 
        <td>Cores ≤ 8</td> 
				<td>0-200</td>        
   </tr>
	  <tr>
        <td>8 < Cores < 24</td> 
        <td>0-400</td> 
   </tr> 
	 <tr>
        <td>Cores ≥ 24</td> 
        <td>0-400 or no speed limit</td> 
   </tr>
	 <tr>
		    <td rowspan="3">Bill-by-Bandwidth</td> 
        <td >Postpaid CVM</td> 
        <td >ALL</td> 
				<td>0-100</td>      
   </tr>
	 <tr>
		    <td rowspan="2">Prepaid CVM</td> 
        <td >Guangzhou Zone 1<br>Guangzhou Zone 2<br>Shanghai Zone 1<br>Hong Kong Zone 1<br>Toronto Zone 1</td> 
				<td>0-200</td>      
   </tr>
	 <tr>
        <td>Other availability zones</td> 
        <td>0-1000</td> 
   </tr>
    <tr>
		    <td>Shared bandwidth</td> 
        <td colspan="2">ALL</td> 
        <td>0-200 or no speed limit</td>    
    </tr>
</table>

### Upper Limit of the Inbound Bandwidth (Upstream Bandwidth)
The inbound bandwidth of public network is the bandwidth that flows into CVM instance.

- If the fixed bandwidth purchased by users is larger than 10 Mbps, Tencent Cloud assigns the public network inbound bandwidth that is equal to the purchased bandwidth.
- If the fixed bandwidth purchased by users is less than 10 Mbps, Tencent Cloud assigns 10 Mbps public network inbound bandwidth.

