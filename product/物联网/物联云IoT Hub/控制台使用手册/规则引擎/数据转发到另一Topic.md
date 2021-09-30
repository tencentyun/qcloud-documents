
## 概述
通过将感兴趣的消息字段转发到另一个 Topic，即可实现不同设备间的 M2M 通信。Topic 的填写支持以下方式：
- **填写一个 Topic 名字**
例如 `${productId}/house_monitor/thermometer`，即可将满足规则的消息转发到这个 Topic。
- **填写带变量的 Topic 名字**
例如 `${productId}/${house}/device`，其中用 `${}` 括起来的 `house` 就代表一个变量名，这个变量名是 SELECT 语句中选取出来的字段内容。

## 示例说明
该示例主要说明带变量的转发 Topic 是如何生效的。假设定义了一条规则，示例如下：
```
SELECT temperature as t, house 
FROM house_monitor/thermometer/get 
WHERE house="tencent" AND temperature > 40
```

此规则从消息中提取了 `t` 和 `house` 这两个字段的值，假定 `house` 字段的内容为 `tencent`。
此时如果定义了转发给 `house_monitor/${house}/app` 这个 Topic，那么规则引擎则会将这个 Topic 中的 `${house}` 变量替换为 "tencent"， 从而将 `t` 和 `house` 的字段内容发送给 `house_monitor/tencent/app` 这个 Topic。

转发全过程如下图所示：
![image](https://main.qcloudimg.com/raw/d4914e4b87c30f9240bbfcd62411be8a.png)

## 配置
1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)，选择左侧菜单栏**规则引擎**，单击需要配置的规则。
2. 在规则详情页面，单击**添加行为操作**。
3. 在弹出的“添加规则”窗口，填写相关信息。单击**保存**即可。
 - 选择行为类型为“republish”。
 - 填写要转发至的 Topic 名称。
![](https://main.qcloudimg.com/raw/ecec657128df4e50498213fda2aaa23f.jpg)

物联网通信平台即可将上报数据发转至该 Topic。

## 转发消息服务质量等级

消息从源 Topic 转发到其它 Topic 时消息服务质量等级不会变化。
- 设备端发布的消息服务质量等级为 QOS0 时则规则引擎将按照 QOS0 的消息进行转发，发布的消息服务质量等级为 QOS1 时则按照 QOS1 进行转发。
- 转发的消息服务质量等级为0时，若转发失败则消息会被丢弃；转发的消息服务质量等级为1，若消息转发失败则会进行转发重试。重试按照3s，6s，9s的时间间隔依次进行三次，若三次重试均失败则将消息保存在离线消息队列。

