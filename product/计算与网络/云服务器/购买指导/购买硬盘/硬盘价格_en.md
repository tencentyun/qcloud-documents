Currently Tencent Cloud provides four types of hard disks: ordinary local disk, local SSD disk, ordinary cloud disk and SSD cloud disk.

Separate purchase of system disks is not supported. The data disk is purchased along with the master server by checking the corresponding item. The system disk is along with the data disk.

## 1. Annual/Monthly Package
>Note:
>
- In units of <font color="red">CNY/GB/month</font>
– Currently, the hard disk is purchased along with the CVM, enjoying a 2-month discount if you choose annual billing mode. That is, the annual billing price equals monthly package price multiplied by 10
- <font color="red">This price does not include the price of CVM hardware (CPU, memory) and network</font>

<table class="diskMonth">
        <tbody><tr>
            <th style="width: 5%;">Billing items</th>
            <th style="width: 5%;">Hard disk type</th>
<th style="width: 10%;">Unit</th>
            <th style="width: 20%;">Step</th>
<th style="width: 20%;">Maximum value</th>
						<th style="width: 20%;">Remarks</th>
            <th style="width: 20%;">Price</th>
        </tr>
        <tr>
            <td rowspan="4">System disk</td>
            <td>Ordinary local disk</td>
<td rowspan="8"><span style="color:red">CNY/GB/month</span></td>
						<td rowspan="4">-</td>
            <td rowspan="4">-</td>
						<td rowspan="4">Free: Linux 20 GB, Windows 50 GB</td>
						<td rowspan="4">-</td>
        </tr>
        <tr>
            <td>Local SSD disk</td>
        </tr>
        <tr>
            <td>Ordinary cloud disk</td>
        </tr>
        <tr>
            <td>SSD cloud disk</td>
        </tr>
				<tr>
            <td rowspan="4">Data disk</td>
            <td>Ordinary local disk</td>
            <td>10 GB</td>
						<td>Increases with the number of CPU cores of your CVM, up to 1000 GB</td>
            <td>-</td>
            <td>0.30</td>
        </tr>
				<tr>
            <td >Local SSD disk</td>
            <td>10 GB</td>
            <td>Increases with the number of CPU cores of your CVM, up to 3000 GB</td>
            <td>-</td>
						<td>0.80</td>
        </tr>
        <tr>
            <td>Ordinary cloud disk</td>
            <td>10 GB</td>
            <td>4000 GB</td>
						<td>-</td>
            <td>0.30</td>
        </tr>
        <tr>
            <td>SSD cloud disk</td>
            <td>250 GB</td>
            <td>4000 GB</td>
						<td>-</td>
            <td>1.10</td>
        </tr>
    </tbody></table>

## 2. Pay by Traffic
>Note:
>
- In units of <font color="red">CNY/100 GB/hour</font>
- <font color="red">This price does not include the price of CVM hardware (CPU, memory) and network</font>

<table class="diskHour">
        <tbody><tr>
            <th style="width: 5%;">Billing items</th>
            <th style="width: 5%;">Hard disk type</th>
						<th style="width: 10%;">Unit</th> 
            <th style="width: 20%;">Step</th>
<th style="width: 20%;">Maximum value</th>
						<th style="width: 20%;">Remarks</th>
            <th style="width: 30%;">Price</th>
        </tr>
        <tr>
            <td rowspan="4">System disk</td>
            <td>Ordinary local disk</td>
<td rowspan="8"><span style="color:red">CNY/100 GB/hour</span></td>
            <td rowspan="4">-</td>
            <td rowspan="4">-</td>
						<td rowspan="4">Free: Linux 20 GB, Windows 50 GB</td>
						<td rowspan="4">-</td>
        </tr>
        <tr>
            <td>Local SSD disk</td>
        </tr>
        <tr>
            <td>Ordinary cloud disk</td>
        </tr>
        <tr>
            <td>SSD cloud disk</td>
        </tr>
				<tr>
            <td rowspan="4">Data disk</td>
            <td>Ordinary local disk</td>
            <td>10 GB</td>
						<td>Increases with the number of CPU cores of your CVM, up to 1000 GB</td>
            <td>-</td>
            <td>0.042</td>
        </tr>
				<tr>
            <td >Local SSD disk</td>
            <td>10 GB</td>
            <td>Increases with the number of CPU cores of your CVM, up to 3000 GB</td>
            <td>-</td>
						<td>0.33</td>
        </tr>
        <tr>
            <td>Ordinary cloud disk</td>
            <td>10 GB</td>
            <td>4000 GB</td>
						<td>-</td>
            <td>0.042</td>
        </tr>
        <tr>
            <td>SSD cloud disk</td>
            <td>250 GB</td>
            <td>4000 GB</td>
						<td>-</td>
            <td>0.33</td>
        </tr>
    </tbody></table>
