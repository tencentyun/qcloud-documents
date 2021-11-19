本文将介绍 WordPress 平台自带的用户管理和登录认证功能。
## 前提条件
- 已开通 [云函数 SCF 服务](https://console.cloud.tencent.com/scf)。
- 已开通 [文件存储 CFS 服务](https://console.cloud.tencent.com/cfs)。
- （可选）准备好已备案的自定义域名，您也可以通过 Serverless 备案资源包完成备案（详情请参见 [ICP 备案](https://cloud.tencent.com/document/product/1154/50706)）。

## 操作步骤
1. 登录 [Serverless 应用控制台](https://console.cloud.tencent.com/scf/list?rid=4&ns=default)，在左侧导航栏选择 **Serverless 应用**，进入 Serverless 应用页面。
2. 在 Serverless 应用页面，单击**新建应用**，进入新建应用页面。
![](https://qcloudimg.tencent-cloud.cn/raw/9e2a325efdc1207e302c6b166b360d6c.png)
3. 在新建应用页面，创建方式选择**应用市场**	，模板选择**快速部署一个 Wordpress 框架**，单击**下一步**。
4. 根据页面提示，配置所需参数，单击**完成**，即可创建 WordPress 应用。
>?相关参数请参见 [快速部署 Wordpress 原生应用](https://cloud.tencent.com/document/product/1154/52643#.E6.8E.A7.E5.88.B6.E5.8F.B0.E9.83.A8.E7.BD.B2)。
>
![](https://qcloudimg.tencent-cloud.cn/raw/501aa510459792beab11b2a47b6ed856.png)
5. 以管理员身份登录后台，在左侧导航栏，单击**用户** > **所有用户** ，进入所有用户页面。
>?假设已部署好的 WordPress 站点根路径是 `https://WORDPRESS.SITE`。
6. 在所有用户页面，可查看 WordPress 的用户列表，以及查看用户详情、维护用户信息、重置密码。
![](https://qcloudimg.tencent-cloud.cn/raw/a164f40d50dc64d4b5b32266db8e6d7a.jpg)
7. 访问站点首页 `https://WORDPRESS.SITE`，单击页面的**登录**，WordPress 默认的登录页面只支持账号密码认证方式。
![](https://qcloudimg.tencent-cloud.cn/raw/2a282033d8ae85fc1b3660139996a516.jpg)
