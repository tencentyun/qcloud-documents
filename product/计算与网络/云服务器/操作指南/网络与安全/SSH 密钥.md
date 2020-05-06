## 操作场景
密码是每台云服务器实例专有的登录凭据。为保证实例的安全可靠，腾讯云提供以下两种加密登录方式：
- [密码登录](https://cloud.tencent.com/document/product/213/6093)
- SSH 密钥对登录。

本文档介绍 SSH 密钥对登录实例相关的常见操作内容。

## 操作步骤

<span id="creatSSH"></span>
### 创建 SSH 密钥
 1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/)。
 2. 在左侧导航栏中，单击【[SSH 密钥](https://console.cloud.tencent.com/cvm/sshkey)】。
 3. 在 SSH 密钥管理页面，单击【创建密钥】。
 4. 在弹出的创建 SSH 密钥窗口中，根据实际需求，选择密钥的创建方式，填写相关信息，并单击【确定】。
 ![](https://main.qcloudimg.com/raw/4e195847f7027ffca6a64616924e09e9.png)
  - 若创建方式选择 “创建新密钥对”，请输入密钥名称。
  - 若创建方式选择 “使用已有公钥”，请输入密钥名称和原有的公钥信息。
 4. 在弹出的提示框中，单击【下载】，即可下载私钥。
 >! 腾讯云不会保管您的私钥信息，请在10分钟内下载和获取私钥。
 > 

<span id="bindingSSH"></span>
### 密钥绑定/解绑云服务器
 1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/)。
 2. 在左侧导航栏中，单击【[SSH 密钥](https://console.cloud.tencent.com/cvm/sshkey)】。
 3. 在 SSH 密钥管理页面，勾选需要绑定/解绑云服务器的 SSH 密钥，单击【绑定/解绑实例】。
 ![](https://main.qcloudimg.com/raw/d24f842ee3ef04bdf5903e2c5b4bd4a2.png)
 4. 在弹出的绑定/解绑实例窗口中，选择地域，勾选需绑定/解绑的云服务器，单击【确定】。


### 修改 SSH 密钥名称/描述
 1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/)。
 2. 在左侧导航栏中，单击【[SSH 密钥](https://console.cloud.tencent.com/cvm/sshkey)】。
 3. 在 SSH 密钥管理页面，勾选需要修改的密钥，单击上方的【修改】。
 ![](https://main.qcloudimg.com/raw/ad9be047567c1b7a820f177e31f78346.png)
 4. 在弹出的修改密钥窗口中，输入新的密钥名称和密钥描述，单击【确定】。

### 删除 SSH 密钥
>! 若 SSH 密钥已关联云服务器或已关联自定义镜像，则该密钥不能删除。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/)。
2. 在左侧导航栏中，单击【[SSH 密钥](https://console.cloud.tencent.com/cvm/sshkey)】。
3. 在 SSH 密钥管理页面，勾选所有需要删除的 SSH 密钥，单击【删除】。
![](https://main.qcloudimg.com/raw/5459959b9bedaa6d0da7d74a0379203d.png)
4. 在弹出的删除密钥窗口中，单击【确定】。

### 使用 SSH 密钥登录 Linux 云服务器

1. [创建 SSH 密钥](#creatSSH)。
2. [将 SSH 密钥绑定云服务器](#bindingSSH)。
3. [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)。
