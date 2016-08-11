# CDN日志管理
1、腾讯云提供CDN日志管理功能供用户下载日志数据，用户可下载账户最近30天内CDN日志数据情况；
2、日志内容依次包括：
<table  style="width:500px">
	<tbody>
		<tr>
			<th scope="row" style="width: 122px;">顺序</th>
			<td style="width: 365px;">日志内容</td>
		</tr>
		<tr>
			<th scope="row" style="width: 122px;">1</th>
			<td style="width: 365px;">请求时间
		</tr>
		<tr>
		<th scope="row" style="width: 122px;">2</th>
			<td style="width: 365px;">访问域名的客户端IP
		</tr>
		<tr>
		<th scope="row" style="width: 122px;">3</th>
			<td style="width: 365px;">被访问域名
		</tr>
		<tr>
		<th scope="row" style="width: 122px;">4</th>
			<td style="width: 365px;">文件请求路径
		</tr>
		<tr>
		<th scope="row" style="width: 122px;">5</th>
			<td style="width: 365px;">本次访问字节数大小
		</tr>
		<tr>
		<th scope="row" style="width: 122px;">6</th>
			<td style="width: 365px;">省份
		</tr>
		<tr>
		<th scope="row" style="width: 122px;">7</th>
			<td style="width: 365px;">运营商
		</tr>
		<tr>
		<th scope="row" style="width: 122px;">8</th>
			<td style="width: 365px;">http返回码
		</tr>
		<tr>
		<th scope="row" style="width: 122px;">9</th>
			<td style="width: 365px;">referer信息
		</tr>
		<tr>
		<th scope="row" style="width: 122px;">10</th>
			<td style="width: 365px;">响应时间(毫秒)
		</tr>
		<tr>
		<th scope="row" style="width: 122px;">11</th>
			<td style="width: 365px;">User-Agent
		</tr>
		<tr>
		<th scope="row" style="width: 122px;">12</th>
			<td style="width: 365px;">range参数
		</tr>
	</tbody>
</table>

**注意：**
1、当日数据会有延时，不建议参考当日日志数据；
2、日志中记录的带宽或流量是应用层（HTTP协议）回包的大小统计而得，会比由TCP层进行统计得出的结算带宽或流量小，因TCP层有三次握手或丢包重传等机制；

您可在CDN控制台下"高级工具"->“日志管理”，页面中下载日志

![](//mccdn.qcloud.com/static/img/0bfbb2d0c8e2a6932d1854499b0f0e9b/image.png)

**CDN日志地区编码映射表**
1：华北地区、2：西北地区、3：东北地区、4：华东地区、5：华中地区、6：西南地区、7：华南地区、8：其他地区；
**CDN日志省份编码映射表**
22：北京、86：内蒙古、146：山西、1069：河北、1177：天津、119：宁夏、152：陕西、1208：甘肃、1467：青海、1468：新疆、145：黑龙江、1445：吉林,、1464：辽宁、2：福建、120：江苏、121：安徽、122：山东、1050：上海、1442：浙江、182：河南、1135：湖北、1465：江西、1466：湖南、118：贵州、153：云南、1051：重庆、1068：四川、1155：西藏、4：广东、173：广西、1441：海南、0：其他、1：港澳台、-1：海外；
**CDN日志运营商编码映射表**
2：中国电信、26：中国联通、43：长城宽带、1046：中国移动、3947：中国铁通；

