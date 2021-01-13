开发一个连接器（**connector**）最简单的方式就是通过 XML 来编写，一个连接器就是一个 XML 文件，以下是一个 XML 描述的 hello-world 连接器，提供了一个 **hello-world** 操作，通过使用 **[Logger](https://cloud.tencent.com/document/product/1270/46959)** 组件来打印日志 `Hello World!`。

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

在企业集成服务控制台，选择 [【自定义连接器】](https://console.cloud.tencent.com/eis/connector)，成功上传自定义连接器 XML 文件后，就可以在集成流中使用该自定义连接器。

将示例的 XML 上传后，前端展示页面如下：

![operation前端展示截图](https://main.qcloudimg.com/raw/1243d83bbf32167fd00a08f465df6b00.png)

**hello-world**：在 **operation** 节点中定义的操作。

**HelloWorld**：在 **display-name** 标签定义的自定义连接器展示名称。

在 **parameters** 节点中定义的参数展示如下：

![参数前端展示截图](https://main.qcloudimg.com/raw/675a210e4029b074bea60ee4f1440daa.png)

在 **properties** 节点中定义的公共配置项前端展示如下：

![配置项前端展示截图](https://main.qcloudimg.com/raw/c7834f65b6f9ce76c451c1be8d82dceb.png)



创建和发布一个集成应用，在集成流中使用 **hello-world** 自定义连接器，创建的集成流如下。

![集成应用截图](https://main.qcloudimg.com/raw/abc930a3e74d26d38923aeea05be8d73.png)

通过 Http Request 触发运行的集成流，在运行监控中可以查看到打印的日志 `Hello World!`。

![固定字符串打印截图](https://main.qcloudimg.com/raw/c07f1c019cf7e5c614a1549d5b5ab85a.png)

可以看到，**hello-world** 自定义连接器只能打印固定的 `Hello World!` 字符串，下面将介绍使用 [DataWay表达式](https://cloud.tencent.com/document/product/1270/46960) 来打印用户输入的字符串。修改 **hello-world** 操作关联的集成流如下：

```xml
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

在集成流 **hello-world** 的实现中，使用了两个 **[Logger](https://cloud.tencent.com/document/product/1270/46959)** 组件，第一个 **[Logger](https://cloud.tencent.com/document/product/1270/46959)** 组件打印参数 **para1** 的输入字符串值，第二个 **[Logger](https://cloud.tencent.com/document/product/1270/46959)** 打印配置项 **prop1** 的输入字符串值。重新上传修改后的 **hello-world** 自定义连接器XML文件，使用新的连接器创建集成应用。在**配置项**输入 `hello world prop1`，在**参数**输入 `hello world para1`。发布新创建的集成应用和触发集成流运行后，在运行监控可以看到将输入的字符串打印在日志中：

![打印输入日志截图](https://main.qcloudimg.com/raw/d438e314c7eaec2bb40dd0911e5f5fa3.png)
