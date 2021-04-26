HTTP 连接器是最常用的 **connector**，也是 **iPaaS** 内置的最重要的 **connector**。它提供了两个组件：HTTP监听触发器（**listener**）和 HTTP 请求操作（**request**）。

## listener

**listener** 触发器在 **flow** 中作为 **source**，用于根据参数指定的域名、端口、路径和方法监听HTTP请求，并在收到 HTTP 请求后，将请求内容封装为**message**输出给第一个 **processor**。在流转完成或者发生错误后，将最后的 **message** 按照参数中指定的输出规则或错误处理规则输出 HTTP 响应。将 HTTP 请求封装为 **message** 的规则为：协议、域名、端口、方法、路径、参数、请求头等信息封装在 **attributes** 中，请求正文封装在 **payload**中。

![http listener组件](https://main.qcloudimg.com/raw/89b5f86d062e8fd8ee238f4117b9ba7d/http%20listener%E7%BB%84%E4%BB%B6.png)


![](https://main.qcloudimg.com/raw/35622ec0bfd9ad4cb704d7bf59dde865.png)

## request

**request 操作**在 **flow** 中作为 **processor**，在收到 **message** 时，按照参数指定的域名、端口、路径、方法和参数发送 HTTP 请求，将得到的 HTTP 响应封装为**message**输出给下一个 **processor。**HTTP 响应封装为 **message** 的规则为：状态码、响应头等信息封装在**attributes**中，响应正文封装在**payload**中。

![http request组件](https://main.qcloudimg.com/raw/80c10053e3abe40acfe299d444d9faa6/http%20request%E7%BB%84%E4%BB%B6.png)


![](https://main.qcloudimg.com/raw/2e1ac641535a15b71974895f322cdac6.png)


## 表达式

在构造 **component** 或 **config** 时，设置的参数可以是字面量（**literal**），也可以是表达式（**expression**）。对于 **processor** 的参数，在 **expression** 中可引用收到的 **message** 中的**payload**、**attributes**、**variables** 和 **error**，并支持简单的计算逻辑，**processor** 在收到**message** 时，会对表达式先进行动态求值（**evaluate**），将得到的值作为 **processor** 真正的参数。对于**source** 或 **config** 的参数，只有在通过 XML 开发 **connector**时，才可以在 **expression** 中则只能引用公共配置中的变量，详细参考"Connector XML开发规范"。

对于每个 **parameter** 和 **property**，有三种表达式模式：支持表达式（**SUPPORTED**）、不支持表达式(**NOT_SUPPORTED**)、只支持表达式(**REQUIRED**)。

当参数值以“#[”开头并以"]"结尾，且对应的参数为 **SUPPORTED** 或 **REQUIRED** 时，参数会在被使用前被**evaluate**。

表达式可以有不同的语言类型和版本，通过在 **app** 中指定 **expressionType** 和 **expressionVersion** 来指定 **app** 中所使用表达式的语言类型和版本。

**expression** 支持单行模式（**inline**）和完整模式（**full**），在单行模式中，**expression** 中只能有一条语句，该语句的执行结果即为组件参数的值，可通过四个全局变量 **payload、attributes、vars**和 **error** 来访问**message** 中的值。在完整模式中，可以放入完整的脚本，在脚本中，需要按表达式语言类型的要求指定一个入口函数，在 **expression** 被 **evaluate** 时，该入口函数会被调用，且 **message** 对象将作为函数参数传入，而函数的返回值则作为最终的组件参数值。

**expression** 支持统一的结构化访问器（**selector**），通过 **selector**，用户可以通过一致的协议结构化地访问 JSON、XML 等二进制对象、多字典、字典、列表等数据结构，协议定义如下：

- 数字选择符，按数组的方式取第**i**个，例如 selecor(0)。
- 字符串选择符，按键值对的方式取值，例如 selecor("key")。当遇到多值键值对时，则返回第一个。
- 多值选择符，按多值键值对的方式取键关联的所有值，返回结构为数组，例如 selecor("*key")。
- 属性选择符，取属性值，例如 selecor("@key")，常见于 XML。
- 元信息选择符，取源信息，例如 selecor("@mimeType")。元信息包括以下几类：
  - 多媒体类型，**^mimeType**。
  - 编码，**^encoding**。
  - 原始二进制，**^raw**。
  - 解析后的值，**^value**。

其中，方法名 selecor 根据不同的表达式实现，可能被定义为具体的方法名，甚至可以被重载为"[...]"这类操作符。
