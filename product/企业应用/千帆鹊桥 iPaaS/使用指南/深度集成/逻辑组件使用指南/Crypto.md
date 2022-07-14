## 简介
Crypto 连接器提供常用的对称、非对称和 PGP 加解密功能。

## 操作说明

### 连接器配置说明
#### 步骤1：创建连接器
单击**“+”**弹出组件筛选框，选择“Crypto”组件。根据业务场景选择不同的操作类型。
![](https://qcloudimg.tencent-cloud.cn/raw/31011685438db8b96f8baa5d1811a40e.png)

#### 步骤2：新建连接配置
1. 单击**新建**，创建 Crypto 连接器配置。
![](https://qcloudimg.tencent-cloud.cn/raw/70794c40b347d2b5e89d2a567b8a82a6.png)
2. 设置配置名称，用户自定义即可，并单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/2e9ff8d01976b6fc12c68c4612aad413.png)
3. 配置加密方式及密钥配置。
![](https://qcloudimg.tencent-cloud.cn/raw/81bb0927f0cac3c3709de39678164010.png)

| 参数     | 数据类型 | 描述                            | **是否必填** | **默认值** |
| :------- | -------- | ------------------------------- | ------------ | ---------- |
| 加密方式 | enum     | 对称加密、非对称加密、PGP 混合加密 | 是           |   -         |

不同加密方式对应的配置如下：
<dx-tabs>
::: 对称加密配置

| 参数         | 数据类型 | 描述                           | **是否必填** | **默认值** |
| :----------- | -------- | ------------------------------ | ------------ | ---------- |
| 密钥填充模式 | eunm     | PBKDF2、NO_PADDING、ZERO_PADDING | 是           | PBKDF2     |


**PBKDF2 模式**


| 参数           | 数据类型 | 描述                                 | **是否必填** | **默认值** |
| :------------- | -------- | ------------------------------------ | ------------ | ---------- |
| PBKDF2 哈希算法 | eunm     | MD5、SHA1、SHA224、SHA256、SHA384、SHA512 | 是           | SHA256     |
| PBKDF2 盐值     | string   | PBKDF2 盐值                           | 是           |    -        |
| PBKDF2 迭代次数 | int      | PBKDF2 迭代次数                       | 是           | 0          |
| 口令           | string   | 密码                                 | 是           |        -    |


**NO_PADDING 或 ZERO_PADDING 模式**


| 参数 | 数据类型 | 描述     | **是否必填** | **默认值** |
| :--- | -------- | -------- | ------------ | ---------- |
| 密钥 | string   | 加密密钥 | 是           |    -        |


[](id:1)

>!密钥长度限制与**组件配置-通用**中选择的加密算法有关，AES/16字节，DES/8字节，3DES/24字节。

:::
::: PGP 加密配置
| 参数        | 数据类型 | 描述             | **是否必填** | **默认值** |
| :---------- | -------- | ---------------- | ------------ | ---------- |
| PGP 私钥证书 | string   | PGP 私钥文件      | 是           |       -     |
| PGP 公钥证书 | string   | PGP 公钥证书      | 是           | -           |
| PGP 钥匙串   | map      | 指纹和密码对信息 | 是           |    -        |
:::
::: 非对称加密配置
| 参数     | 数据类型 | 描述     | **是否必填** | **默认值** |
| :------- | -------- | -------- | ------------ | ---------- |
| 私钥证书 | string   | 私钥文件 | 是           |      -      |
| 公钥证书 | string   | 公钥证书 | 是           |       -     |
:::
</dx-tabs>





### 组件配置说明
Crypto 组件目前支持对称加密、对称解密、非对称加密、非对称解密、PGP 加密、PGP 解密、PGP 签名、PGP 验签等操作，连接器配置新建完毕后进行组件的通用配置。

<dx-tabs>
::: 对称加密
#### 参数配置

| 参数         | 数据类型 | 描述                                                | **是否必填** | **默认值**    |
| :----------- | -------- | --------------------------------------------------- | ------------ | ------------- |
| 加密算法     | enum     | AES、DES、3DES                                        | 是           | AES           |
| 加密模式     | enum     | CBC、ECB                                             | 是           | CBC           |
| 随机向量    | string    | CBC加密模式必填，长度跟密钥长度一致         | CBC加密模式必填          | -        |
| 明文         | entity   | 待加密内容                                          | 是           |      -         |
| 内容填充模式 | enum     | PKCS5_PADDING、ZERO_PADDING、PKCS7_PADDING、NO_PADDING | 是           | PKCS5_PADDING |

**CBC 加密模式**
选择 CBC 加密模式时，随机向量必填，长度跟 [密钥长度](#1) 一致，再填写明文和填充模式即可。
![](https://qcloudimg.tencent-cloud.cn/raw/79d632a96d9f33ee1e07aa2dc4db8c98.png)
**ECB 加密模式**
当选择 ECB 加密模式时，只需填写明文和填充模式，无其他配置项。
![](https://qcloudimg.tencent-cloud.cn/raw/05b1bb3365935092ca11541555f7b74c.png)
####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回加密后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 对称加密案例
1. 添加 Crypto 连接器组件，选择对称加密操作。
![](https://qcloudimg.tencent-cloud.cn/raw/710bd6bd2831384d2533f357cc4d6979.png)
2. 在配置中，填写相关参数。例如：待加密内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes('test', mime_type='text/plain', encoding='utf-8')
```
 配置界面如下：
![](https://qcloudimg.tencent-cloud.cn/raw/1bbc9f8f724c06c99b3d7bc13619f832.png)
3. 执行成功后，message payload 中包含了加密后的二进制内容：
![image-20210521114703633](https://main.qcloudimg.com/raw/84a3272f1c8e9b00ac70278e04038bf3.jpg)

:::
::: 对称解密
#### 参数配置

| 参数         | 数据类型 | 描述                                                | **是否必填** | **默认值**    |
| :----------- | -------- | --------------------------------------------------- | ------------ | ------------- |
| 加密算法     | enum     | AES、DES、3DES                                        | 是           | AES           |
| 加密模式     | enum     | CBC、ECB                                             | 是           | CBC           |
| 随机向量    | string    | CBC加密模式必填，长度跟密钥长度一致         | CBC加密模式必填          | -        |
| 明文         | entity   | 待解密内容                                          | 是           |      -         |
| 内容填充模式 | enum     | PKCS5_PADDING、ZERO_PADDING、PKCS7_PADDING、NO_PADDING | 是           | PKCS5_PADDING |

**CBC 加密模式**
选择 CBC 加密模式时，随机向量必填，长度跟 [密钥长度](#1) 一致，再填写明文和填充模式即可。
![](https://qcloudimg.tencent-cloud.cn/raw/79d632a96d9f33ee1e07aa2dc4db8c98.png)
**ECB 加密模式**
当选择 ECB 加密模式时，只需填写明文和填充模式，无其他配置项。
![](https://qcloudimg.tencent-cloud.cn/raw/05b1bb3365935092ca11541555f7b74c.png)
####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回解密后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 对称解密案例
1. 添加 Crypto 连接器组件，选择对称解密操作。
![](https://qcloudimg.tencent-cloud.cn/raw/5b7aadec604e7dd019fbf779ad1d4cf5.png)
2. 在配置中，填写相关参数。例如：待解密内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes(msg.payload, mime_type='text/plain', encoding='utf-8')
```
 配置界面如下：
![image-20210521115044004](https://main.qcloudimg.com/raw/1dfd01e8fba28bdaf51f37be8ef19dca/pbe_encrypt.png)
3. 执行成功后，message payload 中包含了解密后的二进制内容：
![image-20210521114703633](https://main.qcloudimg.com/raw/a8c57a08eb3cdb79a7a3e05a21bd685e.jpg)
:::
::: 非对称加密
#### 参数配置

| 参数         | 数据类型 | 描述                                     | **是否必填** | **默认值**        |
| :----------- | -------- | ---------------------------------------- | ------------ | ----------------- |
| 加密算法     | enum     | RSA                                      | 是           | RSA               |
| 明文        | entity   | 待加密内容                               | 是           |     -              |
| 填充模式 | enum     | RSA_PKCS1_PADDING、RSA_PKCS1_OAEP_PADDING | 是           | RSA_PKCS1_PADDING |

**RSA_PKCS1_OAEP_PADDING 模式**
内容填充模式选择“RSA_PKCS1_OAEP_PADDING”时，配置如下:

| 参数         | 数据类型 | 描述                                 | **是否必填** | **默认值** |
| :----------- | -------- | ------------------------------------ | ------------ | ---------- |
| OAEP 哈希算法 | eunm     | MD5/SHA1、SHA224、SHA256、SHA384、SHA512 | 是           | SHA256     |

![](https://qcloudimg.tencent-cloud.cn/raw/03c01f26db98706d21ff20174f941236.png)


**RSA_PKCS1_PADDING 模式**
内容填充模式选择“RSA_PKCS1_PADDING”时，无其他配置。
![](https://qcloudimg.tencent-cloud.cn/raw/fbb86919cad6c088ffd6468f1ce43746.png)
####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回加密后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 非对称加密案例
1. 添加 Crypto 连接器组件，选择非对称加密操作。
![](https://qcloudimg.tencent-cloud.cn/raw/017e57cef1eff2c9d6b4a3e054b6f976.png)
2. 在配置中，填写相关参数。例如：待加密内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes('test', mime_type='text/plain', encoding='utf-8')
```
 配置界面如下：
![](https://qcloudimg.tencent-cloud.cn/raw/fbb86919cad6c088ffd6468f1ce43746.png)
3. 执行成功后，message payload 中包含了加密后的二进制内容：
![image-20210521114703633](https://main.qcloudimg.com/raw/7bff19c3c65e48807485e387055b70c6.jpg)
:::
::: 非对称解密
#### 参数配置

| 参数         | 数据类型 | 描述                                     | **是否必填** | **默认值**        |
| :----------- | -------- | ---------------------------------------- | ------------ | ----------------- |
| 加密算法     | enum     | RSA                                      | 是           | RSA               |
| 明文         | entity   | 待解密内容                               | 是           |        -           |
| 填充模式 | enum     | RSA_PKCS1_PADDING、RSA_PKCS1_OAEP_PADDING | 是           | RSA_PKCS1_PADDING |


**RSA_PKCS1_OAEP_PADDING 模式**

| 参数         | 数据类型 | 描述                                 | **是否必填** | **默认值** |
| :----------- | -------- | ------------------------------------ | ------------ | ---------- |
| OAEP 哈希算法 | eunm     | MD5/SHA1、SHA224、SHA256、SHA384、SHA512 | 是           | SHA256     |

![](https://qcloudimg.tencent-cloud.cn/raw/87767f6108cc64f88d7d5b2b68d27560.png)

**RSA_PKCS1_PADDING 模式**
内容填充模式选择“RSA_PKCS1_PADDING”时, 无其他配置。
![](https://qcloudimg.tencent-cloud.cn/raw/28c6bfaf11dd05f7c84562cd9f03944f.png)

####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回解密后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 非对称解密案例
1. 添加 Crypto 连接器组件，选择非对称解密操作。
![](https://qcloudimg.tencent-cloud.cn/raw/017e57cef1eff2c9d6b4a3e054b6f976.png)
2. 在配置中，填写相关参数。例如：待解密内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes(msg.payload, mime_type='text/plain', encoding='utf-8')
```
  配置界面如下：
![](https://qcloudimg.tencent-cloud.cn/raw/28c6bfaf11dd05f7c84562cd9f03944f.png)
3. 执行成功后，message payload中包含了解密后的二进制内容：
![image-20210521114703633](https://main.qcloudimg.com/raw/5370e7abc9908663b7b531fdb5fa1813.jpg)
:::
::: PGP 加密
#### 参数配置

| 参数     | 数据类型 | 描述                               | **是否必填** | **默认值** |
| :------- | -------- | ---------------------------------- | ------------ | ---------- |
| 钥匙串 ID | string   | 钥匙串 ID                           | 是           |      -      |
| 加密算法 | enum     | CAST5、3DES、AES_128、AES_192、AES_256 | 是           | AES_128    |
| 内容     | entity   | 待加密内容                         | 是           |  -          |

![image-20210521114703633](https://main.qcloudimg.com/raw/e7e15db73a35a435ee2825d9b7117b5c.jpg)

####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回加密后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### PGP 加密案例
1. 添加 Crypto 连接器组件，选择 PGP 加密操作。
![对称加密选择](https://main.qcloudimg.com/raw/7dd0fa4440e359e94a07218afac26008/pgp_select.png)
2. 在配置中，填写相关参数。例如：待加密内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes("123456", mime_type='text/plain', encoding='utf-8')
```
 - 配置界面如下：
![image-20210521115044004](https://main.qcloudimg.com/raw/e7e15db73a35a435ee2825d9b7117b5c.jpg)
3. 执行成功后，message payload 中包含了加密后的二进制内容：
![image-20210521114703633](https://main.qcloudimg.com/raw/fd828fd05a080ee8ddbb6697b1a36e2d.jpg)
:::
::: PGP 解密
#### 参数配置

| 参数     | 数据类型 | 描述       | **是否必填** | **默认值** |
| :------- | -------- | ---------- | ------------ | ---------- |
| 钥匙串 ID | string   | 钥匙串 ID   | 是           |        -    |
| 内容     | entity   | 待解密内容 | 是           |    -        |

![image-20210521114703633](https://main.qcloudimg.com/raw/a272412c84b01751b87624c0cbc65bbb.jpg)

####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回解密后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### PGP 解密案例
1. 添加 Crypto 连接器组件，选择 PGP 解密操作。
![对称加密选择](https://main.qcloudimg.com/raw/7dd0fa4440e359e94a07218afac26008/pgp_select.png)
2. 在配置中，填写相关参数。例如：待解密内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes(msg.payload, mime_type='text/plain', encoding='utf-8')
```
 配置界面如下：
![image-20210521115044004](https://main.qcloudimg.com/raw/a272412c84b01751b87624c0cbc65bbb.jpg)
3. 执行成功后，message payload 中包含了加密后的二进制内容：
![image-20210521114703633](https://main.qcloudimg.com/raw/806709d291ccdb97c121bd0ce8f72d43.jpg)

:::
::: PGP 签名
#### 参数配置

| 参数     | 数据类型 | 描述                                 | **是否必填** | **默认值** |
| :------- | -------- | ------------------------------------ | ------------ | ---------- |
| 钥匙串 ID | string   | 钥匙串 ID                             | 是           | -           |
| 签名算法 | enum     | MD5、SHA1、SHA224、SHA256、SHA384、SHA512 | 是           | AES_256    |
| 内容     | entity   | 待签名内容                           | 是           |     -       |

![image-20210521114703633](https://main.qcloudimg.com/raw/689be566e2f79ca02a80cd21aadbbb2a.jpg)

####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回签名后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### PGP 签名案例
1. 添加 Crypto 连接器组件，选择 PGP 签名操作。
![对称加密选择](https://main.qcloudimg.com/raw/7dd0fa4440e359e94a07218afac26008/pgp_select.png)
2. 在配置中，填写相关参数。例如：待签名内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes("123456", mime_type='text/plain', encoding='utf-8')
```
 配置界面如下：
   ![image-20210521115044004](https://main.qcloudimg.com/raw/689be566e2f79ca02a80cd21aadbbb2a.jpg)
3. 执行成功后，message payload 中包含了签名后的二进制内容：
![image-20210521114703633](https://main.qcloudimg.com/raw/b50f5833bf610d5ce2b89851db99cb95.jpg)
:::
::: PGP 验签
#### 参数配置

| 参数     | 数据类型 | 描述       | **是否必填** | **默认值** |
| :------- | -------- | ---------- | ------------ | ---------- |
| 钥匙串 ID | string   | 钥匙串 ID   | 是           |        -    |
| 目标内容 | entity   | 待比较内容 | 是           |       -     |
| 期望内容 | entity   | 签名内容   | 是           |   -         |

![image-20210521114703633](https://main.qcloudimg.com/raw/cb21182d7576364a36081937bf78a89c.jpg)

####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回验证签名后的结果；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### PGP 验签案例
1. 添加 Crypto 连接器组件，选择 PGP 验签操作。
![对称加密选择](https://main.qcloudimg.com/raw/7dd0fa4440e359e94a07218afac26008/pgp_select.png)
2. 在配置中，填写相关参数。例如：期望内容、目标内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes(msg.payload, mime_type='text/plain', encoding='utf-8')
 def dw_process(msg):
       return Entity.from_bytes("123456", mime_type='text/plain', encoding='utf-8')
```
 配置界面如下：
   ![image-20210521115044004](https://main.qcloudimg.com/raw/cb21182d7576364a36081937bf78a89c.jpg)
3. 执行成功后，message payload 中包含验证签名是否正确的结果：
![image-20210521114703633](https://main.qcloudimg.com/raw/2b2ceddf22f289d5a4831402a5459478.jpg)

:::
</dx-tabs>

### 配置“对称加解密”案列
1. 下载 [对称加解密 Demo](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/demo/%E5%AF%B9%E7%A7%B0%E5%8A%A0%E8%A7%A3%E5%AF%86demo.ipaas)。
2. 将 Demo [导入应用](https://cloud.tencent.com/document/product/1270/62261#.E5.AF.BC.E5.85.A5.E5.92.8C.E5.AF.BC.E5.87.BA.E5.BA.94.E7.94.A8) 后，进行调试或发布测试。



