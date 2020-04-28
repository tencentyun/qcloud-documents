## 概述
规则引擎支持用户配置转发规则，将符合条件的设备上报数据转发到云组件 MongoDB ，您可以在 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb) 或者使用云 API 创建 MongoDB 实例后，即可将设备消息写入到对应的 MongoDB 集合中。

下图展示了规则引擎将数据转发给 MongoDB 的整个过程：
![image](https://main.qcloudimg.com/raw/82bc37f6a13c0a357330c09476d8a891.png)


## 配置
1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)，单击左侧菜单【规则引擎】。
2. 进入规则引擎页面，单击需要配置的规则。
3. 在规则详情页面，单击【添加行为操作】。
>?第一次使用时会提示用户授权访问 MongoDB，您需单击【立即授权】才能继续创建。
![](https://main.qcloudimg.com/raw/2eed5a6e3d91545649ce2f3db40c2cc4.png)
4. 进入新增行为页面，选择“数据转发到云数据库（MongoDB）选项”, 最后单击【创建】即可。
![image](https://main.qcloudimg.com/raw/65829264cf904fb8a772b884214a7c02.png)  
5. 授权成功之后，需要配置 MongoDB 实例信息，如下图所示，配置分为如下几个步骤：
    1. 选择地区和 MongoDB 实例。如果账号下还没有实例，单击【创建实例】跳转到 MongoDB 控制台创建一个。
    2. 输入 MongoDB 实例的用户名，MongoDB 官网默认 mongouser。     
    3. 输入 MongoDB 实例的登录密码。
    4. 输入要写入的数据库名。
    5. 输入要写入的集合名。
![image](https://main.qcloudimg.com/raw/0c8503586939b3fe27cbc48339204aa4.png)
