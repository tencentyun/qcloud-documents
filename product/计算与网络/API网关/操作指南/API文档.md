## 操作场景

您可通过 API 文档功能把托管在 API 网关上的 API 生成一份精美的 API 文档，以提供给第三方调用您的 API。
>?API 文档功能完全免费，由 CODING DevOps 提供技术支持，点击 [了解 CODING 的更多能力](https://coding.net/)。

## 前提条件

已经在 API 网关创建了服务和 API（参考 [创建服务](https://cloud.tencent.com/document/product/628/11787) 和 [创建 API ](https://cloud.tencent.com/document/product/628/11795)），并将服务发布到任意环境（参考 [服务发布](https://cloud.tencent.com/document/product/628/11809) ）。

## 操作步骤
### 创建文档

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，在左侧导航栏单击【工具】>【API 文档】。
   ![](https://main.qcloudimg.com/raw/c2df5fec87cd2f29a4f27d540bd4abe7.png)
2. 在 API 文档页面，单击【立即创建】，在弹窗中填写文档名称，选择环境、服务、API 后单击【提交】。
   ![](https://main.qcloudimg.com/raw/7959f140dacae6911eedab4f0c397a4f.png)
3. 耐心等待 API 文档构建完成即可。

### 文档详情

下图为 API 文档的详情页：
![](https://main.qcloudimg.com/raw/450ea44198363f1b787a35a7cdbce174.png)

各参数说明如下：

| 参数 | 说明 |
| ---- | ---- |
| API 文档地址  |  当前 API 文档的访问地址。  |  
| API 文档密码  |  当前 API 文档的密码。API 文档默认加密，必须使用密码才能看到内容。  |  
| 分享口令  |  您可复制口令并分享给第三方。  |  
| 上次更新时间  |  上次更新 API 文档的时间。  |  
| 所属服务  |  生成文档的 API 所属的服务。  |  
| 所属环境  |  服务所发布到的环境，环境可用于生成 API 调用地址。  |  
| 生成文档的 API  |  当前 API 文档包含的 API。  |  

### 访问文档

1. 复制 API 文档地址，在浏览器中输入，即可打开文档登录页；
   ![](https://main.qcloudimg.com/raw/8f617c72722008c7d51889912ae3da12.png)
2. 在文档登录页输入 API 文档密码，即可查看文档内容。
   ![](https://main.qcloudimg.com/raw/6af54019f8304f96d6729314a06d0c43.png)

### 更新文档

编辑生成文档的 API 后，API 文档不会同步触发更新，使用“更新文档”功能可以保证 API 文档与生成文档的 API 信息一致。操作步骤如下：
1. 在文档详情页右上角单击【更新】。
2. 在确认弹窗中单击【确认】，等待文档构建完成即可。
![](https://main.qcloudimg.com/raw/a7ec27c117b42b9a49aa33c1b6faa9ba.png)

### 重置密码

重置密码后会生成新的 API 文档密码，用户只能用新密码访问文档，旧密码将无法使用。操作步骤如下：
1. 单击 API 文档密码后的【重置】。
2. 在确认弹窗中单击【确认】，即可生成新的 API 文档密码。
![](https://main.qcloudimg.com/raw/7f044807940c26b5835b0f4cf510e7b2.png)

### 删除文档

1. 在文档详情页右上角单击【删除】。
2. 在确认弹窗中单击【确认】，即可完成 API 文档的删除。
