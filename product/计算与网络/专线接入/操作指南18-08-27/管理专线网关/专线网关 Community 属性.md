## 前提条件
为了获取 VPC 路由所在地域信息，专线网关和专用通道支持向本地数据中心（IDC）单向传递携带有地域信息的 Community 属性，条件如下：
- 专线网关：关联网络类型为云联网，且开启 Community 属性传递。
- 专用通道：开启 Community 属性传递（功能灰度中，如有需要，请提 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=664&source=0&data_title=专线接入&step=1)）。
- 支持传递 Community 属性的路由：从云端通过专线网关发送给 IDC 侧的 VPC 子网的路由条目（从 IDC 侧发送给专线网关的路由，不支持传递 Community 属性）。
- 支持传递 Community 属性的专线网关地域： 北京、上海、广州、中国香港、弗吉尼亚、硅谷、东京、新加坡。
- 支持传递的 Community 属性值如下表所示，不支持修改和删除。
<table style="width:40%">
<thead>
<tr>
<th>地域</th>
<th>Community 属性值</th>
</tr>
</thead>
<tbody><tr>
<td>华北地区（北京）</td>
<td>58835:10</td>
</tr>
<tr>
<td>华东地区（上海）</td>
<td>58835:21</td>
</tr>
<tr>
<td>华南地区（广州）</td>
<td>58835:20</td>
</tr>
<tr>
<td>华南地区（深圳）</td>
<td>58835:755</td>
</tr>
<tr>
<td>西南地区（重庆）</td>
<td>58835:23</td>
</tr>
<tr>
<td>华东地区（南京）</td>
<td>58835:25</td>
</tr>
<tr>
<td>华东地区（济南 EC）</td>
<td>58835:531</td>
</tr>
<tr>
<td>华中地区（武汉 EC）</td>
<td>58835:27</td>
</tr>
<tr>
<td>华东地区（福州 EC）</td>
<td>58835:591</td>
</tr>
<tr>
<td>华中地区（长沙 EC）</td>
<td>58835:731</td>
</tr>
<tr>
<td>港澳台地区（中国香港）</td>
<td>58835:852</td>
</tr>
<tr>
<td>亚太东南（新加坡）</td>
<td>58835:65</td>
</tr>
<tr>
<td>亚太东南（曼谷）</td>
<td>58835:66</td>
</tr>
<tr>
<td>亚太南部（孟买）</td>
<td>58835:91</td>
</tr>
<tr>
<td>亚太东北（首尔）</td>
<td>58835:82</td>
</tr>
<tr>
<td>亚太东北（东京）</td>
<td>58835:81</td>
</tr>
<tr>
<td>欧洲地区（法兰克福）</td>
<td>58835:49</td>
</tr>
<tr>
<td>欧洲地区（莫斯科）</td>
<td>58835:7</td>
</tr>
<tr>
<td>美国西部（硅谷）</td>
<td>58835:1</td>
</tr>
<tr>
<td>美国东部（弗吉尼亚）</td>
<td>58835:804</td>
</tr>
<tr>
<td>北美地区（多伦多）</td>
<td>58835:705</td>
</tr>
</tbody></table>

## 操作步骤
### 开启/关闭专线网关 Community 属性传递
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左侧导航栏中的**专线网关**。
3. 单击云联网类型的专线网关 ID，进入详情页。
4. 选择**IDC网段**标签页。
5. 单击 Community 属性开关并确定操作，开启或关闭专线网关 Community 属性传递。
![](https://main.qcloudimg.com/raw/a881ad720445f71267c75d7547b433a9.png)

### 查看专用通道 Community 属性传递状态
1. 登录 [专线接入控制台](https://console.cloud.tencent.com/dc/dc)。
2. 单击左侧导航栏中的**专用通道**。
3. 选择专用通道 ID，进入详情页进行查看。
![](https://main.qcloudimg.com/raw/0e569c0f972281ac0902eb4b00fe530e.png)
