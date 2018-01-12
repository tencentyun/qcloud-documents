以下费用实例以中国大陆地区使用为准。
## 案例 1：微信应用和移动端 APP
#### 背景
小明开发了一款汽车服务类应用，可以通过微信和手机 APP 预约汽车服务。小明需要一个空间来存储用户上传的行驶证信息等用于审核，还需要保存本地汽车服务商户的门店照片和用户评价上传照片等。
#### 要求
每月图片总共大约占 100 GB 空间，产生浏览流量 100 GB，预计月读和写请求总计不超过 100 万次。为此，小明将应用服务托管在云服务器 CVM 上，使用对象存储服务 COS 存储图片，并结合 CDN 加速服务使用。
#### 分析
<table>
   <tr>
        <th colspan="2">费用组成</th> 
        <th>具体计算</th>
	<th>费用（元）</th>
   </tr>
   <tr>
        <td colspan="2">存储空间费用</td> 
        <td>(100 GB - 50 GB) × 0.13</td> 
	<td>6.5</td> 
   </tr>
   <tr>
        <td rowspan="3">流量费用</td>
   </tr>
   <tr>
	<td>外网下行</td>
        <td>0</td> 
        <td>0</td>
   </tr>
   <tr>
	<td>CDN 回源</td>
        <td>(100 GB -10 GB) × 0.15</td> 
	<td>13.5</td>
   </tr>
   <tr>
        <td colspan="2">请求费用</td>    
  <td>0</td> 
	<td>0</td>
    </tr>
   <tr>
        <td colspan="2">总计</td>  
	<td>/</td> 
	<td>20</td>
   </tr>
</table>

> **说明：**
**[免费额度](https://cloud.tencent.com/document/product/436/6240)：10 GB CDN 回源流量，100 万次读/写请求。**

**此案例中，小明每月预计需要支付对象存储费用 20 元。**

## 案例 2：网站和论坛
#### 背景
小明运营着一个网站，网站常发布图片、音频、视频并茂的文章，同时还有软件下载区等。
#### 要求
每月文件大小约 1.5 TB，产生流量 500 GB，月 PV 大约 200 万，预计有 500 万次读请求和 20 万次写请求。为此，小明将应用服务托管在云服务器 CVM 上，使用对象存储服务 COS 存储文件，并结合 CDN 加速服务使用。
#### 分析
<table>
   <tr>
        <th colspan="2">费用组成</th> 
        <th>具体计算</th>
	<th>费用（元）</th>
   </tr>
   <tr>
        <td colspan="2">存储空间费用</td> 
        <td>(1500 GB - 50 GB) × 0.13</td> 
	<td>188.5</td> 
   </tr>
   <tr>
        <td rowspan="3">流量费用</td> 
	</tr>
   <tr>
	<td>外网下行</td>
        <td>0</td> 
        <td>0</td>
   </tr>
   <tr>
	<td>CDN 回源</td>
        <td>(500 GB -10 GB) × 0.15</td> 
	<td>73.5</td>
   </tr>
   <tr>
        <td colspan="2">请求费用</td>     
	<td>(500+20-100)×0.01</td> 
	<td>4.2</td>
    </tr>
    <tr>
        <td colspan="2">总计</td>  
	<td>/</td> 
	<td>266.2</td>
    </tr>
</table>

> **说明：**
 **[免费额度](https://cloud.tencent.com/document/product/436/6240)：10 GB CDN 回源流量，100 万次读/写请求。**
 
**此案例中，小明每月预计需要支付对象存储费用 266.1 元。**

*若您仍存疑惑，欢迎通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 咨询，获得更多技术支持或进行价格商议等。*