## 操作场景

IP 访问控制是 API 网关提供的安全防护能力，主要用于限制 API 的调用来源 IP，您可以通过配置某个 API 的 IP 白名单/黑名单来允许/拒绝某个来源的 API 请求。

>?历史功能中的 IP 访问控制策略数据已经迁移到了 IP 访问控制插件中，请您前往 [插件页面](https://console.cloud.tencent.com/apigateway/plugin) 管理。

## 操作步骤

### 步骤1：创建插件

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)。
2. 在左侧导航栏，单击 **插件>系统插件** ，进入系统插件列表页。
3. 单击列表左上角的 **新建** ，插件类型选择 **IP 访问控制插件**。

	<img src="https://qcloudimg.tencent-cloud.cn/raw/301a249483eb3f511622c95d671aa0ca.png" width=800/>

### 步骤2：绑定 API 并生效

1. 在系统插件列表中选中刚刚创建好的插件，单击操作列的**绑定 API**。
2. 在绑定 API 弹窗中选择服务和环境，并选择需要绑定插件的 API。
3. 单击**确定**，即可将插件绑定到 API，此时插件的配置已经对 API 生效。

	<img src="https://qcloudimg.tencent-cloud.cn/raw/4486e4bb98231b5c8d9b038a3fa4c31f.png" width=600/>


## PluginData
<dx-codeblock>
:::  json
{
    "type":"white_list",    // IP访问控制类型，支持白名单模式（white_list）或黑名单模式（black_list）
    "blocks":"1.1.1.1\n1.1.1.0/24"    // IP地址段，用\n分隔
    "descriptions":{"1.1.1.1":"desc", "1.1.1.0/24":"desc"} //ip描述，本字段可省略
}
:::
</dx-codeblock>

## 注意事项

- IP 访问控制插件支持黑名单/白名单方式。使用白名单时，不在白名单的请求将被 API 网关拒绝；使用黑名单时，黑名单中的 IP 请求将被 API 网关拒绝。
- IP 访问控制插件的 IP 支持填写 IP 或 CIDR，多个 IP 或 CIDR 间用英文分号分隔。
- IP 访问控制插件的IP支持增加描述信息，"descriptions" 字段为可选项。


## 使用限制

专享实例中暂时不支持对**内网**客户端 IP 进行访问控制。
