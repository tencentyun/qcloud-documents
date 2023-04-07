

CDN API 2.0下线通知：基于 API 2.0 接口访问时延较高和使用复杂的考虑，我们将于北京时间2022年11月30日下线 2.0 版本。若您的业务仍在使用CDN 的 API 2.0 相关接口，建议尽快将服务升级至CDN API 3.0 接口，避免对您的业务造成影响。

您可参照如下信息完成切换工作：

-   [API 文档中心](https://cloud.tencent.com/document/api)：可以看到所有对外公开的接口信息；
-   [SDK 中心](https://cloud.tencent.com/document/sdk)：可以获取到 API3.0 配套的八种编程语言的 SDK；
-   [API Explorer](https://console.cloud.tencent.com/api/explorer)：可以直接生成 SDK 的调用代码，方便用户实现代码调用。

请您从参照下方的 [API 2.0 切换 3.0 接口表](list) 找到您需要升级的新接口，完成升级。

[](id:list)
## API 2.0 切换 3.0 接口列表

| **V2版本接口**                   | **V3版本接口**                                               | 
|----------------------------------|--------------------------------------------------------------|
| [AddCdnHost ](https://cloud.tencent.com/document/product/228/1406)  | [AddCdnDomain](https://cloud.tencent.com/document/product/228/41123)    |
| [AddCdnOvHost](https://cloud.tencent.com/document/api/228/9814)      | [AddCdnDomain](https://cloud.tencent.com/document/product/228/41123)    |
| AddYYCdnHost                  | [AddCdnDomain](https://cloud.tencent.com/document/product/228/41123)                                           |
| [CdnOverseaPushser](https://cloud.tencent.com/document/api/228/7359)      | [PushUrlsCache](https://cloud.tencent.com/document/product/228/37869) |
| CdnPusher                           | [PushUrlsCache](https://cloud.tencent.com/document/product/228/37870),[PushUrlsCache](https://cloud.tencent.com/document/product/228/37869)|
| [CdnPusherV2 ](https://cloud.tencent.com/document/product/228/15164)  | [PushUrlsCache](https://cloud.tencent.com/document/product/228/37871),[PushUrlsCache](https://cloud.tencent.com/document/product/228/37869)|
| [CdnUrlPusher ](https://cloud.tencent.com/document/product/228/12839)  | [PushUrlsCache](https://cloud.tencent.com/document/product/228/37872),[PushUrlsCache](https://cloud.tencent.com/document/product/228/37869)|
| [CheckOvHost](https://cloud.tencent.com/document/api/228/10948)     | CheckDomain                                                  | 
| [DeleteCdnHost  ](https://cloud.tencent.com/document/product/228/1396)  | [DeleteCdnDomain](https://cloud.tencent.com/document/product/228/41122)                                                       |
| [DeleteCdnOvHost](https://cloud.tencent.com/document/api/228/10946)     | [DeleteCdnDomain](https://cloud.tencent.com/document/product/228/41122)                                                      |
| DescribeCdnHostDetailedInfo               | [DescribeCdnData](https://cloud.tencent.com/document/product/228/30986)                                                       |
| [DescribeCdnHostInfo       ](https://cloud.tencent.com/document/product/228/13022) | [DescribeCdnData](https://cloud.tencent.com/document/product/228/30986)                                                       |
| [DescribeCdnHosts          ](https://cloud.tencent.com/document/product/228/3937)  | [DescribeDomains](https://cloud.tencent.com/document/product/228/41118)                                                       |
| [DescribeOverseaCdnHosts   ](https://cloud.tencent.com/document/api/228/8653)      | [DescribeDomains](https://cloud.tencent.com/document/product/228/41118)                                                       |
| [FlushOrPushOverall        ](https://cloud.tencent.com/document/product/228/12841) | [PushUrlsCache,PurgeUrlsCache](https://cloud.tencent.com/document/product/228/37870)                                                       |
| [GenerateLogList           ](https://cloud.tencent.com/doc/api/231/3950)           | [DescribeCdnDomainLogs](https://cloud.tencent.com/document/product/228/39232)                                                       |
| GetCdnEdgeStatus                                                           | [DescribeIpStatus](https://cloud.tencent.com/document/product/228/41954)                                                       |
| GetCdnHostPathList                                                         | DescribeDomainPathData                                       | 
| GetCdnHostsDetailStat                                                    | [DescribeCdnData,DescribeOriginData](https://cloud.tencent.com/document/product/228/30986)                                                       |
| [GetCdnHostsDetailStatistic](https://cloud.tencent.com/document/product/228/13026) | [DescribeCdnData,DescribeOriginData](https://cloud.tencent.com/document/product/228/30986)                                                       |
| GetCdnHostsHyStat                                                           | [DescribeCdnData,DescribeOriginData](https://cloud.tencent.com/document/product/228/30986)                                                       |
| GetCdnHostsLogStat                                                          | [DescribeCdnData](https://cloud.tencent.com/document/product/228/30986)                                                       |
| GetCdnHostsPathDetailStatistics                                                   | DescribeDomainPathData                                       | 
| GetCdnIps                                                                 | [DescribeIpStatus](https://cloud.tencent.com/document/product/228/41954)                                                       |
| [GetCdnLogList             ](https://cloud.tencent.com/document/product/228/8087)  | [DescribeCdnDomainLogs](https://cloud.tencent.com/document/product/228/39232)                                                       |
| GetCdnMiddleSourceList                                                     | 下线                                                         |
| [GetCdnMonitorData         ](https://cloud.tencent.com/document/product/228/13218) | DescribeMainlandMonitorRealtimeData,DescribeMonitorTrendData |                                                                                                              |
| [GetCdnOriginStat          ](https://cloud.tencent.com/document/product/228/13211) | [DescribeOriginData](https://cloud.tencent.com/document/product/228/30984)                                                       |
| [GetCdnOverseaOpenStat     ](https://cloud.tencent.com/document/api/228/20000)     | [DescribeDomains](https://cloud.tencent.com/document/product/228/41118)                                                       |
| [GetCdnOverseaProvIspDetail](https://cloud.tencent.com/document/api/228/7344)      | [DescribeDistrictIspData ](https://cloud.tencent.com/document/product/228/47395)                                                       |
| [GetCdnOverseaProvIspHyDetailStat](https://cloud.tencent.com/document/api/228/7422)      | [DescribeDistrictIspData](https://cloud.tencent.com/document/product/228/47395)                                                       |
| [GetCdnOverseaPushLogs     ](https://cloud.tencent.com/document/api/228/7360)      | [DescribePushTasks](https://cloud.tencent.com/document/product/228/37872)                                                       |
| [GetCdnOverseaPv           ](https://cloud.tencent.com/document/api/228/7342)      | [DescribeCdnData](https://cloud.tencent.com/document/product/228/30986)                                                       |
| [GetCdnOverseaRefreshLog   ](https://cloud.tencent.com/document/api/228/7347)      | [DescribePurgeTasks](https://cloud.tencent.com/document/product/228/37873)                                                       |
| [GetCdnOverseaStat         ](https://cloud.tencent.com/doc/api/445/6394)           |[ DescribeCdnData ](https://cloud.tencent.com/document/product/228/30986)                                                       |
| GetCdnOverseaStatistics                                                     | [DescribeCdnData ](https://cloud.tencent.com/document/product/228/30986)                                                       |
| [GetCdnOverseaStatTop      ](https://cloud.tencent.com/document/api/228/18003)     | [ListTopData](https://cloud.tencent.com/document/product/228/30983)                                                       |
| [GetCdnOverseaStatusCode   ](https://cloud.tencent.com/document/api/228/7343)      | [DescribeCdnData](https://cloud.tencent.com/document/product/228/30986)                                                       |
| [GetCdnOvHostInfo          ](https://cloud.tencent.com/document/api/228/10947)     | [DescribeDomains ](https://cloud.tencent.com/document/product/228/41118)                                                       |
| [GetCdnProvIspDetailStat   ](https://cloud.tencent.com/document/product/228/7356)  | [DescribeDistrictIspData](https://cloud.tencent.com/document/product/228/47395)                                                       |
| GetCdnPushStatus                                                      |[DescribePushTasks](https://cloud.tencent.com/document/product/228/37872)                                                       |
| [GetCdnRefreshLog          ](https://cloud.tencent.com/doc/api/231/3948)           | [DescribePurgeTasks](https://cloud.tencent.com/document/product/228/37873)                                                       |
| [GetCdnStatTop             ](https://cloud.tencent.com/document/api/228/18004)     | [ListTopData](https://cloud.tencent.com/document/product/228/30983)                                                       |
| GetCdnStatusCode                                                            | [DescribeCdnData ](https://cloud.tencent.com/document/product/228/30986)                                                       |
| [GetCertificates           ](https://cloud.tencent.com/document/api/228/10938)     | DescribeCertificates                                         | 
| GetFlushQuota                                                                  | [DescribePurgeQuota ](https://cloud.tencent.com/document/product/228/41956)                                                       |
| [GetHostCertList           ](https://cloud.tencent.com/document/api/228/12543)     | DescribeCertificates                                         | 
| [GetHostInfoByHost         ](https://cloud.tencent.com/document/product/228/3938)  | [DescribeDomains](https://cloud.tencent.com/document/product/228/41118)                                                       |
| [GetHostInfoById           ](https://cloud.tencent.com/document/product/228/3939)  |[ DescribeDomains  ](https://cloud.tencent.com/document/product/228/41118)                                                       |
| GetOneMinuteDetailStat                                                      | [DescribeCdnData  ](https://cloud.tencent.com/document/product/228/30986)                                                       |
| GetOvAreaIp                                                              | [DescribeIpStatus ](https://cloud.tencent.com/document/product/228/41954)                                                       |
| [GetOverseaCdnLogList      ](https://cloud.tencent.com/document/api/228/8703)      | [DescribeCdnDomainLogs ](https://cloud.tencent.com/document/product/228/39232)                                                       |
| GetOverseaOpList                                                       | 下线，云审计查看                                             |                                                                                                              |
| GetOvIdMapping                                                        | [DescribeMapInfo  ](https://cloud.tencent.com/document/product/228/31296)                                                       |
| GetPackage                                                              | [DescribeTrafficPackages ](https://cloud.tencent.com/document/product/228/39230)                                                       |
| GetPackagePrice                                                              | [DescribeTrafficPackages ](https://cloud.tencent.com/document/product/228/39230)                                                       |
| GetPeakUsageByDay                                                      | [DescribeCdnData ](https://cloud.tencent.com/document/product/228/30986)                                                       |
| GetPornIndentificationInfo                                                  | 下线                                                         |                                                                                                              |
| [GetPushLogs               ](https://cloud.tencent.com/document/product/228/12840) | [DescribePushTasks ](https://cloud.tencent.com/document/product/228/37872)                                                       |
| [OfflineHost               ](https://cloud.tencent.com/document/product/228/1403)  | [StopCdnDomain ](https://cloud.tencent.com/document/product/228/41120)                                                       |
| [OfflineOvHost             ](https://cloud.tencent.com/document/api/228/10945)     | [StopCdnDomain ](https://cloud.tencent.com/document/product/228/41120)                                                       |
| [OnlineHost                ](https://cloud.tencent.com/document/product/228/1402)  | [StartCdnDomain ](https://cloud.tencent.com/document/product/228/41121)                                                       |
| OrderPackage                                                         | 下线，官网购买                                               |                                                                                                              |
| PayPackageOrder                                                            | 下线，官网购买                                               |                                                                                                              |
| [QueryCdnIp                ](https://cloud.tencent.com/document/product/228/12964) | [DescribeIpStatus  ](https://cloud.tencent.com/document/product/228/41954)                                                       |
| QueryCdnServiceIp                                                         | [DescribeIpStatus ](https://cloud.tencent.com/document/product/228/41954)                                                       |
| [RefreshCdnDir             ](https://cloud.tencent.com/doc/api/231/3947)           | [PurgePathCache ](https://cloud.tencent.com/document/product/228/37871)                                                       |
| [RefreshCdnOverSeaDir      ](https://cloud.tencent.com/document/api/228/7389)      | [PurgePathCache](https://cloud.tencent.com/document/product/228/37871)                                                       |
| [RefreshCdnOverSeaUrl      ](https://cloud.tencent.com/document/api/228/7346)      | [PurgeUrlsCache](https://cloud.tencent.com/document/product/228/37870)                                                       |
| [RefreshCdnUrl             ](https://cloud.tencent.com/doc/api/231/3946)           | [PurgeUrlsCache](https://cloud.tencent.com/document/product/228/37870)                                                       |
| [SetHttpsInfo              ](https://cloud.tencent.com/document/product/228/12965) | [UpdateDomainConfig](https://cloud.tencent.com/document/product/228/41116)                                                       |
| StartCdnService                                 | [StartCdnDomain](https://cloud.tencent.com/document/product/228/41121)                                                       |
| [UpdateCdnConfig           ](https://cloud.tencent.com/document/product/228/3933)  | [UpdateDomainConfig ](https://cloud.tencent.com/document/product/228/41116)                                                       |
| [UpdateCdnOverseaConfig    ](https://cloud.tencent.com/document/api/228/10939)     |[ UpdateDomainConfig](https://cloud.tencent.com/document/product/228/41116)                                                       |
