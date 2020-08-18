## 操作场景
API 创建即在 API 网关内完成 API 的定义。该任务指导您通过 API 网关控制台，在服务下创建一个 API。

## 前提条件
已完成 [服务创建](https://cloud.tencent.com/document/product/628/11787)。

## 操作步骤
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)，在左侧菜单栏中选择【服务】。
2. 在服务列表中，单击目标服务的服务名，查看该服务。
3. 在服务信息中，单击【管理 API】标签页，根据后端业务类型选择创建【通用 API】或【微服务 API】。
4. 单击【新建】，进行后续配置。

## API 类型
目前在 API 网关中可创建五种后端类型的 API，其中后端对接 HTTP、SCF、mock、WEBSOCKET 的 API 统称为通用 API，后端对接 TSF 的 API 称为微服务API，具体如下表所示：
<table>
<thead>
  <tr>
    <th>类型</th>
    <th>对接后端</th>
    <th>文档</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="4">通用 API</td>
    <td>HTTP</td>
    <td rowspan="4"><a href="https://cloud.tencent.com/document/product/628/11797">创建通用 API</a></td>
  </tr>
  <tr>
    <td>云函数 SCF</td>
  </tr>
  <tr>
    <td>mock</td>
  </tr>
  <tr>
    <td>WEBSOCKET</td>
  </tr>
  <tr>
    <td>微服务 API</td>
    <td>腾讯微服务平台 TSF</td>
    <td><a href="https://cloud.tencent.com/document/product/628/17561">创建微服务 API</a></td>
  </tr>
</tbody>
</table>

<span id="basic"></span>

## API 基础信息
 API 基础信息包括：
 * API 所属服务：服务是 API 管理的集合，任一具体 API 均需要归属于某一个服务。在 API 创建时，可以选择已创建的服务，或创建新的服务。
 * API 路径：API 的请求域名路径。
 * 方法：API 请求方法。API 路径 + API 请求方法，是 API 的唯一标识。
 * 描述：API 的备注信息。
 ![](https://main.qcloudimg.com/raw/0882f112d159833afd25b07ea6880608.png)

