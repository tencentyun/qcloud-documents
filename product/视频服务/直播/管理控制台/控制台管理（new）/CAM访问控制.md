云直播通过 CAM 访问控制进行权限管理，以便于您管理账户的云直播域名、配置和数据信息。您可以创建、管理或销毁用户（组），将不同的接口权限授予子用户（组），以实现身份管理和策略控制。

当您使用 CAM 的时候，可以将策略与一个用户或一组用户关联起来，策略能够授权或者拒绝用户使用指定资源完成指定任务。

## 基本概念

- 主账号：注册的腾讯云账号。
- 子用户：通过主账号创建，完全归属于主账号。
- 协作者：拥有主账号的身份，被添加为当前主账号的协作者，为当前主账号的子账号之一。
- 用户组：为相同职能的一类用户创建的组，可为其关联策略，便于统一批量授权管理。

详细定义和权限请参见 [CAM 用户](https://cloud.tencent.com/document/product/598/13665)。

## 操作步骤
### 第一步：新建子用户/用户组

主账号可以创建一个或多个子用户，以为其分配特定的角色和策略。子用户有确定的身份 ID 和身份凭证，可登录控制台并完成设置，同时具有 API 访问权限。登录腾讯云控制台，进入 [访问管理](https://console.cloud.tencent.com/cam/) 页面，可新建用户，如下图所示：

![](https://main.qcloudimg.com/raw/ba0f63ed813555c644a7846c678ae954.png)
详细步骤请参见访问管理 [子用户](https://cloud.tencent.com/document/product/598/13674) 和 [用户组](https://cloud.tencent.com/document/product/598/10599)。

### 第二步：为用户/用户组添加策略

用户/用户组管理和策略管理页均可完成策略添加和授权，详细请参见 [授权管理](https://cloud.tencent.com/document/product/598/10602)，简述如下：

- 方法一：进入用户/用户组页面，选择需添加策略的用户/用户组，单击操作列表中的【授权】，选中相应的直播策略，同时单击【确定】即可添加成功。
![](https://main.qcloudimg.com/raw/807613247ce82e74a675671f2ad0775d.jpg)

- 方法二：进入策略页面，选择需添加的策略，单击操作列表中的【关联用户/组】，选中需授权的用户，单击【确定】即可添加成功。
![](https://main.qcloudimg.com/raw/bcecf5b50a67e67e282b9a0f7c8232bc.jpg)

**可添加的策略有**：
1. 添加系统预设策略：通过左侧边栏进入策略页面，可查询当前所有的策略信息。云直播系统预设策略为 [QcloudLIVEFullAccess](https://console.cloud.tencent.com/cam/policy/detail/9545933&QcloudLIVEFullAccess&2)（全读写策略）和 [QcloudLIVEReadOnlyAccess](https://console.cloud.tencent.com/cam/policy/detail/13346800&QcloudLIVEReadOnlyAccess&2)（只读策略）。
2. 添加自定义策略：进入策略页面，单击【新建自定义策略】，选择【按策略生成器创建】，详细请参见 [自定义策略](https://cloud.tencent.com/document/product/598/10601#.E8.87.AA.E5.AE.9A.E4.B9.89.E7.AD.96.E7.95.A5)。

**例如**：
若需将【添加证书】接口授权给子用户，且仅可用于指定域名，按照下述步骤配置：
1. 新建允许访问此接口的域名级策略，进入策略生成器创建策略页面。
2. 填写各输入项，在【效果】项中选择【允许】，在【服务】项中选择【云直播】，在【操作】项中选择【查询域名列表】，在【资源】项中输入需授权的域名。语法为：
 ```
qcs::${ApiModule}:${Region}:uin/:domain/${DomainName}
 ```
 其中：
 - `${ApiModule}`为 live。
 - `${Region}`为 ap-guangzhou。
 - `uin`为授权账号，值为空表示授权给当前账号。
 - `${DomainName}`为需授权的域名。
 示例：`qcs::live:ap-guangzhou::domain/cloud.tencent.com`，单击【添加声明】>【下一步】>【创建策略】，即可生成该策略。策略生成后，通过上述两种方法关联用户/用户组即可。
![](https://main.qcloudimg.com/raw/fb86acf318b04dead5ca12eacf387595.png)

>?若需将接口授权给子用户，且适用所有域名，在【资源】项中填写\*即可。


### 第三步：子账号使用

使用子账号身份（主账号创建的子账号 ID 和密码），调用已授权的 API 接口（例如：“查询域名列表”等），可以获取相应的云直播信息（例如：该账号下的所有域名）。

