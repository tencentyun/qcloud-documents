GPU 机型 GN7vw 实例是基于 NVIDIA Tesla  T4 GPU 卡，配置了 vDWS License 服务器并安装 GRID driver 的渲染型实例，适用于图形图像处理场景（3D 渲染或视频编解码）。GPU 机型 GN7vw 实例的计费模式和价格区别于其他实例，您可根据本文了解其计费详情。

## 计费模式
GPU 机型 GN7vw 计费包含 [实例费用](#instancePrice) 和 [存储费用](#storagePrice) 两部分，采用按月后付费的计费模式。

### 实例费用[](id:instancePrice)

#### 计算周期
按月后付费，若用户使用不满一个月，则按实际使用小时数和当月总小时数的比例计算使用时长占比。

#### 计算公式
不满一个月的实例费用计算公式为：**实例费用 = 使用时长占比 × 实例月价格**
>? 使用时长占比 = 当月实际使用小时数/（当月天数 x 24），精确到小时。
>
例如，某用户于2021年05月创建了一台配置为4核16GB的 GPU 机型 GN7vw 实例，具体创建时间为2021年05月08日 15:04，销毁实例时间为2021年05月23日 18:39，则该用户的实例费用为：

 - 使用时长占比 = （实例销毁时间 - 实例创建时间）/ （当月天数 × 24）= 340 /（31 × 24）=45.7%
 - 实例费用 = 45.7% × 1047 = 478.48（元）

#### 实例价格
<table>
<thead>
<tr>
<th align="left">机型规格</th>
<th align="left">vCPU（核）</th>
<th align="left">内存（GB）</th>
<th>GPU显卡（Tesla T4 ）</th>
<th align="left">价格（元/月）</th>
</tr>
</thead>
<tbody><tr>
<td align="left">GN7vw.LARGE16</td>
<td align="left">4</td>
<td align="left">16</td>
<td>1/4</td>
<td align="left">1047</td>
</tr>
<tr>
<td align="left">GN7vw.2XLARGE32</td>
<td align="left">8</td>
<td align="left">32</td>
<td>1/2</td>
<td align="left">1874</td>
</tr>
<tr>
<td align="left">GN7vw.4XLARGE64</td>
<td align="left">16</td>
<td align="left">64</td>
<td>1</td>
<td align="left">3528</td>
</tr>
<tr>
<td align="left">GN7vw.8XLARGE128</td>
<td align="left">32</td>
<td align="left">128</td>
<td>2</td>
<td align="left">7056</td>
</tr>
</tbody></table>

### 存储费用[](id:storagePrice)

#### 存储类型
**本地存储（SSD）**是基于 NVMe SSD 本地存储，提供低延迟、超高 IOPS、高吞吐量的存储资源。但有丢失数据的风险（例如宿主机宕机时），需要在应用层面保障数据可靠性。

#### 存储价格
单价为1元/GB/月，您可以在创建模块时按需修改系统盘和数据盘的存储容量大小。


>?
>- 不同配置的实例提供不同的计算和存储能力，您可以基于需要提供的服务规模来选择实例的配置及数量。
>- 计费账单在腾讯云计费系统中按实例维度上报，用户可以查看实例 ID、实例名称、开始使用时间、结束使用时间及边缘节点名称等信息。

