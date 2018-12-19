## 云硬盘 CBS 定价

注意：CBS 定价不包含 CVM 实例价格（CPU,内存)及网络价格。有关 CVM 实例价格和网络价格详情，请参见 [CVM 实例价格](/doc/product/213/2176),[网络价格](/doc/product/213/509)。

### 包年包月

<table class="diskMonth">
        <tbody><tr>
            <th style="width: 5%;">计费项</th>
            <th style="width: 5%;">硬盘类型</th>
						<th style="width: 10%;">单位</th>
            <th style="width: 20%;">步长</th>
						<th style="width: 20%;">最大可选值</th>
						<th style="width: 20%;">备注</th>
            <th style="width: 20%;">价格</th>
        </tr>
        <tr>
            <td rowspan="4">系统盘</td>
            <td>普通本地盘</td>
						<td rowspan="9"><span style="color:red">元/GB/月</span></td>
						<td rowspan="4">-</td>
            <td rowspan="4">-</td>
						<td rowspan="4">免费赠送：Linux8GB，Windows50GB</td>
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
            <td rowspan="5">数据盘</td>
            <td>普通本地盘</td>
            <td>10G</td>
						<td>随选择主机CPU核数增加而递增，最高为1000G</td>
            <td>-</td>
            <td>0.30</td>
        </tr>
				<tr>
            <td >SSD本地盘</td>
            <td>10G</td>
            <td>随选择主机CPU核数增加而递增，最高为3000G</td>
            <td>-</td>
						<td>0.80</td>
        </tr>
        <tr>
            <td>(非弹性)云硬盘</td>
            <td>10G</td>
            <td>4000G</td>
						<td>-</td>
            <td>0.30</td>
        </tr>
				 <tr>
            <td>弹性云硬盘</td>
            <td>10G</td>
            <td>4000G</td>
						<td>-</td>
            <td>0.30</td>
        </tr>
        <tr>
            <td>SSD云硬盘</td>
            <td>250G</td>
            <td>4000G</td>
						<td>-</td>
            <td>1.10</td>
        </tr>
    </tbody></table>

【注意事项】
- 单位为 元/GB/月
- 享受包年送两个月的优惠，即包年价等于相应的月单价乘以10

### 按量计费

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
						<td rowspan="9"><span style="color:red">元/100GB/小时</span></td>
            <td rowspan="4">-</td>
            <td rowspan="4">-</td>
						<td rowspan="4">免费赠送：Linux8GB，Windows50GB</td>
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
            <td rowspan="5">数据盘</td>
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
            <td>(非弹性)云硬盘</td>
            <td>10G</td>
            <td>4000G</td>
						<td>-</td>
            <td>0.042</td>
        </tr>
				<tr>
            <td>弹性云硬盘</td>
            <td>10G</td>
            <td>4000G</td>
						<td>-</td>
            <td>0.042</td>
        </tr>
        <tr>
            <td>SSD云硬盘</td>
            <td>10G</td>
            <td>4000G</td>
						<td>-</td>
            <td>0.33</td>
        </tr>
    </tbody></table>

【注意事项】
- 单位为 元/100GB/小时

## 购买指导

### 弹性云盘

我们提供以下两种方式供您购买云硬盘：

- **通用购买渠道**：
登录[云硬盘控制台](https://console.cloud.tencent.com/cvm/cbs)，点击![](//mccdn.qcloud.com/static/img/acaf7d7ec8c66cd55ab9dd1be3319dfb/image.png)即可开始购买。


- **使用快照快速购买**：
如果您需要在新创建的磁盘中保留数据盘快照数据，则可以选择这种方式。
登录[快照控制台](https://console.cloud.tencent.com/cvm/snapshot)，在您要基于的快照后，点击【新建云硬盘】即可开始购买。
![](//mccdn.qcloud.com/static/img/475d66590b426a60c862b9d20373a552/image.png)
   > 注：新购买的磁盘容量可大于等于快照大小。

### 本地盘

本地盘目前只能通过购买云服务器时附带购买，不支持单独购买。

## 调整硬盘配置

- 对于包年包月和按量计费类型的云服务器，当且仅当其系统盘与数据盘均为<font color="red">云硬盘</font>时，才可对配置进行调整。
- 对云硬盘进行扩容时，若云硬盘未挂载则可直接进行扩容；若云硬盘已经挂载在云服务器上，则需要先对云服务器关机再进行扩容或先卸载该云硬盘、进行扩容后再挂载回原服务器。
- 硬盘扩容后需要您手动修改文件系统配置，把新增部分容量使用起来。
- 考虑到用户的安全性，硬盘容量只可扩容，不可缩。

## 到期提醒

### 包年包月
- 到期预警
包年包月的资源会在到期前7天开始，隔天向您推送到期预警，预警消息将通过邮件及短信的方式通知到腾讯云账户的创建者以及所有协作者。

- 欠费预警
包年包月的资源到期当天及每隔天向您推送欠费隔离预警，预警消息将通过邮件及短信的方式通知到腾讯云账户的创建者以及所有协作者。

### 按量计费
 
 ![](//mccdn.qcloud.com/img567f91951599d.png)
 
- 余额预警

系统每天会根据您名下按量付费资源过去24小时的消费情况以及账户余额情况，预估余额可支撑的时间。若可支撑时间小于5天，我们将会向您推送余额预警。预警消息将通过邮件及短信的方式通知到腾讯云账户的创建者以及所有协作者。

- 欠费预警

按量计费资源每个整点进行扣费。在您的账户被扣为负值时（上图中点1），我们将通过邮件及短信的方式通知到腾讯云账户的创建者以及所有协作者。

- 欠费处理

2小时后（上图中点2）CBS 将停止服务且停止扣费。

自动关机后24小时内，若您的账户余额未充值到大于0，不可对其读写；若充值到余额大于0，计费将继续，可进行读写。

自动关机后，余额小于0达到24小时（上图中点3），按量计费CBS将回收，所有数据将会被清理，且<font color="red">不可找回</font>。

【注意事项】
- 按量计费资源不再使用时**请及时销毁**，以免继续扣费。
- 您的实际资源消耗可能不断变化，因此余额预警可能存在一定的误差
