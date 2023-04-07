## 操作场景
本文档介绍 SSH 密钥对登录实例常见的相关操作，例如对 SSH 密钥的创建、绑定、解绑、修改、删除等操作。


<dx-alert infotype="notice" title="">
云服务器需关机后才可绑定或解绑密钥，请参考 [关机实例](https://cloud.tencent.com/document/product/213/4929) 对云服务器进行关机操作。
</dx-alert>



## 操作步骤

### 创建 SSH 密钥[](id:creatSSH)
1. 登录云服务器控制台，选择左侧导航栏中的 **[SSH密钥](https://console.cloud.tencent.com/cvm/sshkey)**。
2. 在 **SSH 密钥**页面，单击**创建密钥**。
3. 在弹出的**创建SSH 密钥**窗口中，配置密钥。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9df80136b7aefd2f079367105bb0166d.png)
 - **创建方式**：
    - 选择**创建新密钥对**，则请输入密钥名称。
    - 选择**导入已有公钥**，则请输入密钥名称和原有的公钥信息。
<dx-alert infotype="notice" title="">
需使用自身不具备密码的公钥，否则将无法通过控制台成功登录实例。
</dx-alert>
 - **密钥名称**：自定义名称。
 - **标签（选填）**：可按需给密钥增加标签，用于资源的分类、搜索和聚合。更多信息请参见 [标签](https://cloud.tencent.com/document/product/651/13334)。
4. 单击**确定**，即可完成创建。
<dx-alert infotype="notice" title="">
单击**确定**后会自动下载私钥，腾讯云不会保存私钥文件。如果私钥文件丢失，可以考虑重新创建密钥，并绑定到对应实例上，请您妥善保存。
</dx-alert>




### 密钥绑定实例[](id:bindingSSH)
1. 登录云服务器控制台，选择左侧导航栏中的 **[SSH密钥](https://console.cloud.tencent.com/cvm/sshkey)**。
2. 在**SSH 密钥**页面，单击需绑定实例密钥所在行右侧的**绑定实例**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d522b51edb289350e56085023d1c928b.png)
3. 在弹出的绑定实例窗口中，选择地域，勾选需绑定的云服务器，单击**绑定**。


### 密钥解绑实例
1. 登录云服务器控制台，选择左侧导航栏中的 **[SSH密钥](https://console.cloud.tencent.com/cvm/sshkey)**。
2. 在 “SSH密钥” 页面，单击解绑实例密钥所在行右侧的**解绑实例**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e04b1f72a9c210062ecca0926855311b.png)
3. 在弹出的解绑实例窗口中，选择地域，勾选需解绑的实例，单击**解绑**。


### 修改 SSH 密钥名称或描述
1. 登录云服务器控制台，选择左侧导航栏中的 **[SSH密钥](https://console.cloud.tencent.com/cvm/sshkey)**。
2. 在 “SSH密钥” 页面，选择密钥名称右侧的 <img  style="margin:-3px 0px" src="https://main.qcloudimg.com/raw/9db81482f9242417d94a04f314b42b19.png"/>。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4fb25cd3978cd8c66c31959aad676dd9.png)
3. 在弹出的“修改密钥”窗口中，输入新的密钥名称和密钥描述，单击**确定**。


### 删除 SSH 密钥

<dx-alert infotype="notice" title="">
若 SSH 密钥已关联云服务器或已关联自定义镜像，则该密钥不能删除。
</dx-alert>


1. 登录云服务器控制台，选择左侧导航栏中的 **[SSH密钥](https://console.cloud.tencent.com/cvm/sshkey)**。
2. 在 “SSH密钥” 页面，您可按需删除单个密钥或批量删除密钥：
<dx-tabs>
::: 删除单个密钥
    1. 选择需要删除的 SSH 密钥所在行右侧的**删除**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4f818d12eaced81cf28ea65e07553eb6.png)
    2. 在弹出的删除密钥窗口中，单击**确定**。
    
:::
::: 批量删除密钥
    1. 勾选需删除的密钥，并单击页面上方的**删除**，进行密钥批量删除操作。
    2. 在弹出的删除密钥窗口中，单击**确定**。如下图所示：
    如果所选密钥对中包含无法删除的密钥对，则该操作仅对允许删除的密钥对进行删除。
![](https://qcloudimg.tencent-cloud.cn/raw/c7ffc2842ce04426869cd4ad89e613ef.png)
		
:::
</dx-tabs>



## 相关操作


### 使用 SSH 密钥登录 Linux 云服务器

1. [创建 SSH 密钥](#creatSSH)。
2. [将 SSH 密钥绑定云服务器](#bindingSSH)。
3. [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)。


### 编辑密钥标签

若您需对 SSH 密钥进行标签的增加、修改、删除操作，可参考以下步骤。若您需了解更多标签相关信息，请参见 [标签](https://cloud.tencent.com/document/product/651/13334)。 

1. 在 “SSH密钥” 页面，单击密钥右侧的**编辑标签**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cada9cc1f72d11e8c5c637a309d99fa9.png)
2. 在弹出的 “编辑标签” 窗口中，请按需进行操作。
3. 调整完毕后单击**确定**即可。

