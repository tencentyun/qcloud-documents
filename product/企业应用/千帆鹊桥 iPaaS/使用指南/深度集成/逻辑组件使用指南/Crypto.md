## 简介
Crypto 连接器提供常用的对称、非对称和 PGP 加解密功能。

## 配置
### 配置参数

| 参数     | 数据类型 | 描述                            | **是否必填** | **默认值** |
| :------- | -------- | ------------------------------- | ------------ | ---------- |
| 加密方式 | enum     | 对称加密、非对称加密、PGP 混合加密 | 是           |   -         |

### 加密方式配置
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





## 操作说明
Crypto 组件目前支持对称加密、对称解密、非对称加密、非对称解密、PGP 加密、PGP 解密、PGP 签名、PGP 验签等操作。

<dx-tabs>
::: 对称加密
#### 参数配置

| 参数         | 数据类型 | 描述                                                | **是否必填** | **默认值**    |
| :----------- | -------- | --------------------------------------------------- | ------------ | ------------- |
| 加密算法     | enum     | AES、DES、3DES                                        | 是           | AES           |
| 加密模式     | enum     | CBC、ECB                                             | 是           | CBC           |
| 明文         | entity   | 待加密内容                                          | 是           |      -         |
| 内容填充模式 | enum     | PKCS5_PADDING、ZERO_PADDING、PKCS7_PADDING、NO_PADDING | 是           | PKCS5_PADDING |

![pbkdf2配置](https://main.qcloudimg.com/raw/1dfd01e8fba28bdaf51f37be8ef19dca/pbe_encrypt.png)

####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回加密后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Crypto 连接器组件，选择对称加密操作。
![对称加密选择](https://main.qcloudimg.com/raw/a0e241c751d2813b2c365b7edbf3325b/pbe_select.png)
2. 在配置中，填写相关参数。例如：待加密内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes('test', mime_type='text/plain', encoding='utf-8')
```
 - 配置界面如下：
![image-20210521115044004](https://main.qcloudimg.com/raw/1dfd01e8fba28bdaf51f37be8ef19dca/pbe_encrypt.png)
3. 执行成功后，message payload 中包含了加密后的二进制内容：
![image-20210521114703633](https://main.qcloudimg.com/raw/84a3272f1c8e9b00ac70278e04038bf3.jpg)

:::
::: 对称解密
#### 参数配置

| 参数         | 数据类型 | 描述                                                | **是否必填** | **默认值**    |
| :----------- | -------- | --------------------------------------------------- | ------------ | ------------- |
| 加密算法     | enum     | AES、DES、3DES                                        | 是           | AES           |
| 加密模式     | enum     | CBC、ECB                                             | 是           | CBC           |
| 明文         | entity   | 待解密内容                                          | 是           |      -         |
| 内容填充模式 | enum     | PKCS5_PADDING、ZERO_PADDING、PKCS7_PADDING、NO_PADDING | 是           | PKCS5_PADDING |

![pbkdf2配置](https://main.qcloudimg.com/raw/1dfd01e8fba28bdaf51f37be8ef19dca/pbe_encrypt.png)

####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回解密后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Crypto 连接器组件，选择对称解密操作。
![对称加密选择](https://main.qcloudimg.com/raw/a0e241c751d2813b2c365b7edbf3325b/pbe_select.png)
2. 在配置中，填写相关参数。例如：待解密内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes(msg.payload, mime_type='text/plain', encoding='utf-8')
```
 - 配置界面如下：
![image-20210521115044004](https://main.qcloudimg.com/raw/1dfd01e8fba28bdaf51f37be8ef19dca/pbe_encrypt.png)
3. 执行成功后，message payload 中包含了解密后的二进制内容：
![image-20210521114703633](https://main.qcloudimg.com/raw/a8c57a08eb3cdb79a7a3e05a21bd685e.jpg)
:::
::: 非对称加密
#### 参数配置

| 参数         | 数据类型 | 描述                                     | **是否必填** | **默认值**        |
| :----------- | -------- | ---------------------------------------- | ------------ | ----------------- |
| 加密算法     | enum     | RSA                                      | 是           | RSA               |
| 内容         | entity   | 待加密内容                               | 是           |     -              |
| 内容填充模式 | enum     | RSA_PKCS1_PADDING、RSA_PKCS1_OAEP_PADDING | 是           | RSA_PKCS1_PADDING |

**RSA_PKCS1_OAEP_PADDING 模式**
内容填充模式选择“RSA_PKCS1_OAEP_PADDING”时，配置如下:

| 参数         | 数据类型 | 描述                                 | **是否必填** | **默认值** |
| :----------- | -------- | ------------------------------------ | ------------ | ---------- |
| OAEP 哈希算法 | eunm     | MD5/SHA1、SHA224、SHA256、SHA384、SHA512 | 是           | SHA256     |

![image-20210521114703633](https://main.qcloudimg.com/raw/096d43d9e95d17c65a7cc03d91ca80d7.jpg)

**RSA_PKCS1_PADDING 模式**
内容填充模式选择“RSA_PKCS1_PADDING”时，无其他配置。

####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回加密后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Crypto 连接器组件，选择非对称加密操作。
![对称加密选择](https://main.qcloudimg.com/raw/85a5b6e21be4e7c907beb912e43e11a4/ae_select.png)
2. 在配置中，填写相关参数。例如：待加密内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes('test', mime_type='text/plain', encoding='utf-8')
```
 - 配置界面如下：
![image-20210521115044004](https://main.qcloudimg.com/raw/096d43d9e95d17c65a7cc03d91ca80d7.jpg)
3. 执行成功后，message payload 中包含了加密后的二进制内容：
![image-20210521114703633](https://main.qcloudimg.com/raw/7bff19c3c65e48807485e387055b70c6.jpg)
:::
::: 非对称解密
#### 参数配置

| 参数         | 数据类型 | 描述                                     | **是否必填** | **默认值**        |
| :----------- | -------- | ---------------------------------------- | ------------ | ----------------- |
| 加密算法     | enum     | RSA                                      | 是           | RSA               |
| 内容         | entity   | 待解密内容                               | 是           |        -           |
| 内容填充模式 | enum     | RSA_PKCS1_PADDING、RSA_PKCS1_OAEP_PADDING | 是           | RSA_PKCS1_PADDING |


**RSA_PKCS1_OAEP_PADDING 模式**

| 参数         | 数据类型 | 描述                                 | **是否必填** | **默认值** |
| :----------- | -------- | ------------------------------------ | ------------ | ---------- |
| OAEP 哈希算法 | eunm     | MD5/SHA1、SHA224、SHA256、SHA384、SHA512 | 是           | SHA256     |

![image-20210521114703633](https://main.qcloudimg.com/raw/096d43d9e95d17c65a7cc03d91ca80d7.jpg)

**RSA_PKCS1_PADDING 模式**
内容填充模式选择“RSA_PKCS1_PADDING”时, 无其他配置。


####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回解密后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Crypto 连接器组件，选择非对称解密操作。
![对称加密选择](https://main.qcloudimg.com/raw/85a5b6e21be4e7c907beb912e43e11a4/ae_select.png)
2. 在配置中，填写相关参数。例如：待解密内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes(msg.payload, mime_type='text/plain', encoding='utf-8')
```
 - 配置界面如下：
![image-20210521115044004](https://main.qcloudimg.com/raw/096d43d9e95d17c65a7cc03d91ca80d7.jpg)
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

#### 案例
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

#### 案例
1. 添加 Crypto 连接器组件，选择 PGP 解密操作。
![对称加密选择](https://main.qcloudimg.com/raw/7dd0fa4440e359e94a07218afac26008/pgp_select.png)
2. 在配置中，填写相关参数。例如：待解密内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes(msg.payload, mime_type='text/plain', encoding='utf-8')
```
 - 配置界面如下：
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

#### 案例
1. 添加 Crypto 连接器组件，选择 PGP 签名操作。
![对称加密选择](https://main.qcloudimg.com/raw/7dd0fa4440e359e94a07218afac26008/pgp_select.png)
2. 在配置中，填写相关参数。例如：待签名内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes("123456", mime_type='text/plain', encoding='utf-8')
```
 - 配置界面如下：
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

#### 案例
1. 添加 Crypto 连接器组件，选择 PGP 验签操作。
![对称加密选择](https://main.qcloudimg.com/raw/7dd0fa4440e359e94a07218afac26008/pgp_select.png)
2. 在配置中，填写相关参数。例如：期望内容、目标内容使用 Dataway 表达式输入：
```python
def dw_process(msg):
    return Entity.from_bytes(msg.payload, mime_type='text/plain', encoding='utf-8')
 def dw_process(msg):
       return Entity.from_bytes("123456", mime_type='text/plain', encoding='utf-8')
```
 - 配置界面如下：
   ![image-20210521115044004](https://main.qcloudimg.com/raw/cb21182d7576364a36081937bf78a89c.jpg)
3. 执行成功后，message payload 中包含验证签名是否正确的结果：
![image-20210521114703633](https://main.qcloudimg.com/raw/2b2ceddf22f289d5a4831402a5459478.jpg)

:::
</dx-tabs>



