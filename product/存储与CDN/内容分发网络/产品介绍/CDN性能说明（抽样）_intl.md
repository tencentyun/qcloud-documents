
## Test Description

### Test Tools

Host (1 core, 1G), Tencent Cloud CDN

### Test Method

Use the benchmarking test method commonly used in the industry. The service provider is Ting Yun.

### Test Parameters
<table style="width: 80%;display: table;margin-bottom:40px;">
	<tbody>
		<tr>
			<th scope="row" style="width:102px">Time</th> 
			<td style="width:385px"> 16:00, Dec 24, 2015 ~ 11:00, Dec 25, 2015 </td> 
		</tr>
		<tr>
			<th scope="row" style="width:102px">Tested cities </th> 
			<td style="width:385px"> All </td> 
		</tr>
		<tr>
			<th scope="row" style="width:102px">Tested ISPs</th> 
			<td style="width:385px"> All </td> 
		</tr>
		<tr>
			<th scope="row" style="width:102px">Origin server link</th> 
			<td style="width:385px"> http://**/20090820_a5168bfe-3791-4a5c-bb59-1244e3ee1153.jpg</td>
		</tr>
		<tr>
			<th scope="row" style="width:102px">Origin server+CDN link</th> 
			<td style="width:385px"> http://**/**/20090820_a5168bfe-3791-4a5c-bb59-1244e3ee1153.jpg</td>
		</tr>
	</tbody>
</table>

## Result Analysis

### Performance Curve

![](https://mc.qcloudimg.com/static/img/e7d9601acfd2cdeeaf6ed8a39808ff44/CDN-CDN+Performance+Test%281%29.png)

### Availability Curve

![](https://mc.qcloudimg.com/static/img/9298d401474f88edfab2d887c6cdbef5/CDN-CDN+Performance+Test%282%29.png)


### Chart Analysis

<table style="display:table;">
	<tbody>
		<tr>
			<th rowspan="2" style="width: 58px;"> Monitoring Task </th>
			<th rowspan="2" style="width: 36px;"> Number of Monitoring Points </th>
			<th colspan="5"> Performance (sec) </th>
			<th colspan="5"> Availability (%) </th>
		</tr>
		<tr>
			<th style="width: 43px;"> Mean </th>
			<th colspan="2" style="width: 107px;"> Best </th>
			<th colspan="2"> Worst </th>
			<th style="width: 45px;"> Mean </th>
			<th colspan="2" style="width: 111px;"> Best </th>
			<th colspan="2"> Worst </th>
		</tr>
		<tr>
			<td style="width: 58px; text-align: center;"> Origin Server </td>
			<td style="width: 36px; text-align: center;"> 1173 </td>
			<td style="text-align: center; width: 43px;"> 1.271 </td>
			<td style="text-align: center; width: 65px;"> 02:00, Dec. 25 </td>
			<td style="text-align: center; width: 38px;"> 1.015 </td>
			<td style="text-align: center; width: 65px;"> 16:00, Dec. 24 </td>
			<td style="text-align: center; width: 51px;"> 1.801 </td>
			<td style="text-align: center; width: 45px;"> 95.48 </td>
			<td style="text-align: center; width: 66px;"> 01:00, Dec. 25 </td>
			<td style="text-align: center; width: 43px;"> 98.53 </td>
			<td style="text-align: center; width: 77px;"> 21:00, Dec. 24 </td>
			<td style="text-align: center; width: 43px;"> 91.23 </td>
		</tr>
		<tr>
			<td style="width: 58px; text-align: center;"> Origin Server - CDN </td>
			<td style="width: 36px; text-align: center;"> 1205 </td>
			<td style="text-align: center; width: 43px;"> 0.291 </td>
			<td style="text-align: center; width: 65px;"> 05:00, Dec. 25 </td>
			<td style="text-align: center; width: 38px;"> 0.209 </td>
			<td style="text-align: center; width: 65px;"> 09:00, Dec. 25 </td>
			<td style="text-align: center; width: 51px;"> 0.421 </td>
			<td style="text-align: center; width: 45px;"> 99.67 </td>
			<td style="text-align: center; width: 66px;"> 16:00, Dec. 24 </td>
			<td style="text-align: center; width: 43px;"> 100.00 </td>
			<td style="text-align: center; width: 77px;"> 09:00, Dec. 25 </td>
			<td style="text-align: center; width: 43px;"> 98.18 </td>
		</tr>
	</tbody>
</table>

### Data Details

<table  style="display: table;">
	<tbody>
		<tr>
			<th rowspan="2"> Time </th>
			<th colspan="3" style="width: 280px;"> Origin Server </th>
			<th colspan="3" style="width: 280px;"> Origin Server+CDN </th>
		</tr>
		<tr>
			<th> Performance (sec) </th>
			<th> Availability (%) </th>
			<th style="width: 71px;"> Number of Monitoring Points </th>
			<th style="width: 76px;"> Performance (sec) </th>
			<th> Availability (%) </th>
			<th> Number of Monitoring Points </th>
		</tr>
		<tr>
			<td style="text-align: center;"> 16:00, Dec.24, 2015 </td>
			<td style="text-align: center;"> 1.801 </td>
			<td style="text-align: center;"> 91.94 </td>
			<td style="text-align: center; width: 71px;"> 62 </td>
			<td style="text-align: center; width: 76px;"> 0.41 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 64 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 17:00, Dec.24, 2015 </td>
			<td style="text-align: center;"> 1.123 </td>
			<td style="text-align: center;"> 94.2 </td>
			<td style="text-align: center; width: 71px;"> 69 </td>
			<td style="text-align: center; width: 76px;"> 0.269 </td>
			<td style="text-align: center;"> 98.63 </td>
			<td style="text-align: center;"> 73 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 18:00, Dec. 24, 2015 </td>
			<td style="text-align: center;"> 1.211 </td>
			<td style="text-align: center;"> 92.31 </td>
			<td style="text-align: center; width: 71px;"> 52 </td>
			<td style="text-align: center; width: 76px;"> 0.247 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 52 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 19:00, Dec. 24, 2015 </td>
			<td style="text-align: center;"> 1.495 </td>
			<td style="text-align: center;"> 95.95 </td>
			<td style="text-align: center; width: 71px;"> 74 </td>
			<td style="text-align: center; width: 76px;"> 0.239 </td>
			<td style="text-align: center;"> 98.65 </td>
			<td style="text-align: center;"> 74 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 20:00, Dec. 24, 2015 </td>
			<td style="text-align: center;"> 1.568 </td>
			<td style="text-align: center;"> 93.65 </td>
			<td style="text-align: center; width: 71px;"> 63 </td>
			<td style="text-align: center; width: 76px;"> 0.357 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 65 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 21:00, Dec. 24, 2015 </td>
			<td style="text-align: center;"> 1.421 </td>
			<td style="text-align: center;"> 91.23 </td>
			<td style="text-align: center; width: 71px;"> 57 </td>
			<td style="text-align: center; width: 76px;"> 0.308 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 60 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 22:00, Dec. 24, 2015 </td>
			<td style="text-align: center;"> 1.255 </td>
			<td style="text-align: center;"> 94.23 </td>
			<td style="text-align: center; width: 71px;"> 52 </td>
			<td style="text-align: center; width: 76px;"> 0.256 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 54 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 23:00, Dec. 24, 2015 </td>
			<td style="text-align: center;"> 1.206 </td>
			<td style="text-align: center;"> 96.83 </td>
			<td style="text-align: center; width: 71px;"> 63 </td>
			<td style="text-align: center; width: 76px;"> 0.241 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 64 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 00:00, Dec. 25, 2015 </td>
			<td style="text-align: center;"> 1.242 </td>
			<td style="text-align: center;"> 92.59 </td>
			<td style="text-align: center; width: 71px;"> 54 </td>
			<td style="text-align: center; width: 76px;"> 0.397 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 53 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 01:00, Dec. 25, 2015 </td>
			<td style="text-align: center;"> 1.309 </td>
			<td style="text-align: center;"> 98.53 </td>
			<td style="text-align: center; width: 71px;"> 68 </td>
			<td style="text-align: center; width: 76px;"> 0.271 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 71 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 02:00, Dec. 25, 2015 </td>
			<td style="text-align: center;"> 1.015 </td>
			<td style="text-align: center;"> 97.37 </td>
			<td style="text-align: center; width: 71px;"> 76 </td>
			<td style="text-align: center; width: 76px;"> 0.253 </td>
			<td style="text-align: center;"> 98.68 </td>
			<td style="text-align: center;"> 76 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 03:00, Dec. 25, 2015 </td>
			<td style="text-align: center;"> 1.154 </td>
			<td style="text-align: center;"> 96.92 </td>
			<td style="text-align: center; width: 71px;"> 65 </td>
			<td style="text-align: center; width: 76px;"> 0.363 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 66 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 04:00, Dec. 25, 2015 </td>
			<td style="text-align: center;"> 1.181 </td>
			<td style="text-align: center;"> 98.33 </td>
			<td style="text-align: center; width: 71px;"> 60 </td>
			<td style="text-align: center; width: 76px;"> 0.225 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 63 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 05:00, Dec. 25, 2015 </td>
			<td style="text-align: center;"> 1.185 </td>
			<td style="text-align: center;"> 98.31 </td>
			<td style="text-align: center; width: 71px;"> 59 </td>
			<td style="text-align: center; width: 76px;"> 0.209 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 59 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 06:00, Dec. 25, 2015 </td>
			<td style="text-align: center;"> 1.131 </td>
			<td style="text-align: center;"> 96.97 </td>
			<td style="text-align: center; width: 71px;"> 66 </td>
			<td style="text-align: center; width: 76px;"> 0.265 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 67 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 07:00, Dec. 25, 2015 </td>
			<td style="text-align: center;"> 1.211 </td>
			<td style="text-align: center;"> 94.83 </td>
			<td style="text-align: center; width: 71px;"> 58 </td>
			<td style="text-align: center; width: 76px;"> 0.212 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 62 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 08:00, Dec. 25, 2015 </td>
			<td style="text-align: center;"> 1.127 </td>
			<td style="text-align: center;"> 93.44 </td>
			<td style="text-align: center; width: 71px;"> 61 </td>
			<td style="text-align: center; width: 76px;"> 0.313 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 62 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 09:00, Dec. 25, 2015 </td>
			<td style="text-align: center;"> 1.224 </td>
			<td style="text-align: center;"> 96.15 </td>
			<td style="text-align: center; width: 71px;"> 52 </td>
			<td style="text-align: center; width: 76px;"> 0.421 </td>
			<td style="text-align: center;"> 98.18 </td>
			<td style="text-align: center;"> 55 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 10:00, Dec. 25, 2015 </td>
			<td style="text-align: center;"> 1.295 </td>
			<td style="text-align: center;"> 98.39 </td>
			<td style="text-align: center; width: 71px;"> 62 </td>
			<td style="text-align: center; width: 76px;"> 0.314 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 65 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> Average/Aggregate </td>
			<td style="text-align: center;"> 1.271 </td>
			<td style="text-align: center;"> 95.48 </td>
			<td style="text-align: center; width: 71px;"> 1173 </td>
			<td style="text-align: center; width: 76px;"> 0.291 </td>
			<td style="text-align: center;"> 99.67 </td>
			<td style="text-align: center;"> 1205 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> Excluded Points </td>
			<td colspan="3" style="text-align: center; width: 232px;"> 0 </td>
			<td colspan="3" style="text-align: center; width: 240px;"> 0 </td>
		</tr>
	</tbody>
</table>

