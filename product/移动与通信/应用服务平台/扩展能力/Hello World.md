基于云开发快速搭建 Web 网站和小程序，轻松实现多端同步，帮助开发者轻松开启云上开发之旅。

## 扩展工作模式

当您使用这个扩展时：

1. 云函数渲染 Web 页面。
2. Web 页面和小程序监听页面内容输入变更并同步。

## 前置要求

已经开通 [云开发](https://console.cloud.tencent.com/tcb)。

## 安装扩展


您可以通过 [云开发控制台](https://console.cloud.tencent.com/tcb/extensions)，来安装和管理扩展。


> ! 
> - 微信小程序开发者请使用**其他登录方式** > **微信公众号登录**登录，再选择关联的小程序账户登录。
> - QQ 小程序开发者可直接通过 QQ 小程序开发者 IDE**云开发**登录，也可以通过关联的腾讯云账户登录。


## 使用扩展

1. 进入 [云开发控制台](https://console.cloud.tencent.com/tcb)，单击需安装扩展的环境（下文以 `custom_env` 指代对应的环境 ID），单击左侧菜单栏**环境**页进入环境设置页：
	1. 单击**登录授权**，打开**匿名登录**开关，允许应用中可以使用匿名登录的方式访问云开发；
![](https://main.qcloudimg.com/raw/490bf26b5c0708f11adb213a40ad9604.png)
	2. 单击**安全配置**，单击 **Web 安全域名**下的**添加域名**，添加云函数 HTTP 触发当前环境默认域名： \${custom_env}.service.tcloudbase.com （该域名是云开发为开发者分配的 HTTP 触发云函数的域名，详情可以参考 [HTTP 触发](https://cloud.tencent.com/document/product/876/41136)），允许在该域名的页面下调用 web 云开发；
![](https://main.qcloudimg.com/raw/d739652c8541c718a7433a440f6b02e1.png)
	3. 访问**安全配置**，然后在**移动应用安全来源**中注册 `touristappid`，添加成功后获取凭证信息备用；
![](https://main.qcloudimg.com/raw/5e56f42805e822f2a19ecd35ffaf2ad6.png)
2. 打开 custom_env 环境下的**云数据库**，找到 `tcb_hello_world` 集合进入详情，进入**权限设置** tab 页，单击**切换到安全规则**，输入：
```json
{
		"read": true,
		"write": true
}
```
3. Web 网站：使用浏览器可访问 `https://${custom_env}.service.tcloudbase.com/tcb_hello_world` 。
4. 微信小程序：访问 [Hello World](https://developers.weixin.qq.com/s/Gddfw8mr7egW) 获取代码片段，一键导入代码到微信开发者 IDE 中（不要配置 `AppID`）；在项目 `app.js` 中更新如下配置：
```javascript
const cloud = tcb.init({
  env: "${custom_env}", // 当前环境的ID
  appSign: "touristappid",
  appSecret: {
    appAccessKeyId: "移动应用安全来源 版本", // 步骤1.3中获取的移动应用安全来源版本
    appAccessKey: "移动应用安全来源 凭证" // 步骤1.3中获取的移动应用安全来源凭证
  }
});
```
5. 在 Web 或小程序中拖动数字，即可在另一端看到相同的变化。
> !该扩展为示例 Demo，请按照使用指引来完成配置。注册安全来源时要以 `touristappid` 来注册；在小程序中体验时，不需要配置 `AppID`，填入 `touristappid` 对应的版本及凭证信息即可。


## 其他

### 扩展配置信息

您可以配置以下参数：

- 环境 ID：选择要部署的环境，在哪个环境下使用。

### 计费

此扩展使用其他云开发或其他腾讯云服务，可能会产生相关费用：

- 云函数（[产品定价](https://buy.cloud.tencent.com/price/tcb) 及 [使用明细](https://console.cloud.tencent.com/tcb)）。
- 云数据库（[产品定价](https://buy.cloud.tencent.com/price/tcb) 及 [使用明细](https://console.cloud.tencent.com/tcb)）。

当您使用云开发扩展时，您只需要为您使用的云资源付费；云开发与云上其他资源分开计费，您可以在 [费用中心](https://console.cloud.tencent.com/expense/bill/overview) 查看具体信息。

### 创建的资源

- **Type:** Cloud Function。
  **Description:** 借用云开发 http service 能力，渲染 web 页面，方便开发者体验云开发能力。
- **Type:** Cloud DB。
  **Description:** 存储用户操作数据，借用实时数据库能力，监听数据变更，实现数据多端同步。

### 权限授予

#### 主账号

该扩展能力使用云开发自有资源即可完成，无需再授予其他权限。

#### 子账号

如果想让子账号也能使用该扩展，需要为子账号授予如下权限才能使用：

- **策略:** QcloudAccessForTCBRole
-   **描述:** 云开发（TCB）对云资源的访问权限。
