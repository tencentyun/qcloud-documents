## 前提条件
如果您想通过 Git 仓库来构建容器镜像，那么请先完成 [源码仓库授权](https://cloud.tencent.com/document/product/457/10153) 操作。

## 操作步骤
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的【镜像仓库】，在下拉列表中单击【我的镜像】，进入 我的镜像库页面，单击右侧【构建配置】。
![](//mc.qcloudimg.com/static/img/450d3f500a9ceb3d2269e71a6ca3f9af/image.png)
3. 进入构建规则页面，配置相关信息：
### Github 构建规则
 - **代码源**： 选择 Github。
 - **Organization**：选择您的 Organization，通常为您的 Github 账户，如果您属于多个组织，那么挑选其中一个。
 - **Repository**：选择您需要构建容器镜像的仓库。
 - **触发方式**：复选模式，支持当 push 代码到某个分支或者新的 Tag 时，自动触发容器镜像构建。您也可以都不选到镜像仓库详情页的镜像构建页手动构建。
 - **版本命名规则**：即容器镜像 ** Tag 命名规则**，镜像 Tag 名支持格式化，可以包含分支名 / 仓库 Tag 名。
 i：**更新时间**：镜像构建时间。
 ii：**commit 号**：分支 / Tag 最近的 commit 号。
 >**注意：**
 >如果在某个分支或者Tag 上进行自动构建，且版本命名规则包含了分支 / 标签，那么分支或者 Tag 名不能包含特殊字符，例如不能包含 /，$ 等特殊字符，可以包含大小写字符，下划线（_），连接符（-）。
 - **Dockerfile路径**：Dockerfile 在仓库中的**相对路径**。默认为空，可以不填，表示 Dockerfile 位于项目的根目录下，且文件名必须为 Dockerfile，以大写 D 开头。如果 Dockerfile 位于其它目录，例如位于仓库的 build 目录下，文件名为 Dockerfile，那么 Dockerfile 路径为：`build/Dockerfile`。
![](//mc.qcloudimg.com/static/img/1f5a9fd325da7dd63ea4c4408f314d3f/image.png)

### Gitlab构建规则
- **代码源**：选择 Gitlab。
- **Group**：选择一个 Gitlab 的Group。
- **Repository**：选择您需要构建容器镜像的仓库。
- **触发方式**：复选模式，支持当 push 代码到某个分支或者新的 Tag 时，自动触发容器镜像构建。您也可以都不选到镜像仓库详情页的镜像构建页手动构建。
- **版本命名规则**：即容器镜像 ** Tag 命名规则**，镜像 Tag 名支持格式化，可以包含分支名 / 仓库 Tag 名。
 i：**更新时间**：镜像构建时间。
 ii：**commit 号**：分支 / Tag 最近的 commit 号。
 >**注意：**
 >如果在某个分支或者 Tag 上进行自动构建，且版本命名规则包含了分支 / 标签，那么分支或者 Tag 名不能包含特殊字符，例如不能包含 /，$ 等特殊字符，可以包含大小写字符，下划线（_），连接符（-）。
- **Dockerfile路径**：Dockerfile 在仓库中的**相对路径**。默认为空，可以不填，表示 Dockerfile 位于项目的根目录下，且文件名必须为 Dockerfile，以大写 D 开头。如果 Dockerfile 位于其它目录，例如位于仓库的 build 目录下，文件名为 Dockerfile，那么 Dockerfile 路径为：`build/Dockerfile`。
![](//mc.qcloudimg.com/static/img/b5732ca8ff3d6e27efe562e0a2a534f6/image.png)

## 自动构建
如果您完成了构建规则的配置，并且触发方式选择了添加新 Tag 时触发或者提交代码到分支时触发，那么当您提交一个新的分支或者 push 代码到指定仓库时，会自动触发容器镜像的构建，整个构建过程在腾讯云的容器平台上进行，构建完成后，按照您定义的版本命名规则，会生成新的镜像，并上传到腾讯云容器镜像仓库。



