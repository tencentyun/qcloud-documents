## 操作场景
云端开发环境 Cloud Studio 支持从 Git 仓库导入代码来创建工作空间。当您选择这种方式导入时，您需要先将 Cloud Studio 的 [SSH 公钥](https://coding.net/help/doc/account/ssh-key.html#SSH) 添加到目标仓库的公钥列表，这样您在导入代码时就无需再次验证身份了。
本文以导入 GitHub 仓库为例，指导您将 Cloud Studio 的 SSH 公钥添加到 Git 仓库。

## 操作步骤
1. 登录 [云端开发环境 Cloud Studio 控制台](https://console.cloud.tencent.com/cloudstudio/workspace)。
2. 在左侧导航中，选择【[设置](https://console.cloud.tencent.com/cloudstudio/setting)】。
3. 在设置页面中，单击复制 SSH 公钥（下图阴影部分的字符串）。
![](https://main.qcloudimg.com/raw/0199ebac144a34597c68850876e50ea9.png)
4. 在 [GitHub 平台的个人 SSH 公钥设置页面](https://github.com/settings/keys)，单击右上角的【New SSH Key】。
![](https://main.qcloudimg.com/raw/77b574177af570a0ca0a4951a706613f.jpg)
5. 将步骤3复制的 SSH 公钥粘贴到 Key 输入框内。Title 填写公钥的名称，如“Cloud Studio”，如果空着系统会自动生成。
6. 单击【Add SSH key】，保存 SSH 公钥。
![](https://main.qcloudimg.com/raw/52124af3fd0dac79d0dee23e5630339b.jpg)

添加完成之后，您可以将该 Github 上的代码仓库导入到 Cloud Studio，并使用 Git 提交代码到该仓库。其它 Git 仓库的设置与之类似，可以参考此文设置。
