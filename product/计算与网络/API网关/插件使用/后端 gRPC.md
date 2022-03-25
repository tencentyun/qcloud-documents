
## 操作场景

后端 gRPC 插件用于客户端到 API 网关使用 HTTP/HTTPS 协议，API 网关到业务后端使用 gRPC/gRPCS 协议的情况。
通过后端 gRPC 插件，API网关可获得用于把 HTTP/HTTPS 协议转换为 gRPC/gRPCS 协议的 `.proto` 文件，并根据 `.proto` 文件中定义的规则来转换请求内容，再将转换后的内容传递给业务后端。

## 请求流程

![](https://qcloudimg.tencent-cloud.cn/raw/4f5eec8d3445e456ce0b415e8742c0e7.png)

## 操作步骤

### 步骤1：创建插件

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)。
2. 在左侧导航栏，单击**插件—系统插件**，进入系统插件列表页。
3. 单击页面左上角的**新建**，选择插件类型为**后端gRPC**，新建一个后端 gRPC 插件。缓存插件的配置项如下：

<table>
<tr>
<th>参数</th>
<th>是否必填	</th>
<th>说明</th>
</tr>
<tr>
<td>.proto 描述文件</td>
<td>必填	</td>
<td>用于把 HTTP/HTTPS 协议转换为 gRPC/gRPCS 协议的 `.proto` 文件</br>文件中代码遵循 ProtoBuf 语法，支持 proto2 和 proto3 两个版本</td>
</tr>
</table>

![](https://qcloudimg.tencent-cloud.cn/raw/15a80050f204abe7da29ce3824a65b38.png)

### 步骤2：绑定 API 并生效

1. 在列表中选中刚刚创建好的插件，单击操作列的**绑定 API**。
2. 在绑定 API 弹窗中选择服务和环境，并选择需要绑定插件的 API。
   ![](https://main.qcloudimg.com/raw/d7fd3c3539d6f623f45ebfdf0674d97e.png)
3. 单击**确定**，即可将插件绑定到 API，此时插件的配置已经对 API 生效。

## 注意事项

- `.proto` 描述文件大小不能超过1MB。
- 描述文件必须严格遵循 ProtoBuf 语法。
- 当 API 前端配置为 HTTP/HTTPS 协议，后端为 gRPC/gRPCS 协议时，如果此 API 未绑定“后端gRPC”插件，请求将会报错。
- 仅客户端请求是 POST、GET、PUT、PATCH、DELETE 方法时，才能正常请求“前端配置为 HTTP/HTTPS 协议，后端为 gRPC/gRPCS 协议的API”，其他方法会报错。
