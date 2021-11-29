
以下展示了 VPC-CNI 各网络模式 Pod 数量默认限制，如不满足需求，可以 [提交工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=350&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1CCS) 调整限制。

## 共享网卡 Pod 数量限制

共享网卡的 Pod 数量受限于节点可绑定的网卡数量和单网卡可绑定的 IP 数量，默认情况下，多网卡的**单节点 PodIP 数量上限 = 最大可绑定辅助网卡数 * 单网卡可绑定辅助 IP 数**，而单网卡的**单节点 PodIP 数量上限 = 单网卡可绑定辅助 IP 数**。默认情况详见下表：
<table style="width:600px;">
<tr>
	<th style="width:30%">CPU 核数</th><th>1</th><th>2-6</th><th>8-10</th><th>>=12</th>
</tr>
<tr>
	<td>最大可绑定辅助弹性网卡</td><td>1</td><td>3</td><td>5</td><td>7</td>
</tr>
<tr>
	<td>单网卡可绑定辅助 IP 数</td><td>5</td><td>9</td><td>19</td><td>29</td>
</tr>
<tr>
	<td>非固定 IP 模式（多网卡）单节点 Pod IP 上限</td><td>5</td><td>27</td><td>95</td><td>203</td>
</tr>
<tr>
	<td>固定 IP 模式（单网卡）单节点 Pod IP 上限</td><td>5</td><td>9</td><td>19</td><td>29</td>
</tr>
</table>

各机型可绑定的网卡数量和单网卡可绑定的 IP 数量略有差异， 详情见 [弹性网卡使用限制](https://cloud.tencent.com/document/product/576/18527)。

## 独占网卡模式 Pod 数量限制

独占网卡的 Pod 数量只受限于节点可绑定的网卡数量，同时只支持 S5、SA2、IT5、SA3 等部分机型，默认情况详见下表：
<table style="width:600px;">
<tr>
<th style ="width:95px;height:45px;position:relative;font-weight:700;" valign="top"><div style="position:absolute;width:1px;height:115px;top:0;left:0;background-color: #d9d9d9;transform:rotate(-60deg);transform-origin:top;"></div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CPU核数<br>机型</th><th>1</th><th>2</th><th>4</th><th>>=8</th><th>>=128</th>
</tr>
<tr>
	<td>S5</td><td>4</td><td>9</td><td>19</td><td>39</td><td>23</td>
</tr>
<tr>
	<td>SA2</td><td>4</td><td>9</td><td>19</td><td>39</td><td>23</td>
</tr>
<tr>
	<td>IT5</td><td>4</td><td>9</td><td>19</td><td>39</td><td>23</td>
</tr>
<tr>
	<td>SA3</td><td>4</td><td>9</td><td>15</td><td>15</td><td>15</td>
</tr>
</table>
