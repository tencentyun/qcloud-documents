## 概述
规则引擎支持用户配置转发规则，将符合条件的设备上报数据转发到云组件 MongoDB ，您可以在 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb) 或者使用云 API 创建 MongoDB 实例后，即可将设备消息写入到对应的 MongoDB 集合中。

下图展示了规则引擎将数据转发给 MongoDB 的整个过程：
![](https://main.qcloudimg.com/raw/ce65ecf23f563cf2226c17e690cdcf1d.png)

## 配置
1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)，单击左侧菜单**规则引擎**。
2. 进入规则引擎页面，通过单击“规则名称”选择需要配置的规则。
3. 在规则详情页面，单击**添加行为操作**。
>?第一次使用时会提示用户授权访问 MongoDB，您需单击**立即授权**才能继续创建。
![](https://main.qcloudimg.com/raw/e8a768ff185aafebf79b63db710bccc9.jpg)
4. 进入新增行为页面，选择“数据转发到云数据库（MongoDB）选项”。
![](https://main.qcloudimg.com/raw/c4be9f3dfa1ec60dad5a9246db29f40d.jpg)
5. 授权成功之后，需要配置 MongoDB 实例信息，如下图所示，配置分为如下几个步骤：
    1. 选择地区和 MongoDB 实例。如果账号下还没有实例，单击**创建实例**跳转到 MongoDB 控制台创建一个。
    2. 输入 MongoDB 实例的用户名，MongoDB 官网默认 mongouser。     
    3. 输入 MongoDB 实例的登录密码。
    4. 输入要写入的数据库名。
    5. 输入要写入的集合名。
![](https://main.qcloudimg.com/raw/5afe47d64dac569a759a69dc9c02fbd5.jpg)

## 重发机制

重发机制用于在消息转发过程中发生失败的情况下，进行再次重发以达到接受消息的目的，具体说明如下：
- 若消息转发失败，系统则会进行转发重试，重试按照1s、3s、10s的时间间隔依次进行，若三次重试均失败，则将消息丢弃掉。
- 若用户配置了“转发错误行为操作”，在三次重试失败后，将按“转发错误行为操作”的配置，再进行一次消息转发，如果仍失败，则将消息丢弃掉。
