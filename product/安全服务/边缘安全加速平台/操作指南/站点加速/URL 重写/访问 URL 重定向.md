## 功能简介

将客户端实际发起访问请求的 URL 由节点重定向到目标 URL。

## 适用场景

将您业务场景中原先需要源站生成并返回的 URL 重定向，改为直接由 EdgeOne 边缘节点构造并且返回，减少回源的网络延时和源站生成 URL 重定向的负载，提升客户端访问性能。

## 操作指南

1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**规则引擎**。

2. 在规则引擎页面，选择所需站点，可按需配置访问 URL 重定向规则。如何使用规则引擎，请参见 规则引擎。

3. 配置项说明：

   | 配置项       | 说明                                                         |
   | :----------- | :----------------------------------------------------------- |
   | 目标 URL     | 希望重定向的目标 URL，例如：`https://www.example.com/images/foo.jpg` 或 `https://www.example.com/foo/bar` |
   | 携带查询参数 | 是否携带原查询参数至目标 URL ，默认会携带                    |
   | 状态码       | 选择重定向的响应状态码：<br>- 302（默认）<br/>- 301<br/>- 303<br/>- 307 |

## 配置示例

若请求 URL `https://www.example.com/path/foo.html` 的访问 URL 重定向配置如下：

![](https://qcloudimg.tencent-cloud.cn/raw/f6fc8e8bdfc23f2e945bd060f759ba9a.png)

则客户端请求：`https://www.example.com/path/foo.html?key1=value1`，则节点响应 301 重定向至`https://www.example.com/newpath/bar.html`。
