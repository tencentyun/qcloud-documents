## 操作场景
本文档介绍 SSH 密钥对登录实例常见的相关操作，例如对 SSH 密钥的创建、绑定、解绑、修改、删除等操作。


<dx-alert infotype="notice" title="">
云服务器需关机后才可绑定或解绑密钥，请参考 [关机实例](https://cloud.tencent.com/document/product/213/4929) 对云服务器进行关机操作。
</dx-alert>



## 操作步骤

### 创建 SSH 密钥[](id:creatSSH)
 1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/)。
 2. 在左侧导航栏中，单击 **[SSH 密钥](https://console.cloud.tencent.com/cvm/sshkey)**。
 3. 在 SSH 密钥管理页面，单击**创建密钥**。
<dx-alert infotype="notice" title="">
单击**确定**后会自动下载私钥，腾讯云不会保管您的私钥信息，请务必妥善保管您的私钥。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/c6670263e32491f583d1bf0a31e19ce7.png">
  <ul>
  <li> 若创建方式选择 “创建新密钥对”，请输入密钥名称。</li>
  <li>若创建方式选择 “导入已有公钥”，请输入密钥名称和原有的公钥信息。</li>
	</ul>



### 密钥绑定实例[](id:bindingSSH)
 1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/)。
 2. 在左侧导航栏中，单击 **[SSH 密钥](https://console.cloud.tencent.com/cvm/sshkey)**。
 3. 在 SSH 密钥管理页面，勾选需要绑定云服务器的 SSH 密钥，并单击**绑定实例**。如下图所示：
![](https://main.qcloudimg.com/raw/454857fb36fc098e3de5d7987a8b9c46.png)
 4. 在弹出的绑定实例窗口中，选择地域，勾选需绑定的云服务器，单击**确定**。


### 密钥解绑实例
 1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/)。
 2. 在左侧导航栏中，单击 **[SSH 密钥](https://console.cloud.tencent.com/cvm/sshkey)**。
 3. 在 SSH 密钥管理页面，勾选需要解绑云服务器的 SSH 密钥，并单击**解绑实例**。如下图所示：
![](https://main.qcloudimg.com/raw/6b84f5c8a8460f435444044726404991.png)
 4. 在弹出的解绑实例窗口中，选择地域，勾选需解绑的云服务器，单击**确定**。


### 修改 SSH 密钥名称/描述
 1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/)。
 2. 在左侧导航栏中，单击 **[SSH 密钥](https://console.cloud.tencent.com/cvm/sshkey)**。
 3. 在 SSH 密钥管理页面，选择密钥名称右侧的 <img  style="margin:-3px 0px" src="https://main.qcloudimg.com/raw/9db81482f9242417d94a04f314b42b19.png"/>。如下图所示：
![](https://main.qcloudimg.com/raw/d6392148e08a8a6c527dd5aae0088eaf.png)
 4. 在弹出的修改密钥窗口中，输入新的密钥名称和密钥描述，单击**确定**。

### 删除 SSH 密钥

<dx-alert infotype="notice" title="">
若 SSH 密钥已关联云服务器或已关联自定义镜像，则该密钥不能删除。
</dx-alert>


1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/)。
2. 在左侧导航栏中，单击 **[SSH 密钥](https://console.cloud.tencent.com/cvm/sshkey)**。您可按需删除单个密钥或批量删除密钥：
<dx-tabs>
::: 删除单个密钥
    1. 在 SSH 密钥管理页面，选择需要删除的 SSH 密钥所在行右侧的**删除**。如下图所示：
![](https://main.qcloudimg.com/raw/e9094886151039cd1843e0ebc2a8dfb7.png)
    2. 在弹出的删除密钥窗口中，单击**确定**。
    
:::
::: 批量删除密钥
    1. 在 SSH 密钥管理页面，勾选需删除的密钥并单击页面上方的**删除**，进行密钥批量删除操作。
    2. 在弹出的删除密钥窗口中，单击**确定**。如下图所示：
    如果所选密钥对中包含无法删除的密钥对，则该操作仅对允许删除的密钥对进行删除。
		![](https://main.qcloudimg.com/raw/568387aa0a8a59c5a34c61ae3193c921.png)
		
:::
</dx-tabs>



### 使用 SSH 密钥登录 Linux 云服务器

1. [创建 SSH 密钥](#creatSSH)。
2. [将 SSH 密钥绑定云服务器](#bindingSSH)。
3. [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)。
