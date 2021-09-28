
## 简介
- SOAP（简单对象访问协议：Simple Object Access Protocol）是基于 XML 的简易协议，可使应用程序在 HTTP 之上进行信息交换，用于访问网络服务。SOAP 提供一种标准的方法，使得运行在不同的操作系统并使用不同的技术和编程语言的应用程序可以互相进行通信。
- SOAP = HTTP + XML，本质即遵守 SOAP 编码规则的 HTTP 请求/响应。一条 SOAP 消息即为遵循 SOAP 协议规则的 XML 文档。主要包含下列元素：
 - 必需的 Envelope 元素，用于把此 XML 文档标识为一条 SOAP 消息。
 - 可选的 Header 元素，包含头部信息。如果 Header 元素被提供，则它必须是 Envelope 元素的第一个子元素。
 - 必需的 Body 元素，包含所有的调用和响应信息。
 - 可选的 Fault 元素，提供有关在处理此消息所发生错误的信息。
- WSDL 是基于 XML 的用于描述 Web Services 以及如何访问 Web Services 的语言。WSDL 是一种使用 XML 编写的文档，该文档可描述某个 Web service。它可规定服务的位置，以及此服务提供的操作（或方法）。
- SOAP 连接器即基于 SOAP 协议规则向 Web Services 发送请求的连接器。

## 连接器配置
<dx-tabs>
::: 通用配置
| 参数             | 数据类型 | 描述                                                   | 是否必填 | 默认值  |
| ---------------- | -------- | ------------------------------------------------------ | -------- | ------- |
| WSDL Location    | string   | Web 服务的 WSDL URL 链接                                  | 是       |    -     |
| WSDL 文件  | string   | Web 服务的 WSDL 文件                                  | 否       |     -    |
| 使用 WSDL URL    | bool   | 是否使用 WSDL URL 链接进行分析                        | 否       |  true       |
| Service          | string   | Web 服务的 serviceName，通过 WSDL 文件获取                 | 是       |    -     |
| Port             | string   | Web 服务的 portName，通过 WSDL 文件获取                    | 是       |    -     |
| 协议版本         | enum     | SOAP 协议版本：soap1.1、soap1.2                         | 否       | soap1.1 |
| 编码方式         | string   | SOAP Message 编码方式：UTF-8、UTF-16、ASCII、ISO-8859-1 | 否       | UTF-8   |
| 请求超时时间（秒） | int      | SOAP请求超时时间（秒）（范围：0～300）                   | 否       | 60（s） |
:::
::: 高级配置
| 参数             | 数据类型 | 描述                 | 是否必填 | 默认值 |
| ---------------- | -------- | -------------------- | -------- | ------ |
| 缓存过期时间（秒） | int      | WSDL 文件缓存过期时间 | 否       | 90（s） |

:::
</dx-tabs>

**连接器配置界面如下：**
![](https://main.qcloudimg.com/raw/9ef6d67756fa7be8ae9d16a194f9915f.png)

## 操作配置

SOAP 请求操作如下：

### 输入参数

| 参数                     | 数据类型 | 描述                                                         | 是否必填 | 默认值       |
| ------------------------ | -------- | ------------------------------------------------------------ | -------- | ------------ |
| 接口名称                 | string   | 请求 operation                                                | 是       |    -          |
| 请求体                   | string   | SOAP Message body，只支持表达式输入                          | 是     |     -         |
| 请求头                   | string   | SOAP Message headers，只支持表达式输入                       | 是       |     -         |
| Web Service Security 使能 | bool     | 是否通过可视化输入参数增加 Web Service Security 身份认证请求头 | 否       | false        |
| WsseMustUnderstand 属性   | bool     | 请求接收者是否必须认可该请求头                               | 否       | true         |
| UsernameTokenId 属性      | string   | Web Service Security 身份认证请求头 wsse:UsernameToken wsu:Id 属性值 | 否       |       -       |
| 用户名                   | string   | Web Service Security身份认证请求头 wsse:Username 属性值        | 否       |      -        |
| 密码                     | string   | Web Service Security身份认证请求头 wsse:Password 属性值        | 否       |      -        |
| 密码类型属性             | enum     | Web Service Security身份认证请求头 wsse:Password <br>Type类型：PasswordText、PasswordDigest | 否       | PasswordText |
| 增加随机数属性           | bool     | 是否使用自动生成的随机数作为 wsse:Nonce 属性值                 | 否       | false        |
| 用户自定义随机数         | string   | 用户自定义输入 Web Service Security 身份认证请求头 wsse:Nonce 属性值，此时增加随机数属性参数需设置为 false | 否       |  -            |
| 增加创建时间属性         | bool     | 是否使用自动生成的创建时间作为 wsu:Created 属性值              | 否       | false        |
| 用户自定义创建时间       | string   | 用户自定义输入 Web Service Security 身份认证请求头 wsu:Created 属性值，此时增加创建时间属性参数需设置为 false | 否       |   -           |

![](https://main.qcloudimg.com/raw/762833d4322e1b3f92640e3dcfad496a.png)

### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 dict 类型；执行失败后，payload 为空       |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 返回 SOAP 组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |


**消息的 attributes：**


<table>
<thead>
<tr>
<th>attributes 信息</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>attrs.statusCode</td>
<td>响应的状态码，例如：200</td>
</tr>
<tr>
<td>attrs.reasonPhrase</td>
<td>响应的文本描述，例如：OK</td>
</tr>
<tr>
<td>attrs.headers</td>
<td>响应的 Header，结果为 dict&lt;string, list<string>&gt;</string></td>
</tr>
<tr>
<td>attrs.cookies</td>
<td>响应的 Cookie，结果为 dict&lt;string, string&gt;</td>
</tr>
</tbody></table>

**消息的 Payload：**
SOAP 请求返回的响应 Response 为 XML 格式，会首先进行一次 Flatten 处理，将 XML 转换为 dict 类型，然后放到消息 payload 中，后续可通过 dataway 表达式直接访问。
- 正确输出为 dict 类型，例如:
```json
{
    "Body": {
        "AddResponse": {
            "AddResult": "5"
        }
    }
}
```
- 错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "SOAP:CONNECT Can not find method:Add1 in wsdl description"
}
```

### 案例
1. 在连接器列表中选择 SOAP 连接器，选择 SOAP 请求操作。
![](https://main.qcloudimg.com/raw/5d658fc3501df8b8048accddf9071a92/SOAP3.png)
![](https://main.qcloudimg.com/raw/4be3cab5e90c0f36636735cd7a8b692b/SOAP4.png)
2. 输入连接器配置参数，其中 WSDL Location = "http://www.dneonline.com/calculator.asmx?WSDL",Service="Calculator" , Port = "CalculatorSoap"，其他参数保持默认值即可。具体如下图：
![](https://main.qcloudimg.com/raw/424ef72b61a46bf25f76b00f1bef3db1.png)
 - 默认使用 WSDL URL 参数设置为 true，此时会根据 WSDL Location 参数值提供的 wsdl url 链接进行解析；当使用 WSDL URL 参数设置为 false 时，用户也可通过输入 WSDL 文件参数值来对 Web 服务的 WSDL 文件内容进行解析。
![](https://main.qcloudimg.com/raw/8fa4beca8e96dd626c5d2dba228f77f5.png)
    - 首先在 SOAP 组件前添加 SetVariable 组件，变量名设置为 wsdlFile，变量值类型选择 entity.xml、值设为 WSDL Url 链接的 xml 内容。
 ![](https://main.qcloudimg.com/raw/387713ece686b1340fab943c63a03cb6.png)
 ![](https://main.qcloudimg.com/raw/1991339488d1c1d9ca04d3da1ad46e26.png)
    - 然后在 SOAP 组件连接器配置中将使用 WSDL URL 参数设置为 false，将 WSDL 文件参数设置为 msg.vars["wsdlFile"] 变量值保存即可。
    ![](https://main.qcloudimg.com/raw/4dd0a10976c165cd5e61aa8fc1060f50.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。接口名称设为“Add”（根据 WSDL 文件 operation 参数获取），请求头、请求体表达式输入见下图：
![](https://main.qcloudimg.com/raw/8d95e7105fba0ebfc0d6b732cf4e9002/SOAP6.png)
 - SOAP 请求体表达式输入见下图：
![](https://main.qcloudimg.com/raw/841db66a32142b9c4059217b9f36d08c/SOAP7.png)
 - SOAP请求头表达式输入见下图，默认为空：
![](https://main.qcloudimg.com/raw/82bc59eb4bd57bb098ef6365a3088144/SOAP8.png)
 - 当需要支持 Web Service Security 身份认证方式时，SOAP 请求头表达式输入可参考下图进行配置：
![image-20210427104857762](https://main.qcloudimg.com/raw/d6c6fe05f5c7dd923580baf890969692/SOAP13.png)
 - 或者将 Web Service Security 使能设置为 true，进行 Web Service Security 身份认证请求头参数的可视化编辑，具体可参考下图进行配置：
![image-20210427104857762](https://main.qcloudimg.com/raw/8dfc5f1a7e057e4dcc109d77434a5153.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/22062f5b31ed3baa0b70a8515302a4fd/SOAP9.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/b1e1ce9b5048be5b6335130264a2728f/SOAP10.png)
 - SOAP 返回 payload 响应结果如下，即为请求体中 intA 和 intB 两数相加结果。
![](https://main.qcloudimg.com/raw/f59c7ac4562782a74813a56e11c1d10d/SOAP11.png)
![](https://main.qcloudimg.com/raw/761eaa64aa2a7c9baebbcb6b0103c7ae/SOAP12.png)
