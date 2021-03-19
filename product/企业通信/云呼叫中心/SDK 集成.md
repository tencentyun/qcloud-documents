## 总体介绍
TCCC SDK 旨在满足具有开发资源的客户，将 TCCC 的能力便捷地集成到自有的系统中，且与 TCCC Web 坐席页面保持基本一致。
开发者可以通过 [快速集成](#integrate) 中的步骤，快速将 SDK 集成到自己的系统中，便于第一时间体验 SDK 效果。然后通过 [最佳实践](#practice) 对 SDK 进行完整集成，并应用于生产环境。

<span id = "integrate"></span>
## 快速集成
### 注意事项
快速集成中所描述的获取 SDK 登录 Token 的方式只用于调试，生产环境集成 SDK 请参考下面的 [最佳实践](#practice)。
### 步骤1：获取密钥

获取主账号访问密钥或者子账号访问密钥文档请参考 [主账号访问密钥管理](https://cloud.tencent.com/document/product/598/40488)。请注意生产环境中**密钥要放在后台，一定不要写在页面上**。

### 步骤2：获取 SDK 登录 Token

获取 Token 接口的相关说明，请查阅 [创建 SDK 登录 Token](https://cloud.tencent.com/document/api/679/49227)。除了文档中使用 SDK 或者接口的方式获取之外，通过 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=ccc&Version=2020-02-10&Action=CreateSDKLoginToken) 可以**更快速**获取 Token，并用于调试。<span id = "above"></span>
![](https://main.qcloudimg.com/raw/446da4e24d5d1052dd17ecae01174fe7.png)
进入 API Explorer 界面之后，使用 [上图步骤](#above) 获取到的密钥发送请求。
![](https://main.qcloudimg.com/raw/9ca0ca3737b0e3c0ff3bf81d1b097fd8.png)
>!Token 的有效期目前只有 10 分钟，请在获取到之后立即进行调试使用，避免过期。

### 步骤3：同步客服账号
申请过 TCCC 实例之后，TCCC 实例中至少有一位管理账号，快速集成时可以使用这一账号，如果需要使用其他账号进行快速集成，请参阅 [客服管理](https://cloud.tencent.com/document/product/679/48056) 的操作步骤进行手动添加。

### 步骤4：初始化 SDK
<span id = "Examples"></span>示例如下：
```javascript
// 调用腾讯云 API 获取 Token, SdkURL
// API 接口连接 https://cloud.tencent.com/document/api/679/49227
// 自己需要补充 SdkAppId 和 SeatUserId
const scriptDom = document.createElement('script')
scriptDom.dataset.token = Token
scriptDom.dataset.sdkAppId =SdkAppId
scriptDom.dataset.userid = SeatUserId
scriptDom.src = SdkURL
document.body.appendChild(scriptDom)
```
效果如下图所示：
![](https://main.qcloudimg.com/raw/409fdbf91e4eec0580e12a7f8ef77fc1.png)

<span id = "practice"></span>
## 最佳实践 
### 总体流程

详细如下图所示：
![](https://main.qcloudimg.com/raw/3d60d94dd3bac96c3697ef18e69e4d63.png)
**流程解析：**
1. 开发者页面登录鉴权请求，一般是密码登录。
2. <span id = "step2"></span>开发者后台对鉴权信息进行校验，通过则进行下一步，否则返回错误。
3. 开发者后台向 TCCC 后台请求，获取 SDK 登录 Token。
4. TCCC 后台返回 SDK 登录 Token。
5. <span id = "step5"></span>开发者后台向开发者页面 返回 SDK 登录 Token 和 URL。
6. 开发者页面使用**第5步**返回的 Token 和 URL 初始化 SDK。
7. 页面会使用 URL 加载 SDK。
8. 页面初始化 SDK 完毕之后，SDK 内部会请求 TCCC 后台对初始化传入的 Token 进行校验。
9. TCCC 后台校验 Token，如果通过会返回 SDK 的登录票据，否则返回错误。
10. TCCC 后台返回 SDK 登录票据。

###  步骤1：获取密钥
 获取密钥流程与 [快速集成](#integrate) 中保持一致。

### 步骤2：同步客服账号
同步客服账号有两种方式：
- 使用 TCCC 管理端 [手动添加客服账号](https://cloud.tencent.com/document/product/679/48056)。
- 使用腾讯云 [API](https://cloud.tencent.com/document/api/679/49677#4.-.E7.A4.BA.E4.BE.8B) 或者 [SDK](https://cloud.tencent.com/document/api/679/49677#SDK) 从**后台**添加客服账号，**此种方式下，建议使用 SDK**。

开发者可以根据自己实际情况采用上述任一方式向 TCCC 同步客服账号。

### 步骤3：获取 SDK 登录 Token
开发者后台在总体流程 [**第2步**](#step2) 鉴权通过之后，使用 [接口](https://cloud.tencent.com/document/api/679/49227) 拉取 SDK 登录 Token，返回给开发者页面用以初始化 TCCC SDK。

### 步骤4：初始化 SDK
开发者页面使用总体流程 [**第5步**](#step5) 中获取 Token 和 URL初始化 SDK，[示例代码](#Examples) 在快速集成的初始化 SDK 章节已给出。
