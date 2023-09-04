## 操作场景
API 创建即在 API 网关内完成 API 的定义。该任务指导您通过 API 网关控制台，在服务下创建一个 API。

## 前提条件
已完成 [服务创建](https://cloud.tencent.com/document/product/628/11787)。

## 操作步骤
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/service) ，在左侧导航栏单击服务。
2. 在服务列表中，单击目标服务的服务名，查看该服务。
3. 在服务信息中，单击**管理 API** 标签页。
4. 单击 **新建**，进行后续配置。

## API 类型及后端类型
目前在 API 网关中可创建两种 API类型，第一种类型是通用 API，后端对接支持（公网 URL/IP、VPC、SCF、COS 、Mock）。第二种类型是微服务 API，后端对接支持（微服务框架 TSF、VPC），具体如下表所示。
其中，后端类型依赖该产品资源支持该地域，如对应产品不支持某个地域，例如事件总线不支持深圳金融，则 API 网关亦不支持。
如有特殊业务需要，可提交工单需求。
<table>
<thead>
  <tr>
    <th>类型</th>
    <th>对接后端</th>
    <th>文档</th>
		<th>特殊限制</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="6">通用 API</td>
    <td>公网 URL/IP</td>
    <td><a href="https://cloud.tencent.com/document/product/628/52199">创建后端对接公网 URL/IP 的 API</a></td>
    <td>全地域支持，除去成都地域共享服务的API不支持</td>

  </tr>
  <tr>
	<td>VPC 内资源</td>
  <td><a href="https://cloud.tencent.com/document/product/628/52200">创建后端对接 VPC 内资源的 API</a></td>
	<td>全地域支持</td>
  </tr>
  <tr>
    <td>云函数 SCF</td>
		<td><a href="https://cloud.tencent.com/document/product/628/52201">创建后端对接云函数 SCF 的 API</a></td>
			<td>全地域支持</td>
  </tr>
	<tr><td>对象存储 COS</td>
<td><a href="https://cloud.tencent.com/document/product/628/70988">创建后端对接对象存储 COS 的 API</a></td>
	<td>全地域支持</td>
</tr>
	<tr>
	<td>事件总线</td>
<td><a href="https://cloud.tencent.com/document/product/628">创建后端对接事件总线 EB 的 API</a></td>
	<td>全地域支持，除去深圳金融地域共享和专享后端类型选择 EB 时暂不支持</td>
</tr>

  <tr>
    <td>Mock</td>
		<td><a href="https://cloud.tencent.com/document/product/628/52202">创建后端对接 Mock 的 API</a></td>	
		<td>全地域支持</td>
  </tr>
 <tr>
    <td rowspan="6">微服务 API</td>
    <td>微服务平台 TSF</td>
    <td><a href="https://cloud.tencent.com/document/product/628/52203">创建后端对接微服务TSF 的 API</a></td>
			<td>全地域支持，除去深圳金融共享和专享暂不支持</td>
  </tr>
  <tr>
	<td>VPC 内资源</td>
  <td><a href="https://cloud.tencent.com/document/product/628/52200">创建后端对接 VPC 内资源的 API</a></td>
		<td>全地域支持，除去深圳金融共享和专享暂不支持</td>
  </tr>
</tbody>
</table>

<span id="basic"></span>

## API 基础信息
 API 基本信息包括：
 * API 所属服务：服务是 API 管理的集合，任意一个具体 API 均需要归属于某一个服务。在 API 创建时，需要选择已创建的服务。
 * API 访问路径：API 的请求域名路径。
 * 方法：API 请求方法。API 路径 + API 请求方法，是 API 的唯一标识。
 * 描述：API 的备注信息。
 * 前端方法：API请求的前端类型，如 HTTP 或 HTTPS
 
 <img src="https://qcloudimg.tencent-cloud.cn/raw/d1a18e3aca09a4e5544eaf44fd3aa5e4.png " width=600/>
 
 
 ## API 前端路径匹配优先级
 
- 如果 API path 以 = 开始，代表精确匹配，优先级最高。
- 如果 API path 以 ^~ 开始，代表优先前缀匹配，后面不能跟正则表达式，优先级第二。
- 如果 API path 为正则表达式（包括有路径变量），优先级第三。
- 如果 API path 为普通字符串，字符串最长时优先级高，满足最长匹配。 
