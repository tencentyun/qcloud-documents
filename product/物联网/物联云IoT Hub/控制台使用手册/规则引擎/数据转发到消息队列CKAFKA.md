## 概述
规则引擎支持用户配置规则将符合条件的设备上报数据转发到 [消息队列 CKAFKA](https://cloud.tencent.com/product/CKafka) （以下简称 CKAFKA ），用户的应用服务器再从 CKAFKA 中读取数据内容进行处理。以此利用 CKAFKA 高吞吐量的优势，为用户打造高可用性的消息链路。  

下图展示了规则引擎将数据转发给 CKAFKA 的整个过程：

![avatar](https://main.qcloudimg.com/raw/ae9179db06123982f14857891aeabb8a.png)

## 配置
1. 登录 [规则引擎](https://console.cloud.tencent.com/iotcloud/rules/rule) 控制台页面，点击所要配置的规则。
![](https://main.qcloudimg.com/raw/397a3f63168850cfeaeacc02098b66e7.png)

2. 在规则详情页面，单击【添加行为】按钮。在弹出的“新增行为”窗口，选择行为“数据转发到消息队列（CKAFKA）”；依次选择 CKAFKA 实例和 Topic，点击【创建】即可。
![avatar](https://main.qcloudimg.com/raw/38ae9c8f13937126d3fb0adba61d28d2.png) 
**说明：**第一次使用时会提示用户授权访问CKAFKA，用户需点击【授权访问CKAFKA】才能继续创建。
![avatar](https://main.qcloudimg.com/raw/c4824d0ea85b05ea6ea524feed4c02f2.png) 
3. 完成以上配置后，物联云平台会将符合规则条件的设备上报数据转发至用户配置的 CKAFKA ；用户可参考 [【CKAFKA使用入门】](https://cloud.tencent.com/document/product/597/10112) 在自己的应用服务器上读取数据进行处理。