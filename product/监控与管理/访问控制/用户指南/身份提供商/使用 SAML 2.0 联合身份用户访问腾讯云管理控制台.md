## 操作场景

腾讯云支持基于 SAML 2.0（安全断言标记语言 2.0）的联合身份验证，SAML 2.0 是许多身份验证提供商（Identity Provider， IdP）使用的一种开放标准。您可以通过基于 SAML 2.0 联合身份验证将身份提供商与腾讯云进行集成，从而实现身份提供商用户自动登录（单一登录）腾讯云控制台管理腾讯云的资源，不必为企业或组织中的每一个成员都创建一个 CAM 子用户。

## 操作步骤

您可以通过本步骤创建一个或多个角色作为身份提供商的载体登录腾讯云管理控制台，授予权限后可以在权限范围内通过腾讯云控制台管理主账号下的资源。

1. 通过浏览器访问身份提供商的门户网站，并选择跳转到腾讯云管理控制台。
2. 该门户网站可以验证当前用户的身份。
3. 验证成功后，该门户网站会生成一个 SAML 2.0 身份验证响应，其中包括识别用户身份的断言以及用户的相关属性。该门户网站将此响应发送到客户端浏览器。
4. 该客户端浏览器将被重定向到腾讯云单一登录终端节点并发布 SAML 断言。
5. 终端节点将代表用户请求临时安全凭证，并创建一个使用这些凭证的控制台登录 URL。
6. 腾讯云将登录 URL 作为重定向发回客户端。
7. 该客户端浏览器将重定向到腾讯云管理控制台。如果 SAML 2.0 身份验证响应包含映射到多个 CAM 角色的属性，则系统将首先提示用户选择要用于访问控制台的角色。

从用户的角度来看，整个流程以透明的方式进行：用户在您企业组织的内部门户网站开始操作，在腾讯云管理控制台结束操作，无需提供任何腾讯云凭证。有关如何配置此行为的概述以及指向详细步骤的链接，请参阅以下章节。

### 在企业组织中配置基于 SAML 2.0 的身份提供商<span id="step2.0"></span>

在您的企业组织中，配置身份存储（例如 Azure Active Directory）以使用基于 SAML 2.0 的身份提供商，例如 Azure Active Directory、OneLogin、Okta 等。通过使用身份提供商，可以生成一个元数据文档。该文档将您的企业组织描述为包含身份验证密钥的身份提供商，会把您企业组织的门户网站配置为将访问腾讯云管理控制台的用户请求路由至腾讯云终端节点，以便使用 SAML 2.0 断言进行身份验证。如何配置您的身份提供商来生成 metadata.xml 文件取决于您的身份提供商。请参阅您的 IdP 文档以获得指示，或参阅以下文档。

- [Azure Active Directory 单点登录腾讯云指南](https://cloud.tencent.com/document/product/598/35713)
- [OneLogin 单点登录腾讯云指南](https://cloud.tencent.com/document/product/598/35817)
- [Okta 单点登录腾讯云指南](https://cloud.tencent.com/document/product/598/37658)
- [ADFS 单点登录腾讯云指南](https://cloud.tencent.com/document/product/598/42702)

### 在 CAM 中创建 SAML 身份提供商

您可以在访问管理（CAM）控制台创建一个 SAML 2.0 身份提供商，该身份提供商是访问管理（CAM）中的一个实体，可以认为是外部授信账号集合。基于 SAML 2.0 联合身份验证的身份提供商描述了支持 SAML 2.0（安全断言标记语言 2.0）标准的身份提供商服务。在创建过程中，您可以上传在 [在企业组织中配置基于 SAML 2.0 的身份提供商](#step2.0) 中的身份提供商的元数据文档。详细请参阅 [创建身份提供商](https://cloud.tencent.com/document/product/598/30290)。

### 在腾讯云中为 SAML 提供商用户配置权限

您可以创建一个角色，用于建立您企业组织中的身份提供商和腾讯云的互信关系。在 SAML 2.0 断言上下文中，角色可分配给身份提供商验证身份的联合身份用户使用。此角色允许身份提供商请求临时安全证书进行腾讯云资源访问。在此过程中，您可以为该角色关联策略和设置角色的使用条件，从而决定联合身份用户在腾讯云资源的访问范围及使用条件。详细请参阅 [为身份提供商创建角色](https://cloud.tencent.com/document/product/598/19381#.E9.80.9A.E8.BF.87.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.88.9B.E5.BB.BA)。

### 配置身份提供商的单一登录

下载并保存腾讯云联合元数据 XML文档：http://cloud.tencent.com/saml.xml， 将您企业组织中的身份提供商属性映射到腾讯云的属性，建立您企业组织中的身份提供商和腾讯云的互信关系。安装该文件的方式取决于您的身份提供商。一些提供商为您提供了键入该 URL 的选项，此时，身份提供商将为您获取并安装该文件。另一些提供商则要求您从该 URL 处下载该文件，然后将其作为本地文件提供。请参阅您的 IdP 文档以获得指示，或参阅以下文档。

- [Azure Active Directory 单点登录腾讯云指南](https://cloud.tencent.com/document/product/598/35713)
- [OneLogin 单点登录腾讯云指南](https://cloud.tencent.com/document/product/598/35817)
- [Okta 单点登录腾讯云指南](https://cloud.tencent.com/document/product/598/37658)
- [ADFS 单点登录腾讯云指南](https://cloud.tencent.com/document/product/598/42702)

### SAML 响应示例

SAML 示例如下：

```
<samlp:Response>
    <saml:Issuer>...</saml:Issuer>
    <ds:Signature>
            ...
    </ds:Signature>
    <samlp:Status>
        ...
    </samlp:Status>
    <saml:Assertion>
        <saml:Issuer>...</saml:Issuer>
        <saml:Subject>
            <saml:NameID>${NameID}</saml:NameID>
            <saml:SubjectConfirmation>
                ...
            </saml:SubjectConfirmation>
        </saml:Subject>
        <saml:Conditions>
            <saml:AudienceRestriction>
                <saml:Audience>${Audience}</saml:Audience>
            </saml:AudienceRestriction>
        </saml:Conditions>
        <saml:AuthnStatement>
            ...
        </saml:AuthnStatement>
        <saml:AttributeStatement>
            <saml:Attribute Name="https://cloud.tencent.com/SAML/Attributes/RoleSessionName">
                ...
            </saml:Attribute>
            <saml:Attribute Name="https://cloud.tencent.com/SAML/Attributes/Role">
                ...
            </saml:Attribute>
        </saml:AttributeStatement>
    </saml:Assertion>
</samlp:Response>
```

在 SAML 断言的  AttributeStatement 元素中，必须包含以下腾讯云要求的 Attribute 元素：

1.  Name 属性值为 https://cloud.tencent.com/SAML/Attributes/Role 的 Attribute 元素，该元素为必选，可以有多个。其包含的 AttributeValue 元素取值代表允许当前用户扮演的角色，取值的格式是由角色描述与身份提供商描述组合而成的，中间用英文逗号（,）隔开。

  > ? 如果是多个，当使用控制台登录时，将会在界面上列出所有角色供用户选择。
  >
  > 以下是一个 Role Attribute 元素示例：

```
<Attribute Name="https://cloud.tencent.com/SAML/Attributes/Role">      
  <AttributeValue>qcs::cam::uin/{AccountID}:roleName/{RoleName1},qcs::cam::uin/{AccountID}:saml-provider/{ProviderName1}</AttributeValue>
  <AttributeValue>qcs::cam::uin/{AccountID}:roleName/{RoleName2},qcs::cam::uin/{AccountID}:saml-provider/{ProviderName2}</AttributeValue>
</Attribute>               
```

如果是同一个身份提供商，也可以合并为一条，不同角色 ARN 之间使用英文分号（;） 隔开。

```
<Attribute Name="https://cloud.tencent.com/SAML/Attributes/Role">       
<AttributeValue>qcs::cam::uin/{AccountID}:roleName/{RoleName1};qcs::cam::uin/{AccountID}:roleName/{RoleName2},qcs::cam::uin/{AccountID}:saml-provider/{ProviderName}</AttributeValue>
</Attribute>                            
```

> ? 在 Role 源属性中 {AccountID}，{RoleName} ，{ProviderName} 分别替换内容下：

 - {AccountID} 替换为您的腾讯云主帐户 ID，可前往 [账号信息 - 控制台](https://console.cloud.tencent.com/developer) 查看。
 - {RoleName}替换您在腾讯云为身份提供商所创建的角色名称（单击查看如何在腾讯云 [为身份提供商创建的角色](https://cloud.tencent.com/document/product/598/19381#.E9.80.9A.E8.BF.87.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.88.9B.E5.BB.BA)），角色名称可前往 [角色 - 控制台](https://console.cloud.tencent.com/cam/role) 查看。
 - {ProviderName} 替换您在腾讯云创建的 SAML 身份提供商名称，可前往 [身份提供商 - 控制台](https://console.cloud.tencent.com/cam/idp) 查看。 

2. Name 属性值为 https://cloud.tencent.com/SAML/Attributes/RoleSessionName 的 Attribute 元素，该元素为必选且只能有一个。该字段由用户自定义，长度不超过32个字符。以下是一个 RoleSessionName Attribute 元素示例。该示例中，“userName”可替换成您的自定义信息。

```
<Attribute Name="https://cloud.tencent.com/SAML/Attributes/RoleSessionName">
<AttributeValue>userName</AttributeValue>
</Attribute>                   
```
