腾讯云微搭低代码自定义 API 支持调用第三方服务接口或使用代码来实现业务逻辑。开发者可以在应用、工作流或其他自定义 API 中使用 API。

## 自定义 API 方法实现方式

目前自定义 API 支持三种方式来实现自定义业务逻辑：

- **HTTP 请求**：使用 HTTP 方式调用外部服务，通过简单的配置 HTTP 请求地址、方法、参数等即可完成方法的配置。
- **自定义代码**：集成了常用 NPM 包、数据模型、API 等 [方法](https://cloud.tencent.com/document/product/1301/68440)，只支持 JS 开发语言，可以用来实现自定义业务逻辑。
- **云开发云函数**：用户可以创建和使用云开发的云函数来实现完整的服务端功能，并通过自定义 API 的方法绑定并调用。

具体如何实现自定义 API 可以参见 [新建自定义 API](https://cloud.tencent.com/document/product/1301/68457)。

## 自定义 API 的使用

开发者可以在应用编辑器或其他自定义 API 中使用：
<table>
<tr>
<th colspan = "2" style = "width:41%">使用场景</th>
<th>操作指引</th>
</tr>
<tr>
<td rowspan = "2">应用编辑器</td>
<td><a href = "https://cloud.tencent.com/document/product/1301/68458#components">添加行为事件</a></td>
<td>在组件行为可以调用自定义 API 方法。</td>
</tr>
<tr>
<td><a href = "https://cloud.tencent.com/document/product/1301/68458#editor">自定义方法</a></td>
<td>可以在应用的低代码编辑器及微搭组件的组件代码中使用。</td>
</tr>
<tr>
<td colspan = "2"><a href = "https://cloud.tencent.com/document/product/1301/68458#custom">自定义 API 方法</a></td>
<td>在其他自定义 API 中通过<b>自定义代码</b>方式，可以调用其他自定义 API。</td>
</tr>
</table>

