## 独立产品迁移指引文档

<table>
<thead>
  <tr>
    <th>产品名称</th>
    <th>迁移指引文档地址</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>云点播</td>
    <td><a href="https://cloud.tencent.com/document/product/266/80469">云点播 VOD API 2.0切换 API 3.0指引</a></td>
  </tr>
  <tr>
    <td>云直播</td>
    <td><a href="https://cloud.tencent.com/document/product/267/82004#list">云直播 CSS API 2.0切换 API 3.0指引</a></td>
  </tr>
  <tr>
    <td>内容分发网络</td>
    <td><a href="https://cloud.tencent.com/document/api/228/80982">内容分发网络 CDN API 2.0切换 API 3.0指引</a></td>
  </tr>
  <tr>
    <td>私有网络<br>安全防火墙</td>
    <td><a href="https://cloud.tencent.com/document/product/215/81827">私有网络 API 2.0切换 API 3.0指引</a></td>
  </tr>
  <tr>
    <td>云监控</td>
    <td><a href="https://cloud.tencent.com/document/product/248/81039">云监控接口迁移说明</a></td>
  </tr>
  <tr>
    <td>DNSPod</td>
    <td><a href="https://docs.dnspod.cn/notices/api-2-upgrade/">腾讯云解析 API 2.0升级通知</a></td>
  </tr>
  <tr>
    <td>云数据库 Redis</td>
    <td><a href="https://cloud.tencent.com/document/product/239/83200">云数据库 Redis 云 API 2.0全面下线公告</a></td>
  </tr>
  <tr>
    <td>云数据库 MySQL</td>
    <td><a href="https://cloud.tencent.com/document/product/236/82663">云数据库 MySQL API 2.0切换 API 3.0指引</a></td>
  </tr>
  <tr>
    <td>负载均衡</td>
    <td><a href="https://cloud.tencent.com/document/product/214/82364">负载均衡 API 2.0切换 API 3.0指引</a></td>
  </tr>
  <tr>
    <td>消息队列(CMQ)</td>
    <td><a href="https://cloud.tencent.com/document/product/1496/83970">消息队列 CMQ 版 API 2.0切换至 TDMQ CMQ 版 API 3.0指引</a></td>
  </tr>
  <tr>
    <td>弹性公网IP</td>
    <td><a href="https://cloud.tencent.com/document/product/1199/83744">弹性公网 IP API 2.0切换 API 3.0指引</a></td>
  </tr>
</tbody>
</table>



## 其他产品 API 2.0切换3.0接口对应
### 专线接入 DC
| API 2.0 接口                 | API 3.0 接口                 |
|------------------------------|------------------------------|
| DescribeDirectConnectTunnels | [DescribeDirectConnectTunnels](https://cloud.tencent.com/document/product/216/19819) |
| DescribeDirectConnects       | [DescribeDirectConnects](https://cloud.tencent.com/document/product/216/34826)       |
| DeleteDirectConnectTunnel    | [DeleteDirectConnectTunnel](https://cloud.tencent.com/document/product/216/19820)    |

### 容器服务 CCS
<table>
<thead>
  <tr>
    <th>API 2.0 接口</th>
    <th>API 3.0 接口</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>CheckClusterRouteTableCidrConflict</td>
    <td><a href="https://cloud.tencent.com/document/api/457/37180">DescribeRouteTableConflicts</a></td>
  </tr>
  <tr>
    <td>CreateClusterRoute</td>
    <td><a href="https://cloud.tencent.com/document/api/457/37186">CreateClusterRoute</a></td>
  </tr>
  <tr>
    <td>CreateClusterRouteTable</td>
    <td><a href="https://cloud.tencent.com/document/api/457/37185">CreateClusterRouteTable</a></td>
  </tr>
  <tr>
    <td>CreateClusterService</td>
    <td><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
  </tr>
  <tr>
    <td>DeleteClusterRoute</td>
    <td><a href="https://cloud.tencent.com/document/api/457/37184">DeleteClusterRoute</a></td>
  </tr>
  <tr>
    <td>DescribeCluster</td>
    <td><a href="https://cloud.tencent.com/document/api/457/31862">DescribeClusters</a></td>
  </tr>
  <tr>
    <td>DescribeClusterContainer</td>
    <td><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
  </tr>
  <tr>
    <td>DescribeClusterInstances</td>
    <td><a href="https://cloud.tencent.com/document/api/457/31863">DescribeClusterInstances</a></td>
  </tr>
  <tr>
    <td>DescribeClusterRoute</td>
    <td><a href="https://cloud.tencent.com/document/api/457/37181">DescribeClusterRoutes</a></td>
  </tr>
  <tr>
    <td>DescribeClusterRouteTable</td>
    <td><a href="https://cloud.tencent.com/document/api/457/37182">DescribeClusterRouteTables</a></td>
  </tr>
  <tr>
    <td>DescribeClusterService</td>
    <td><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
  </tr>
  <tr>
    <td>DescribeClusterServiceInfo</td>
    <td><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
  </tr>
  <tr>
    <td>DescribeInstanceLog</td>
    <td><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
  </tr>
  <tr>
    <td>DescribeServiceEvent</td>
    <td><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
  </tr>
  <tr>
    <td>DescribeServiceInstance</td>
    <td><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
  </tr>
  <tr>
    <td>GetClustersResourceStatus</td>
    <td>已下线，无对应V3接口</td>
  </tr>	
  <tr>
    <td>GetLogDaemonStatus</td>
    <td>已下线，无对应V3接口</td>
  </tr>
  <tr>
    <td>ModifyClusterServiceImage</td>
    <td><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
  </tr>
  <tr>
    <td>RedeployClusterService</td>
    <td><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
  </tr>
</tbody>
</table>


### 云服务器 CVM
<table>
<thead>
  <tr>
    <th>API 2.0 接口</th>
    <th>API 3.0 接口</th>
    <th>说明</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>DescribeAvailabilityZones</td>
    <td><a href="https://cloud.tencent.com/document/product/213/15707">DescribeZones</a></td>
    <td>-</td>
  </tr>
  <tr>
    <td>DescribeInstances</td>
    <td><a href="https://cloud.tencent.com/document/product/213/15728">DescribeInstances</a></td>
    <td>1. uuid 转化为 InstanceIds<br>2. 其他过滤条件放到 Filters 中维护</td>
  </tr>
  <tr>
    <td>DescribeInstancesStatusV3</td>
    <td><a href="https://cloud.tencent.com/document/product/213/15738">DescribeInstancesStatus</a></td>
    <td>直接替代</td>
  </tr>
  <tr>
    <td>DescribeKeyPairs</td>
    <td><a href="https://cloud.tencent.com/document/product/213/15699">DescribeKeyPairs</a></td>
    <td>keyIds -&gt; KeyIds<br>不再支持 keyName 过滤</td>
  </tr>
  <tr>
    <td>DescribeZoneAbility</td>
    <td><a href="https://cloud.tencent.com/document/product/213/15707">DescribeZones</a></td>
    <td>-</td>
  </tr>
  <tr>
    <td rowspan="6">InquiryInstancePrice</td>
    <td><a href="https://cloud.tencent.com/document/api/213/15726">InquiryPriceRunInstances</a></td>
    <td rowspan="6">不同询价场景使用不同的新接口替代<br>创建 -&gt; InquiryPriceRunInstances<br>续费 -&gt; InquiryPriceRenewInstances<br>重装 -&gt; InquiryPriceResetInstance<br>配置系统升级 -&gt; InquiryPriceResetInstancesType<br>扩容实例磁盘 -&gt; InquiryPriceResizeInstanceDisks<br>调整实例计费模式 -&gt; InquiryPriceModifyInstancesChargeType</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/213/15725">InquiryPriceRenewInstances</a></td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/213/15747">InquiryPriceResetInstance</a></td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/213/15733">InquiryPriceResetInstancesType</a></td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/213/15751">InquiryPriceResizeInstanceDisks</a></td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/213/17965">InquiryPriceModifyInstancesChargeType</a></td>
  </tr>
  <tr>
    <td>ModifyInstanceAttributes</td>
    <td><a href="https://cloud.tencent.com/document/api/213/15739">ModifyInstancesAttribute</a></td>
    <td>1. ipList, uuidList 新接口不再支持，需要转化为 InstanceIds<br>2. alias 在新接口中是 InstanceName</td>
  </tr>
  <tr>
    <td>RenewInstance</td>
    <td><a href="https://cloud.tencent.com/document/api/213/15740">RenewInstances</a></td>
    <td>goodsDetail 中的信息需要提取到外层<br>1. uuid 转化为 InstanceIds<br>2. 新接口使用 InstanceChargePrepaid 传入预付费的相关信息，包括 Period（代替 timeSpan)，TimeUnit（支持按天/月两种模式）<br>3. purchaseSource 不再需要传入</td>
  </tr>
  <tr>
    <td>ResetInstancePassword</td>
    <td><a href="https://cloud.tencent.com/document/api/213/15736">ResetInstancesPassword</a></td>
    <td>1. uuidList 新接口不再支持，需要转化为 InstanceIds<br>2. password 转化为 Password<br>3. hardPowerOffFlag 转化为 ForceStop</td>
  </tr>
  <tr>
    <td>RestartInstances</td>
    <td><a href="https://cloud.tencent.com/document/api/213/15742">RebootInstances</a></td>
    <td>1. uuidList 新接口不再支持，需要转化为 InstanceIds<br>2. softPowerOffFlag/hardPowerOffFlag 转化为 ForceReboot</td>
  </tr>
  <tr>
    <td>RunInstances</td>
    <td><a href="https://cloud.tencent.com/document/api/213/15730">RunInstances</a></td>
    <td>goodsDetail 中的信息需要提取到外层，字段较多不一一列举</td>
  </tr>
  <tr>
    <td>RunInstancesHour</td>
    <td><a href="https://cloud.tencent.com/document/api/213/15730">RunInstances</a>（按量计费和包年包月在 v3 收敛到同一个接口）</td>
    <td>goodsDetail 中的信息需要提取到外层，字段较多不一一列举</td>
  </tr>
  <tr>
    <td>StartInstances</td>
    <td><a href="https://cloud.tencent.com/document/api/213/15735">StartInstances</a></td>
    <td>uuidList 新接口不再支持，需要转化为 InstanceIds</td>
  </tr>
  <tr>
    <td>StopInstances</td>
    <td><a href="https://cloud.tencent.com/document/api/213/15743">StopInstances</a></td>
    <td>1. uuidList 新接口不再支持，需要转化为 InstanceIds<br>2. softPowerOffFlag/hardPowerOffFlag 转化为 ForceStop<br>3. actionType 转化为 StopType</td>
  </tr>
</tbody>
</table>

### 账号服务 account
| API 2.0 接口    | API 3.0 接口     |
|-----------------|------------------|
| DescribeProject | [DescribeProjects](https://cloud.tencent.com/document/product/651/78725) |
