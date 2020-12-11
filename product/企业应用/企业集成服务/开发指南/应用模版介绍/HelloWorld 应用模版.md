企业集成服务平台内置多种应用模版，帮助用户快速适配各种场景，应用模版针对各种常见业务场景抽象出通用的流配置，方便用户快速配置业务流。



HelloWorld 应用是一个新手指引导向的基础应用模版，通过五个组件配置一条简单的流，帮助您快速快入门鹊桥企业集成服务。


## 操作步骤

#### 1. 创建应用

1. 登录 [企业集成服务]() 控制台。
2. 单击【添加应用】，在弹出的添加应用窗口中，配置如下选项：
	- 应用名称：输入应用名称。支持25位以内的中文、字母、数字、\_或-。
	- 添加方式：选择【HelloWord 模板】。企业集成服务提供 HelloWorld 模板和空白应用。
![](https://main.qcloudimg.com/raw/45151dbce9c84131605e6b189c85167f.png)
3. 单击【确定】即可创建 HelloWord 模板的应用。



#### 2. 流配置介绍

应用中已配置好流 HelloWorld_Flow，该流中包括五个组件：HTTP Listener、Set Payload、两个 Transform 和 Logger。

![流配置](https://main.qcloudimg.com/raw/ac294ab5271243fab27994463070c79c/%E6%B5%81%E9%85%8D%E7%BD%AE.png)

HTTP Listener组件绑定了连接器配置HelloWorld_Config，设置了监听路径为/，域名前缀为80的监听域名。

![监听路径](https://main.qcloudimg.com/raw/e6f3f3e4a4cd148027a3e949b3a1fdfa/%E7%9B%91%E5%90%AC%E8%B7%AF%E5%BE%84.png)

![监听域名前缀](https://main.qcloudimg.com/raw/e755954016415fa1e204820aac81dd09/%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D%E5%89%8D%E7%BC%80.png)

Set Payload组件给payload属性设置了“Hello”的返回值。

![set payload](https://main.qcloudimg.com/raw/80ec1db546abeb1dc30b20f83b296908/set%20payload.png)

第一个Transform组件对payload属性的返回值拼接了字符串“World”。

![transform1](https://main.qcloudimg.com/raw/1a833af7dd9a76924a6da8615a740948/transform1.png)

第二个Transform组件将payload属性返回成一个entity类型，以json的形式将返回值展示出来。

![transform2](https://main.qcloudimg.com/raw/ad4e1093de272b5985aa125ff54e63d6/transform2.png)

Logger组件打印了payload属性的内容。

![logger](https://main.qcloudimg.com/raw/72abac80005aa4b3490a4c8c55f8397d/logger.png)

#### 3.发布应用

点击画布右上方的发布按钮，选择要发布的地域，应用当前版本进入运行中的状态。

![发布](https://main.qcloudimg.com/raw/0465c751175fc1cd854a8e03098c6b65/%E5%8F%91%E5%B8%83.png)

![发布2](https://main.qcloudimg.com/raw/bd581341c0bef593b64c6f068e47b587/%E5%8F%91%E5%B8%832.png)

复制监听域名，在浏览器的新标签中粘贴此域名并前往，得到流中设置的返回值。

![复制域名](https://main.qcloudimg.com/raw/60df79552e81495e429c5a37b80625d0/%E5%A4%8D%E5%88%B6%E5%9F%9F%E5%90%8D.png)

![验证](https://main.qcloudimg.com/raw/058f748ef5bfadb6c8d64a6020e73550/%E9%AA%8C%E8%AF%81.png)

