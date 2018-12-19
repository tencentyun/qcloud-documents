## 测试说明

### 测试工具

主机（单核1G），腾讯云CDN

### 测试方法

采用业内通用的基调测速方法，服务提供商为听云

### 测试参数
<table style="width: 80%;display: table;margin-bottom:40px;">
	<tbody>
		<tr>
			<th scope="row" style="width:102px">测试时间</th> 
			<td style="width:385px"> 2015-12-24 16:00 ~ 2015-12-25 11:00 </td> 
		</tr>
		<tr>
			<th scope="row" style="width:102px">测试城市</th> 
			<td style="width:385px"> 全部 </td> 
		</tr>
		<tr>
			<th scope="row" style="width:102px">测试运营商</th> 
			<td style="width:385px"> 全部 </td> 
		</tr>
		<tr>
			<th scope="row" style="width:102px">源站链接</th> 
			<td style="width:385px"> http://**/20090820_a5168bfe-3791-4a5c-bb59-1244e3ee1153.jpg</td>
		</tr>
		<tr>
			<th scope="row" style="width:102px">源站+CDN链接</th> 
			<td style="width:385px"> http://**/**/20090820_a5168bfe-3791-4a5c-bb59-1244e3ee1153.jpg</td>
		</tr>
	</tbody>
</table>

## 结果分析

### 性能曲线

![](https://mccdn.qcloud.com/img568e2caf9efd1.png)

### 可用性曲线

![](https://mccdn.qcloud.com/img568e2cb5b8eb8.png)


### 图表分析

<table style="display:table;">
	<tbody>
		<tr>
			<th rowspan="2" style="width: 58px;"> 监测任务 </th>
			<th rowspan="2" style="width: 36px;"> 监测点数 </th>
			<th colspan="5"> 性能(秒) </th>
			<th colspan="5"> 可用性(%) </th>
		</tr>
		<tr>
			<th style="width: 43px;"> 均值 </th>
			<th colspan="2" style="width: 107px;"> 最好 </th>
			<th colspan="2"> 最差 </th>
			<th style="width: 45px;"> 均值 </th>
			<th colspan="2" style="width: 111px;"> 最好 </th>
			<th colspan="2"> 最差 </th>
		</tr>
		<tr>
			<td style="width: 58px; text-align: center;"> 源站 </td>
			<td style="width: 36px; text-align: center;"> 1173 </td>
			<td style="text-align: center; width: 43px;"> 1.271 </td>
			<td style="text-align: center; width: 65px;"> 12月25日 02:00 </td>
			<td style="text-align: center; width: 38px;"> 1.015 </td>
			<td style="text-align: center; width: 65px;"> 12月24日 16:00 </td>
			<td style="text-align: center; width: 51px;"> 1.801 </td>
			<td style="text-align: center; width: 45px;"> 95.48 </td>
			<td style="text-align: center; width: 66px;"> 12月25日 01:00 </td>
			<td style="text-align: center; width: 43px;"> 98.53 </td>
			<td style="text-align: center; width: 77px;"> 12月24日 21:00 </td>
			<td style="text-align: center; width: 43px;"> 91.23 </td>
		</tr>
		<tr>
			<td style="width: 58px; text-align: center;"> 源站-CDN </td>
			<td style="width: 36px; text-align: center;"> 1205 </td>
			<td style="text-align: center; width: 43px;"> 0.291 </td>
			<td style="text-align: center; width: 65px;"> 12月25日 05:00 </td>
			<td style="text-align: center; width: 38px;"> 0.209 </td>
			<td style="text-align: center; width: 65px;"> 12月25日 09:00 </td>
			<td style="text-align: center; width: 51px;"> 0.421 </td>
			<td style="text-align: center; width: 45px;"> 99.67 </td>
			<td style="text-align: center; width: 66px;"> 12月24日 16:00 </td>
			<td style="text-align: center; width: 43px;"> 100.00 </td>
			<td style="text-align: center; width: 77px;"> 12月25日 09:00 </td>
			<td style="text-align: center; width: 43px;"> 98.18 </td>
		</tr>
	</tbody>
</table>

### 数据明细

<table  style="display: table;">
	<tbody>
		<tr>
			<th rowspan="2"> 时间 </th>
			<th colspan="3" style="width: 280px;"> 源站 </th>
			<th colspan="3" style="width: 280px;"> 源站+CDN </th>
		</tr>
		<tr>
			<th> 性能(秒) </th>
			<th> 可用性(%) </th>
			<th style="width: 71px;"> 监测点数 </th>
			<th style="width: 76px;"> 性能(秒) </th>
			<th> 可用性(%) </th>
			<th> 监测点数 </th>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月24日 16:00 </td>
			<td style="text-align: center;"> 1.801 </td>
			<td style="text-align: center;"> 91.94 </td>
			<td style="text-align: center; width: 71px;"> 62 </td>
			<td style="text-align: center; width: 76px;"> 0.41 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 64 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月24日 17:00 </td>
			<td style="text-align: center;"> 1.123 </td>
			<td style="text-align: center;"> 94.2 </td>
			<td style="text-align: center; width: 71px;"> 69 </td>
			<td style="text-align: center; width: 76px;"> 0.269 </td>
			<td style="text-align: center;"> 98.63 </td>
			<td style="text-align: center;"> 73 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月24日 18:00 </td>
			<td style="text-align: center;"> 1.211 </td>
			<td style="text-align: center;"> 92.31 </td>
			<td style="text-align: center; width: 71px;"> 52 </td>
			<td style="text-align: center; width: 76px;"> 0.247 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 52 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月24日 19:00 </td>
			<td style="text-align: center;"> 1.495 </td>
			<td style="text-align: center;"> 95.95 </td>
			<td style="text-align: center; width: 71px;"> 74 </td>
			<td style="text-align: center; width: 76px;"> 0.239 </td>
			<td style="text-align: center;"> 98.65 </td>
			<td style="text-align: center;"> 74 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月24日 20:00 </td>
			<td style="text-align: center;"> 1.568 </td>
			<td style="text-align: center;"> 93.65 </td>
			<td style="text-align: center; width: 71px;"> 63 </td>
			<td style="text-align: center; width: 76px;"> 0.357 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 65 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月24日 21:00 </td>
			<td style="text-align: center;"> 1.421 </td>
			<td style="text-align: center;"> 91.23 </td>
			<td style="text-align: center; width: 71px;"> 57 </td>
			<td style="text-align: center; width: 76px;"> 0.308 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 60 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月24日 22:00 </td>
			<td style="text-align: center;"> 1.255 </td>
			<td style="text-align: center;"> 94.23 </td>
			<td style="text-align: center; width: 71px;"> 52 </td>
			<td style="text-align: center; width: 76px;"> 0.256 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 54 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月24日 23:00 </td>
			<td style="text-align: center;"> 1.206 </td>
			<td style="text-align: center;"> 96.83 </td>
			<td style="text-align: center; width: 71px;"> 63 </td>
			<td style="text-align: center; width: 76px;"> 0.241 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 64 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月25日 00:00 </td>
			<td style="text-align: center;"> 1.242 </td>
			<td style="text-align: center;"> 92.59 </td>
			<td style="text-align: center; width: 71px;"> 54 </td>
			<td style="text-align: center; width: 76px;"> 0.397 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 53 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月25日 01:00 </td>
			<td style="text-align: center;"> 1.309 </td>
			<td style="text-align: center;"> 98.53 </td>
			<td style="text-align: center; width: 71px;"> 68 </td>
			<td style="text-align: center; width: 76px;"> 0.271 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 71 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月25日 02:00 </td>
			<td style="text-align: center;"> 1.015 </td>
			<td style="text-align: center;"> 97.37 </td>
			<td style="text-align: center; width: 71px;"> 76 </td>
			<td style="text-align: center; width: 76px;"> 0.253 </td>
			<td style="text-align: center;"> 98.68 </td>
			<td style="text-align: center;"> 76 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月25日 03:00 </td>
			<td style="text-align: center;"> 1.154 </td>
			<td style="text-align: center;"> 96.92 </td>
			<td style="text-align: center; width: 71px;"> 65 </td>
			<td style="text-align: center; width: 76px;"> 0.363 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 66 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月25日 04:00 </td>
			<td style="text-align: center;"> 1.181 </td>
			<td style="text-align: center;"> 98.33 </td>
			<td style="text-align: center; width: 71px;"> 60 </td>
			<td style="text-align: center; width: 76px;"> 0.225 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 63 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月25日 05:00 </td>
			<td style="text-align: center;"> 1.185 </td>
			<td style="text-align: center;"> 98.31 </td>
			<td style="text-align: center; width: 71px;"> 59 </td>
			<td style="text-align: center; width: 76px;"> 0.209 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 59 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月25日 06:00 </td>
			<td style="text-align: center;"> 1.131 </td>
			<td style="text-align: center;"> 96.97 </td>
			<td style="text-align: center; width: 71px;"> 66 </td>
			<td style="text-align: center; width: 76px;"> 0.265 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 67 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月25日 07:00 </td>
			<td style="text-align: center;"> 1.211 </td>
			<td style="text-align: center;"> 94.83 </td>
			<td style="text-align: center; width: 71px;"> 58 </td>
			<td style="text-align: center; width: 76px;"> 0.212 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 62 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月25日 08:00 </td>
			<td style="text-align: center;"> 1.127 </td>
			<td style="text-align: center;"> 93.44 </td>
			<td style="text-align: center; width: 71px;"> 61 </td>
			<td style="text-align: center; width: 76px;"> 0.313 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 62 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月25日 09:00 </td>
			<td style="text-align: center;"> 1.224 </td>
			<td style="text-align: center;"> 96.15 </td>
			<td style="text-align: center; width: 71px;"> 52 </td>
			<td style="text-align: center; width: 76px;"> 0.421 </td>
			<td style="text-align: center;"> 98.18 </td>
			<td style="text-align: center;"> 55 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 2015年12月25日 10:00 </td>
			<td style="text-align: center;"> 1.295 </td>
			<td style="text-align: center;"> 98.39 </td>
			<td style="text-align: center; width: 71px;"> 62 </td>
			<td style="text-align: center; width: 76px;"> 0.314 </td>
			<td style="text-align: center;"> 100 </td>
			<td style="text-align: center;"> 65 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 平均/汇总 </td>
			<td style="text-align: center;"> 1.271 </td>
			<td style="text-align: center;"> 95.48 </td>
			<td style="text-align: center; width: 71px;"> 1173 </td>
			<td style="text-align: center; width: 76px;"> 0.291 </td>
			<td style="text-align: center;"> 99.67 </td>
			<td style="text-align: center;"> 1205 </td>
		</tr>
		<tr>
			<td style="text-align: center;"> 排除点数 </td>
			<td colspan="3" style="text-align: center; width: 232px;"> 0 </td>
			<td colspan="3" style="text-align: center; width: 240px;"> 0 </td>
		</tr>
	</tbody>
</table>
