本文为您介绍如何绑定 GitLab 私有云服务。

## 进入团队管理页

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击【立即使用】进入 CODING 使用页面。
2. 将鼠标移至页面右上角的头像处，会出现下拉菜单，单击进入团队管理界面。

CODING 支持您关联 GitLab 公有云和私有云等外部仓库，在关联之后您就可以在 CODING 的持续集成、制品库等模块中使用外部仓库。具体使用步骤如下：

1.  绑定 GitLab 私有云服务
2.  关联 GitLab 代码仓库
3.  在 CODING 中使用 GitLab 仓库

前提条件：

-   只有团队所有者、团队管理员以及被授予服务集成权限的成员才可以进行绑定操作；
-   您的私有 GitLab 需要暴露在公网才能保证在 CODING 中授权成功；
-   您的私有 GitLab 版本需要在 GitLab 10.7 及以上才能保证仓库可以成功关联并检出；

## 绑定 GitLab 私有云服务

### 1. 在 GitLab 私有云创建应用

登录 GitLab 私有云后，点击右上角账号图标中的【Settings】->【Applications】 进入第三方应用授权管理页面，创建一个新应用，参数填写如下，填写完毕后点击【Save application】。

-   重定向 URL（Redirect URL）需填写：<https://e.coding.net/api/oauth2/platforms/gitlab_private/callback>
-   Scopes 需勾选 api、read_user、read_repository 这三项
-   注意：如果您的 Scopes 选项中无法找到上述选项，请检查您的私有 GitLab 版本是否符合前提条件要求。

![](https://help-assets.codehub.cn/enterprise/20200722152249.png)

创建成功后，GitLab 会生成对应的应用 ID（Application ID）和密匙（Secret）。

![](https://help-assets.codehub.cn/enterprise/20200722152847.png)


### 2. 在 CODING 的服务集成绑定 GitLab 私有云

登录 CODING ，点击右上角【团队管理】进入团队帐户页面。点击【服务集成】->【GitLab 私有云】->【绑定】。

![](https://help-assets.codehub.cn/enterprise/20200730160937.png)

在绑定弹窗中输入信息，其中 Application ID 和 Secret 就是上个步骤在 GitLab 私有云创建应用时生成的，填写完毕后点击【授权绑定】。

![](https://help-assets.codehub.cn/enterprise/20191226141232.png)

跳转至 GitLab 授权页面后，请点击【授权（Authorize）】完成授权。

![](https://help-assets.codehub.cn/enterprise/20200722153925.png)

在 CODING 绑定成功后，在原页面点击【已完成授权】。

![](https://help-assets.codehub.cn/enterprise/20201111191340.png)

绑定成功后，您可以在页面中看到【已绑定】标志。


> 如需解除绑定，在服务集成页面中点击您要解绑的第三方服务后的【查看详情】，在详情弹窗页中点击【解除绑定】即可。
>
>![](https://help-assets.codehub.cn/enterprise/20200102111338.png)

## 关联 GitLab 代码仓库

在绑定 GitLab 私有云服务成功后，即可前往项目内关联代码仓库。

点击【项目设置】->【开发者选项】->【外部仓库管理】->【关联新代码库】：

![](https://help-assets.codehub.cn/enterprise/20191226144356.png)

在关联代码库页面，填写信息如下：

1.  选择代码库来源
2.  选择认证方式:
-   推荐 OAuth，您只需点击授权即可，快捷简单
-   用户名密码，需选择对应的凭据。如果无可用凭据，您需去凭据页面创建“用户名密码”凭据，填写代码来源服务的帐户密码。
3.  填写代码库地址
4.  选择开放的项目模块

填写完毕后，点击【确认】

![](https://help-assets.codehub.cn/enterprise/20191226143900.png)

关联新外部仓库成功后，您就可以在列表中看该仓库。

![](https://help-assets.codehub.cn/enterprise/20191226144922.png)

> 如需取消外部仓库关联，在【项目设置】->【开发者选项】->【外部仓库管理】，点击外部仓库名称进入代码库详情页面，在取消关联模块点击【确认】。

## 在 CODING 中使用 GitLab 仓库

在关联外部仓库成功后，您就可以在 CODING 中已被授权的模块（持续集成、制品库等）中使用这些仓库。

以 CODING 持续集成为例，除了 CODING 自有仓库外，目前 CODING 已支持以下三种外部仓库：GitHub.com / GitLab.com / GitLab 私有云。

![](https://help-assets.codehub.cn/enterprise/20200302152947.png)

## 防火墙 IP 放行名单

如果您的服务器、GitLab 设置了防火墙，请放行 CODING IP：

```text
212.129.144.0/24
212.64.105.0/24
```

并且打开 CODING 持续集成，查看构建节点 IP，进行放行：

![](https://help-assets.codehub.cn/enterprise/20200826163506.png)