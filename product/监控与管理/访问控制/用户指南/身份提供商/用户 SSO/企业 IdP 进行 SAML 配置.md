##  操作场景

企业原有的身份系统作为身份提供商（IdP），需进行腾讯云 SP 的 SAML 配置，以建立企业 IdP 对腾讯云的信任，实现企业 IdP 用户通过用户 SSO 的方式登录腾讯云。

## 操作步骤

1. 从腾讯云获取 SAML 服务提供商元数据 URL。
   1. 腾讯云账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)。
   2. 在左侧导航栏中，单击**身份提供商** > **用户 SSO**。
   3. 在用户 SSO 管理页面可查看或复制当前用户的 SAML 服务提供商元数据 URL。
      ![](https://qcloudimg.tencent-cloud.cn/raw/e36ef305cfbabd0cefdf57ad16c8cd8d.png)
2. 在企业 IdP 中创建一个 SAML SP 并将腾讯云配置为可信赖的服务提供商，具体配置方式可根据企业 IdP 的实际情况选择以下几种：
   - 企业 IdP 支持 URL 配置：将步骤1中的腾讯云服务提供商元数据 URL 直接复制到企业 IdP 中进行配置。
   - 企业 IdP 支持上传文件配置：将步骤1中的腾讯云服务提供商元数据 URL 复制到浏览器打开并保存为 XML 格式的文件，然后再将文件上传到企业 IdP 中进行配置。
   - 上述两种方式企业 IdP 均不支持：这种情况，需要在企业 IdP 上手动配置以下参数：

| 参数      | 是否必选 | 说明                                                         |
| --------- | -------- | ------------------------------------------------------------ |
| Entity ID | 必选     | 下载的元数据 XML 中，EntityDescriptor 元素的 entityID 属性值。 |
| ACS URL   | 必选     | 下载的元数据 XML 中，AssertionConsumerService 元素 Location 属性值。 |

> ? 如您需要指定跳转腾讯云的其他页面，可使用 https://cloud.tencent.com/login/saml?s_url=xxxx 形式指定，其中 xxxx 为需要指定的地址，需要做 urlencode。
