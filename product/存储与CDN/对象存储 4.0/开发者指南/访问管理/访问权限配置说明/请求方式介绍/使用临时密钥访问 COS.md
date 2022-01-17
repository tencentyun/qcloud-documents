## 临时密钥简介

临时密钥是由 [安全凭证服务（Security Token Service,STS）](https://cloud.tencent.com/document/product/1312/48195) 提供的临时访问凭证。临时密钥由 TmpSecretId、TmpSecretKey 和 Token 三部分组成，相比于永久密钥，临时密钥具有以下特点：
-	有效时间短（30min - 36h），不必暴露永久密钥，降低账号泄露风险。
-	在获取临时密钥时，可通过传入 policy 参数设置临时权限来进一步约束使用者的权限范围。

因此，临时密钥适用于前端直传等临时授权场景，相比永久密钥，分发临时密钥给不受信任的用户，安全性更高。

## 获取临时密钥

获取临时密钥，可以通过我们提供的 COS STS SDK 方式获取，也可以直接通过 STS 云 API 的方式获取。
详情可参考 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)。

## 临时密钥的权限

申请临时密钥之前，您必须拥有访问管理（Cloud Access Management，CAM）用户（腾讯云主账号或子账号），可以通过设置 Policy 参数，为临时密钥增加临时策略约束使用者的权限。
- 若不设置 policy 参数，获取的临时密钥具有与 CAM 用户相同的权限。
- 若设置了 policy 参数，获取的临时密钥会在 CAM 用户权限的基础上，进一步将权限限制在 policy 设置的范围以内。

假设，“A”代表 CAM 用户的原有权限，“B”代表通过 policy 参数为临时密钥设置的权限，“A”和“B”的交集代表了临时密钥最终的有效权限。

如下图，CAM 用户权限和 policy 临时权限的交集为有效权限：
![](https://qcloudimg.tencent-cloud.cn/raw/572574445d9af1b01e3bd33cb82d830a.png)

如下图，policy 在 CAM 用户权限以内，policy 为有效权限：
![](https://qcloudimg.tencent-cloud.cn/raw/ebc98a1e309ec5d9ce4420284ca52c6d.png)

## 使用临时密钥访问 COS

![](https://qcloudimg.tencent-cloud.cn/raw/36aca86fa63cb782214eb58789a9c82c.png)
临时密钥包括 SecretId、SecretKey 和 Token，每个主账号和子账号都可以生成多个临时密钥。相比永久密钥，临时密钥的有效期只有30分钟 - 36小时。临时密钥适用于前端直传等临时授权场景，相比永久密钥，分发临时密钥给不受信任的用户，安全性更高，详情参考 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048) 及 [用于前端直传的临时密钥使用指引](https://cloud.tencent.com/document/product/436/40265)。

- 发起 API 请求
类似永久密钥，您也可以通过临时密钥生成签名，填入请求头部 Authorization，形成签名请求。COS 接收到请求后，会校验签名是否有效，以及临时密钥是否过期。
签名算法的介绍请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778)，COS 同时提供了 [签名生成工具](https://cos5.cloud.tencent.com/static/cos-sign/)，也可以通过 SDK 生成签名，可参考 [SDK 签名实现](https://cloud.tencent.com/document/product/436/7778#sdk-.E7.AD.BE.E5.90.8D.E5.AE.9E.E7.8E.B0)。
- 使用 SDK 工具
安装 SDK 工具后，除了使用临时密钥初始化用户身份信息，您也可以使用临时密钥（SecretId、SecretKey、Token）初始化 COSClient，直接使用SDK进行上传、下载等操作，而无需生成签名。临时密钥生成可参考临时密钥生成及使用指引。

Java SDK 参考示例如下，更多语言 demo 可参考 [SDK 概览](https://cloud.tencent.com/document/product/436/6474)。

```
// 1 传入获取到的临时密钥 (tmpSecretId, tmpSecretKey, sessionToken)
String tmpSecretId = "SECRETID";
String tmpSecretKey = "SECRETKEY";
String sessionToken = "TOKEN";
BasicSessionCredentials cred = new BasicSessionCredentials(tmpSecretId, tmpSecretKey, sessionToken);
// 2 设置 bucket 的地域, COS 地域的简称请参阅 https://cloud.tencent.com/document/product/436/6224
// clientConfig 中包含了设置 region, https(默认 http), 超时, 代理等 set 方法, 使用可参阅源码或者常见问题 Java SDK 部分
Region region = new Region("COS_REGION");
ClientConfig clientConfig = new ClientConfig(region);
// 3 生成 cos 客户端
COSClient cosClient = new COSClient(cred, clientConfig);
```

## 临时密钥的使用场景

临时密钥主要用于授权第三方临时访问 COS。例如，用户开发了客户端 App，将数据存储在 COS 存储桶上，此时将永久密钥直接存放在 App 客户端上是不安全的，但又需要授予客户端上传、下载的权限，针对这种场景可使用临时密钥。
![](https://qcloudimg.tencent-cloud.cn/raw/e15d7339e894311f4e3003735cde9eff.png)

如上图所示，用户开发了 App 客户端，用户服务器上存放有永久密钥，使用临时密钥进行前端直传需要经过以下几步：
1.	App 客户端向用户服务器请求临时密钥，用于上传、下载数据。
2.	用户服务器使用永久密钥身份，向 STS 服务器申请临时密钥。
3.	STS 服务返回临时密钥给用户服务器。
4.	用户服务器将临时密钥下发到 App 客户端。
5.	App 客户端使用临时密钥生成签名请求，向 COS 请求上传、下载数据。

临时密钥适用于前端数据直传的使用场景，您可以参考以下最佳实践使用临时密钥：
- [Web 端直传实践](https://cloud.tencent.com/document/product/436/9067)
- [小程序直传实践](https://cloud.tencent.com/document/product/436/34929)
- [移动应用直传实践](https://cloud.tencent.com/document/product/436/9068)

