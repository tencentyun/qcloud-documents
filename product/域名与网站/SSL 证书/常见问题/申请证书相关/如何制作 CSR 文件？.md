
### 如何制作 CSR 文件？

本文档指导您如何制作 CSR（Certificate Signing Request）文件。

#### 前提条件
申请数字证书之前，您需要准备生成证书的密钥文件和 CSR 文件。CSR 文件是您的公钥证书原始文件，包含了您的服务器信息和您的单位信息，需要提交给 CA 认证中心进行审核。建议您使用系统创建的 CSR 文件，避免出现输入信息错误而导致审核失败。若您选择手动生成 CSR 文件，请务必妥善保管并备份您的密钥文件，手动生成 CSR 文件时需要注意以下信息：
- 输入的中文信息需要使用 UTF-8 编码格式，请在编辑 OpenSSL 工具时，指定支持 UTF-8 编码格式。
- 证书服务系统对 CSR 文件的密钥长度有严格要求，密钥长度必须是 2048bit，密钥类型必须是 RSA。
- 如果申请证书是多域名或者通配子域名，在 Common Name 或 What is your first and last name? 区域只需要输入一个域名。

#### 使用 OpenSSL 工具生成 CSR 文件
1. 登录运行 Linux 系统的一台本地计算机或服务器。
2. 安装 OpenSSL 工具，详情可参考 [如何安装 OpenSSL？](https://cloud.tencent.com/document/product/400/5707)
3. 执行以下命令，即可生成 CSR 文件。
```
openssl req -new -nodes -sha256 -newkey rsa:2048 -keyout [$Key_File] -out [$OpenSSL_CSR]
```
>?
 - **new**：指定生成一个新的 CSR 文件。
 - **nodes**：指定密钥文件不被加密。
 - **sha256**：指定摘要算法。
 - **newkey rsa:2048**：指定密钥类型和长度。
 - **[$Key_File]**：密钥文件名称。
 - **[$OpenSSL_CSR]**：加密后文件的存放路径。
4. 根据系统返回的提示，输入生成 CSR 文件所需的信息。以下是关于提示的说明：
 - **Organization Name**：公司名称，可以是中文或英文。
 - **Organizational Unit Name**：部门名称，可以是中文或英文。
 - **Country Code**：申请单位所属国家，只能是两个字母的国家码。例如，中国填写为 CN。
 - **State or Province Name**：州名或省份名称，可以是中文或英文。
 - **Locality Name**：城市名称，可以是中文或英文。
 - **Common Name**：申请 SSL 证书的具体网站域名。
 - **Email Address**：可选择不输入。
 - **Challenge Password**：可选择不输入。
5. 按照命令提示输入相应内容后，即可在当前目录下获取密钥文件和 CSR 文件。

