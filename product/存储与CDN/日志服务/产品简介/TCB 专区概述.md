## 什么是 TCB

云开发（Tencent Cloud Base，TCB）是腾讯云为移动开发者提供的一站式后端云服务，帮助开发者统一构建和管理资源，免去了移动应用开发过程中繁琐的服务器搭建及运维、域名注册及备案、数据接口实现等繁琐流程，开发者可以专注于业务逻辑的实现，而无需理解后端逻辑及服务器运维知识，开发门槛更低，效率更高。
关于 TCB 接入指南、使用手册，请参考 [TCB 官方文档](https://cloud.tencent.com/document/product/876)。

### 架构图

TCB 引入 Serverless 技术架构，让您在构建应用的过程中，无需关注计算资源的获取和运维。Serverless 架构并非无服务器，其服务器被隐藏至后台运行。您无需考虑基础设施，从而节约更多时间成本。

以 TCB 在小程序中的应用为例：在小程序端，使用官方提供的接口，在云函数端，使用官方提供的 Node SDK，就可以操作云资源，同时 TCB 也可兼容用户原有的后台架构。
![](https://main.qcloudimg.com/raw/4ca2de52c09ebb90564b9189bd8c8d0f.png)

## 什么是 TCB 专区

日志服务 TCB 专区是为了保存云开发 TCB 相关产品（无服务函数 SCF 等）运行时产生的日志，而独立搭建的日志集群。在底层硬件层面独立于日志服务其他地域（北京、上海、广州、成都等地域）。

只有当您在“微信小程序开发者工具”中开通了“云开发”服务后，才能在腾讯云控制台中看到“TCB专区”。如需了解如何开通”云开发”服务，请参考 [TCB 快速入门文档](https://cloud.tencent.com/document/product/876/31614)。

## 限制说明

与非 TCB 专区的地域（北京、上海、广州、成都等地域）相比，TCB 专区内的日志资源（日志集、日志主题）在腾讯云控制台和腾讯云 API 上有相关使用限制，仅支持在腾讯云控制台上查询资源用量，日志集和日志主题基础信息，不开放腾讯云 API 接口。

下表是关于 TCB 专区资源限制的详细说明：

<table>
   <tr>
      <th>资源类别</th>
      <th>操作项</th>
      <th>腾讯云控制台</th>
      <th>腾讯云 API</th>
			<th><center>说明</center></th>
   </tr>
   <tr>
      <td>概览</td>
      <td>查看</td>
			<td><b>支持</b></td>
      <td>不支持</td>
      <td>支持在腾讯云控制台中查看 TCB 资源消耗，不提供腾讯云 API 接口</td>
   </tr>
   <tr>
      <td rowspan=4>日志集</td>
      <td>创建</td>
      <td>不支持</td>
      <td>不支持</td>
      <td>微信开发工具中，开启日志服务时创建，不开放接口</td>
   </tr>
   <tr>
      <td>删除</td>
      <td>不支持</td>
      <td>不支持</td>
      <td>微信开发工具中，关闭日志服务时删除，不开放接口</td>
   </tr>
   <tr>
      <td>修改</td>
      <td>不支持</td>
      <td>不支持</td>
      <td>微信开发工具默认配置，不开放接口</td>
   </tr>
   <tr>
      <td>查询</td>
			<td><b>支持</b></td>
      <td>不支持</td>
      <td>仅支持在腾讯云控制台查看，不提供腾讯云 API 接口</td>
   </tr>
   <tr>
      <td rowspan=4>日志主题</td>
      <td>创建</td>
      <td>不支持</td>
      <td>不支持</td>
      <td>微信开发工具中，开启日志服务时创建，不开放接口</td>
   </tr>
   <tr>
      <td>删除</td>
      <td>不支持</td>
      <td>不支持</td>
      <td>微信开发工具中，关闭日志服务时删除，不开放接口</td>
   </tr>
   <tr>
      <td>修改</td>
      <td>不支持</td>
      <td>不支持</td>
      <td>微信开发工具默认配置，不开放接口</td>
   </tr>
   <tr>
      <td>查询</td>
			<td><b>支持</b></td>
      <td>不支持</td>
      <td>仅支持在腾讯云控制台查看，不提供腾讯云 API 接口</td>
   </tr>
   <tr>
      <td>日志采集</td>
      <td>采集配置</td>
      <td>不支持</td>
      <td>不支持</td>
      <td>采集配置由 TCB 产品侧默认设定，不开放接口</td>
   </tr>
   <tr>
      <td rowspan=2>日志检索</td>
      <td>配置</td>
      <td>不支持</td>
      <td>不支持</td>
      <td>检索配置由 TCB 产品侧默认设定，不开放接口</td>
   </tr>
   <tr>
      <td>检索</td>
      <td>不支持</td>
      <td>不支持</td>
      <td>日志检索请移步到微信开发工具，云平控制台不开放检索接口</td>
   </tr>
   <tr>
      <td rowspan=4>机器组管理</td>
      <td>创建</td>
      <td>不支持</td>
      <td>不支持</td>
      <td rowspan=4>TCB 日志主题不涉及机器组管理功能</td>
   </tr>
   <tr>
      <td>删除</td>
      <td>不支持</td>
      <td>不支持</td>
   </tr>
   <tr>
      <td>修改</td>
      <td>不支持</td>
      <td>不支持</td>
   </tr>
   <tr>
      <td>查询</td>
      <td>不支持</td>
      <td>不支持</td>
   </tr>
   <tr>
      <td rowspan=4>日志投递</td>
      <td>创建</td>
      <td>不支持</td>
      <td>不支持</td>
      <td rowspan=4>TCB 日志主题不涉及日志投递功能</td>
   </tr>
   <tr>
      <td>删除</td>
      <td>不支持</td>
      <td>不支持</td>
   </tr>
   <tr>
      <td>修改</td>
      <td>不支持</td>
      <td>不支持</td>
   </tr>
   <tr>
      <td>查询</td>
      <td>不支持</td>
      <td>不支持</td>
   </tr>
</table>
