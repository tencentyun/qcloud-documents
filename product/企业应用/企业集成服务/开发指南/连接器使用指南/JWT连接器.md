## 简介

JWT（Json Web Toke）是一种用于在网络应用环境间传递声明而执行的一种基于 JSON 的开放标准（[RFC 7519](https://link.jianshu.com/?t=https://tools.ietf.org/html/rfc7519)）。JWT 被设计为紧凑且安全的，适用于分布式站点的单点登录（SSO）场景。Json Web Toke 的声明一般被用来在身份提供者和服务提供者间传递被认证的用户身份信息，以便于从资源服务器获取资源，也可用于增加一些额外的其它业务逻辑所必须的声明信息，Json Web Toke 也可直接被用于认证，也可被加密。

JWT 连接器提供生成 Json Web Token 以及校验 Json Web Toke 的相关功能。

## 配置

配置参数：

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| :------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 签名方法 | enum     | NONE/HMAC-SHA-256/HMAC-SHA-384/HMAC-SHA-512/RSA-SHA-256/RSA-SHA-384/RSA-SHA-512/RSAPSS-SHA-256/RSAPSS-SHA-384/RSAPSS-SHA-512 | 是           | NONE       |

选择“NONE”时，无配置参数，如下图：

![配置](https://qcloudimg.tencent-cloud.cn/raw/056d9f8028c14685a234c1b634efc671.png)

选择“HMAC-SHA-256/HMAC-SHA-384/HMAC-SHA-512”时，配置参数如下：

| 参数     | 数据类型 | 描述     | **是否必填** |
| :------- | -------- | -------- | ------------ |
| HMAC 密钥 | string   | HMAC密钥 | 是           |   

![配置](https://qcloudimg.tencent-cloud.cn/raw/bb4feee9a3477b366fca1efb0fa681a5.png)

选择”RSA-SHA-256/RSA-SHA-384/RSA-SHA-512/RSAPSS-SHA-256/RSAPSS-SHA-384/RSAPSS-SHA-512“时，配置参数如下：

| 参数         | 数据类型 | 描述            | **是否必填** | 
| :----------- | -------- | --------------- | ------------ | 
| 私钥证书文件 | string   | RSA 私钥证书文件 | 是           |  
| 公钥证书文件 | string   | RSA 公钥证书文件 | 是           |   



![配置](https://qcloudimg.tencent-cloud.cn/raw/aa1a1396e17612b459cc2691ee812db8.png)

## 操作说明

JWT 组件目前支持生成  JWT 和校验 JWT 操作。

### 生成 Json Web Toke

#### 参数配置

| 参数                | 数据类型 | 描述                                                 | **是否必填** | **默认值** |
| :------------------ | -------- | ---------------------------------------------------- | ------------ | ---------- |
| 签发者（iss）         | string   | JWT 签发者                                            | 否           |            |
| 主题（sub）           | string   | JWT 主题                                              | 否           |            |
| 唯一身份标识 ID（jti） | string   | JWT 的唯一身份标识 ID                                  | 否           |            |
| 接收者列表（aud）    | []string | 接收 JWT 的对象列表                                    | 否           |            |
| 签发时间（iat）       | datetime | JWT 的签发时间                                        | 否           |            |
| 有效起始时间（nbf）   | datetime | JWT 的有效起始时间，定义在该时间之前，JWT 都是不可用的 | 否           |            |
| 有效时间（exp）  | int      | 有效起始时间加上有效时间为 JWT 的过期时间，单位：秒              | 否           | 3600       |


![pbkdf2配置](https://qcloudimg.tencent-cloud.cn/raw/3b6dd3f15f35f0632aaf3e674f27b449.png)

#### 输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | <li>执行成功后，payload 为 binary 类型，返回生成的 JWT 内容。</li><li>执行失败后，payload 为空。</li> |
| error       |  <li>执行成功后，error 为空。</li><li>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。</li> |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 继承上个组件的 variable 信息。                                   |


#### 案例

1. 添加 JWT 组件，选择生成 JsonWebToken 操作：
![对称加密选择](https://qcloudimg.tencent-cloud.cn/raw/169ae00329f8d0955499f516d6b2d2da.png)

2. 在连接器配置中，填写相关参数：
   ![image-20210521115044004](https://qcloudimg.tencent-cloud.cn/raw/9b055ac523a641e2a1c05c9a4d0f3a7f.png)

3. 在操作配置填写参数如下：
![image-20210521115044004](https://qcloudimg.tencent-cloud.cn/raw/714c7f6544667c66940ae01b0fea9e0d.png)

4. 执行成功后，message payload 中为 JsonWebToken 内容：
![image-20210521114703633](https://qcloudimg.tencent-cloud.cn/raw/eab57c1baf54a294f0009a90fa3d6ecc.png)

### 校验 JsonWebToken

#### 参数配置

| 参数            | 数据类型 | 描述                          | **是否必填** | 
| :-------------- | -------- | ----------------------------- | ------------ | 
| Token           | string   | 生成的 Json Web Token          | 是           |   
| 接收者列表（aud） | []string | 用于校验接收 JWT 的对象是否匹配 | 否           |   

![pbkdf2配置](https://qcloudimg.tencent-cloud.cn/raw/788c97b744e01c1f02c0810ab5eb2084.png)

#### 输出

操作执行成功后，输出结果会保存在Message消息体的payload；执行失败后，错误信息会保存在 message 消息体的 error。

组件输出的 message 信息如下：

| message属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     |  <li>执行成功后，payload 为 binary 类型，返回校验解析 JWT 后的内容。</li><li>执行失败后，payload 为空。</li> |
| error       | <li>执行成功后，error 为空。</li><li>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。</li> |
| attribute   | 继承上个组件的 attribute 信息。                                 |
| variable    | 继承上个组件的 variable 信息。                                   |

#### 案例

1. 添加 JWT 组件，选择校验 JsonWebToken 操作
![对称加密选择](https://qcloudimg.tencent-cloud.cn/raw/169ae00329f8d0955499f516d6b2d2da.png)

2. 在连接器配置中，填写相关参数：
   ![image-20210521115044004](https://qcloudimg.tencent-cloud.cn/raw/9b055ac523a641e2a1c05c9a4d0f3a7f.png)

3. 在操作配置填写参数如下：
![image-20210521115044004](https://qcloudimg.tencent-cloud.cn/raw/3111a67d71ec0dfe38b706f38809888a.png)

4. 执行成功后，message payload 中为校验解析后的 JsonWebToken 内容：
![image-20210521114703633](https://qcloudimg.tencent-cloud.cn/raw/9a40c0e13540b3dbc9ed0d33ab707cbb.png)
