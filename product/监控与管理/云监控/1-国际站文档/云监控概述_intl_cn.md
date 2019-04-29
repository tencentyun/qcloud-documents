腾讯云云监控可实时监控您的腾讯云云产品资源，是所有云产品的监控管理总入口。您可以在这里看到最全、最详细的监控数据。云监控实时对[云服务器](https://cloud.tencent.com/product/cvm.html)、[云数据库](https://cloud.tencent.com/product/cdb-overview.html)、[负载均衡](https://cloud.tencent.com/product/clb.html)等云产品监控，提取云产品关键指标，以监控图表形式展示。您可以通过使用腾讯云云监控全面地了解您的资源使用率、应用程序性能和云产品运行状况，并且支持设置自定义告警阈值，并根据您自定义的规则发送通知。

云监控服务主要用图表化信息帮助您了解云产品运行状况和性能，告警推送消息帮助您第一时间了解业务异常，让您无需额外开发，就能全面掌控云产品资源使用、运行情况。用户可以使用[云监控控制台](https://console.cloud.tencent.com/monitor/overview)、[云监控 API](https://cloud.tencent.com/doc/api/405) 或 [腾讯云 CLI](https://cloud.tencent.com/doc/product/440) 获取相关监控数据。

## 云监控提供的基本功能
您可在云监控控制台获得以下功能的入口：

| 模块    | 能力             | 主要功能                                    |
| ----- | -------------- | --------------------------------------- |
| 监控概况  | 云监控概况          | 提供总体概况，告警概况。总体监控信息一览                    |
| 我的告警  | 支持用户自定义告警阈值    | 当前支持云服务器、云数据库、CDN、VPN等产品的告警设置服务         |
| 云产品监控 | 查看云产品监控视图      | 当前云监控控制台支持云数据库、云服务器、memcached 等云产品的监控视图 |
| 自定义监控 | 查看用户自定义的监控指标数据 | 用户预先定义好的自定义监控指标及上报的数据                   |
| 流量监控  | 流量监控           | 查看用户整体带宽信息                              |

## 云监控支持的服务
当前，云监控产品可自动监控以下服务。一旦您开始使用某服务，它会自动向云监控发送指标数据。

> 当前云监控提供1分钟、5分钟、1小时、1天多种监控数据统计粒度，如云服务器、云数据库等大部分产品均能支持1分钟监控粒度，即每隔 1 分钟统计一次数据；部分产品仅支持5分钟统计粒度，即每隔 5 分钟统计一次数据。

- [云服务器 CVM](https://cloud.tencent.com/doc/product/213)
- [云硬盘 CBS](https://cloud.tencent.com/doc/product/362)（仅当挂载在运行的云服务器上时）
- [负载均衡 CLB](https://cloud.tencent.com/doc/product/214)
- [专线 DC](https://cloud.tencent.com/doc/product/216)
- [内容分发网络 CDN](https://cloud.tencent.com/doc/product/228)
- [对象存储服务 COS](https://cloud.tencent.com/doc/product/430)
- [云数据库 MySQL](https://cloud.tencent.com/doc/product/236)
- [云数据库 TDSQL](https://cloud.tencent.com/doc/product/237)
- [云数据库 SQL Server](https://cloud.tencent.com/doc/product/238)
- [云存储 Redis](https://cloud.tencent.com/doc/product/239)
- [云缓存 Memcached](https://cloud.tencent.com/doc/product/241)

## 云监控的架构
云监控为用户提供了基础指标监控和数据存储，您可通过控制台查看这些产品的指标数据，也可以通过 API 拉取指标数据。如果云监控提供的基础指标监控无法满足您的诉求，您还可以使用 [自定义监控](https://cloud.tencent.com/doc/product/397) 功能自行上报指标数据，并在云监控控制台查看相应的数据图表。

云监控是一个为所有云资源存储指标数据的空间。所有其他云产品（例如 CVM）将指标数据存放在存储库中，而您可以根据这些指标进行检索。同时在云监控控制台中使用云产品存放的原始数据进行统计指标，然后以图形化的方式显示数据。

![](http://mc.qcloudimg.com/static/img/e17600ac6f357ce818470a179fde9aca/image.png)