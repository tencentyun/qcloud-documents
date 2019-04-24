## 概述
通过将感兴趣的消息字段转发到另一个 Topic，可以实现不同设备间的 M2M 通信。Topic 的填写支持以下方式：
- **填写一个 Topic 名字**
例如 `${productId}/house_monitor/thermometer`，这样就会把满足规则的消息转发到这个 Topic。
- **填写带变量的 Topic 名字**
例如 `${procductId}/${house}/device`, 其中用 `${}` 括起来的 `house` 就代表一个变量名，这个变量名是 SELECT 语句中选取出来的字段内容。

## 示例说明
该示例主要说明带变量的转发 Topic 是如何生效的。假设定义了一条规则，示例如下：
```
SELECT temperature as t, house 
FROM house_monitor/thermometer/get 
WHERE house="tencent" AND temperature > 40
```

此规则从消息中提取了 `t` 和 `house` 这两个字段的值，假定 `house` 字段的内容为 `tencent`。
此时如果定义了转发给 `house_monitor/app/{house}` 这个 Topic，那么规则引擎就会把这个 Topic 中的 `${house}` 变量替换为 "tencent"， 从而将 `t` 和 `house` 的字段内容发送给 `house_monitor/app/tencent` 这个 Topic。

转发全过程如下图所示：
![image](https://mc.qcloudimg.com/static/img/2fd61f602479ab39f47e7d6eb4f93558/gui3.png)
## 配置
1. 登录物联网通信控制台，选择左侧菜单栏【[规则引擎](https://console.cloud.tencent.com/iotcloud/rules/rule)】，单击需要配置的规则。
![](https://main.qcloudimg.com/raw/0a0a0e5bc48aa0d4492ac0b8d3c7413c.png)
2. 在规则详情页面，单击【添加行为】。
3. 在弹出的“新增行为”窗口，选择行为“republish”，填写要转发至的 Topic 名称，单击【创建】即可。
![image](https://main.qcloudimg.com/raw/1b87e2ca055b5d0581c2fe7e6568c8fb.png)
物联网通信平台会将上报数据发转至该 Topic。

