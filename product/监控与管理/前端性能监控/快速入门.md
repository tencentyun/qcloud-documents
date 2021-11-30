本文将为您介绍如何快速使用前端性能监控。


## 步骤1：创建业务系统[](id:step1)
1. 登录 [前端性能监控控制台](https://console.cloud.tencent.com/rum)。
2. 在左侧菜单栏点击 **应用管理**>**业务系统**。
3. 在业务系统管理页单击**创建业务系统**，在弹框中填写业务名称并勾选相关协议即可。

## 步骤2：接入应用[](id:step2)
 1. 登录 [前端性能监控](https://console.cloud.tencent.com/rum)。
 2. 在左侧菜单栏中单击**数据总览**。
 3. 在数据总览页单击**应用接入**，根据下列表格配置应用信息。
<table>
<th>
 配置项
</th>
<th>
 说明
</th>
<tr>
<td>
 应用名称
</td>
<td>
 自定义应用名称，方便您在前端监控平台辨识该应用。
</td>
</tr>
<tr>
<td>
 应用描述
</td>
<td>
 填写应用描述 ，如应用用途、应用简介等，方便其它用户了解该应用。
</td>
</tr>
<tr>
<td>
 应用类型
</td>
<td>
 支持 Web 、小程序（微信、QQ）、Hippy、Weex 和 React Native 应用类型接入。
</td>
</tr>
<tr>
<td>
 应用仓库地址（可选）
</td>
<td>
 填写您的应用仓库地址，可不填写。
</td>
</tr>
<tr>
<td>
 所属业务系统
</td>
<td>
 该功能用于分类管理您接入的应用，您可以根据研发团队、业务逻辑、应用类别等进行应用分类管理。若您没有可用团队，您可以单击右侧的**点我创建**链接，填写完信息后，单击**确认**即创建成功。
</td>
</tr>
<tr>
<td>
 开启 URL 自动聚类
</td>
<td>
 开启后将隶属于同一个域名的 URL ，便于聚类分析。例如<code>app.qq.com/user/123/index.html </code> 和 <code>app.qq.com/user/456/index.html </code> 将会聚类成为 <code>app.qq.com/user/*/index.html </code>。
</td>
</tr>
<tr>
<td>
 抽样率
</td>
<td>
 抽样率用于控制用户侧性能数据（页面测速，接口测速和静态资源测速）上报的比例，其中 100% 表示不抽样，0% 表示完全不上报性能数据。
</td>
</tr>
</table>

4.配置完后单击**下一步**，参考下列说明选择一种方式安装 SDK 。
- **npm**方式安装 SDK（所有应用类型均可使用该方式接入）。下列 Web 应用为例说明如何通过 npm 方式接入 SDK。
 i. 在接入指引页面中复制提供的首行命令，引入 npm 包。
![](https://qcloudimg.tencent-cloud.cn/raw/daf5b47188e69bcf3a6d77f0231b9848.png)
 ii. 在接入指引页面中复制提供的代码初始化 SDK。
![](https://qcloudimg.tencent-cloud.cn/raw/db365dbaa753145e917e7bc1cc955266.png)

- **&lt;script&gt; 标签引入**方式接入 SDK（仅支持 Web 接入类型）。
 i. 在接入指引页面复制提供的 `<script>` 标签 代码。
ii. 把**&lt;script&gt; 标签引入**类型下的代码引入到 `<head></head>` 标签中即可。
![](https://qcloudimg.tencent-cloud.cn/raw/2a0b0ab2df53d6a3650724e299907913.png)
<dx-alert infotype="explain" title="">
按照上述步骤接入后即可使用数据总览、页面性能、异常分析、页面访问（PV、UV）、API 监控和静态资源功能。如需使用日志查询、离线日志、自定义测速和自定义事件，需参考接入指引上报数据。
</dx-alert>


## 步骤3：查看监控数据[](id:step3)
应用接入成功且有一定的数据上报后，您可以前端性能监控控制台查看异常分析和页面性能、页面访问等监控数据。
