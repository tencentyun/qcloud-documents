### 概述
规则引擎支持用户配置转发规则，将符合条件的设备上报数据转发到云组件 MongoDB ，用户在 [MongoDB控制台](https://console.cloud.tencent.com/mongodb) 或者使用云 API 创建 MongoDB 实例后，就可以将设备消息写入到对应的 MongoDB 集合中。
下图展示了规则引擎将数据转发给 MongoDB 的整个过程：
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forward_mongodb.png)


### 配置
1. 登录 [规则引擎](https://console.cloud.tencent.com/iotcloud/rules/rule) 控制台页面，单击所要配置的规则。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forward_mysql_list_rules.png)

2. 单击【添加行为操作】按钮，并选择“数据转发到云数据库(MongoDB)选项”, 最后单击【创建】即可。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forward_mongodb_select_action.png)  
**说明**：第一次使用时会提示用户授权访问 MongoDB，用户需单击【立即授权】才能继续创建。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forwad_mongodb_need_auth.png)
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forwad_mongodb_now_auth.png)

3. 授权成功之后，需要配置 MongoDB 实例信息，如下图所示，配置分为如下几个步骤：

    1. 选择地区和 MongoDB 实例。如果帐号下还没有实例，那么单击"创建实例"跳转到 MongoDB 控制台创建一个
    2. 输入 MongoDB 实例的用户名,MongoDB 官网默认 mongouser。     
    3. 输入 MongoDB 实例的登录密码
    4. 输入要写入的数据库名。
    5. 输入要写入的集合名。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forward_mongodb_config_instance.png)




