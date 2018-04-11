## 数据转发到消息队列CMQ Topic

### 概述
规则引擎支持用户配置规则将符合条件的设备上报数据转发到消息队列 CMQ Topic，用户在[CMQ控制台](https://console.cloud.tencent.com/mq/topic?rid=1)或者使用云API订阅CMQ Topic后，就可以接收到来自CMQ Topic的消息推送。 CMQ Topic的消息推送机制为用户提供了高可靠的异步接收消息的能力。
下图展示了规则引擎将数据转发给 CMQ Topic 的整个过程：
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_cmq_topic.png)


### 配置
1. 登录 [规则引擎](https://console.cloud.tencent.com/iotcloud/rules/rule) 控制台页面，点击所要配置的规则。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_cmqtopic01.png)

2. 点击【添加行为操作】按钮，并选择“数据转发到消息队列(CMQ-Topic)选项”, 最后点击【创建】即可。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_cmqtopic02.png)


**说明**：第一次使用时会提示用户授权访问 CMQ Topic，用户需点击【立即授权】才能继续创建。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_cmqtopic03.png)

![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_cmqtopic04.png)



### 相关文档
1. [使用云API创建CMQ Topic订阅](https://cloud.tencent.com/document/api/406/5853)

