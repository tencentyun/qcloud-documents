## 操作场景
腾讯云云函数（SCF）针对单函数，提供从公网 Git 仓库拉取代码部署的能力。

## 前提条件
 - 已开通云函数 Git 拉取代码功能。
 Git 拉取代码目前为内测发布功能，可通过 [内测申请](https://cloud.tencent.com/apply/p/kd8np1at8r) 获取此功能。
 - 请对应您的公网 Git 仓库获取认证信息。SCF 支持以下公网 Git 仓库：
  - [Github](#git)
  - [Coding](#coding) 
  - [码云](#yun)





[](id:git)
### Git 认证信息
**用户名：**Git 帐户的用户名。
**密码：**Git 帐户的私人令牌或者密码。

#### 获取 Github 私人令牌
1. 进入 [Github tokens](https://github.com/settings/tokens) 页面，勾选 repo 获取仓库的读/写权限。如下图所示：
![](https://main.qcloudimg.com/raw/6e12bcb45bbd998d80440a0e0849f035.png)
2. 单击页面下方的**Generate token**，即可看到生成的私人令牌。

[](id:coding)
### Coding 认证信息
**用户名：** 登录 Coding 并进入个人首页，记录浏览器地址栏 `/u/` 后的内容作为用户名。如下图所示：
![](https://main.qcloudimg.com/raw/966071a6c017ae3ca337cfed7b302f77.png)
**密码：**Coding 帐户的私人令牌。

#### 获取 Coding 私人令牌
请参考 [Coding 私人令牌](https://open.coding.net/personal-access-token/#%E5%88%9B%E5%BB%BA%E4%B8%AA%E4%BA%BA%E8%AE%BF%E9%97%AE%E4%BB%A4%E7%89%8C) 文档获取。 
设置令牌时，请勾选 `project:depot` 获取仓库的读/写权限。如下图所示：
![](https://main.qcloudimg.com/raw/2a221caac37be9b91767c8ef1065371a.png)

[](id:yun)
### 码云认证信息
**用户名：**码云帐户的用户名。
**密码**：码云帐户的私人令牌。

#### 获取码云私人令牌
1. 进入 [码云私人令牌设置](https://gitee.com/profile/personal_access_tokens) 页面，单击页面右上角的**生成私人令牌**。
2. 在私人令牌配置页面，勾选 `projects` 后单击**提交**，即可在弹出页面看到生成的私人令牌。如下图所示：
![](https://main.qcloudimg.com/raw/4ecc29dd0cc3b3a5137f92bd90b84813.png)

## 操作步骤
1.登录 [SCF 控制台](https://console.cloud.tencent.com/scf/index)，选择**广州**。
>!Git 拉取代码功能目前仅支持**北京**和**广州**。
>
2. 选择左侧导航栏**函数服务**，单击**新建**。如下图所示：
![](https://main.qcloudimg.com/raw/3edbe1d2a74e21a2800bd21b08741f50.png)
3. 在“新建函数”页面，填写函数信息，单击**下一步**。如下图所示：
 - **函数类型**：选择“事件”。
 - **函数名称**：可根据您的实际需求填写，本文以 “hello” 为例。
 - **运行环境**：选择 “Node.js 8.9”。
 - **创建方式**：选择“空白函数”。
 若您选择创建方式为“模板函数”，请前往“函数代码”页面通过 Git 拉取代码。
![](https://main.qcloudimg.com/raw/b9375bc943bbb78ccb6c0c83c8d06dfe.png)
4. 在“函数配置”页面，“提交方法”选择“通过git上传代码包”，并填写您使用的 Git 仓库相关信息。
![](https://main.qcloudimg.com/raw/8992b7bc2e06f9135164f5cb69783817.png)
5.单击**完成**，即可成功拉取代码并创建函数。
>!拉取成功后，云函数文件夹将被 Git 仓库对应文件夹覆盖。

