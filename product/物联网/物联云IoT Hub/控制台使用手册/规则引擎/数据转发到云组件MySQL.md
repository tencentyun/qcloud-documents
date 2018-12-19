### 概述
规则引擎支持用户配置转发规则，将符合条件的设备上报数据转发到云组件 MySQL ，用户在 [MySQL 控制台](https://console.cloud.tencent.com/cdb) 或者使用云 API 创建 MySQL 实例和表后，就可以将设备消息中的指定字段写入到对应的 MySQL 表中。指定写入表中的字段是高度可配置的，如何配置写入字段在文档后续中会有说明(配置 MySQL 实例小节中)。 
下图展示了规则引擎将数据转发给 MySQL 的整个过程：
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forward_mysql.png)

### 配置
1. 登录 [规则引擎](https://console.cloud.tencent.com/iotcloud/rules/rule) 控制台页面，单击所要配置的规则。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forward_mysql_list_rules.png)

2. 单击【添加行为操作】按钮，并选择“数据转发到云数据库(MySQL)选项”, 最后单击【创建】即可。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forward_mysql_select_action.png)
**说明**：第一次使用时会提示用户授权访问 MySQL，用户需单击【立即授权】才能继续创建。
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forwad_mysql_need_auth.png)
![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forward_mysq_auth_now.png)

3. 授权成功之后，需要配置 MySQL 实例信息和写入的字段信息，如下图所示，配置分为如下几个步骤：
3.1 选择地区和 MySQL实例。如果帐号下还没有实例，那么点击"创建实例"跳转到 MySQL 控制台创建一个
3.2 输入刚才创建的 MySQL 实例的用户名。     
3.3 输入实例的登录密码
3.4 选择要写入的数据库名。如果创建的 MySQL 实例下还没有建立数据库的话，单击"建库/建表"按钮跳转到 MySQL 控制台去创建一个新的数据库。具体操作可以参见文档末尾的"相关文档"小节。
3.5 选择要写入的表。如果创建的数据库下还没有建立表的话，点击"建库/建表"按钮跳转到 MySQL 控制台去创建一个新的表。
3.6 配置要写入的字段。这里有两列："字段名称"和"值"。"字段名称"对应的是数据库表中的字段，表示要写入的字段。"值"表示要写入对应字段的值。值的来源可以是消息体(注意消息体必须是 Json 格式才支持提取值 )，或者是在这里填入常量。
>注意：
>如果来源是消息体，那么使用"${}"来引用消息体内的字段。如果要指定常量，直接填相应的值就行了，比如 5 或者 hello 这样的数字或者字符串字面值。

![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_forward_mysql_config_instance.png)

### 相关文档
[创建 MySQL 库和表教程](https://cloud.tencent.com/document/product/236/8465)

