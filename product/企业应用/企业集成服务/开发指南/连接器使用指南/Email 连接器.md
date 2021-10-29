

## 简介

Email 连接器可用于发送和收取邮件。
- 邮件发送 SMTP 协议
SMTP 是一个相对简单的基于文本的协议，在其之上指定一条消息的一个或多个接收者（在大多数情况下被确认是存在的），然后进行消息文本传输。SMTP 规定在两个相互通信的 SMTP 进程之间应如何交换信息。由于 SMTP 使用 CS 方式，因此负责发送邮件的 SMTP 进程为 SMTP 客户，而负责接收邮件的 SMTP 进程为 SMTP 服务器。至于邮件内部的格式，邮件如何存储，以及邮件系统应以多快的速度来发送邮件，SMTP 未做出规定。
- 邮件读取 POP3 和 IMAP 协议
常用的邮件读取协议有两个，即邮局协议第3个版本 POP3 和网际报文存取协议 IMAP (Internet Message Access Protocol)。
 - **邮局协议**（英语：**P**ost **O**ffice **P**rotocol，缩写：**POP**）是 [TCP/IP](https://zh.wikipedia.org/wiki/TCP/IP) 协议族中的一员，由1996年5月发行之 [RFC 1939](https://tools.ietf.org/html/rfc1939) 首次定义。此协议主要用于支持使用客户端远程管理在服务器上的 [电子邮件](https://zh.wikipedia.org/wiki/电子邮件)。最新版本为 **POP3**，全名“Post Office Protocol - Version 3”，而提供 [SSL](https://zh.wikipedia.org/wiki/SSL) 加密的 POP3 协议则被称为 **POP3S**。
 - **因特网信息访问协议**（英语：**I**nternet **M**essage **A**ccess **P**rotocol，缩写：**IMAP**；以前称作**交互邮件访问协议**）是一个应用层协议，用来从本地邮件客户端（例如：Microsoft [Outlook](https://zh.wikipedia.org/wiki/Outlook)、[Foxmail](https://zh.wikipedia.org/wiki/Foxmail)、[Mozilla Thunderbird](https://zh.wikipedia.org/wiki/Mozilla_Thunderbird)）访问远程服务器上的邮件。在使用 IMAP 时，在用户的计算机上运行 IMAP 客户程序，然后与接收方的邮件服务器上的 IMAP 服务器程序建立 TCP 连接。用户在计算机上即可操纵邮件服务器的邮箱，就像在本地操纵一样，因此 **IMAP 是一个联机协议**。

## 连接器配置
Email 连接器需提供如下连接配置，POP3 协议和 IMAP 协议的连接信息可只提供其中一种，或同时提供。

Email 连接器配置参数如下：
<dx-tabs>
::: 基础设置
| 参数           | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| -------------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 默认发件人地址 | string   | 默认发件人地址                                               | 是       |    -    |
| 用户名         | string   | 邮箱登录用户名                                               | 是       |   -     |
| 密码           | string   | 邮箱登录密码，163邮箱、QQ 邮箱等邮箱使用的是授权码，需要开通 POP3 或 IMAP 收件服务后，使用授权码登录 | 是       |    -    |
| 协议类型       | enum     | 选择收信的协议类型：可选 POP3 或 IMAP 或 ALL                      | 否       | ALL    |
| 超时时间       | int      | 设置连接的超时时间                                           | 否       | 10s    |

:::
::: POP设置
| 参数                   | 数据类型 | 描述                                                       | 是否必填 | 默认值 |
| ---------------------- | -------- | ---------------------------------------------------------- | -------- | ------ |
| POP3 服务器地址         | string   | POP3 服务器地址                                             | 是       |    -    |
| POP3 服务器端口号       | int      | POP3 服务器端口号                                           | 是       |    -    |
| POP3 使能 TLS            | bool     | 是否使用 TLS 链接                                            | 否       | false  |
| POP3 TLS 连接客户端证书 | file     | 可选，使用提供的证书对连接进行加密                         | 否       |    -    |
| POP3 TLS 连接客户端 Key  | file     | 可选，使用提供的证书对连接进行加密，需和客户端证书同时提供 | 否       |   -     |
| POP3 TLS 连接服务端证书 | file     | 可选，使用提供的证书对连接进行加密                         | 否       |   -     |
:::
::: IMAP设置
| 参数                   | 数据类型 | 描述                                                       | 是否必填 | 默认值 |
| ---------------------- | -------- | ---------------------------------------------------------- | -------- | ------ |
| IMAP 服务器地址         | string   | POP3 服务器地址                                             | 是       |  -      |
| IMAP 服务器端口号       | int      | POP3 服务器端口号                                           | 是       |    -    |
| IMAP 使能 TLS            | bool     | 是否使用 TLS 链接                                            | 否       | false  |
| IMAP TLS 连接客户端证书 | file     | 可选，使用提供的证书对连接进行加密                         | 否       |   -     |
| IMAP TLS 连接客户端 Key  | file     | 可选，使用提供的证书对连接进行加密，需和客户端证书同时提供 | 否       |   -     |
| IMAP TLS 连接服务端证书 | file     | 可选，使用提供的证书对连接进行加密                         | 否       |  -      |

:::
::: SMTP设置
| 参数                   | 数据类型 | 描述                                                       | 是否必填 | 默认值 |
| ---------------------- | -------- | ---------------------------------------------------------- | -------- | ------ |
| SMTP 服务器地址         | string   | POP3 服务器地址                                             | 是       |  -      |
| SMTP 服务器端口号       | int      | POP3 服务器端口号                                           | 是       |  -      |
| SMTP 使能 TLS            | bool     | 是否使用 TLS 链接                                            | 否       | false  |
| SMTP TLS 连接客户端证书 | file     | 可选，使用提供的证书对连接进行加密                         | 否       |  -      |
| SMTP TLS 连接客户端 Key  | file     | 可选，使用提供的证书对连接进行加密，需和客户端证书同时提供 | 否       |  -      |
| SMTP TLS 连接服务端证书 | file     | 可选，使用提供的证书对连接进行加密                         | 否       |  -      |
:::
</dx-tabs>

**连接器配置界面如下：**
![](https://main.qcloudimg.com/raw/a0850bf550289b7b84bd263d2fbc720e/image-20210408143647905.png)	
![](https://main.qcloudimg.com/raw/4261cf210864e74282bc8b06f7ae0406/image-20210408143710751.png)	


## 操作说明
Email 连接器包含发送邮件、删除邮件、标记邮件、清理文件夹、收取邮件-IMAP、收取邮件-POP3共6种操作

<dx-tabs>
::: 发送邮件
#### 输入参数

| 参数         | 数据类型         | 说明                                    | 是否必填 | 默认值     |
| ------------ | ---------------- | --------------------------------------- | -------- | ---------- |
| 发件人       | string           | 发件人地址                              | 否       |    -        |
| 收件人       | string         | 收件人地址列表，至少提供一个收件地址    | 是       |    -        |
| 抄送         | string         | 抄送地址列表                            | 否       |   -         |
| 密送         | string         | 密送地址列表                            | 否       |   -         |
| 回复地址     | string         | 回复地址列表                            | 否       |   -         |
| 主题         | string           | 邮件主题                                | 否       | 无主题     |
| 邮件头       | map              | 邮件头                                  | 否       |      -      |
| 正文         | string           | 邮件正文                                | 否       |      -      |
| 正文MIME类型 | 枚举             | 正文 MIME 类型，可选 text/plain、text/html | 否       | text/plain |
| 附件         | Attachment | 附件列表                                | 否       |        -    |
| 编码格式     | 枚举             | 编码格式                                | 否       | base64     |

**Attachment 参数**

| 参数     | 数据类型 | 说明                              | 是否必填 | 默认值 |
| -------- | -------- | --------------------------------- | -------- | ------ |
| 文件名   | string   | 附件文件名                        | 是       |   -     |
| 文件内容 | byte   | 文件内容，仅支持使用 dataway 表达式 | 是       |      -  |

![](https://main.qcloudimg.com/raw/d5d77161ea781ee446100412399d209a/image-20210408143853136.png)	
![](https://main.qcloudimg.com/raw/beed8fb784e8aad9984b7f9f13fdca87/image-20210408143917013.png)	

####  输出参数

发送邮件操作执行成功后，继承上个组件的 payload 信息；执行失败后，错误信息会保存在 message 消息体的 error。
**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload 信息                                    |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值不变。执行失败后，message error 值（error 值不固定）如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "535 Login Fail. Please enter your authorization code to login. More information in http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256\"
}
```

#### 案例
1. 在邮箱设置中打开 POP3 或 IMAP 协议，例如：在163邮箱中打开 POP3 和 IMAP 协议，并记住授权码。
 - 在 Outlook 邮箱设置中，找到“同步电子邮件”选项卡，并打开 POP。Outlook 邮箱打开 POP 的设置方式如下图：
![](https://main.qcloudimg.com/raw/20cafdcccbd09ac3108ed7bc7001511c/image-20210425202443019.png)	
 - QQ 邮箱、163邮箱可参考以下帮助文档：
  - QQ 邮箱：[QQ 邮箱授权码设置](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256)、[QQ 邮箱开启 POP3/SMTP/IMAP 功能](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=166)。
  - 163邮箱：[163邮箱设置](https://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2cda80145a1742516)。
  - 其他邮箱可在邮箱帮助文档中查看 POP3 及 IMAP 相关主题。
2. 按照邮箱帮助设置 IMAP、POP3、SMTP 服务器地址和端口号，在连接设置中填写正确的地址信息，填写用户名（xxx@163.com）和密码（163、QQ 等邮箱使用的授权码）；使用 ssl 的端口时，使能 TLS 开关需设置为 True。
3. 单击测试连接，查看设置是否正确。
4. 填写邮件的收件人、主题、正文等信息；附件信息必须使用 dataway，仅接受字节数组作为附件的内容。
 - **添加附件示例：**
    - 在附件栏单击**添加**。
![](https://main.qcloudimg.com/raw/f26f0d5b5c7d17f22e3405b734cd117c/image-20210425203305730.png)	
    - 依次输入附件文件名、附件内容。
    >!附件内容必须是字节数组。
    
![](https://main.qcloudimg.com/raw/e58be79f24ebdec3efa35627e0c9d0c4/image-20210425203342557.png)	

:::
::: 删除邮件
删除邮件将指定文件夹中的指定 ID 的邮件标记为删除。

#### 输入参数

| 参数       | 数据类型 | 说明             | 是否必填 | 默认值 |
| ---------- | -------- | ---------------- | -------- | ------ |
| 邮件文件夹 | string   | 操作的邮件文件夹 | 否       | INBOX  |
| 邮件ID     | int      | 要删除的邮件 ID   | 是       |     -   |


####  输出参数

删除操作执行成功后，继承上个组件的 payload 信息；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload 信息                                    |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值不变。执行失败后，message error 值（error 值不固定）如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "535 Login Fail. Please enter your authorization code to login. More information in http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256\"
}
```

#### 案例
1. 使用发送操作中的邮件连接信息。
2. 填写邮件文件夹，并填写邮件 ID（在收取邮件操作中，会返回邮件id及其内容），例如：下图的配置将 INBOX 文件夹（收件夹）下指定邮件 ID 的邮件标记为删除。
![](https://main.qcloudimg.com/raw/c730af528bcc524f7026534bac8e8768/image-20210408143958803.png)	
:::
::: 清理文件夹
清理文件夹将删除文件夹中标记为删除的邮件。

#### 输入参数

| 参数       | 数据类型 | 说明             | 是否必填 | 默认值 |
| ---------- | -------- | ---------------- | -------- | ------ |
| 邮件文件夹 | string   | 操作的邮件文件夹 | 否       | INBOX  |


####  输出参数

清理文件夹操作执行成功后，继承上个组件的 payload 信息；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload 信息                                    |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值不变。执行失败后，message error 值（error 值不固定）如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "535 Login Fail. Please enter your authorization code to login. More information in http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256\"
}
```

#### 案例
1. 使用发送操作中的邮件连接信息。
2. 填写邮件文件夹，下图的配置将删除掉 INBOX 文件夹下的标记为删除的全部邮件（注意：此功能受邮件服务器设置影响，如设置为不允许客户端删信，则此动作不会生效）。
![](https://main.qcloudimg.com/raw/34955f7dcda5cdf37903a10578c37a65/image-20210408144029440.png)	

:::
::: 标记邮件
标记邮件将指定文件夹中的指定 ID 的邮件标记为删除、已读或旗标。

#### 输入参数

| 参数       | 数据类型 | 说明                                   | 是否必填 | 默认值 |
| ---------- | -------- | -------------------------------------- | -------- | ------ |
| 邮件文件夹 | string   | 操作的邮件文件夹                       | 否       | INBOX  |
| 邮件 ID     | int      | 要删除的邮件 ID                         | 是       |   -     |
| 标记为     | 枚举     | 将指定 ID 的邮件标记为：删除、已读、旗标 | 是       |   -     |


####  输出参数

标记邮件操作执行成功后，继承上个组件的 payload 信息；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload 信息                                    |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值不变。执行失败后，message error 值（error 值不固定）如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "535 Login Fail. Please enter your authorization code to login. More information in http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256\"
}
```

#### 案例
1. 使用发送操作中的邮件连接信息。
2. 填写邮件文件夹，并填写邮件 ID（在收取邮件中，会返回邮件 ID 及其内容）；
3. 选择标记动作。下图的配置，将 INBOX 文件夹（收件夹）中邮件 ID 为1的邮件标记为已读。
![](https://main.qcloudimg.com/raw/b9fdbe6bfdd1e013c1743d625b11aa16/image-20210408144118903.png)	

:::
::: 收取邮件（POP3 协议）
收取邮件（POP3 协议）按照指定的过滤条件，收取符合过滤条件的全部邮件（不能指定邮件文件夹）。

#### 输入参数

| 参数         | 数据类型    | 说明         | 是否必填 | 默认值 |
| ------------ | ----------- | ------------ | -------- | ------ |
| 邮件过滤条件 | POP3Matcher | 邮件过滤条件 | 否       |    -    |
| 最大收取量   | int         | 最大收取量   | 否       | 10     |
| 起始邮件 ID   | int         | 起始邮件 ID   | 否       | 0      |

**POP3Matcher**

| 参数           | 数据类型 | 说明                                             | 是否必填 | 默认值 |
| -------------- | -------- | ------------------------------------------------ | -------- | ------ |
| 起始时间       | datetime | 收取此时间之后的邮件                             | 否       |   -     |
| 截止时间       | datetime | 收取此时间之前的邮件                             | 否       |    -    |
| 主题筛选       | string   | 筛选邮件主题，收取主题中包含该字段的邮件         | 否       |    -    |
| 发件人地址筛选 | string   | 筛选邮件发件人，收取发件人地址中包含该字段的邮件 | 否       |     -   |
| 收件人地址筛选 | string   | 筛选邮件收件人，收取收件人地址中包含该字段的邮件 | 否       |   -     |


#### 输出参数

收取邮件（POP3 协议）操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，list 成员为 dict 类型，键表示邮件各字段名称，值表示邮件字段值 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值如下：
```json
[
    {
        "Header":Object{...},
        "Subject":" some subject",
        "Sender":null,
        "From":[
            {
                "Name":"帐户名称",
                "Address":"abc@efg.com"
            }
        ],
        "ReplyTo":null,
        "To":[
            {
                "Name":"",
                "Address":"receiverAddress@qq.com"
            }
        ],
        "Cc":null,
        "Bcc":null,
        "Date":"2021-03-01T23:42:53-08:00",
        "MessageID":"IKBLXSIQ3DU4.PKYL66BZ4RFP3@BY1PEPF00001EF1",
        "MailID":1,
        "InReplyTo":null,
        "References":null,
        "ResentFrom":null,
        "ResentSender":null,
        "ResentTo":null,
        "ResentDate":"0001-01-01T00:00:00Z",
        "ResentCc":null,
        "ResentBcc":null,
        "ResentMessageID":"",
        "ContentType":"",
        "Content":"",
        "HTMLBody":"... HTML Body Content ...",
        "TextBody":"... Text Body Content ...",
        "Attachments":null,
        "EmbeddedFiles":null
    },
    {
        "Header":{},
        "Subject":"邮件主题",
        "Sender":null,
        "From":[
            {
                "Name":"帐户名称",
                "Address":"abc@efg.com"
            }
        ],
        "ReplyTo":null,
        "To":[
            {
                "Name":"",
                "Address":"receiverAddress@qq.com"
            }
        ],
        "Cc":null,
        "Bcc":null,
        "Date":"2021-03-08T00:05:34-08:00",
        "MessageID":"GM63WJUK5DU4.Y7UK7WAJ3VBS2@BL02EPF0000195A",
        "MailID":2,
        "InReplyTo":null,
        "References":null,
        "ResentFrom":null,
        "ResentSender":null,
        "ResentTo":null,
        "ResentDate":"0001-01-01T00:00:00Z",
        "ResentCc":null,
        "ResentBcc":null,
        "ResentMessageID":"",
        "ContentType":"",
        "Content":"",
        "HTMLBody":"",
        "TextBody":"",
        "Attachments":[
            {
                "FileName":"test.pdf",
                "ContentType":"application/pdf; name="test.pdf"",
                "Data":"base64 encoded content"
            },
            ...
            {}
        ],
        "EmbeddedFiles":[
            {
                "CID":"colors",
                "ContentType":"image/png; name="colors.png"",
                "Data":"base64 encoded content"
            },
            ...
            {}
        ]
    }
]
```
执行失败后，message error 值（error 值不固定）如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "535 Login Fail. Please enter your authorization code to login. More information in http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256\"
}
```

#### 案例
1. 使用发送操作中的邮件连接信息。
2. 填写过滤条件，参考输入条件中的 POP3Matcher；填写最大收取量和起始邮件 ID。按下图示例填写的配置，将收取邮件服务器收信时间在2021-01-01 10:28:38 ~ 2021-04-25 10:28:38之间、邮件主题包含 test、发件人包含 someone、收件人包含 somereceiver 的邮件，邮件 ID 从1开始，共收取10封邮件（若满足条件的邮件数不足10，则返回全部满足条件的邮件）。
![image-20210426102433488](https://main.qcloudimg.com/raw/665473baffb1954c3bd3bc9cc063e1d4/image-20210426102433488.png)
:::
::: 收取邮件（IMAP 协议）
收取邮件（IMAP 协议）按照指定的过滤条件，收取符合过滤条件的全部邮件。

#### 输入参数

| 参数         | 数据类型    | 说明                 | 是否必填 | 默认值 |
| ------------ | ----------- | -------------------- | -------- | ------ |
| 邮件文件夹   | string      | 操作的邮件文件夹名称 | 否       | INBOX  |
| 邮件过滤条件 | IMAPMatcher | 邮件过滤条件         | 否       |  -      |
| 最大收取量   | int         | 最大收取量           | 否       | 10     |
| 起始邮件 ID   | int         | 起始邮件 ID           | 否       | 0      |

#### IMAPMatcher

| 参数           | 数据类型 | 说明                                                         | 是否必填 | 默认值 |
| -------------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 已读           | bool     | 取值为 False 时，仅收取未读邮件；取值为 True 时，仅收取已读邮件；取值为 None 时，不使用该条件过滤 | 否       | None   |
| 已回复         | bool     | 取值为 False 时，仅收取未回复邮件；取值为 True 时，仅收取已回复邮件；取值为 None 时，不使用该条件过滤 | 否       | None   |
| 旗标           | bool     | 取值为 False 时，仅收取无旗标邮件；取值为 True 时，仅收取旗标邮件；取值为 None 时，不使用该条件过滤 | 否       | None   |
| 起始时间       | datetime | 收取此时间之后的邮件                                         | 否       |    -    |
| 截止时间       | datetime | 收取此时间之前的邮件                                         | 否       |   -     |
| 主题筛选       | string   | 筛选邮件主题，收取主题中包含该字段的邮件                     | 否       |   -     |
| 发件人地址筛选 | string   | 筛选邮件发件人，收取发件人地址中包含该字段的邮件             | 否       |   -     |
| 收件人地址筛选 | string   | 筛选邮件收件人，收取收件人地址中包含该字段的邮件             | 否       |  -      |


####  输出参数

收取邮件（IMAP 协议）操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，list 成员为 dict 类型，键表示邮件各字段名称，值表示邮件字段值 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值如下：
```json
[
    {
        "Header":Object{...},
        "Subject":" some subject",
        "Sender":null,
        "From":[
            {
                "Name":"帐户名称",
                "Address":"abc@efg.com"
            }
        ],
        "ReplyTo":null,
        "To":[
            {
                "Name":"",
                "Address":"receiverAddress@qq.com"
            }
        ],
        "Cc":null,
        "Bcc":null,
        "Date":"2021-03-01T23:42:53-08:00",
        "MessageID":"IKBLXSIQ3DU4.PKYL66BZ4RFP3@BY1PEPF00001EF1",
        "MailID":1,
        "InReplyTo":null,
        "References":null,
        "ResentFrom":null,
        "ResentSender":null,
        "ResentTo":null,
        "ResentDate":"0001-01-01T00:00:00Z",
        "ResentCc":null,
        "ResentBcc":null,
        "ResentMessageID":"",
        "ContentType":"",
        "Content":"",
        "HTMLBody":"... HTML Body Content ...",
        "TextBody":"... Text Body Content ...",
        "Attachments":null,
        "EmbeddedFiles":null
    },
    {
        "Header":{},
        "Subject":"邮件主题",
        "Sender":null,
        "From":[
            {
                "Name":"帐户名称",
                "Address":"abc@efg.com"
            }
        ],
        "ReplyTo":null,
        "To":[
            {
                "Name":"",
                "Address":"receiverAddress@qq.com"
            }
        ],
        "Cc":null,
        "Bcc":null,
        "Date":"2021-03-08T00:05:34-08:00",
        "MessageID":"GM63WJUK5DU4.Y7UK7WAJ3VBS2@BL02EPF0000195A",
        "MailID":2,
        "InReplyTo":null,
        "References":null,
        "ResentFrom":null,
        "ResentSender":null,
        "ResentTo":null,
        "ResentDate":"0001-01-01T00:00:00Z",
        "ResentCc":null,
        "ResentBcc":null,
        "ResentMessageID":"",
        "ContentType":"",
        "Content":"",
        "HTMLBody":"",
        "TextBody":"",
        "Attachments":[
            {
                "FileName":"test.pdf",
                "ContentType":"application/pdf; name="test.pdf"",
                "Data":"base64 encoded content"
            },
            ...
            {}
        ],
        "EmbeddedFiles":[
            {
                "CID":"colors",
                "ContentType":"image/png; name="colors.png"",
                "Data":"base64 encoded content"
            },
            ...
            {}
        ]
    }
]
```
执行失败后，message error 值（error 值不固定）如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "535 Login Fail. Please enter your authorization code to login. More information in http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256\"
}
```

#### 案例
1. 使用发送操作中的邮件连接信息。
2. 填写邮件文件夹、过滤条件（参考输入条件中的 IMAPMatcher）、填写最大收取量和起始邮件 ID。按下图示例填写的配置，将收取邮件服务器收信时间在2021-01-01 10:28:38 ~ 2021-04-25 10:28:38之间、邮件主题包含 test、发件人包含 someone、收件人包含 somereceiver 的邮件，邮件 ID 从1开始，且是已读的邮件，共收取10封邮件（若满足条件的邮件数不足10，则返回全部满足条件的邮件）。
![image-20210426103054703](https://main.qcloudimg.com/raw/93117d7471bd567e857ae174ae499cb8/image-20210426103054703.png)

:::
</dx-tabs>


