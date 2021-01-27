企业集成服务平台内置多种应用模版，帮助用户快速适配各种场景，应用模版针对各种常见业务场景抽象出通用的流配置，方便用户快速配置业务流。



HelloWorld 应用是一个新手指引导向的基础应用模版，通过五个组件配置一条简单的流，帮助您快速快入门鹊桥企业集成服务。


## 前提条件

企业集成服务控制台需要填写 [申请信息](https://cloud.tencent.com/apply/p/5tgx7ibxzl) 申请使用。


## 操作步骤

#### 1. 创建应用

1. 登录 [企业集成服务](https://console.cloud.tencent.com/eis) 控制台。
2. 单击【添加应用】，在弹出的添加应用窗口中，配置如下选项：
	- 应用名称：输入应用名称。支持25位以内的中文、字母、数字、\_或-。
	- 添加方式：选择【HelloWorld模版】创建应用。
![](https://main.qcloudimg.com/raw/45151dbce9c84131605e6b189c85167f.png)
3. 单击【确定】即可创建 HelloWord 模板应用。



#### 2. 流配置介绍

1. 单击上述创建的 HelloWord 应用名称，进入应用详情页面。
2. HelloWord 模板应用已配置好流 HelloWorld_Flow，该流中包括五个组件：[HTTP Listener](#httplistener)、[Set Payload](#setpayload)、两个 [Transform](#transform) 和 [Logger](#logger)。
![](https://main.qcloudimg.com/raw/8f95869b0f6d609d6d10ba17902cad58.jpg)

<span id="httplistener"></span>

#### HTTP Listener 组件
HTTP Listener 组件绑定了连接器配置 HelloWorld_Config，设置了监听路径为 `/`，域名前缀为80的监听域名。


![](https://main.qcloudimg.com/raw/325ee8228e4408f82b1389126b7c5860.jpg)


![](https://main.qcloudimg.com/raw/eac6eeaa4c6327caabfd6a5f6384b3aa.jpg)


<span id="setpayload"></span>

#### Set Payload 组件
Set Payload 组件给 payload 属性设置了返回值“Hello” 。

![](https://main.qcloudimg.com/raw/fb582f19bd8d87f2ca38275449fae64f.jpg)


<span id="transform"></span>

#### Transform 组件

- 第一个 Transform 组件对 payload 属性的返回值拼接了字符串“World”。
![](https://main.qcloudimg.com/raw/aaf231c8c0846fddb4bf00c4653f4e8f.jpg)
- 第二个 Transform 组件将 payload 属性返回成一个 entity 类型，以 JSON 的形式将返回值展示出来。
![](https://main.qcloudimg.com/raw/592e72a77a537eebc4bd6f943d5b6572.jpg)

<span id="logger"></span>

#### Logger 组件
Logger 组件打印了 payload 属性的内容。

![](https://main.qcloudimg.com/raw/8de092920ff086fc7b1c899b6d33cdef.jpg)


#### 3. 发布应用

1. 单击页面右上角的【发布】，选择要发布的地域。
![](https://main.qcloudimg.com/raw/f345d5eb6dda3c6ea542562b9d953458.jpg)
2. 单击【确定】，应用将开始发布，发布完成进入运行中的状态。
3. 单击【HTTP Listener 组件】弹出组件窗口，单击组件窗口右侧的【查看】，将弹出连接器配置窗口。
![](https://main.qcloudimg.com/raw/572b86dd81e88bc85bab318c0915800d.jpg)
4. 在地域右侧单击复制按钮即可复制监听域名。
5. 在浏览器地址栏粘贴此域名并前往，即可得到流中设置的返回值。
![](https://main.qcloudimg.com/raw/83294d535443c7297c6d5246878e0f4f.jpg)


