## 简介

通过编写 XML 是开发连接器（Connector）最简单的方式，一个 Connector 即为一个 XML 文件。
本文将通过一个 XML 描述的 hello-world 连接器，介绍如何创建 hello-world 操作，并通过使用 [Logger](https://cloud.tencent.com/document/product/1270/46959#logger) 组件来打印日志 Hello World!。


## 操作步骤

### 准备 XML 文件


本文提供以下 XML 文件，您需要将其保存到本地，并命名为 xxxx.xml 格式的文件。
```xml
<module apiVersion="1.0.0" apiType="XML" expressionType="dataway" expressionVersion="1.0.0" >
    <name>hello-world</name>
    <version>1.0.0</version>
    <display-name>HelloWorld</display-name>
    <description>Hello World !!!</description>
    <declaration>
        <operations>
            <operation name="hello-world" flowRef="hello-world"/>
        </operations>
    </declaration>
    <body>
        <flows>
            <flow name="hello-world">
                <logger message="Hello World!" level="INFO"/>
            </flow>
        </flows>
    </body>
</module>
```

### 创建自定义连接器

1. 登录企业集成服务控制台，在左侧菜单栏中单击【[自定义连接器](https://console.cloud.tencent.com/eis/connector)】。
2. 单击【添加连接器】，在弹出的添加自定义连接器窗口中单击【选择文件】。
![](https://main.qcloudimg.com/raw/cd29bb84ef204addcd649590a53dff0e.jpg)
3. 选择上述准备的 XML 文件，单击【确认上传】>【确认】，即可将 XML 文件上传到企业集成服务控制台。
4. 成功上传自定义连接器 XML 文件后，即可在集成流中使用该自定义连接器。
#### 查看
将示例的 XML 上传后，前端展示页面如下：
![operation前端展示截图](https://main.qcloudimg.com/raw/1243d83bbf32167fd00a08f465df6b00.png)
**hello-world**：在 **operation** 节点中定义的操作。
**HelloWorld**：在 **display-name** 标签定义的自定义连接器展示名称。
	- 在 **parameters** 节点中定义的参数展示如下：
	![参数前端展示截图](https://main.qcloudimg.com/raw/675a210e4029b074bea60ee4f1440daa.png)
	- 在 **properties** 节点中定义的公共配置项前端展示如下：
	![](https://main.qcloudimg.com/raw/48eb0168ebd34af6737740e0d98d79b7.png)

### 创建应用

1. 登录企业集成服务控制台，在左侧菜单栏中单击【[应用管理](https://console.cloud.tencent.com/eis)】。
2. 单击【添加应用】，在弹出的添加应用窗口中选择添加方式，本文选择”空白应用“方式。
 - HelloWorld 模版：企业集成服务提供的 HelloWorld 模版。
 - 空白应用：创建集成留为空的应用。
3. 单击【确定】创建应用并默认进入集成流页面。
4. 在页面右侧可以查看到上述步骤创建到 HelloWorld 连接器。
5. 在集成流中使用 **hello-world** 自定义连接器，创建的集成流如下。
![集成应用截图](https://main.qcloudimg.com/raw/abc930a3e74d26d38923aeea05be8d73.png)
6. 通过 Http Request 触发运行的集成流，在运行监控中可以查看到打印的日志 `Hello World!`。
![固定字符串打印截图](https://main.qcloudimg.com/raw/c07f1c019cf7e5c614a1549d5b5ab85a.png)
从上图可以得出 **hello-world** 自定义连接器只能打印固定的 `Hello World!` 字符串，以下介绍如何使用 [DataWay表达式](https://cloud.tencent.com/document/product/1270/46960) 来打印用户输入的字符串。修改 **hello-world** 操作关联的集成流如下：
```
<module apiVersion="1.0.0" apiType="XML" expressionType="dataway" expressionVersion="1.0.0" >
    <name>hello-world</name>
    <version>1.0.0</version>
    <display-name>HelloWorld</display-name>
    <description>Hello World !!!</description>
    <declaration>
        <properties>
            <property name="prop1" type="string" displayName="配置项"/>
        </properties>
        <operations>
            <operation name="hello-world" flowRef="hello-world">
                <parameters>
                    <parameter name="para1" type="string" displayName="参数" displayGroup="基础信息"/>
                </parameters>
            </operation>
        </operations>
    </declaration>
    <body>
        <flows>
            <flow name="hello-world">
                <logger message="#[msg.vars['para1']]" level="INFO"/>
                <logger message="#[msg.vars['properties']['prop1']]" level="INFO"/>
            </flow>
        </flows>
    </body>
</module>
```
 在集成流 **hello-world** 的实现中，使用了两个 [Logger](https://cloud.tencent.com/document/product/1270/46959#logger) 组件，第一个 [Logger](https://cloud.tencent.com/document/product/1270/46959#logger) 组件打印参数 **para1** 的输入字符串值，第二个 [Logger](https://cloud.tencent.com/document/product/1270/46959#logger) 打印配置项 **prop1** 的输入字符串值。重新上传修改后的 **hello-world** 自定义连接器XML文件，使用新的连接器创建集成应用。在**配置项**输入 `hello world prop1`，在**参数**输入 `hello world para1`。发布新创建的集成应用和触发集成流运行后，在运行监控可以看到将输入的字符串打印在日志中：
![打印输入日志截图](https://main.qcloudimg.com/raw/d438e314c7eaec2bb40dd0911e5f5fa3.png)
