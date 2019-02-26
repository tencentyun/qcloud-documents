目前腾讯云提供共四种硬盘类型：普通本地盘，SSD本地盘，普通云硬盘和SSD云硬盘。

系统盘当前不支持独立售卖。数据盘在购买页时勾选，随主服务器一起购买。系统盘类型跟随数据盘。



## 1. 按量计费
>注意：
>
- 单位为 <font color="red">美元/100GB/小时</font>
- <font color="red">本价格不包含主机硬件（CPU、内存）及网络价格</font>

<table class="diskHour">
        <tbody><tr>
            <th style="width: 5%;">计费项</th>
            <th style="width: 5%;">硬盘类型</th>
						<th style="width: 10%;">单位</th> 
            <th style="width: 20%;">步长</th>
						<th style="width: 20%;">最大可选值</th>
						<th style="width: 20%;">备注</th>
            <th style="width: 30%;">价格</th>
        </tr>
        <tr>
            <td rowspan="4">系统盘</td>
            <td>普通本地盘</td>
						<td rowspan="8"><span style="color:red">美元/100GB/小时</span></td>
            <td rowspan="4">1G</td>
            <td rowspan="4">500G</td>
						<td rowspan="4">-</td>
						<td rowspan="4">-</td>
        </tr>
        <tr>
            <td>SSD本地盘</td>
        </tr>
        <tr>
            <td>普通云硬盘</td>
        </tr>
        <tr>
            <td>SSD云硬盘</td>
        </tr>
				<tr>
            <td rowspan="4">数据盘</td>
            <td>普通本地盘</td>
            <td>10G</td>
						<td>随选择主机CPU核数增加而递增，最高为1000G</td>
            <td>-</td>
            <td>0.042</td>
        </tr>
				<tr>
            <td >SSD本地盘</td>
            <td>10G</td>
            <td>随选择主机CPU核数增加而递增，最高为3000G</td>
            <td>-</td>
						<td>0.33</td>
        </tr>
        <tr>
            <td>普通云硬盘</td>
            <td>10G</td>
            <td>4000G</td>
						<td>-</td>
            <td>0.042</td>
        </tr>
        <tr>
            <td>SSD云硬盘</td>
            <td>250G</td>
            <td>4000G</td>
						<td>-</td>
            <td>0.33</td>
        </tr>
    </tbody></table>
