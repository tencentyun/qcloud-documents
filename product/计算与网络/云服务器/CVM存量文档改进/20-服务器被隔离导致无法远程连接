本文档介绍云服务器因外网被隔离导致无法登录问题的解决方案。

## 故障现象
云服务器被隔离可能由于该台服务器违反了当前法律法规的要求。您可以通过以下方式查看该台服务器是否处于被隔离的状态。
- 云服务器外网被隔离时，将会通过 [控制台站内信](https://console.cloud.tencent.com/message) 或发送短信的方式将违规隔离通知到您。
 - 站内信图片：
![](//mc.qcloudimg.com/static/img/3c8ecd4ac301180e3632a25343be0697/image.png)
或者
![](//mc.qcloudimg.com/static/img/cd3fbf748d3ff61adf3d2198853d18de/image.png)
 - 短信图片：
![](//mc.qcloudimg.com/static/img/afaff154fa12695844055422f4f103e6/image.png)
- [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 中的"监控/状态"栏 显示该云服务器状态：隔离中。


## 问题原因
云服务器出现违规事件或风险事件时，会对违规机器进行部分隔离操作（除内网的22 、36000 、3389登录接口，其余网络访问全部隔离，开发者可以通过跳板机的方式登录服务器）。
详见 [云安全违规事件的等级划分及处罚说明](https://cloud.tencent.com/document/product/301/2003)。

## 解决办法

 1. 按照站内信或者短信提示处理违规内容。处理好安全隐患，必要时重做系统。
 2. 如果不是您个人行为导致的违规，那么您的服务器有可能已被恶意入侵。解决方案请参考： [主机安全](https://cloud.tencent.com/document/product/296)。
 3. 排除安全隐患或停止违规后，请通过 [提交工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%20CVM) 联系客服解除隔离。

