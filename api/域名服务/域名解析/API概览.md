## 1. 域名解析相关接口

| 接口功能 | Action Name | 功能描述 |
|---------|---------|---------|
| [创建域名](http://www.qcloud.com/doc/api/262/%E5%88%9B%E5%BB%BA%E5%9F%9F%E5%90%8D) | CreateDomain | 云解析平台中添加指定的主域名，例如qcloud.com。 |
| [查询域名](http://www.qcloud.com/doc/api/262/%E6%9F%A5%E8%AF%A2%E5%9F%9F%E5%90%8D) | DescribeDomains | 查询云解析的所有域名列表。 |
| [开启域名解析](http://www.qcloud.com/doc/api/262/%E5%BC%80%E5%90%AF%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90)    | StartDomain | 开启单个主域名的解析。 |
| [暂停域名解析](http://www.qcloud.com/doc/api/262/%E6%9A%82%E5%81%9C%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90) |  StopDomain | 暂停单个主域名的解析。 |
|[删除域名](http://www.qcloud.com/doc/api/262/%E5%88%A0%E9%99%A4%E5%9F%9F%E5%90%8D) | DeleteDomain | 从云解析平台中移除指定的主域名。 |

## 2. 解析记录相关接口

| 接口功能 | Action Name | 功能描述 |
|---------|---------|---------|
| [创建记录](https://www.qcloud.com/doc/api/383/%E5%88%9B%E5%BB%BA%E8%AE%B0%E5%BD%95) | CreateResourceRecord | 指定主域名、子域添加一条解析记录，支持关联到云服务器、云数据库资源。 |
| [查询管理记录任务](https://www.qcloud.com/doc/api/383/4536)  | GetTaskResult | 添加关联云资源记录类型是异步操作，该接口支持根据taskId查询关联记录任务的执行结果。 |
| [查询记录](https://www.qcloud.com/doc/api/383/%E6%9F%A5%E8%AF%A2%E8%AE%B0%E5%BD%95) | DescribeResourceRecord | 查询指定主域名的所有解析记录。 |
| [查询关联记录详情](https://www.qcloud.com/doc/api/383/%E6%9F%A5%E8%AF%A2%E5%85%B3%E8%81%94%E8%AE%B0%E5%BD%95%E8%AF%A6%E6%83%85) |  DescribeResourceRecordDetail | 查询指定云资源的解析记录。 |
| [修改记录](https://www.qcloud.com/doc/api/383/%E4%BF%AE%E6%94%B9%E8%AE%B0%E5%BD%95) | UpdateResourceRecord | 修改指定主域名、子域的解析记录。 |
| [启用记录](https://www.qcloud.com/doc/api/383/%E5%90%AF%E7%94%A8%E8%AE%B0%E5%BD%95) | StartResourceRecord | 开启指定主域名、子域某条记录的解析。 |
| [暂停记录](https://www.qcloud.com/doc/api/383/%E6%9A%82%E5%81%9C%E8%AE%B0%E5%BD%95) | StopResourceRecord | 暂停指定主域名、子域某条记录的解析。 |
| [删除记录](https://www.qcloud.com/doc/api/383/%E5%88%A0%E9%99%A4%E8%AE%B0%E5%BD%95)  | DeleteResourceRecord | 移除指定主域名的一条解析记录。 |

## 2. 2.0版本接口

| 接口功能 | Action Name | 功能描述 |
|---------|---------|---------|
| [获取域名记录列表](https://www.qcloud.com/doc/api/383/5609) | RecordList | 可根据域名、子域名筛选获取解析记录列表。 |

Ps：2.0版本接口将陆续更新，不影响现有版本接口的使用。