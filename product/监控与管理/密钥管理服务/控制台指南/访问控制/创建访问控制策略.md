## 可授权的资源类型
资源级权限是能够指定用户对哪些资源具有执行操作的能力。密钥管理系统部分接口支持使用资源级权限对密钥进行操作，可控制允许用户何时执行操作或是否允许用户使用特定资源。密钥管理系统目前可授权的资源类型如下：

| 资源类型 | 授权策略中资源描述方法 |
|---------|---------|
| 所有的密钥资源 | `qcs::kms:$region:uin/$uin:key/*` | 
|账号 $creatorUin 创建的所有密钥资源|`qcs::kms:$region:uin/$uin:key/creatorUin/$creatorUin/*`|
|账号 $creatorUin 创建的 ID 为 $keyId 的密钥资源|`qcs::kms:$region:uin/$uin:key/creatorUin/$creatorUin/$keyId`|

其中以$为前缀的单词均为代称：
- $uin 指代主账号 ID。
- $region 指代地域。
- $creatorUin 指代创建该资源的账号 ID。
- $keyId 指代密钥 ID。

## 支持资源级授权的 API 列表
密钥管理系统部分接口支持资源级授权，您可以指定子账号拥有特定资源的接口权限。

| API 接口 | 描述信息 | 
|---------|---------|
|DescribeWhiteBoxKeyDetails  |获取白盒密钥列表|
|EnableWhiteBoxKeys |批量启用白盒密钥|
|DeleteWhiteBoxKey | 删除白盒密钥|
|DescribeWhiteBoxKey| 展示白盒密钥的信息|
|EnableWhiteBoxKey| 启用白盒密钥|
|EncryptByWhiteBox |使用白盒密钥进行加密|
|DescribeWhiteBoxDecryptKey| 获取白盒解密密钥|
|DisableWhiteBoxKey|禁用白盒密钥|
|AsymmetricSm2Decrypt |非对称密钥 Sm2 解密|
|AsymmetricRsaDecrypt| 非对称密钥 RSA 解密|
|GetPublicKey |获取非对称密钥的公钥|
|EnableKey| 启动主密钥|
|DisableKey| 禁用主密钥|
|GetKeyRotationStatus| 查询密钥轮换状态|
|ReEncrypt |密文刷新|
|DisableWhiteBoxKeys |批量展示白盒密钥的信息|
|UpdateKeyDescription| 修改主密钥描述信息|
|UpdateAlias |	修改别名|
|DisableKeyRotation| 禁止密钥轮换|
|EnableKeyRotation |开启密钥轮换|
|EnableKeys| 批量启动主密钥|
|DisableKeys| 批量禁用主密钥|
|DescribeKey |获取主密钥属性|
|DescribeKeys |获取多个主密钥属性|
|CancelKeyDeletion| 取消 CMK 计划删除操作|
|ScheduleKeyDeletion |	CMK 计划删除接口|
|DeleteImportedKeyMaterial |删除导入的密钥材料|
|ImportKeyMaterial |导入密钥材料|
|GetParametersForImport |获取导入主密钥（CMK）材料的参数|
|GenerateDataKey |生成数据密钥|
|Decrypt |解密|
|Encrypt |加密|

## 创建策略

1. 登录 [访问管理](https://console.cloud.tencent.com/cam/overview) 控制台。
2. 在左侧菜单中，选择**策略** > **新建自定义策略** > **按策略语法创建**，进入策略创建页面。
3. 选择策略模板，例如空白模板或 KMS 策略模板，单击**下一步**。
4. 输入策略名称和策略内容，策略内容可参见下方示例。
<img src="https://main.qcloudimg.com/raw/1a9757deed55dc37144485ba7f83822c.jpg" width="80%">
5. 单击**创建策略**，即可创建。





