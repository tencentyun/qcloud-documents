<table class="cvmMonth">
        <tbody><tr>
            <th style="width: 10%;" rowspan="2">Feature</th>
            <th style="width: 10%;" rowspan="2">Billing Model</th>
                        <th style="width: 30%;" rowspan="2">Configuration</th>
            <th style="width: 50%;" colspan="7">Price</th>
        </tr>
        <tr>
            <th>Beijing<br>Shanghai<br>Guangzhou</th>
                        <th>Hong Kong</th>
                                                 <th>Singapore</th>
            <th>Toronto</th> 
	<th>Korea</th> 
		<th>Frankfurt</th>
			<th>Silicon Valley</th>
        </tr>
        <tr>
            <td>Custom VPC</td>
            <td colspan="9" rowspan="4" align="center">Free</td>
        </tr>
        <tr>
            <td>Custom Subnet</td>
        </tr>
        <tr>
            <td>Custom Routing</td>
        </tr>
        <tr>
        
                
       <tr>
            <td>VPN Gateway</td>
            <td>Bill by hour<br>(USD/month)</td>
            <td>Per hour</td>
            <td>0.078</td>
            <td>0.088</td>
            <td>0.12</td>
            <td>0.12</td>
			<td>0.088</td>
            <td>0.088</td>
            <td>0.088</td>
        </tr>
                                <tr>
            <td rowspan="4">NAT Gateway</td>
            <td rowspan="3">Rental fee for gateway<br>(USD/hour)</td>
            <td>Small</td>
            <td>0.089</td>
            <td>0.13</td>
                                    <td>0.13</td>
                        <td>0.14</td>
			<td>0.13</td>
            <td>0.13</td>
            <td>0.13</td>
        </tr>
                <tr>
            <td>Medium</td>
            <td>0.28</td>
            <td>0.39</td>
                        <td>0.39</td>
                        <td>0.42</td>
			<td>0.39</td>
            <td>0.39</td>
			<td>0.39</td>
        </tr>
                <tr>
            <td>Large</td>
            <td>0.89</td>
            <td>1.3</td>
                        <td>1.3</td>
                        <td>1.4</td>
			<td>1.3</td>
			<td>1.3</td>
			<td>1.3</td>
        </tr>
                <td colspan="2">Charge for traffic consumption (Only the traffic from NAT gateway to the Internet is billed. The NAT gateway traffic for users with a bandwidth package is charged to the bill of bandwidth package)<br>(USD/GB)</td>
            <td>0.12</td>
            <td>0.12</td>
                        <td>0.081</td>
                        <td>0.077</td>
			<td>0.12</td>
			<td>0.077</td>
			<td>0.077</td>
        </tr>
                <tr>
                    <td>Regional Peering Connection</td>
                 <td colspan="9" rowspan="1" align="center">Free</td>
                 </tr>
        </tr>
    <tr>
            <td rowspan="5">Cross-region Peering Connection</td>
                        <td rowspan="5">Peak bandwidth of the day<br><br>Bill by days (USD/Mbps/day) <br><br>Peak bandwidth is calculated as the average bandwidth every 5 minutes<br></td>
                        <td>(0, 20] Mbps</td>
                        <td colspan="1" rowspan="1" align="center">3.19</td>
                        <td colspan="6" rowspan="1" align="center">15</td>
        </tr>
                
                <tr>
                <td>(20M, 100] Mbps</td>
                        <td colspan="1" rowspan="1" align="center">1.98</td>
                        <td colspan="6" rowspan="1" align="center">12</td>
                </tr>
                
                <tr>
                <td>(100, 500] Mbps</td>
                <td colspan="1" rowspan="1" align="center">1.48</td>
                        <td colspan="6" rowspan="1" align="center">9</td>
                </tr>
                
                <tr>
                <td>(500, 2000] Mbps</td>
				<td colspan="1" rowspan="1" align="center">1.19</td>
                        <td colspan="6" rowspan="1" align="center">6</td>
                </tr>
                
             <tr>
                <td >> 2000 Mbps</td>
				<td colspan="1" rowspan="1" align="center">0.82</td>
                        <td colspan="6" rowspan="1" align="center">5</td>
                </tr>
                </tr>
                    
                
    </tbody></table>


 >Note:
 >
 - For users with a bandwidth package for bandwidth sharing, the outbound traffic from NAT gateway is charged to the bill of bandwidth package (the network traffic fee of USD 0.12/GB will not be charged separately). You're recommended to set a limit on the outbound bandwidth of the NAT gateway, so as to avoid an expensive bandwidth package fee due to an excessively high outbound bandwidth. Click to view [Billing Methods for Bandwidth Package](https://cloud.tencent.com/doc/product/213/%E8%B4%AD%E4%B9%B0%E7%BD%91%E7%BB%9C%E5%B8%A6%E5%AE%BD#.E5.B8.A6.E5.AE.BD.E5.8C.85.E8.AE.A1.E8.B4.B9)
 - For the information on more prices, please contact your business representative.
