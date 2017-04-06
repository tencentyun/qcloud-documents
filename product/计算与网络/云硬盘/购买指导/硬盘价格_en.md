## Price Description of Block Storage Devices
<table class="cvmMonth">
        <tbody><tr>
            <th style="width: 10%;" rowspan="2">Item</th>
            <th style="width: 40%;" colspan="2">Local disk</th>
            <th style="width: 50%;" colspan="3">Cloud disk</th>
        </tr>
        <tr>
            <th>Local HDD</th>
            <th>SSD local disk</th>
			<th>HDD cloud disk</th>
			<th>SSD cloud disk</th>
            <th>Premium cloud disk</th>
        </tr>
        <tr>
            <td>Capacity of a single disk (used as a data disk)</td>
            <td>10GB - 1,000GB</td>
            <td>10GB - 250GB</td>
						<td>10GB - 16,000GB</td>
            <td>250GB - 4,000GB</td>
            <td>50GB - 4,000GB</td>
        </tr>
        <tr>
            <td>Maximum throughput</td>
            <td>40-hundreds MB/s</td>
            <td>300 MB/s</td>
						<td>40-100 MB/s</td>
            <td>150-260 MB/s</td>
            <td>75-130 MB/s</td>
        </tr>
					<tr>
            <td>Formula for calculating throughput performance </td>
            <td>N/A</td>
            <td>N/A</td>
						<td>N/A</td>
            <td>Throughput={min 150+0.147*(purchased capacity-250GB), max 260} MB/s<br>
The minimum throughput value is 150 MB/s with an increment of 0.147 MB/s per GB and the upper limit is 260 MB/s;</td>
            <td>Throughput={min 75+disk capacity*0.147, max 130} MB/s<br>The minimum throughput value is 75 MB/s, and the upper limit is 130 MB/s;
</td>
        </tr>
        <tr>
            <td>Maximum IOPS</td>
            <td>Hundreds-2,000</td>
            <td>30,000</td>
						<td>Hundreds-1,000</td>
            <td>6,000-24,000</td>
            <td>1,500-4,500</td>
        </tr>
				<tr>
            <td>Formula for calculating IOPS performance</td>
            <td>N/A</td>
            <td>N/A</td>
						<td>N/A</td>
            <td>IOPS={min 6,000+24*capacity, max 24,000}<br>
24 IOPS are provided per GB, and the upper limit is 24,000; the minimum IOPS value is 6,000;</td>
            <td>IOPS={min 1,500+8*capacity, max 4,500}<br>
8 IOPS are provided per GB, and the upper limit is 4,500; the minimum IOPS value is 1,500;
</td>
        </tr>
								<tr>
            <td>Price</td>
            <td>Annual or monthly plan: RMB 0.3/GB/month<br>
Pay by usage: RMB 0.042/100G/hour</td>
            <td>Annual or monthly plan: RMB 0.8/GB/month<br>
Pay by usage: RMB 0.33/hour/100GB</td>
            <td>Annual or monthly plan: RMB 0.3/GB/month<br>
Pay by usage: RMB 0.042/hour/100GB</td>
						<td>Annual or monthly plan: RMB 1.1/GB/month<br>
Pay by usage: RMB 0.332/hour/100GB</td>
            <td>Annual or monthly plan: RMB 0.35/GB/month<br>
Pay by usage: RMB 0.09/hour/100GB</td>
        </tr>
        
    </tbody></table>
    
**Note:**

- System disk must be purchased when you purchase a CVM, and cannot be purchased separately.

- You can enjoy 2-month discount if you choose annual or monthly plan. In other words, annual billing price equals monthly price multiplied by 10.
 
 

