## 概述
腾讯云事件总线（EventBridge）与腾讯千帆鹊桥 iPaaS 携手，将安全、稳定、高效的无服务器事件管理平台和腾讯千帆鹊桥 iPaaS 的多种连接器集成，帮助您轻松实现无服务器事件驱动架构。
当账号下云服务 ping 不可达，或异常重启时，可配置 EB 收集告警通过腾讯千帆鹊桥 iPaaS 配置企业微信机器人、钉钉机器人和飞书机器人。触达到对应企业群中，让异常告警第一时间触达到运维人员，可作出相应措施。

## 操作场景
假设您的企业正在使用企业微信、钉钉或飞书作为司内协同办公软件，您同时有使用大量的腾讯云云上资源：云服务器、云存储、负载均衡等。作为该企业的 IT 负责人，您希望腾讯云云上资源出现异常时，能有告警信息直接触达到工作群，方便 IT 部同事能第一时间处理。您可以参考如下流程配置一个简单的告警推送流。

![](https://qcloudimg.tencent-cloud.cn/raw/fda6e7d8541e5fe817157853cdea0745.png)

您可参考以下步骤进行配置：

## 腾讯千帆鹊桥 iPaaS 端配置指引
**腾讯云事件总线**到**企业微信机器人**集成流配置操作指引：

### 前期准备

#### 步骤1：获取腾讯云事件总线相关配置

您可在 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey，通过 API 获取告警信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9aaef61d9f50481f6274aca38cc61e13.png)

#### 步骤2：获取企业微信、钉钉或飞书机器人相关配置 

您可根据以下指引获取 webhook 链接。
<dx-tabs>
::: 企业微信机器人
添加企业微信机器人及获取 webhook 可参考 [产品文档](https://cloud.tencent.com/document/product/1270/61088#.E6.AD.A5.E9.AA.A45.EF.BC.9A.E9.85.8D.E7.BD.AE.E6.89.A7.E8.A1.8C.E5.BA.94.E7.94.A8.EF.BC.88.E4.BC.81.E4.B8.9A.E5.BE.AE.E4.BF.A1.E6.9C.BA.E5.99.A8.E4.BA.BA.EF.BC.89)。
![](https://qcloudimg.tencent-cloud.cn/raw/febe355bcffe250349688a01bfb9f94c.png)

:::
::: 钉钉机器人
添加钉钉机器人及获取 webhook 可参考 [产品文档](https://developers.dingtalk.com/document/robots/custom-robot-access)。
  ![](https://qcloudimg.tencent-cloud.cn/raw/e3886ca6597367aa1b6465a899d4eed9.png)
:::
::: 飞书机器人
添加钉钉机器人及获取 webhook 可参考 [产品文档](https://www.feishu.cn/hc/zh-CN/articles/360024984973#lineguid-AQqBzn)。
:::
</dx-tabs>

 

### 集成流设计
#### 步骤1：创建集成流 

1. 登录 [企业集成服务控制台](https://console.cloud.tencent.com/eis)。
2. 单击**深度集成 > 选择对应项目 > 添加应用**，选择空白应用，并命名为 “EB - 企业微信机器人（应用名称可自行定义）”。
![](https://qcloudimg.tencent-cloud.cn/raw/29fa12309ec3063d66a7dae258f6c0eb.png)
3. 单击**确定**，进入默认对应应用名称（此处为 “EB - 企业微信机器人”）的应用编辑页。选中 NewFlow 进入集成流编辑页面。
![](https://qcloudimg.tencent-cloud.cn/raw/bb90265829e2d06a62320d571571d036.png)

#### 步骤2：配置 Trigger  

配置腾讯云事件总线连接器，作为集成流的触发器，具体步骤如下：

1. 单击应用编辑页 “Trigger 框”中的未配置。在弹框提示选择 “Trigger 组件”，此处请选择**腾讯云事件总线**作为触发器。选择**EventBridge**。
![](https://qcloudimg.tencent-cloud.cn/raw/3063e67483355f2d5a6e3498c6e7a286.png)
2. 单击**新建**腾讯云事件总线连接器配置。
![](https://qcloudimg.tencent-cloud.cn/raw/1b182c7f0aff22b30808caecaf9b0988.png)
3. 填写连接器配置名称为 “腾讯云事件总线 #0（可自定义名称）”，并单击**下一步**。
    - 地域：填写告警云服务资源所在地域即可。
    - SecretId 及 SecretKey：请通过 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 获取。
![](https://qcloudimg.tencent-cloud.cn/raw/5b4d9246249e576e4185a87ba66f42bc.png)
4. 填写通用配置。
    - 监听域名：自定义英文字母命名，例如：ebtestdd
    - 监听路径：/
    - 消息属性：payload
    - 类型选择：空
![](https://qcloudimg.tencent-cloud.cn/raw/9ec80014b15ca3d9717f61e105e56232.png)

#### 步骤3：保存 EventBridge 信息 

使用逻辑组件 Set Variable 保存 EventBridge 事件的 region、资源 ID、requestId 等信息，具体步骤如下：
1. 单击画布中的 “+” 弹出组件筛选框。选择 Set Variable 组件。
![](https://qcloudimg.tencent-cloud.cn/raw/4862e35aadb19578d572b8778369ad1d.png)
2. 将事件总线中的 region、资源 ID、requestId 用变量名 body 通过存在 message 的 variables 进行保留。
![](https://qcloudimg.tencent-cloud.cn/raw/ae61bbd33ca05384a2ffe8dbd2c417a8.png)
3. 单击变量值后面的 f (x) 切换到表达式输入模式，使用表达式获取变量值。
    - 变量值为：any
    - 表达式如下所示：
   ```
      def dw_process (msg):
           return 
   ```
![](https://qcloudimg.tencent-cloud.cn/raw/4a92a9ed0edb0874b67bf7d6d8e8a3aa.png)


#### 步骤4：配置 Try 组件捕获子流错误 

Try 组件的作用是捕获错误，可以捕获 Try 中子流运行时抛出的错误和系统错误。当 Try 中配置的子流抛出错误后，Catch 可根据配置的错误类型进行捕获。配置步骤如下：
1. 单击 画布中的 “+” 弹出组件筛选框。选择 Try 组件。
2. 单击画布中的 Catch 选框。设置错误类型为 ANY。
    - 错误类型：ANY，当 Catch 中配置的错误类型为 "any" 时，可以捕获所有错误。
![](https://qcloudimg.tencent-cloud.cn/raw/393185a65a1f0cd3f91e5c73a8b790c0.png)

#### 步骤5：配置 Logger 组件，输出报错到控制台 

Logger 组件用来在控制台输出日志，并不会改变 message 中的内容。详情见 [Logger 组件](https://cloud.tencent.com/document/product/1270/55402)。
1. 单击 画布中的 “+” 弹出组件筛选框。选择 Logger 组件。
2. 配置 Logger 组件。
    - 日志级别：ERROR
    - 日志类别：ebtest
    - 日志类容：any
    - 表达式如下所示：
  ```
      def dw_process (msg):
          return 
  ```
![](https://qcloudimg.tencent-cloud.cn/raw/3197da160ecc382bcc4b214a6980e6d5.png)

#### 步骤6：配置机器人推送消息（企业微信机器人）[](id:step6)

1. 单击 画布中的 “+” 弹出组件筛选框。选择**企业微信机器人**连接器。
2. 此处请选择**发送 markdown 消息**。
![](https://qcloudimg.tencent-cloud.cn/raw/962cd4080c43e376fce199a9e3ffc23d.png)
3. 单击**新建**企业微信机器人连接器配置。
![](https://qcloudimg.tencent-cloud.cn/raw/3d19a228b6170989515cf64835090b83.png)
4. 填写连接器配置名称为 “企业机器人 #0（可自定义名称）”，并单击下一步。
    - webhook 地址：填入完成的带 https 协议的 Webhook 地址。添加企业微信机器人及获取 webhook 可参考 [产品文档](https://cloud.tencent.com/document/product/1270/61088#.E6.AD.A5.E9.AA.A45.EF.BC.9A.E9.85.8D.E7.BD.AE.E6.89.A7.E8.A1.8C.E5.BA.94.E7.94.A8.EF.BC.88.E4.BC.81.E4.B8.9A.E5.BE.AE.E4.BF.A1.E6.9C.BA.E5.99.A8.E4.BA.BA.EF.BC.89)。
![](https://qcloudimg.tencent-cloud.cn/raw/a073bc23adb138f6c232c71752d9b1e5.png)
5. 填写通用配置
单击变量值后面的 f(x) 切换到表达式输入模式，使用表达式获取变量值。
    - 表达式示例：
```python
      def dw_process (msg):
       result = '''<font color=\"warning\"> 收到告警信息，请及时处理 </font>\n
         > 实例 ID:<font color=\"comment\">''' + msg.vars.get ('body').get ('subject') + '''</font>
         > 地域:<font color=\"comment\">''' + msg.vars.get ('body').get ('region') + '''</font>
         > 事件名称:<font color=\"comment\">''' + msg.vars.get ('body').get ('type')  + '''</font>'''
    return result;
```
    - 消息属性：payload
    - 类型选择：空
![](https://qcloudimg.tencent-cloud.cn/raw/a2d29ac2a3b00a34ab9cb1b9ff9f0db3.png)

>! 若要将推送端切换为钉钉机器人或飞书机器人。修改步骤6的连接器配置即可，其余配置及参数均相同。

#### 步骤7：发布集成流 

按照上述步骤配置完成后，单击控制台右上角的发布按钮即可发布集成应用。
用户可自行选择单个地域或多个地域发布。
![](https://qcloudimg.tencent-cloud.cn/raw/19b24858628f0788256005172b247a6d.png)

## 腾讯云事件总线端配置指引
完成腾讯千帆鹊桥 iPaaS 端的集成流配置后，还需要在腾讯云事件总线端配置相应事件集规则，才可完成按照所配置的规则触发集成流。

腾讯云事件总线控制台，自带一个默认的云服务事件集，包含了常见了云上事件连接器：负载均衡、云服务器、文件存储等，都配有不同的事件告警，用户可以根据需要创建对应事件规则使用。


#### 步骤1：开通事件总线 
使用事件总线前需要主账号给对应角色授权。您可参考以下文档开始使用事件总线：
- [开通事件总线](https://cloud.tencent.com/document/product/1359/56068)
- [告警推送配置与管理](https://cloud.tencent.com/document/product/1359/61494)
- [目前接入事件总线的事件源](https://cloud.tencent.com/document/product/1359/56074)

#### 步骤2：新建事件规则 

开通后，登录 [事件总线控制台](https://console.cloud.tencent.com/eb) 选择**事件规则**，单击**新建事件规则**。本文以云服务器为例。按照如下截图创建规则后，单击**确定**保存规则即可。操作步骤详情见 [创建事件规则](https://cloud.tencent.com/document/product/1359/56085)。

![](https://qcloudimg.tencent-cloud.cn/raw/2b2a1e22a0857a8d4dfe389946e58565.png)
- 地域：北京上海广州，用户可自行选择。
- 事件集：在新建事件规则时，控制台左上方选择。（默认事件集，包含了常见了云上事件连接器）
- 规则名称：用户自定义，以 EBqw1 为例。
- 规则说明：用户自定义，可以用一段剪短的话描述此规律的应用范围，方便区分。
- 事件模式：可先云服务预设或自定义事件，例如：云服务预设事件。
- 云服务类型：包含多个事件源，例如：云服务器。
- 事件类型：可选择单个事件或全部事件，例如：全部事件。
- 事件模式预览：系统根据用户的选择自动生成。
- 触发方式：选择云函数（腾讯千帆鹊桥 iPaaS 场景下）。
- 函数类型：选择模板函数（腾讯千帆鹊桥 iPaaS 场景下）。
- 函数模板：选择 SaaS 连接器（EIS 提供支持）（千帆 i 腾讯千帆鹊桥 iPaaS 场景下）。
- 命名空间：default。
- 函数名称：用户自定义，列 ebqw1。
- 集成项目：选择上述配置集成流所在的项目。
- 应用：选择上述配置对应的应用名称。。
- 集成流：选择上述配置对应的流名称。
- 立即启用事件规则：开启。

>! 当集成应用处于运行中状态时，才可以在事件规则中被选中。

#### 步骤3：模拟事件告警触发 

1. 登录 [事件总线控制台](https://console.cloud.tencent.com/eb) 选择**事件集**，本文以默认事件集为例。单击**发送事件 > 默认模板**，选择**云服务器** > **云服务器 - 机器重启**。
![](https://qcloudimg.tencent-cloud.cn/raw/da8b53b837c32753284a09d9deacf8d5.png)
2. 会自动生成事件字段，单击**确定**即可触发模拟告警信号。
![](https://qcloudimg.tencent-cloud.cn/raw/4e8c22cc2f60f0952753dddf3275b78d.png)
3. 验证模拟效果。
 成功触发后，已配置的接收端内部群会受到对应机器人的消息推送。消息推送的内容，与集成流设计 [步骤6](#step6) 的表达式内容相关。
   ![](https://qcloudimg.tencent-cloud.cn/raw/55fe0d99de7d11445c9b61b5def07078.png)

#### 实测效果展示图 
按照上述配置完成后，当服务器或者配置的其他规则有对应规则触发时，机器人会自动推送消息到对应群聊。保证故障信息触达的及时性。

尝试触发服务器重启，分别测试了三个集成流的展示如下：

- 企业微信机器人：
![](https://qcloudimg.tencent-cloud.cn/raw/01a220198336b6d2fdb2b184c59a4f30.png)
企微微信群推送消息：
![](https://qcloudimg.tencent-cloud.cn/raw/8e7190cedef1105cc0881035ff284088.png)

- 钉钉内部群推送消息：
![](https://qcloudimg.tencent-cloud.cn/raw/3c9ce678ea42210e53fdcb379b089311.png)
- 飞书内部群推送消息：
![](https://qcloudimg.tencent-cloud.cn/raw/efde0393c39545707c39706d9c26b8c1.png)


