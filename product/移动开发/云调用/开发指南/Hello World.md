本文介绍扩展程序 Hello World，方便您快速搭建 Web 应用和小程序，体验云开发多端同步能力。最后成型的应用展示如下：
![](https://main.qcloudimg.com/raw/a24c7f33c3123fd954dfe3c0ae761557.png)

您将使用云开发完成的功能有：

- 云函数渲染 Web 页面
- Web 页面和小程序监听页面，内容输入变更同步

## 准备工作

1. 登录腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb)，选择【微信公众号】登录方式，授权使用腾讯云登录小程序环境。
2. 单击环境名称，进入环境总览页面，如下所示：
   ![](https://main.qcloudimg.com/raw/553e753bafd5de308a2f8518162d83d9.png)
> ! 
> - 请记住您的环境 ID，这个 ID 在后续步骤将被使用。您可单击**资源概况**上方的【<img src="https://main.qcloudimg.com/raw/a06f957521023a64e977041f9181f251.jpg"  style="margin:0;">】图标进行复制。
> - 微信小程序开发者请使用【其他登录方式】>【微信公众号登录】登录，再选择关联的小程序账户登录；QQ 小程序开发者可直接通过 QQ 小程序开发者 IDE【云开发】按钮登录，也可以通过关联的腾讯云账户登录。

## 操作步骤

### 步骤1：安装扩展

您可以通过 [云开发控制台](https://console.cloud.tencent.com/tcb/extensions) 安装和管理扩展。

1. 进入云开发控制台 [云调用](https://console.cloud.tencent.com/tcb/extensions) 页面。
2. 单击 Hello World 扩展能力的【安装】，进行安装扩展。
	 ![](https://main.qcloudimg.com/raw/1955ccf06eb35d45a6cff3feef5475c2.png)
3. 扩展能力安装完毕后，会在该环境内新建一个云函数 `tcb_hello_world` 和一个云数据库集合 `tcb_hello_world`。
	 ![](https://main.qcloudimg.com/raw/26a2a4537d3fc12132378c8427feecfc.png)

### 步骤2：登录方式配置

1. 进入云开发控制台【环境】菜单内的 [登录授权](https://console.cloud.tencent.com/tcb/env/login) 页面。
2. 开启【匿名登录】，允许在应用中使用匿名登录的方式访问云开发。
	 ![](https://main.qcloudimg.com/raw/a1c1e2427fd4ec76f461561edf2e703d.png)

### 步骤3：数据库权限配置

1. 进入云开发控制台的 [数据库](https://console.cloud.tencent.com/tcb/db) 页面。
2. 单击 `tcb_hello_world` 集合名称进入集合详情页。
![](https://main.qcloudimg.com/raw/1268b3c1eb5b598b77c06a6c1f8dbeec.png)
3. 单击切换到【权限设置】页签，单击【切换到安全规则】，在权限设置编辑框内输入：
```json
{
		"read": true,
		"write": true
}
```
![](https://main.qcloudimg.com/raw/2c072e843b9c0c1309f64b4ba437c894.png)

### 步骤4：访问网页应用

1. 进入云开发控制台【环境】菜单内的 [云接入](https://console.cloud.tencent.com/tcb/env/access) 页面。
2. 找到 `/tcb_hello_world` 触发路径，单击打开网页应用。
	 ![](https://main.qcloudimg.com/raw/709920fc05332c75be107cbc3dc79de2.png)

### 步骤5：移动应用安全来源

1. 进入云开发控制台【环境】菜单内的 [安全配置](https://console.cloud.tencent.com/tcb/env/safety) 页面。
2. 在**移动应用安全来源**中单击【添加应用】，应用标识内填写 `touristappid`，将授权的应用加入白名单并在使用 SDK 时传入分配的凭证信息，才可在终端应用（小程序、App）中使用云开发的身份验证服务。
	 ![](https://main.qcloudimg.com/raw/5bf9d305d560ca89c991247767fa6775.png)
3. 添加完应用之后，单击【获取凭证】，复制凭证至本地，后续该凭证将用于验证移动应用的安全来源。
	 ![](https://main.qcloudimg.com/raw/7c231092d266e9d1ea29a571bc500fbc.png)

### 步骤6：小程序开发

1. 首先打开微信开发者工具，再在浏览器中访问 [Hello World](https://developers.weixin.qq.com/s/Gddfw8mr7egW) 获取代码片段，一键导入代码到微信开发者 IDE 中。注意在导入时，AppID 与云开发中 [安全配置](https://console.cloud.tencent.com/tcb/env/safety) 的**移动应用安全来源**应用标识保持一致。
![](https://main.qcloudimg.com/raw/28e0912fad50e561dc4ef6f731a5bfff.png)
2. 在项目 app.js 中更新如下配置：
```javascript
const cloud = tcb.init({
		env: "${custom_env}", // 当前环境的ID
		appSign: "touristappid",
		appSecret: {
			appAccessKeyId: "移动应用安全来源 版本", // 步骤5.2中获取的移动应用安全来源版本
			appAccessKey: "移动应用安全来源 凭证" // 步骤5.3中获取的移动应用安全来源凭证
		}
});
```
3. 保存小程序代码后，预览小程序界面。
![](https://main.qcloudimg.com/raw/c4d5193da6db5db4604a50ef6ad11a8d.png)


## 结语

到这里，使用云开发完成 Web 端与小程序端的应用同步就已经完成。当您拖动 Web 应用中的数字，微信小程序内也会同步发生改变。效果图如下：
![](https://main.qcloudimg.com/raw/a24c7f33c3123fd954dfe3c0ae761557.png)


## 其他

### 扩展配置信息

您可以配置以下参数：

环境 ID：选择要部署的环境，在哪个环境下使用。

### 计费

此扩展使用其他云开发或其他腾讯云服务，可能会产生相关费用：

- 云函数（[产品定价](https://buy.cloud.tencent.com/price/tcb) 及 [使用明细](https://console.cloud.tencent.com/tcb)）
- 云数据库（[产品定价](https://buy.cloud.tencent.com/price/tcb) 及 [使用明细](https://console.cloud.tencent.com/tcb)）

当您使用云开发扩展时，您只需要为您使用的云资源付费；云开发与云上其他资源分开计费，您可以在 [费用中心](https://console.cloud.tencent.com/expense/bill/overview) 查看具体信息。

### 创建的资源

- __Type__：Cloud Function
  __Description__：借用云开发 HTTP Service 能力，渲染 Web 页面，方便开发者体验云开发能力
- __Type__：Cloud DB
  __Description__：存储用户操作数据，借用实时数据库能力，监听数据变更，实现数据多端同步

### 权限授予

#### 主账户

该扩展能力使用云开发自有资源即可完成，无需再授予其他权限。

#### 子账户

如果想让子账户也能使用该扩展，需要为子账户授予如下权限才能使用：

- __策略__：QcloudAccessForTCBRole
- __描述__：云开发（TCB）对云资源的访问权限
