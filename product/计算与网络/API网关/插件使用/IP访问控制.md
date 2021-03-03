## 操作场景

IP 访问控制是 API 网关提供的安全防护能力，主要用于限制 API 的调用来源 IP，您可以通过配置某个 API 的 IP 白名单/黑名单来允许/拒绝某个来源的 API 请求。

>?原有的 IP 访问控制策略数据已经迁移到了 IP 访问控制插件中，请您前往 [插件页面](https://console.cloud.tencent.com/apigateway/plugin) 管理。

## 操作步骤

### 步骤1：创建插件

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)。
2. 在左侧导航栏，单击【插件】，进入插件列表页。
3. 单击页面左上角的【新建】，新建一个 IP 访问控制插件。
	  ![](https://main.qcloudimg.com/raw/f235b18119f3c55a41f95d4bbebe42f5.png)

### 步骤2：绑定 API 并生效

1. 在列表中选中刚刚创建好的插件，点击操作列的【绑定API】。
2. 在绑定 API 弹窗中选择服务和环境，并选择需要绑定插件的 API。
	 ![](https://main.qcloudimg.com/raw/d7fd3c3539d6f623f45ebfdf0674d97e.png)
3. 单击【确定】，即可将插件绑定到 API，此时插件的配置已经对 API 生效。

## 注意事项

- IP 访问控制插件支持黑名单/白名单方式。使用白名单时，不在白名单的请求将被 API 网关拒绝；使用黑名单时，黑名单中的 IP 请求将被 API 网关拒绝。
- IP 访问控制插件的 IP 支持填写 IP 或 CIDR，多个 IP 或 CIDR 间用英文分号分隔。
