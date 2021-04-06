本文为您介绍对于 API SecretKey 进行白盒密钥加解密的操作示例，详情步骤如下：

## 密钥的管理和分发
### 步骤1：创建白盒密钥
>!
>- 白盒密钥为收费项，详情请参见 [计费概述](https://cloud.tencent.com/document/product/573/34388#.E7.99.BD.E7.9B.92.E5.AF.86.E9.92.A5) 和 [购买方式](https://cloud.tencent.com/document/product/573/18809#.E8.B4.AD.E4.B9.B0.E7.99.BD.E7.9B.92.E5.AF.86.E9.92.A5)。
>- 创建白盒密钥对是通过调用白盒服务来实现的，支持控制台方式和 API 方式，本文示例采用控制台方式。
>
1. 登录 [密钥管理系统（合规）控制台](https://console.cloud.tencent.com/kms2/whitebox)，在左侧菜单栏选择【白盒密钥管理】>【用户密钥管理】页面，根据业务需求切换“地域” ，单击【新建】。
![](https://main.qcloudimg.com/raw/19359ddbc7123b64339f96c0160bc42f.png)
2. 在弹出的对话框，填写白盒密钥名称，选择加密算法，描述信息及标签（两者选填），单击【确定】，即可完成白盒密钥的创建。
![](https://main.qcloudimg.com/raw/500e3fb4b03e556d1e839c06ab08d8fb.png)

### 步骤2：控制台获取 API SecretKey
1. 使用主账号登录 [API 密钥管理控制台](https://console.cloud.tencent.com/cam/capi)，查看您的 API 密钥 。
2. 在密钥操作列中，单击【显示】，完成身份验证，获取并复制 SecretKey。
![](https://main.qcloudimg.com/raw/56cb5e8dccb266796937a5fe17eaa3e7.png)

### 步骤3：对 SecretKey 明文进行 base64 编码
将步骤2中获取的 SecretKey 内容进行 base64 编码。 例如，要加密的 SecretKey 明文是：lY9Ynrabcdj05YH1234LE370HOM，使用 openssl 命令生成 base64 编码后的结果为：`bFk5WW5yYWJjZGowNVlIMTIzNExFMzcwSE9NCg==`。
```
echo lY9Ynrabcdj05YH1234LE370HOM | openssl base64
```

### 步骤4：使用白盒密钥加密 API SecretKey
1. 登录 [密钥管理系统（合规）控制台](https://console.cloud.tencent.com/kms2/whitebox)，在白盒密钥列表，单击“白盒密钥ID/名称”或“操作”列的【加密】。
![](https://main.qcloudimg.com/raw/f7657edb34801f683ea8a29a6f4ac2f5.png)
2. 在弹出的对话框，将步骤3中获取的编码内容填充至明文（base64）文本框中，单击【白盒加密】。
![](https://main.qcloudimg.com/raw/ca314494fae1a17e0da7fe66ed9ee635.png)
3. 加密成功之后，会返回随机生成的初始化向量（简称 IV） 和加密后的密文，单击【下载IV】和【下载密文】 ，即可完成内容的下载。
>?其中初始化向量（简称 IV） 和加密后的密文均已进行 base64 编码。
>
![](https://main.qcloudimg.com/raw/5ef7869f287d91ad3368694d600c5987.png)

### 步骤5：下载解密密钥
1. 登录 [密钥管理系统（合规）控制台](https://console.cloud.tencent.com/kms2/whitebox)，在白盒密钥列表，单击“白盒密钥ID/名称”，进入密钥基本信息页面。
2. 在密钥基本信息页面，单击【下载解密密钥】，并命名为 decrypt_key_sm4.bin。
![](https://main.qcloudimg.com/raw/b8a61818f72e65dbd97eaa9bf7357ac1.png)

### 步骤6：下载解密 SDK 文件
1. 登录 [密钥管理系统（合规）控制台](https://console.cloud.tencent.com/kms2/whitebox)，在白盒密钥列表，单击右侧的【下载解密SDK文件】。
![](https://main.qcloudimg.com/raw/876b4187e5e4b0eee350c0be463356c1.png)
2. 在弹出的对话框，根据各业务系统自身的编程语言，选择下载相应编程语言的解密 SDK，并将 SDK 集成到业务系统中。
![](https://main.qcloudimg.com/raw/1e4b73df39bb47b893669d8157b48d04.png)

### 步骤7：白盒解密密钥和 API SecretKey 密文分发
管理员将上述步骤中下载的解密密钥、IV 和密文三个文件，分发给各业务系统的开发或运维人员。其中，解密密钥部署到相应业务系统的文件中，而初始化向量 IV 和密文会作为 SDK 的传参。
>! 下载的解密密钥是一个二进制 bin 文件，需要将该文件和可执行文件（已经集成了解密 SDK）放在相同的服务器上，文件路径将作为 SDK 的解密参数。
例如：[代码示例](https://cloud.tencent.com/document/product/573/54237) 中指定目录为 ./data，表示放在和可执行文件相同父目录的 data 子目录中。

## 业务集成 
### 使用 API SecretKey 密文
- 在业务逻辑中调用 SDK 的解密函数（whitebox_decrypt），传入参数：decrypt_key_bin_dir（步骤7中解密密钥存放的目录）、decrypt_key_sm4.bin（步骤5中下载的解密密钥，其对应的文件名）、InitializationVector（步骤4中下载的 IV）、CipherText（步骤4中用白盒加密后的 SecretKey 密文）和 algorithmType，从而获得解密后的明文
- 其中 algorithmType 是生成密钥时使用的算法类型，取值为0或1。0表示 AES_256，1表示 SM4。
- 关于白盒密钥如何进行解密，请参考 [白盒密钥解密代码示例](https://cloud.tencent.com/document/product/573/54237) ，各语言 SDK 均有详细的代码示例。

