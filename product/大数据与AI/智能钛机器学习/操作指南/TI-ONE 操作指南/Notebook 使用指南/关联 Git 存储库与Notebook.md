## 操作场景
腾讯云 TI 平台 TI-ONE 支持 Notebook 与 Git 存储库关联。您可以将 Notebook 保存到 Git 库中，不必担忧信息因为 Notebook 实例的删除和关闭而丢失。您也可以将一个 Notebook 实例与一个默认存储库和多个其他存储库同时关联，最多关联3个其他存储库。

与存储库关联有以下特性优势：
- **持续存储**
Notebook 实例中的笔记本存储在腾讯云 CBS 中，与 Git 存储库关联后，您可以在 Notebook 实例之外管理您的笔记本，避免实例误删导致的数据丢失。
- **项目合作**
当与多个伙伴协同开发机器学习项目时，将 Notebook 数据存储到 Git 存储库将方便您进行数据的共享与版本控制。
- **开源项目的学习**
目前很多机器学习项目都在 Github 等平台上开源，用户可以轻松关联自己的笔记本实例与公开库，并下载其中的 Jupyter notebooks，基于其进行学习。


## 操作详情
### 新增存储库
前往 Notebook [Git 存储库](https://console.cloud.tencent.com/tione/notebook/gitpage) 页面，单击【新增存储库】，在弹窗中输入存储库的名称，目标存储库的 URL 以及存储库分支的名称（可选）。如果目标存储库为需要验证的私有存储库，您必须准确输入所需的用户名与密码，用于凭证验证。
![](https://main.qcloudimg.com/raw/e43f2bfe1861d95815e21f53e4492efc.png)

>!
>- 出于密钥安全考虑，凭证将由腾讯云 KMS 产品进行加密和存储，具体内容请参见 [KMS 说明](https://cloud.tencent.com/product/kms/details) 与  [KMS 定价](https://cloud.tencent.com/product/kms/pricing)，历史创建的密钥可前往 [KMS 控制台](https://console.cloud.tencent.com/kms2/product) 查看。
>- 对于 GitHub 存储库，建议使用个人访问令牌而不是您的账户密码。具体详情请参考 [创建用于命令行的个人访问令牌](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) 文档。

                
### 新增 Notebook 实例关联 Git 存储库
前往 **Notebook** 页面，单击【新建实例】，您可以在 Git 存储的下拉列表中看到在第一步创建的存储库名称。单击➕图标可以添加除默认存储库以外的其他存储库，最多添加3个其他存储库。

除了选择在第一步创建的存储库，用户还可以选择在此实例中克隆一个公共 Git 存储库，然后在输入框中正确输入此公共存储库的 URL 即可。

进入 Notebook 后，成功关联的存储库将在左栏的 Git 模块下显示。
![](https://main.qcloudimg.com/raw/23cb8710e860a331bff3012fc1c3ba5b.png)

### 历史实例关联 Git 存储库
已经创建的 Notebook 实例也可以与 Git 存储库关联。如果是运行中的实例，您需要先单击【停止】，再单击【编辑】，对 Git 存储相关信息进行编辑，重新**启动**后成功关联的存储库将在左栏的 Git 模块下显示。

### 编辑已创建的 Git 存储库
前往**Notebook-Git 存储库**页面，单击【编辑】，可以对已创建的 Git 存储库的密钥进行编辑。
>!一旦创建，存储库的名称和 URL 将**不能**修改，如果输入错误，建议删除重新新建。
