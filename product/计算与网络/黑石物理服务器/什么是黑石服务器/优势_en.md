Compared with self-built data center, CPM allows you to build your private cloud faster, with Tencent Cloud providing cross-region interconnection between data center private　networks as well as VPCs, BM　load balancers, NAT gateway, operation and maintenance, monitoring, security protection and other capabilities. If your business is sensitive to performance, you're recommended to use CPM for a more powerful computing capability without any compromise on performance.

## Comparison with Self-built IDC Through Co-location
<table class="table-striped">

		<tr>
			<th>&nbsp;</th>
			<th>Cloud Physical Machine</th>
			<th>Self-built IDC Through Co-location</th>
		</tr>
		
		<tr>
		<th>Elasticity</th>
		<td>
        <p>Elastic scale-up and flexible configuration</p>
        <li>You can flexibly customize the CPM configurations, including CPU, memory, hard disk, ENI, GPU card, etc., and add extra configurations rapidly to meet actual needs. Tencent Cloud provides all accessories needed for the addition of configurations, on-site addition of configurations for IDC as well as after-addition maintenance service</li>
        <li>With Tencent Cloud resource pool, you can purchase dozens of CPMs just through on-click and achieve a scale-up of clusters rapidly to meet the need during peak hours.</li>
        </td>
		<td>
		<p>Lack of elasticity and flexibility</p>
            <li>Self-addition of extra configurations may cause your loss of eligibility for manufacturer's maintenance service.</li>
            <li>Substantial resource reserve is needed to satisfy the requirement of temporary scale-up. After traffic peak hours, you'll be faced with overcapacity and asset depreciation.</li>
        </td>
		</tr>
		
        <tr>
		<th>Ease of use</th>
		<td>
        <p>"Out of the Box" and rapid deployment</p>
        <li>After customizing the hardware configuration of CPMs, you can also specify the installation requirements for operating system, Raid level, system partition, etc. Most of the devices can be deployed within 4 hours.     </li>
        <li>You can perform online operations, such as shutdown, boot-up, reboot, reinstallation, on the CPMs on the console or through cloud APIs. You can also connect to the out-of-band network O&M server via SSL VPN.</li>
        </td>
		<td>
		<p>Effort and time consuming</p>
            <li>You have to contact IDC on-site engineers for operations on CPMs, which is both effort and time consuming.</li>
       
        </td>
		</tr>


 	 	<tr>
		<th>An all-around approach</th>
		<td>
        <p>Integration of various cloud services</p>
        <li>Tencent Cloud data centers in different regions can interconnect with each other over private networks using their high-speed connected networks</li>
        <li>VPC, BM load balancer, NAT gateway and other cloud services are provided</li>
		<li>Network resource cloud APIs are provided to support virtualization</li>
        </td>
		<td >
		<p>High cost</p>
            <li>The interconnection over private network can only be achieved by establishing a dedicated connectivity, which is expensive.</li>
			<li>BM load balancer, NAT gateway and other services need to be built independently</li>
       
        </td>
		</tr>
		
         <tr>
		<th>Security</th>
		<td>
        <p>Three-dimensional protection and professional support</p>
        <li>VPC allows you to customize the IP range, and decide which CPMs can be configured as public or private, to ensure the privacy and security of nodes.</li>
        <li>Trojan detection, brute-force attack protection, vulnerability scanning, WAF, login security, and other basic host security protections are provided. A wide range of free-of-charge basic security services can shield your business from security risks;</li>
        <li>Free DDoS protection with a quota of 10 G features high defense capability to eliminate your worry about security problems.</li>
        </td>
		<td >
		<p>Vulnerable to hacker intrusion</p>
            <li>Additional security protection services need to be purchased</li>
       
        </td>
		</tr>
		
<tr>
		<th>Care-free</th>
		<td>
        <p>O&M service provided on a 24/7 basis</p>
        <li>To rapidly fix hardware failures, Tencent Cloud provides a dedicated standby hardware pool in each data center. The faulty hardware will be replaced after diagnosed by on-site engineers. </li>
        <li>Tencent Cloud's professional network engineer team can deal with various network failures caused by ENI, switch and ISPs.
</li>
        
        </td>
		<td>
		<p>Lack of professionalism</p>
            <li>Devices need to be maintained independently upon the expiration of warranty. A deficiency in the ability to solve network problems exists.</li>
       
        </td>
		</tr>
		
        <th>Cost-saving</th>
		<td>
        <p>Purchase-on-demand and pay-by-usage</p>
        <li>CPM is available in several billing modes such as monthly and annual plan. You can purchase as you grow and pay by usage, without the need to make a huge one-off investment so as to reduce costs.</li>
        <li>You can customize the CPM configurations which can be added on or reduced later in a more flexible way until being adjusted to the right ones.</li>
        
        </td>
		<td>
		<p>High rental and operation&maintenance costs</p>
            <li>Vast component reserve is required and maintenance and on-site services need to be purchased from manufacturers and IDCs for a rapid troubleshooting of hardware.</li>
            <li>A huge sum of money needs to be invested in the one-off purchase of a large number of servers, which leads to an expensive cost and problems such as device depreciation.</li>
        </td>
		</tr>

	
</table>



## Performance Comparison
This section provides an overview of comparison of network performance between standalone machines.

<table>
<tr>
<th>Performance Metric</th>
<th>CPM</th>
<th>CVM</th>
<th>Performance Comparison</th>
</tr>

<tr>
<td>256 B file (TCP) - Transmission bandwidth (Mbits/sec)</td>
<td>9501.62</td>
<td>2577.15</td>
<td>268.69%</td>
</tr>

<tr>
<td>1500 B file (TCP) - transmission bandwidth (Mbits/sec)</td>
<td>9601.57</td>
<td>2507.33</td>
<td>278.95%</td>
</tr>

<tr>
<td nowrap>32-1024 B persistent connection - packets/sec</td>
<td>1067986.67</td>
<td>125523</td>
<td>750.83%</td>
</tr>

<tr>
<td nowrap>32-1024 B short connection - packets/sec</td>
<td>112317.5</td>
<td>7127.39</td>
<td>1475.86%</td>
</tr>

<tr>
<td>256 B file (UDP) - transmission bandwidth (Mbits/sec)</td>
<td>7968.24</td>
<td>122.4</td>
<td>6410.00%</td>
</tr>

<tr>
<td>1424 B file (UDP) - transmission bandwidth (Mbits/sec)</td>
<td>9655.08</td>
<td>522.01</td>
<td>1749.60%</td>
</tr>

<tr>
<td>1500 B file (UDP) - transmission bandwidth (Mbits/sec)</td>
<td>9539.66</td>
<td>615.93</td>
<td>1448.82%</td>
</tr>
</table>


