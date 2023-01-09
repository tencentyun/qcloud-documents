## 接口补充说明

### DescribeDetailedSingleProbeData
关联文档：[DescribeDetailedSingleProbeData](https://cloud.tencent.com/document/api/280/66205)
目前云拨测控制台中的多维分析页面如下图示：
![](https://qcloudimg.tencent-cloud.cn/raw/ea74285e9d57053313023900df10e88d.png)

该页面大致可以范围两部分：
- 可视化图表部分：如平均耗时、错误次数等，实际上是指标；所谓指标就是基于每次的拨测结果，按时间、过滤条件等进行聚合计算后得到。
- 拨测详情列表部分：每次拨测的详细结果列表，这部分就是单次任务下某个拨测点的采集情况。

该接口主要是用于调用拨测详情列表部分，即用于获取单次的拨测结果。

下列主要对 Fields 相关的字段进行解析，不同任务类型，SortField 参数和 SelectedFields.N 参数取值不同。可参考下列说明进行入参。
![](https://qcloudimg.tencent-cloud.cn/raw/a4b0c829858d599aa2344acb7d393eab.png)

#### 所有任务类型公共字段
| 字段     | API 查询时的取值 | 备注                              |
| :------- | :--------------- | :-------------------------------- |
| 状态码   | ErrorId          | 就是拨测结果的状态码，0 为正常状态。 |
| 拨测时间 | ProbeTime        | -                                 |
| 拨测地址 | TargetAddress    | 拨测的目标地址。                    |

#### 网络质量

| 字段               | API 查询时的取值      |
| ------------------ | -------------------- |
| 拨测时间           | ProbeTime            |
| 地区               | District             |
| 城市               | City                 |
| 运营商             | Operator             |
| 拨测点 IP          | ProbeIP              |
| 拨测点 IPV6 地址   | ProbeIPV6            |
| 拨测点 DNS         | ProbeDNS             |
| 访问点信息         | VisitInfo            |
| 节点类型           | ClientName           |
| NS 服务 IP          | NSIP                 |
| NS 服务域名        | NSName               |
| 错误次数           | ErrorCount           |
| Ping 时延(ms)      | PingTime             |
| Ping 有效样本      | PingValidCount       |
| Ping 错误样本      | PingErrorCount       |
| Ping 错误信息      | PingErrorInfo        |
| Ping 总次数        | PingCount            |
| Ping 超时次数      | PingTimeoutCount     |
| Ping 丢包率(%)     | PingPackageLossRate  |
| Ping 丢包数        | PingPackageLossCount |
| DNS 查询用时(ms)   | DNSQueryTime         |
| DNS 有效次数       | DNSValidCount        |
| DNS 解析错误次数   | DNSErrorCount        |
| DNS 错误信息       | DNSErrorInfo         |
| Tracert 时延(ms)   | TracertAvgTime       |
| Tracert 有效样本   | TracertValidCount    |
| Tracert 错误样本   | TracertErrorCount    |
| Tracert 错误信息   | TracertErrorInfo     |
| Tracert 跃点数(次) | TracertSkipCount     |
| 总劫持次数(次)     | HijackCount          |

#### 端口性能

| 字段                     | API 查询时的取值 |
| ------------------------ | ---------------- |
| 拨测时间                 | ProbeTime        |
| 地区                     | District         |
| 城市                     | City             |
| 运营商                   | Operator         |
| 拨测点 IP                | ProbeIP          |
| 拨测点 IPV6地址          | ProbeIPV6        |
| 拨测点 DNS               | ProbeDNS         |
| 访问点信息               | VisitInfo        |
| 节点类型                 | ClientName       |
| 整体性能(ms)             | DTime            |
| 正确率（对响应进行校验） | VerifyRate       |
| DNS 用时(ms)             | DNSTime          |
| TCP 用时(ms)             | ConnectionTime   |
| 发送用时(ms)             | RequestTime      |
| 接收用时(ms)             | ResponseTime     |
| 响应用时(ms)             | WaitTime         |
| SSL 用时(ms)             | SSLTime          |

#### 文件传输（上传/下载）

| 字段               | API 查询时的取值     |
| ------------------ | -------------------- |
| 拨测时间           | ProbeTime            |
| 地区               | District             |
| 城市               | City                 |
| 运营商             | Operator             |
| 拨测点 IP          | ProbeIP              |
| 拨测点 IPV6 地址   | ProbeIPV6            |
| 拨测点 DNS         | ProbeDNS             |
| 访问点信息         | VisitInfo            |
| 节点类型           | ClientName           |
| 错误次数           | ErrorCount           |
| 整体性能(ms)       | TotalTime            |
| 平均传输速度(KB/s) | AvgTransferSpeed     |
| 传输大小(B)        | TransferSize         |
| 传输用时(ms)       | TransferTime         |
| DNS 用时(ms)       | TransferDNSTime      |
| TCP 用时(ms)       | TransferTCPTime      |
| 发送用时(ms)       | TransferSendTime     |
| 接收用时(ms)       | TransferRecTime      |
| 响应用时(ms)       | TransferResponseTime |
| SSL 用时(ms)       | TransferSSLTime      |
| 首包用时(ms)       | FirstPacketTime      |
| 重定向次数(次)     | RedirectTimes        |
| 慢次数(次)         | SlowCount            |
| 劫持次数(次)       | HijackCount          |
| 域名劫持次数(次)   | HijackDomainCount    |

#### 页面性能

| 字段                         | API 查询时的取值             |
| ---------------------------- | --------------------------- |
| 拨测时间                     | ProbeTime                   |
| 地区                         | District                    |
| 城市                         | City                        |
| 运营商                       | Operator                    |
| 拨测点 IP                    | ProbeIP                     |
| 拨测点 IPV6 地址             | ProbeIPV6                   |
| 拨测点 DNS                   | ProbeDNS                    |
| 访问点信息                   | VisitInfo                   |
| 节点类型                     | ClientName                  |
| 错误次数                     | ErrorCount                  |
| 整体性能(ms)                 | DTime                       |
| 100K 耗时(ms)                | K100Time                    |
| 文档完成用时(ms)             | DocumentFinishTime          |
| 首包到达用时(ms)             | FirstPacketArrivalTime      |
| 渲染用时(ms)                 | RenderTime                  |
| 整体下载速度(KB/s)           | OverallDownloadSpeed        |
| 渲染速度(KB/s)               | RenderSpeed                 |
| 基础文档下载速度(KB/s)       | FileDownloadSpeed           |
| 投影 DNS 用时(ms)            | ProjectionDNSQueryTime      |
| 投影 TCP 用时(ms)            | ProjectionTCPConnectionTime |
| 投影请求用时(ms)             | ProjectionRequestTime       |
| 投影响应用时(ms)             | ProjectionResponseTime      |
| 投影下载用时(ms)             | ProjectionDownloadTime      |
| 投影 SSL 握手用时(ms)        | ProjectionSSLTime           |
| block 投影用时(ms)           | BlockProjectionTime         |
| 基础文档 DNS 查询用时(ms)    | FileDNSQueryTime            |
| 基础文档 TCP 连接用时(ms)    | FileTCPConnectionTime       |
| 基础文档发送请求用时(ms)     | FileRequestTime             |
| 基础文档服务器响应用时(ms)   | FileResponseTime            |
| 基础文档下载用时(ms)         | FileDownloadTime            |
| 基础文档 SSL 用时(ms)        | FileSSLTime                 |
| 平均 DNS 查询用时(ms)        | AvgDNSQueryTime             |
| 平均 TCP 连接用时(ms)        | AvgTCPConnectTime           |
| 平均发送请求用时(ms)         | AvgRequestTime              |
| 平均服务器响应用时(ms)       | AvgResponseTime             |
| 平均下载用时(ms)             | AvgDownloadTime             |
| 平均 SSL 握手用时(ms)        | AvgSSLTime                  |
| 首屏用时(ms)                 | FirstScreenTime             |
| 首屏完全渲染用时(ms)         | FirstFullTime               |
| 慢次数(次)                   | SlowCount                   |
| 首次渲染用时(ms)             | PageStartRender             |
| DOMTree 加载完成用时(ms)     | DOMLoadTime                 |
| 页面触发 onload 事件用时(ms) | OnloadTime                  |
| 总下载字节数(B)              | BytesReceived               |
| 基础文档下载字节数(B)        | FileDownloadSize            |
| DNS 解析次数(次)             | DNSLookUps                  |
| RoundTrips(个)               | RoundTrips                  |
| TCP 建连次数(次)             | TCPConnects                 |
| 错误元素个数(个)             | ErrEleCount                 |
| 首屏错误元素个数(个)         | FirstErrEleNum              |
| 首屏内元素总个数(个)         | FirstEleAllNum              |
| 重定向元素个数(个)           | RedirectEleNum              |
| 重定向次数(次)               | RedirectCount               |
| 劫持次数                     | HijackCount                 |
| 域名劫持次数(次)             | HijackDomainCount           |
| 元素劫持次数(次)             | HijackEleCount              |
| 302劫持次数(次)              | Hijack302Count              |
| 302跳转成功次数(次)          | Hijack302SuccessCount       |
| 302正常跳转次数(次)          | HijackNormalCount           |
| 302跳转失败次数(次)          | HijackErrorCount            |
| 302跳转第三方次数(次)        | HijackThirdCount            |

#### 音视频体验

| 指标名             | api字段名            |
| ------------------ | -------------------- |
| 拨测时间           | ProbeTime            |
| 地区               | District             |
| 城市               | City                 |
| 运营商             | Operator             |
| 拨测点 IP          | ProbeIP              |
| 拨测点 IPV6 地址   | ProbeIPV6            |
| 拨测点 DNS         | ProbeDNS             |
| 访问点信息         | VisitInfo            |
| 节点类型           | ClientName           |
| 错误次数           | ErrorCount           |
| 总下载字节数(B)    | TotalDownloadSize    |
| 吞吐用时(ms)       | TotalDownTime        |
| 平均下载速度(KB/s) | AvgDownloadSpeed     |
| 视频首包用时(ms)   | ConnectingTime       |
| 资源 DNS 用时(ms)  | ResourceDNSTime      |
| 资源 TCP 用时(ms)  | ResourceConnectTime  |
| 资源响应用时(ms)   | ResourceResponseTime |
| 资源 SSL 用时(ms)  | ResourceSSLTime      |
| 总缓冲用时(ms)     | TotalBufferTime      |
| 首次播放时间(ms)   | FirstPlayTime        |
| 首帧用时(ms)       | FirstFrameTime       |
| 首帧下载字节数(B)  | FirstDownSize        |
| 首帧下载速度(KB/s) | FirstDownSpeed       |
| 首次缓冲用时(ms)   | FirstBufferTime      |
| 首播持续时间(ms)   | FirstDurationTime    |
| 页面首屏用时(ms)   | PageFirstTime        |
| 总缓冲次数(次)     | BufferNum            |
| 卡顿次数(次)       | LagNumber            |
| 卡顿时间(ms)       | LagTime              |
| 卡顿时间占比(%)    | LagRate              |
| 等待用时占比(%)    | WaitRate             |
| 音频码率(Kbps)     | AudioRate            |
| 视频码率(Kbps)     | VideoRate            |
| 劫持次数(次)       | HijackCount          |
| 域名劫持次数(次)   | HijackDomainCount    |

### CreateProbeTasks
相关接口：
- [CreateProbeTasks](https://cloud.tencent.com/document/api/280/66213)

下列主要对如下字段补充说明：
![](https://qcloudimg.tencent-cloud.cn/raw/030864b564e00ad82512b3c75a93e00b.png)

#### TaskType 取值说明
其中 TaskType 的具体取值关系如下：

| 任务类型 | TaskType 取值 |
| :------- | :------------ |
| 页面性能 | 1             |
| 文件上传 | 2             |
| 文件下载 | 3             |
| 端口性能 | 4             |
| 音视频   | 5             |

#### Parameters 取值
**网络质量**
示例取值：
```
{
  "ipType": 0,
  "netIcmpOn": 1,
  "netIcmpActivex": 0,
  "netIcmpTimeout": 20,
  "netIcmpInterval": 0.5,
  "netIcmpNum": 4,
  "netIcmpSize": 32,
  "netIcmpDataCut": 1,
  "netDnsOn": 1,
  "netDnsTimeout": 20,
  "netDnsQuerymethod": 1,
  "netDnsNs": "",
  "netDigOn": 0,
  "netDnsServer": 0,
  "netTracertOn": 1,
  "netTracertTimeout": 20,
  "netTracertNum": 0,
  "whiteList": "",
  "blackList": "",
  "netIcmpActivexStr": ""
}
```


具体参数说明：

| 参数名            | 是否必填 | 类型   | 描述                                                      |
| :---------------- | :------- | :----- | :-------------------------------------------------------- |
| ipType            | 是       | int    | IP类型。<br>1：ipv4 <br>2：ipv6 <br>0：自动                           |
| grabBag           | 是       | int    | 抓包。目前还不支持，统一填0                               |
| netIcmpOn         | 是       | int    | 启用 icmp 协议 Ping。<br>0：不启用<br>1：启用                   |
| netIcmpActivex    | 是       | int    | Ping 协议。<br>0：icmp <br>1：tcp <br>2：udp                          |
| netIcmpTimeout    | 是       | int    | Ping 探测超时，单位s。默认填20                            |
| netIcmpInterval   | 是       | float  | 执行间隔，单位s。默认填0.5                                |
| netIcmpNum        | 是       | int    | Package 数量。可填1~40，默认填20                          |
| netIcmpSize       | 是       | int    | Package 大小，单位B。默认填32                             |
| netIcmpDataCut    | 是       | int    | 切分 Package。<br>0：不切分 <br>1：切分<br>默认填1                  |
| netDnsOn          | 是       | int    | 启用 DNS 探测。<br>0：不启用<br>1：启用                         |
| netDnsTimeout     | 是       | int    | DNS 解析超时，单位s。默认填5                              |
| netDnsQuerymethod | 是       | int    | DNS 查询方式。<br>1：递归查询 <br>2：迭代查询<br>默认填1            |
| netDnsNs          | 是       | string | 指定 DNS 服务器，如果没有填 ""                             |
| netDigOn          | 是       | int    | 使用 dig 命令的监测结果。<br>0：不启用 <br>1：启用                |
| netDnsServer      | 是       | int    | DNS 服务类型。<br>0：ipv4 <br>1：ipv6 <br>2：自动<br>默认填2            |
| netTracertOn      | 是       | int    | 启用 tracert 探测。<br>0：不启用 <br>1：启用<br>默认填1             |
| netTracertTimeout | 是       | int    | 探测超时，单位 s。默认填60                                |
| netTracertNum     | 是       | int    | 最大跃点数。默认填30                                      |
| whiteList         | 是       | string | DNS 白名单。格式为 www.abc.com:220.0.3.*，如果没有填""     |
| blackList         | 是       | string | DNS 劫持黑名单。格式为 www.abc.com:220.0.3.*，如果没有填"" |
| netIcmpActivexStr | 是       | string | 默认填""                                                  |

#### 端口性能

示例取值：

```
{
  "ipType": 0,
  "protocolRequestType": "T:",
  "protocolCharacterEncoding": 0,
  "protocolType": 1,
  "protocolRequestContent": "GET /static/ping.html HTTP/1.1\nAccept: */*\nHost: example.com\nAccept-Encoding: gzip, deflate, br\nConnection: keep-alive\n\n\n\n\n\n\n",
  "protocolCustomHost": 1,
  "protocolCustomHostIp": "",
  "protocolVerifyWay": 2,
  "protocolVerifyText": "ping"
}
```

具体参数说明：

| 参数名                    | 是否必填 | 类型   | 描述                                                         |
| :------------------------ | :------- | :----- | :----------------------------------------------------------- |
| ipType                    | 是       | int    | IP 类型。<br>1：ipv4 <br>2：ipv6 <br>0：自动                             |
| grabBag                   | 是       | int    | 抓包。目前还不支持，统一填0                                  |
| protocolRequestType       | 是       | string | 请求类型。<br>B：表示二进制 <br>T：表示存文本 <br>F：表示文件，默认请填 <br>T：(注意这里有冒号) |
| protocolCharacterEncoding | 是       | int    | 字符编码。<br>0：UTF8 <br>1：GB2312 <br>2：GBK <br>3：UNICODE，默认请填0     |
| protocolType              | 是       | int    | 协议类型。<br>0：TCP <br>1：SSL <br>2：UDP <br>3：HTTP                       |
| protocolRequestContent    | 是       | string | 请求内容。例如 GET / HTTP/1.1\nUser-Agent: curl                |
| protocolCustomHost        | 是       | int    | 自定义 Host。<br>0：随机 <br>1：轮询                                 |
| protocolCustomHostIp      | 是       | string | 自定义 Host 的内容，如果没有填 ""                             |
| protocolVerifyWay         | 是       | int    | 校验方式。默认填0                                            |
| protocolVerifyText        | 是       | string | 校验内容。默认填 ""                                           |
| http.method               | 是       | string | 请求方式。可选 GET、POST、PUT、DELETE、HEAD、PATCH、OPTIONS、TRACE |
| http.targetUrl            | 是       | string | 目标地址。例如：https://abc.com                              |
| http.header               | 否       | json   | HTTP Header。例如 `[{"name":"Monitor-Token","value":"b6efc19cddf21b14"}]` |
| http.baseAuth             | 否       | json   | HTTP Auth。例如 `[{"user":"aaa", "password": "123"}]`          |
| http.query                | 否       | json   | HTTP 查询参数。例如 `[[{"name":"pageNumber","value":"1"},{"name":"pageSize","value":"20"}]]` |
| http.body                 | 是       | string | 默认填 ""                                                     |
| http.reqBodyText          | 是       | string | 默认填 ""                                                     |
| http.contentType          | 是       | int    | 默认填4                                                      |
| http.verify.enable        | 否       | bool   | 是否启用验证。<br>true：启用 <br>false：不启用                       |
| http.verify.header        | 否       | json   | 例如 `{"aaa":{"method":0,"expectValue":"bbb"}}`，其中 method 可选<br>0：不验证 <br>1：相等 <br>2：正则匹配 <br>3：数值范围 <br>4：包含 <br>5：MD5 |
| http.verify.statusCode    | 否       | json   | 例如 `{"method":1,"expectValue":"404"}`，其中 method 可选<br>0：不验证 <br>1：相等 <br>3：数值范围 <br>4：包含 |
| http.verify.body          | 否       | json   | 例如 `{"method":1,"expectValue":"aaa"}`，其中 method 可选<br>0：不验证 <br>1：相等 <br>2：正则匹配 <br>3：数值范围 <br>4：包含 <br>5：MD5 |



#### 文件上传
取值示例：
```
{
  "ipType": 0,
  "uploadType": "POST",
  "uploadCustomHost": 1,
  "uploadCustomHostIp": "",
  "uploadTransmissionSize": 1024,
  "uploadSpecificFileUrl": "https://example.com/example_file_url",
  "uploadFileMd5": "44eff19d4cd66ff89ed34cda30af988e"
}
```



 具体参数说明：

| 参数名                 | 是否必填 | 类型   | 描述                                                         |
| :--------------------- | :------- | :----- | :----------------------------------------------------------- |
| ipType                 | 是       | int    | IP类型。<br>1：ipv4 <br>2：ipv6 <br>0：自动                              |
| uploadType             | 是       | string | 上传使用的 HTTP Method，例如 POST/PUT                            |
| uploadCustomHost       | 否       | int    | 自定 Host 中 IP 的选取方式。<br>0：随机。<br>1：轮询                     |
| uploadCustomHostIp     | 否       | string | 自定义 Host 的设置，示例取值：<br>IPv4：192.168.2.1,192.168.2.5:img.a.com|192.168.2.1[8080]:img.a.com|<br>IPv6：[0:0:0:0:0:0:0:1][8080],[0:0:0:0:0:0:0:2][8081]:www.a.com|
| uploadTransmissionSize | 是       | int    | 传输的大小，单位KB                                           |
| uploadSpecificFileUrl  | 否       | string | 指定要上传文件的下载地址（先下载，后上传）。若不指定则会按照上传大小来随机生成要上传的内容 |
| uploadFileMd5          | 否       | string | 通过 uploadSpecificFileUrl 指定文件时，文件的校验 MD5 只。     |
| monitorTimeout         | 否       | int    | 检测超时，单位秒，默认60                                     |
| uploadFileName         | 否       | string | 上传的文件名                                                 |

#### 文件下载
取值示例：
```
{
  "ipType": 0,
  "downloadTransmissionSize": 1024,
  "downloadCustomHost": 1,
  "downloadCustomHostIp": "",
  "whiteList": "",
  "blackList": ""
}
```

具体参数说明：

| 参数名                   | 是否必填 | 类型   | 描述                                                         |
| :----------------------- | :------- | :----- | :----------------------------------------------------------- |
| ipType                   | 是       | int    | IP类型。<br>1：ipv4 <br>2：ipv6 <br>0：自动                              |
| downloadCustomHost       | 否       | int    | 自定 Host 中 IP 的选取方式。<br>0：随机<br>1：轮询                 |
| downloadCustomHostIp     | 否       | string | 自定义 Host 的设置，示例取值：<br>IPv4：192.168.2.1,192.168.2.5:img.a.com|192.168.2.1[8080]:img.a.com| <br>IPv6：[0:0:0:0:0:0:0:1][8080],[0:0:0:0:0:0:0:2][8081]:www.a.com |
| downloadTransmissionSize | 是       | int    | 传输的大小，单位KB。                                           |
| whiteList                | 否       | string | 域名劫持判断白名单.www.baidu.com:202.0.3.* （即 www.baidu.com 域名下以202.0.3. 开头的 IP 都不认为是被劫持。 |
| blackList                | 否       | string | 域名劫持判断黑名单.www.baidu.com:202.0.3.* （即 www.baidu.com 域名下以202.0.3. 开头的 IP 都认为是被劫持。 |
| monitorTimeout           | 否       | int    | 检测超时 ，单位秒，默认60。                                    |

#### 3.2.2.5. 页面性能
取值示例：
```
{
  "ipType": 0,
  "navCustomHost": 1,
  "navCustomHostIp": ""
}
```

具体参数说明：
<table>
    <tr>
        <th>参数名称</td>
        <th>是否必填</td>
        <th>参数类型</td>
        <th>参数描述 </td>
    </tr>
    <tr>
        <td>ipType</td>
        <td>是</td>
        <td>int</td>
        <td>IP类型。<br>1：ipv4 <br>2：ipv6 <br>0：自动 </td>
    </tr>
    <tr>
        <td>navCustomHost</td>
        <td>否</td>
        <td>int</td>
        <td>自定Host中IP的选取方式。<br>0：随机<br>1：轮询 </td>
    </tr>
    <tr>
        <td>navCustomHostIp</td>
        <td>否</td>
        <td>string</td>
        <td>自定义Host的设置，示例取值：<br>IPv4：192.168.2.1,192.168.2.5:img.a.com|192.168.2.1[8080]:img.a.com|&nbsp;<br>IPv6：[0:0:0:0:0:0:0:1][8080],[0:0:0:0:0:0:0:2][8081]:www.a.com| </td>
    </tr>
    <tr>
        <td>whiteList</td>
        <td>否</td>
        <td>string</td>
        <td>域名劫持判断白名单.www.baidu.com:202.0.3.* （即 www.baidu.com 域名下以202.0.3. 开头的IP都不认为是被劫持。 </td>
    </tr>
    <tr>
        <td>blackList</td>
        <td>否</td>
        <td>string</td>
        <td>域名劫持判断黑名单.www.baidu.com:202.0.3.* （即 www.baidu.com 域名下以202.0.3. 开头的IP都认为是被劫持。 </td>
    </tr>
    <tr>
        <td>flowHijackJumpTimes</td>
        <td>否</td>
        <td>int</td>
        <td rowspan="2">流量劫持（实际上是302重定向劫持识别）的相关参数。flowHijackJumpTimes：识别元素<br>flowHijackLogo：识别标识（与最终的地址做匹配判断，而非页面内容）劫持标识判断的是最终跳转到的URL（不包含查询参数）。<br>针对浏览页面时**302跳转情况**进行分类统计。（监测前提是页面中有302的元素，一般监测基础文档发生302后的情况）。<br>有如下几种：<li>跳转成功：判断规则是在设置的最多元素识别个数之内成功匹配到元素的关键信息，判断为跳转成功。跳转成功时统计跳转次数，从第一个302跳转算起。<li>跳转到错误页面：判断规则是关键信息匹配失败，并且页面元素总个数（元素瀑布图中元素的个数）小于设置的识别元素个数，判断为跳转到错误页面。<li>跳转到第三方网站：只要页面元素总个数超过（大于）设置的元素识别个数，被认为跳转到了第三方地址。 </td>
    </tr>
    <tr>
        <td>flowHijackLogo</td>
        <td>否</td>
        <td>string</td>
    </tr>
</table>

#### 音视频
取值示例：
```
{
  "ipType": 0,
  "streamType": 0,
  "streamMonitorTimeout": 30,
  "streamAddressType": 0,
  "streamCustomHost": 1,
  "streamCustomHostIp": "",
  "whiteList": "",
  "blackList": ""
}
```


具体参数说明：

| 参数名称               | 是否必填 | 参数类型   | 参数描述                                                         |
| :------------------- | :------- | :----- | :----------------------------------------------------------- |
| ipType               | 是       | int    | IP类型。<br>1：ipv4 <br>2：ipv6 <br>0：自动                              |
| streamType           | 是       | int    | 资源类型。<br>0：音频<br>1：视频。                                 |
| streamMonitorTimeout | 否       | int    | 检测超时，单位秒，默认60。                                     |
| streamAddressType    | 是       | int    | 要检测资源的地址类型。<br>0：页面地址<br>1：资源地址                |
| streamCustomHost     | 否       | int    | 自定 Host 中 IP 的选取方式。<br>0：随机<br>1：轮询                 |
| streamCustomHostIp   | 否       | string | 自定义 Host 的设置，示例取值：<br>IPv4：192.168.2.1,192.168.2.5:img.a.com|192.168.2.1[8080]:img.a.com| <br>IPv6：[0:0:0:0:0:0:0:1][8080],[0:0:0:0:0:0:0:2][8081]:www.a.com|
| whiteList            | 否       | string | 域名劫持判断白名单.www.baidu.com:202.0.3.* （即 www.baidu.com 域名下以202.0.3. 开头的 IP 都不认为是被劫持 |
| blackList            | 否       | string | 域名劫持判断黑名单.www.baidu.com:202.0.3.* （即 www.baidu.com 域名下以202.0.3. 开头的 IP 都认为是被劫持 |

### Nodes 取值说明
该取值用于选择具体的拨测点，可通过 [DescribeProbeTasks](https://cloud.tencent.com/document/api/280/66204) 获取拨测点机器对应的取值（其中的 Code 字段）。

