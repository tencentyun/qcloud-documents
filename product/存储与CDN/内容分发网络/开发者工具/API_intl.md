Tencent Cloud CDN provides developers with a variety of APIs to cater for the operation & maintenance practices of different developers. For more details, please refer to [Tencent Cloud API Documentation](http://cloud.tencent.com/doc/api/231/%E7%AE%80%E4%BB%8B).

Tencent Cloud CDN provides the following APIs:

##### Domain Management APIs

| API                                | Action Name                              | Description                              |
| ---------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Add accelerated domain             | [AddCdnHost](https://cloud.tencent.com/doc/api/231/1406) | Add a domain to CDN. User can add a self-owned domain to CDN. |
| Activate CDN domain                | [OnlineHost](https://cloud.tencent.com/doc/api/231/1402) | Activate the acceleration service for a domain based on domain ID |
| Deactivate CDN domain              | [OfflineHost](https://cloud.tencent.com/doc/api/231/1403) | Deactivate the acceleration service for a domain based on domain ID. In this case, 404 status code will be returned for any access to the resources under the domain. |
| Delete accelerated domain          | [DeleteCdnHost](https://cloud.tencent.com/doc/api/231/1396) | Delete a domain based on the domain ID. The domain to be deleted must be in an offline status. |
| Modify origin server configuration | [UpdateCdnHost](https://cloud.tencent.com/doc/api/231/1397) | Set the origin server information based on domain ID and domain name. This can be set to a origin server domain name (supported domain name: PORT), or set to multiple origin server IPs ( supported IP: PORT). The port number should be between 0 and 65535. |
| Modify domain configuration        | [UpdateCdnConfig](https://cloud.tencent.com/doc/api/231/3933) | Based on domain ID and project ID, set cache configuration, cache mode, hotlink protection configuration, hosting header configuration, full-path cache configuration and origin server configuration and other configurations for a domain. |
| Set caching rules                  | [UpdateCache](https://cloud.tencent.com/doc/api/231/3934) | Set the cache rules corresponding to the domain name according to the domain ID. |
| Switch the project of domain       | [UpdateCdnProject](https://cloud.tencent.com/doc/api/231/3935) | Specify the ID of the project to which a domain will be switched based on domain ID. This allows switching between projects. |

##### Domain Query APIs

| API                                     | Action Name                              | Description                              |
| --------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Query domain information                | [DescribeCdnHosts](https://cloud.tencent.com/doc/api/231/3937) | Query the details of all domains, including all configuration information. Paged query is supported. |
| Query domain information by domain name | [GetHostInfoByHost](https://cloud.tencent.com/doc/api/231/3938) | Query the details of domains by domain name. Multiple domain query is supported. |
| Query domain information by domain ID   | [GetHostInfoById](https://cloud.tencent.com/doc/api/231/3939) | Query the details of domains by domain ID. Multiple domain query is supported. |

##### Consumption and Statistics Query APIs

| API                                 | Action Name                              | Description                              |
| ----------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Query CDN consumption statistics    | [DescribeCdnHostInfo](https://cloud.tencent.com/doc/api/231/3941) | Query the CDN statistics based on the information entered by user, such as time range, consumption type, project ID and domain name. |
| Query CDN consumption details       | [DescribeCdnHostDetailedInfo](https://cloud.tencent.com/doc/api/231/3942) | Query the CDN statistics based on the information entered by user, such as time range, consumption type, project ID and domain name. For query of statistics details, the time granularity for the time range of 1-3 days, 4-7 days and 8-90 days is 5 minutes, 1 hour and 1 day, respectively. |
| Query status code statistics        | [GetCdnStatusCode](https://cloud.tencent.com/doc/api/231/3943) | Query statistics details of 200, 206, 304, 404, 416 and 500 error codes based on the information entered by user, such as time range, project ID, domain name and time granularity. |
| Query TOP100 consumption statistics | [GetCdnStatTop](https://cloud.tencent.com/doc/api/231/3944) | Query TOP 100 ranking of provinces, ISPs and URLs  based on the information entered by user, such as time range, project ID, domain name, consumption type and time granularity. |

**Note**:
+ For queries of consumption and statistics, the time range of data is limited to **90 days**.

##### Refresh and Prefetch APIs

| API               | Action Name                              | Description                              |
| ----------------- | ---------------------------------------- | ---------------------------------------- |
| Query refresh log | [GetCdnRefreshLog](https://cloud.tencent.com/doc/api/231/3948) | Query the refresh log based on the information entered by user, such as time range and URL. |
| Refresh URL       | [RefreshCdnUrl](https://cloud.tencent.com/doc/api/231/3946) | Delete a resource from the node based on the resource URL (multiple URLs are allowed) submitted by user. If any user accesses the resource following the deletion, the request will be directly sent to origin server for the latest content. |
| Refresh Directory | [RefreshCdnDir](https://cloud.tencent.com/doc/api/231/3947) | Delete a resource from the node based on the resource directory (multiple directories are allowed) submitted by user. If any user accesses the resource following the deletion, the request will be directly sent to origin server for the latest resource. |

##### Log Query APIs

| API                      | Action Name                              | Description                              |
| ------------------------ | ---------------------------------------- | ---------------------------------------- |
| Query log download links | [GenerateLogList](https://cloud.tencent.com/doc/api/231/3950) | Query everyday log download links of a domain in a month based on the domain ID entered by user (only one ID is allowed). |


