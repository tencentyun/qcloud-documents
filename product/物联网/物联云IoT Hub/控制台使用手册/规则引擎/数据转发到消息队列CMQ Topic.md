
### 概述
规则引擎支持用户配置规则将符合条件的设备上报数据转发到消息队列 CMQ Topic，用户在 [CMQ 控制台](https://console.cloud.tencent.com/mq/topic?rid=1) 或者使用云 API 订阅 CMQ Topic 后，就可以接收到来自 CMQ Topic 的消息推送。 CMQ Topic 的消息推送机制为用户提供了高可靠的异步接收消息的能力。
下图展示了规则引擎将数据转发给 CMQ Topic 的整个过程：
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_cmq_topic.png)


### 配置
1. 登录 [规则引擎](https://console.cloud.tencent.com/iotcloud/rules/rule) 控制台页面，点击所要配置的规则。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_cmqtopic01.png)

2. 单击【添加行为操作】按钮，并选择“数据转发到消息队列(CMQ-Topic)选项”，选择地域和Topic，最后单击【创建】即可。
![image](https://main.qcloudimg.com/raw/b44562eacac2546ce6cc6b63f159110e.png)


**说明**：第一次使用时会提示用户授权访问 CMQ Topic，用户需单击【立即授权】才能继续创建。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_cmqtopic03.png)

![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_cmqtopic04.png)



### 相关文档
 [使用云API创建 CMQ Topic 订阅](https://cloud.tencent.com/document/api/406/5853)
