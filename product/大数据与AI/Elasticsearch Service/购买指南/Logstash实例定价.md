Logstash 实例目前支持包年包月和按量计费两种计费模式：
- 包年包月实例部署方案：实例的全部节点计费模式均为 [包年包月（预付费）](https://cloud.tencent.com/document/product/555/9618)，适用于长期存在且计算量稳定的实例。
- 按量计费实例部署方案：实例的全部节点计费模式均为 [按量计费](https://cloud.tencent.com/document/product/555/9617)，适用于短时间存在或周期性存在的实例。

Logstash 实例的计费项包括节点机型和节点存储两部分，实例收取的费用由全部节点构成。

## 节点机型价格
### 节点机型
Logstash 实例支持以下节点类型：

<table>
  <tr>
    <th width="15%">类型</th>
    <th width="15%">子类型</th>
    <th width="70%">描述</th>
  </tr>
	<tr>
	<td rowspan="2">标准型实例族</td>
	<td><a href="#step2">标准型 S1</a></td>
	<td rowspan="2">提供均衡的计算、内存和网络资源，可满足大多数场景下的应用资源需求</td>
	</tr>
	<tr>
	<td><a href="#step1">标准型 SA2</a></td>
	</tr>
 <tr>
</table>

[](id:step1)

### 标准型 SA2 定价

#### 包年包月

<table class="tg">
  <tr>
    <th class="tg-llyw" rowspan="2">节点机型</th>
		<th class="tg-llyw" rowspan="2">节点规格</th>
    <th class="tg-llyw" rowspan="2">CPU</th>
    <th class="tg-llyw" rowspan="2">内存（GB）</th>
    <th class="tg-llyw" rowspan="2">适用场景</th>
    <th class="tg-llyw" colspan="26">预付费（元/个/月）</th>
  </tr>
  <tr>
    <td class="tg-llyw" colspan="1">北京/上海/广州/南京</td>
    <td class="tg-llyw" colspan="1">成都/重庆</td>
  </tr>
	<tr>
    <td class="tg-0pky"  rowspan="12">标准型 SA2 </td>
    <td class="tg-0pky">LOGSTASH.S1.MEDIUM4</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">生产</td>
   	<td class="tg-0pky">140.8</td>
    <td class="tg-0pky">126.6</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.MEDIUM8</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">211.2</td>
    <td class="tg-0pky">189.8</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.LARGE16</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">422.4</td>
    <td class="tg-0pky">379.6</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.2XLARGE16</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">563.2</td>
    <td class="tg-0pky">506.4</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.2XLARGE32</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">844.8</td>
    <td class="tg-0pky">759.2</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.4XLARGE32</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">1126.4</td>
    <td class="tg-0pky">1012.8</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.4XLARGE64</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">64</td>
    <td class="tg-0pky">生产</td>
			<td class="tg-0pky">1689.6</td>
    <td class="tg-0pky">1518.4</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.6XLARGE48</td>
    <td class="tg-0pky">24</td>
    <td class="tg-0pky">48</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">1689.6</td>
    <td class="tg-0pky">1519.2</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.6XLARGE96</td>
    <td class="tg-0pky">24</td>
    <td class="tg-0pky">96</td>
    <td class="tg-0pky">生产</td>
			<td class="tg-0pky">2534.4</td>
    <td class="tg-0pky">2277.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.8XLARGE64</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">64</td>
    <td class="tg-0pky">生产</td>
			<td class="tg-0pky">2252.8</td>
    <td class="tg-0pky">2025.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.8XLARGE128</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">128</td>
    <td class="tg-0pky">生产</td>
			<td class="tg-0pky">3379.2</td>
    <td class="tg-0pky">3036.8</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.8XLARGE128</td>
    <td class="tg-0pky">48</td>
    <td class="tg-0pky">96</td>
    <td class="tg-0pky">生产</td>
			<td class="tg-0pky">3379.2</td>
    <td class="tg-0pky">3038.4</td>
  </tr> 
</table>




#### 按量计费

<table class="tg">
  <tr>
    <th class="tg-llyw" rowspan="2">节点机型</th>
		<th class="tg-llyw" rowspan="2">节点规格</th>
    <th class="tg-llyw" rowspan="2">CPU</th>
    <th class="tg-llyw" rowspan="2">内存（GB）</th>
    <th class="tg-llyw" rowspan="2">适用场景</th>
    <th class="tg-llyw" colspan="26">后付费（元/个/小时）</th>
  </tr>
  <tr>
    <td class="tg-llyw" colspan="1">北京/上海/广州/南京</td>
    <td class="tg-llyw" colspan="1">成都/重庆</td>
  </tr>
	<tr>
    <td class="tg-0pky"  rowspan="12">标准型 SA2 </td>
    <td class="tg-0pky">LOGSTASH.S1.MEDIUM4</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">生产</td>
   	<td class="tg-0pky">0.29</td>
    <td class="tg-0pky">0.26</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.MEDIUM8</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">0.43</td>
    <td class="tg-0pky">0.39</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.LARGE16</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">0.86</td>
    <td class="tg-0pky">0.77</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.2XLARGE16</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">1.14</td>
    <td class="tg-0pky">1.03</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.2XLARGE32</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">1.72</td>
    <td class="tg-0pky">1.55</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.4XLARGE32</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">2.29</td>
    <td class="tg-0pky">2.06</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.4XLARGE64</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">64</td>
    <td class="tg-0pky">生产</td>
			<td class="tg-0pky">3.43</td>
    <td class="tg-0pky">3.09</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.6XLARGE48</td>
    <td class="tg-0pky">24</td>
    <td class="tg-0pky">48</td>
    <td class="tg-0pky">生产</td>
		<td class="tg-0pky">3.43</td>
    <td class="tg-0pky">3.09</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.6XLARGE96</td>
    <td class="tg-0pky">24</td>
    <td class="tg-0pky">96</td>
    <td class="tg-0pky">生产</td>
			<td class="tg-0pky">5.15</td>
    <td class="tg-0pky">4.64</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.8XLARGE64</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">64</td>
    <td class="tg-0pky">生产</td>
			<td class="tg-0pky">4.58</td>
    <td class="tg-0pky">4.12</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.8XLARGE128</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">128</td>
    <td class="tg-0pky">生产</td>
			<td class="tg-0pky">6.87</td>
    <td class="tg-0pky">6.18</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.8XLARGE128</td>
    <td class="tg-0pky">48</td>
    <td class="tg-0pky">96</td>
    <td class="tg-0pky">生产</td>
			<td class="tg-0pky">6.87</td>
    <td class="tg-0pky">6.18</td>
  </tr> 
</table>


[](id:step2)

### 标准型 S1 定价

#### 包年包月

<table class="tg">
  <tr>
	  <th class="tg-llyw" rowspan="2">节点机型</th>
    <th class="tg-llyw" rowspan="2">节点规格</th>
    <th class="tg-llyw" rowspan="2">CPU</th>
    <th class="tg-llyw" rowspan="2">内存（GB）</th>
    <th class="tg-llyw" rowspan="2">适用场景</th>
    <th class="tg-llyw" colspan="14">预付费（元/个/月）</th>
  </tr>
  <tr>
    <td class="tg-llyw" colspan="1">北京/上海/广州/南京</td>
    <td class="tg-llyw" colspan="1">成都/重庆</td>
		<td class="tg-llyw" colspan="1">北京/上海/深圳金融</td>
    <td class="tg-llyw" colspan="1">中国香港</td>
    <td class="tg-llyw" colspan="1">新加坡</td>
    <td class="tg-llyw" colspan="1">泰国</td>
		<td class="tg-llyw" colspan="1">孟买</td>
		<td class="tg-llyw" colspan="1">首尔</td>
		<td class="tg-llyw" colspan="1">日本</td>
    <td class="tg-llyw" colspan="1">美国硅谷</td>
		<td class="tg-llyw" colspan="1">弗吉尼亚</td>
    <td class="tg-llyw" colspan="1">多伦多</td>
		<td class="tg-llyw" colspan="1">法兰克福</td>
		<td class="tg-llyw" colspan="1">俄罗斯</td>  
  </tr>
  <tr>
    <td class="tg-0pky"  rowspan="14">标准型 S1</td>
    <td class="tg-0pky">LOGSTASH.S1.MEDIUM4</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">198.2</td>
    <td class="tg-0pky">180</td>
    <td class="tg-0pky">316.8</td>
    <td class="tg-0pky">272.8</td>
    <td class="tg-0pky">272.8</td>
    <td class="tg-0pky">264</td>
    <td class="tg-0pky">228.8</td>
    <td class="tg-0pky">308</td>
    <td class="tg-0pky">308</td>
    <td class="tg-0pky">290.4</td>
    <td class="tg-0pky">226.6</td>
    <td class="tg-0pky">226.6</td>
		<td class="tg-0pky">308</td>
		<td class="tg-0pky">290.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.MEDIUM8</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">297.4</td>
    <td class="tg-0pky">270</td>
    <td class="tg-0pky">475.2</td>
    <td class="tg-0pky">409.2</td>
    <td class="tg-0pky">409.2</td>
    <td class="tg-0pky">396</td>
    <td class="tg-0pky">343.2</td>
    <td class="tg-0pky">462</td>
    <td class="tg-0pky">462</td>
    <td class="tg-0pky">435.6</td>
    <td class="tg-0pky">339.8</td>
    <td class="tg-0pky">339.8</td>
		<td class="tg-0pky">462</td>
		<td class="tg-0pky">435.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.LARGE16</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">594.8</td>
    <td class="tg-0pky">540</td>
    <td class="tg-0pky">950.4</td>
    <td class="tg-0pky">818.4</td>
    <td class="tg-0pky">818.4</td>
    <td class="tg-0pky">792</td>
    <td class="tg-0pky">686.4</td>
    <td class="tg-0pky">924</td>
    <td class="tg-0pky">924</td>
    <td class="tg-0pky">871.2</td>
    <td class="tg-0pky">679.6</td>
    <td class="tg-0pky">679.6</td>
		<td class="tg-0pky">924</td>
		<td class="tg-0pky">871.2</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.2XLARGE16</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">792.8</td>
    <td class="tg-0pky">720</td>
    <td class="tg-0pky">1267.2</td>
    <td class="tg-0pky">1091.2</td>
    <td class="tg-0pky">1091.2</td>
    <td class="tg-0pky">1056</td>
    <td class="tg-0pky">915.2</td>
    <td class="tg-0pky">1232</td>
    <td class="tg-0pky">1232</td>
    <td class="tg-0pky">1161.6</td>
    <td class="tg-0pky">906.4</td>
    <td class="tg-0pky">906.4</td>
		<td class="tg-0pky">1232</td>
		<td class="tg-0pky">1161.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.2XLARGE32</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">1189.6</td>
    <td class="tg-0pky">1080</td>
    <td class="tg-0pky">1900.8</td>
    <td class="tg-0pky">1636.8</td>
    <td class="tg-0pky">1636.8</td>
    <td class="tg-0pky">1584</td>
    <td class="tg-0pky">1372.8</td>
    <td class="tg-0pky">1848</td>
    <td class="tg-0pky">1848</td>
    <td class="tg-0pky">1742.4</td>
    <td class="tg-0pky">1359.2</td>
    <td class="tg-0pky">1359.2</td>
		<td class="tg-0pky">1848</td>
		<td class="tg-0pky">1742.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.4XLARGE32</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">1585.6</td>
    <td class="tg-0pky">1440</td>
    <td class="tg-0pky">2534.4</td>
    <td class="tg-0pky">2182.4</td>
    <td class="tg-0pky">2182.4</td>
    <td class="tg-0pky">2112</td>
    <td class="tg-0pky">1830.4</td>
    <td class="tg-0pky">2464</td>
    <td class="tg-0pky">2464</td>
    <td class="tg-0pky">2323.2</td>
    <td class="tg-0pky">1812.8</td>
    <td class="tg-0pky">1812.8</td>
		<td class="tg-0pky">2464</td>
		<td class="tg-0pky">2323.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.4XLARGE64</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">64</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">2379.2</td>
    <td class="tg-0pky">2160</td>
    <td class="tg-0pky">3801.6</td>
    <td class="tg-0pky">3273.6</td>
    <td class="tg-0pky">3273.6</td>
    <td class="tg-0pky">3168</td>
    <td class="tg-0pky">2745.6</td>
    <td class="tg-0pky">3696</td>
    <td class="tg-0pky">3696</td>
    <td class="tg-0pky">3484.8</td>
    <td class="tg-0pky">2718.4</td>
    <td class="tg-0pky">2718.4</td>
		<td class="tg-0pky">3696</td>
		<td class="tg-0pky">3484.8</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.6XLARGE48</td>
    <td class="tg-0pky">24</td>
    <td class="tg-0pky">48</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">2378.4</td>
    <td class="tg-0pky">2160</td>
    <td class="tg-0pky">3801.6</td>
    <td class="tg-0pky">3273.6</td>
    <td class="tg-0pky">3273.6</td>
    <td class="tg-0pky">3168</td>
    <td class="tg-0pky">2745.6</td>
    <td class="tg-0pky">3696</td>
    <td class="tg-0pky">3696</td>
    <td class="tg-0pky">3484.8</td>
    <td class="tg-0pky">2719.2</td>
    <td class="tg-0pky">2719.2</td>
		<td class="tg-0pky">3696</td>
		<td class="tg-0pky">3484.8</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.6XLARGE96</td>
    <td class="tg-0pky">24</td>
    <td class="tg-0pky">96</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">3568.8</td>
    <td class="tg-0pky">3240</td>
    <td class="tg-0pky">5702.4</td>
    <td class="tg-0pky">4910.4</td>
    <td class="tg-0pky">4910.4</td>
    <td class="tg-0pky">4752</td>
    <td class="tg-0pky">4118.4</td>
    <td class="tg-0pky">5544</td>
    <td class="tg-0pky">5544</td>
    <td class="tg-0pky">5227.2</td>
    <td class="tg-0pky">4077.6</td>
    <td class="tg-0pky">4077.6</td>
		<td class="tg-0pky">5544</td>
		<td class="tg-0pky">5227.2</td>
  </tr>
		<tr>
    <td class="tg-0pky">LOGSTASH.S1.8XLARGE64</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">64</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">3171.2</td>
    <td class="tg-0pky">2880</td>
    <td class="tg-0pky">5068.8</td>
    <td class="tg-0pky">4364.8</td>
    <td class="tg-0pky">4364.8</td>
    <td class="tg-0pky">4224</td>
    <td class="tg-0pky">3660.8</td>
    <td class="tg-0pky">4928</td>
    <td class="tg-0pky">4928</td>
    <td class="tg-0pky">4646.4</td>
    <td class="tg-0pky">3625.6</td>
    <td class="tg-0pky">3625.6</td>
		<td class="tg-0pky">4928</td>
		<td class="tg-0pky">4646.4</td>
  </tr>
			<tr>
    <td class="tg-0pky">LOGSTASH.S1.8XLARGE128</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">128</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">4758.4</td>
    <td class="tg-0pky">4320</td>
    <td class="tg-0pky">7603.2</td>
    <td class="tg-0pky">6547.2</td>
    <td class="tg-0pky">6547.2</td>
    <td class="tg-0pky">6336</td>
    <td class="tg-0pky">5491.2</td>
    <td class="tg-0pky">7392</td>
    <td class="tg-0pky">7392</td>
    <td class="tg-0pky">6969.6</td>
    <td class="tg-0pky">5436.8</td>
    <td class="tg-0pky">5436.8</td>
		<td class="tg-0pky">7392</td>
		<td class="tg-0pky">6969.6</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.12XLARGE96</td>
    <td class="tg-0pky">48</td>
    <td class="tg-0pky">96</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">4756.8</td>
    <td class="tg-0pky">4320</td>
    <td class="tg-0pky">7603.2</td>
    <td class="tg-0pky">6547.2</td>
    <td class="tg-0pky">6547.2</td>
    <td class="tg-0pky">6336</td>
    <td class="tg-0pky">5491.2</td>
    <td class="tg-0pky">7392</td>
    <td class="tg-0pky">7392</td>
    <td class="tg-0pky">6969.6</td>
    <td class="tg-0pky">5438.4</td>
    <td class="tg-0pky">5438.4</td>
		<td class="tg-0pky">7392</td>
		<td class="tg-0pky">6969.6</td>
  </tr>
</table>




#### 按量计费

<table class="tg">
  <tr>
	  <th class="tg-llyw" rowspan="2">节点机型</th>
    <th class="tg-llyw" rowspan="2">节点规格</th>
    <th class="tg-llyw" rowspan="2">CPU</th>
    <th class="tg-llyw" rowspan="2">内存（GB）</th>
    <th class="tg-llyw" rowspan="2">适用场景</th>
    <th class="tg-llyw" colspan="14">后付费（元/个/小时）</th>
  </tr>
  <tr>
    <td class="tg-llyw" colspan="1">北京/上海/广州/南京</td>
    <td class="tg-llyw" colspan="1">成都/重庆</td>
		<td class="tg-llyw" colspan="1">北京/上海/深圳金融</td>
    <td class="tg-llyw" colspan="1">中国香港</td>
    <td class="tg-llyw" colspan="1">新加坡</td>
    <td class="tg-llyw" colspan="1">泰国</td>
		<td class="tg-llyw" colspan="1">孟买</td>
		<td class="tg-llyw" colspan="1">首尔</td>
		<td class="tg-llyw" colspan="1">日本</td>
    <td class="tg-llyw" colspan="1">美国硅谷</td>
		<td class="tg-llyw" colspan="1">弗吉尼亚</td>
    <td class="tg-llyw" colspan="1">多伦多</td>
		<td class="tg-llyw" colspan="1">法兰克福</td>
		<td class="tg-llyw" colspan="1">俄罗斯</td>  
  </tr>
  <tr>
    <td class="tg-0pky"  rowspan="14">标准型 S1</td>
    <td class="tg-0pky">LOGSTASH.S1.MEDIUM4</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">0.72</td>
    <td class="tg-0pky">0.65</td>
    <td class="tg-0pky">1.15</td>
    <td class="tg-0pky">0.55</td>
    <td class="tg-0pky">0.65</td>
    <td class="tg-0pky">0.54</td>
    <td class="tg-0pky">0.46</td>
    <td class="tg-0pky">0.63</td>
    <td class="tg-0pky">0.63</td>
    <td class="tg-0pky">0.59</td>
    <td class="tg-0pky">0.46</td>
    <td class="tg-0pky">0.46</td>
		<td class="tg-0pky">0.63</td>
		<td class="tg-0pky">0.59</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.MEDIUM8</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">1.08</td>
    <td class="tg-0pky">0.98</td>
    <td class="tg-0pky">1.73</td>
    <td class="tg-0pky">0.83</td>
    <td class="tg-0pky">0.97</td>
    <td class="tg-0pky">0.8</td>
    <td class="tg-0pky">0.69</td>
    <td class="tg-0pky">0.94</td>
    <td class="tg-0pky">0.94</td>
    <td class="tg-0pky">0.88</td>
    <td class="tg-0pky">0.69</td>
    <td class="tg-0pky">0.69</td>
		<td class="tg-0pky">0.94</td>
		<td class="tg-0pky">0.88</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.LARGE16</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">2.15</td>
    <td class="tg-0pky">1.96</td>
    <td class="tg-0pky">3.45</td>
    <td class="tg-0pky">1.66</td>
    <td class="tg-0pky">1.95</td>
    <td class="tg-0pky">1.61</td>
    <td class="tg-0pky">1.38</td>
    <td class="tg-0pky">1.88</td>
    <td class="tg-0pky">1.88</td>
    <td class="tg-0pky">1.77</td>
    <td class="tg-0pky">1.38</td>
    <td class="tg-0pky">1.38</td>
		<td class="tg-0pky">1.88</td>
		<td class="tg-0pky">1.77</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.2XLARGE16</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">2.87</td>
    <td class="tg-0pky">2.61</td>
    <td class="tg-0pky">4.6</td>
    <td class="tg-0pky">2.22</td>
    <td class="tg-0pky">2.6</td>
    <td class="tg-0pky">2.14</td>
    <td class="tg-0pky">1.84</td>
    <td class="tg-0pky">2.5</td>
    <td class="tg-0pky">2.5</td>
    <td class="tg-0pky">2.36</td>
    <td class="tg-0pky">1.84</td>
    <td class="tg-0pky">1.84</td>
		<td class="tg-0pky">2.5</td>
		<td class="tg-0pky">2.36</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.2XLARGE32</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">4.31</td>
    <td class="tg-0pky">3.92</td>
    <td class="tg-0pky">6.9</td>
    <td class="tg-0pky">3.32</td>
    <td class="tg-0pky">3.9</td>
    <td class="tg-0pky">3.21</td>
    <td class="tg-0pky">2.76</td>
    <td class="tg-0pky">3.75</td>
    <td class="tg-0pky">3.75</td>
    <td class="tg-0pky">3.53</td>
    <td class="tg-0pky">2.76</td>
    <td class="tg-0pky">2.76</td>
		<td class="tg-0pky">3.75</td>
		<td class="tg-0pky">3.53</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.4XLARGE32</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">5.74</td>
    <td class="tg-0pky">5.23</td>
    <td class="tg-0pky">9.2</td>
    <td class="tg-0pky">4.43</td>
    <td class="tg-0pky">5.21</td>
    <td class="tg-0pky">4.29</td>
    <td class="tg-0pky">3.68</td>
    <td class="tg-0pky">5</td>
    <td class="tg-0pky">5</td>
    <td class="tg-0pky">4.71</td>
    <td class="tg-0pky">3.68</td>
    <td class="tg-0pky">3.68</td>
		<td class="tg-0pky">5</td>
		<td class="tg-0pky">4.71</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOGSTASH.S1.4XLARGE64</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">64</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">8.61</td>
    <td class="tg-0pky">7.84</td>
    <td class="tg-0pky">13.8</td>
    <td class="tg-0pky">6.64</td>
    <td class="tg-0pky">7.8</td>
    <td class="tg-0pky">6.42</td>
    <td class="tg-0pky">5.52</td>
    <td class="tg-0pky">7.51</td>
    <td class="tg-0pky">7.51</td>
    <td class="tg-0pky">7.07</td>
    <td class="tg-0pky">5.52</td>
    <td class="tg-0pky">5.52</td>
		<td class="tg-0pky">7.51</td>
		<td class="tg-0pky">7.07</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.6XLARGE48</td>
    <td class="tg-0pky">24</td>
    <td class="tg-0pky">48</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">8.61</td>
    <td class="tg-0pky">7.84</td>
    <td class="tg-0pky">13.8</td>
    <td class="tg-0pky">6.65</td>
    <td class="tg-0pky">7.81</td>
    <td class="tg-0pky">6.43</td>
    <td class="tg-0pky">5.52</td>
    <td class="tg-0pky">7.51</td>
    <td class="tg-0pky">7.51</td>
    <td class="tg-0pky">7.07</td>
    <td class="tg-0pky">5.52</td>
    <td class="tg-0pky">5.52</td>
		<td class="tg-0pky">7.51</td>
		<td class="tg-0pky">7.07</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.6XLARGE96</td>
    <td class="tg-0pky">24</td>
    <td class="tg-0pky">96</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">12.92</td>
    <td class="tg-0pky">11.76</td>
    <td class="tg-0pky">20.7</td>
    <td class="tg-0pky">9.96</td>
    <td class="tg-0pky">11.7</td>
    <td class="tg-0pky">9.63</td>
    <td class="tg-0pky">8.28</td>
    <td class="tg-0pky">11.26</td>
    <td class="tg-0pky">11.26</td>
    <td class="tg-0pky">10.6</td>
    <td class="tg-0pky">8.28</td>
    <td class="tg-0pky">8.28</td>
		<td class="tg-0pky">11.26</td>
		<td class="tg-0pky">10.6</td>
  </tr>
		<tr>
    <td class="tg-0pky">LOGSTASH.S1.8XLARGE64</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">64</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">11.48</td>
    <td class="tg-0pky">10.45</td>
    <td class="tg-0pky">18.4</td>
    <td class="tg-0pky">8.87</td>
    <td class="tg-0pky">10.41</td>
    <td class="tg-0pky">8.57</td>
    <td class="tg-0pky">7.36</td>
    <td class="tg-0pky">10.01</td>
    <td class="tg-0pky">10.01</td>
    <td class="tg-0pky">9.42</td>
    <td class="tg-0pky">7.36</td>
    <td class="tg-0pky">7.36</td>
		<td class="tg-0pky">10.01</td>
		<td class="tg-0pky">9.42</td>
  </tr>
			<tr>
    <td class="tg-0pky">LOGSTASH.S1.8XLARGE128</td>
    <td class="tg-0pky">32</td>
    <td class="tg-0pky">128</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">17.22</td>
    <td class="tg-0pky">15.68</td>
    <td class="tg-0pky">27.6</td>
    <td class="tg-0pky">13.28</td>
    <td class="tg-0pky">15.6</td>
    <td class="tg-0pky">12.84</td>
    <td class="tg-0pky">11.04</td>
    <td class="tg-0pky">15.01</td>
    <td class="tg-0pky">15.01</td>
    <td class="tg-0pky">14.13</td>
    <td class="tg-0pky">11.04</td>
    <td class="tg-0pky">11.04</td>
		<td class="tg-0pky">15.01</td>
		<td class="tg-0pky">14.13</td>
  </tr>
	<tr>
    <td class="tg-0pky">LOGSTASH.S1.12XLARGE96</td>
    <td class="tg-0pky">48</td>
    <td class="tg-0pky">96</td>
    <td class="tg-0pky">生产</td>
    <td class="tg-0pky">17.22</td>
    <td class="tg-0pky">15.68</td>
    <td class="tg-0pky">27.6</td>
    <td class="tg-0pky">13.3</td>
    <td class="tg-0pky">15.62</td>
    <td class="tg-0pky">12.86</td>
    <td class="tg-0pky">11.04</td>
    <td class="tg-0pky">15.01</td>
    <td class="tg-0pky">15.01</td>
    <td class="tg-0pky">14.13</td>
    <td class="tg-0pky">11.04</td>
    <td class="tg-0pky">11.04</td>
		<td class="tg-0pky">15.01</td>
		<td class="tg-0pky">14.13</td>
  </tr>
</table>





## 节点存储价格

北京、上海、广州地域费用如下：

| 磁盘类型   | 预付费（元/GB/月） | 后付费（元/GB/小时） |
| ---------- | ------------------ | -------------------- |
| SSD 云盘   | 1                  | 0.0025               |
| 高性能云盘 | 0.35               | 0.0009               |

其他地域请参考 [云硬盘价格总览](https://cloud.tencent.com/document/product/362/2413)。

## 费用计算示例 
以下用两个示例来说明两种计费模式下的计费构成。

### 包年包月模式费用计算
>?服务器实例的价格随时间变动，下文中的数值仅作参考，具体价格可查看 Logstash [购买页](https://buy.cloud.tencent.com/logstash)。
>
用户在广州二区，购买了一个 Logstash 实例，包含2个节点，每个节点规格是2核4G（LOGSTASH.S1.MEDIUM4），每个节点存储量20G，采用SSD 云盘，购买时长是1个月，用户所需支付的费用计算如下：
- 节点2核4G（ES.S1.MEDIUM4）：198.2 元/个/月
- SSD 云盘20G：1 元/GB/月 × 20 = 20 元/个/月
- 节点个数：2 个

总的费用为：（198.2 + 20）× 2 = 436.4 元/月

### 按量付费模式费用计算
>?服务器实例的价格随时间变动，下文中的数值仅作参考，具体价格可查看 Logstash [购买页](https://buy.cloud.tencent.com/logstash)。
>
用户在广州二区，购买了一个 Logstash 实例，包含2个节点，每个节点规格是2核4G（LOGSTASH.S1.MEDIUM4），每个节点存储量20G，采用SSD 云盘，购买时长是5小时，用户所需支付的费用计算如下：

- 节点2核4G（ES.S1.MEDIUM4）：0.72 元/个/小时
- SSD 云盘20G：0.0025 元/GB/小时 × 20 = 0.05 元/个/小时
- 节点个数：2个
- 购买时长：5小时

总的费用为：（0.72 + 0.05）× 2 × 5 = 7.7 元
