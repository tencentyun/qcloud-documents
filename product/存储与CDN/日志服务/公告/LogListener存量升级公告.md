尊敬的腾讯云用户，您好！

为了提升产品体验，避免存量版本历史遗留问题影响您的业务，建议您尽快将 LogListener 版本实例 [升级至2.5.0以上](https://cloud.tencent.com/document/product/614/17414)。

登录 [日志服务控制台](https://console.cloud.tencent.com/cls/hosts)，体验日志服务更多新功能。


LogListener 版本支持新功能如下：

| LogListener 版本 | 功能支持                    | 功能说明                                 | 相关文档                                 |
| --------------- | ----------------------- | ------------------------------- | -------------------------------------- |
| v2.6.2         | 支持增量采集功能 | 支持用户在配置采集配置时，选择全量/增量采集策略。 | -     |
| v2.6.0         | 支持腾讯云 CVM 批量部署功能 | 支持在云服务器上批量部署 Loglistener 实例，对云服务器日志进行采集，用户无须再手动安装 Loglistener 相关配置。 | -     |
| v2.5.4          | 支持 LogListener 服务日志功能 | LogListener 服务日志功能支持记录 LogListener 端运行状态和采集监控的日志数据并配置可视化视图，提供重要指标数据。 | [LogListener 服务日志](https://cloud.tencent.com/document/product/614/55281) |
| v2.5.2          | 支持上传解析失败日志        | 所有解析失败的日志，均以 LogParseFailure 作为键名称（Key），原始日志内容作为值（Value）进行上传。 | -                                                            |
| v2.5.0          | 支持 LogListener 自动升级功能 | 支持用户在控制台预设时间段指定机器组进行 agent 自动升级，也可对目标机器实行手动升级。 | [LogListener 升级指南](https://cloud.tencent.com/document/product/614/55468) |
| v2.4.5          | 支持多行-完全正则采集模式   | LogListener 采集配置规则新增【多行-完全正则】提取模式采集日志。 | [完全正则（多行）](https://cloud.tencent.com/document/product/614/52366) |
| v2.4.5          | 支持毫秒级日志数据采集      | LogListener 使用采集时间支持毫秒级时间戳。开启时间采集后，LogListener 携带毫秒级的 Unix 时间戳进行上传。 | -                                                            |
| v2.3.9          | 支持采集路径配置黑名单      | 日志采集客户端 LogListener 支持配置采集路径黑名单，用户可以指定采集时忽略指定的目录和文件。 | -                                                            |
| v2.3.5          | 支持日志上下文检索功能      | 增加定位当前日志功能，快速定位目标日志滚动查看上下文。 增加多个字符串高亮功能，快速标记出用户检索的关键词。 增加过滤条件功能，快速定位目标字符串所在日志。 | [上下文检索分析](https://cloud.tencent.com/document/product/614/53248) |

感谢您的理解与支持，我们将持续更新功能特性，为您提供更优质可靠的产品服务！
若在此期间有任何问题可以进入 [在线客服](https://console.cloud.tencent.com/workorder/category) 咨询，我们将竭诚为您服务！


此致

腾讯云团队




