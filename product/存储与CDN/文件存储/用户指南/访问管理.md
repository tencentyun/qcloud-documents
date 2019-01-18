文件存储 CFS 已接入 CAM 鉴权，方便主账户为其他用户或者用户组分配权限。CFS 目前能够为被授权用户或用户组提供 "完全控制" 的权限：即授权后，该用户可执行文件系统及权限组相关的所有操作。
当需要为其他用户授权管理文件存储 CFS 时，请按照以下操作步骤，在对应的策略下关联需要被授权的用户或用户组。

## 用户/用户组授权
### 1. 查找策略
登录 [访问管理控制台](https://console.cloud.tencent.com/cam)，单击【策略管理】左侧导航栏。在策略管理界面右侧的搜索框中搜索 QcloudCFSFullAccess，QcloudCFSFullAccess 策略适用于使用 API 访问的用户或用户组，可为其提供文件存储 CFS 的全读写访问权限。
>**注意：**AdministratorAccess 策略为最高权限策略，适用于通过控制台访问或 API 访问的用户/用户组，但此策略权限范围较广，请谨慎使用。

![](https://main.qcloudimg.com/raw/37a6bd78ac799ce968202e29f210fbed.png)

### 2. 进入策略详情页
查找完毕后，单击 QcloudCFSFullAccess 策略名称，进入到详情页面。
![](https://main.qcloudimg.com/raw/944d82819bdd522aaa91226a2529d2cb.png)

### 3. 为用户/用户组授权
在策略详情页，选择单击【关联用户/组】， 然后单击【关联用户/用户组】按钮，在弹出的窗口中查找并勾选被授权的用户或用户组，最后单击【确定】按钮完成授权。
![](https://main.qcloudimg.com/raw/ebb2a3893bc78bb583ac929d4bdbfbf6.png)


## 取消用户/用户组授权
如需取消已授权用户的权限，可在对应策略详情页的【关联用户/组】列表中，勾选需要取消授权的用户，然后单击【解除用户】操作，确认解除授权后，该用户/用户组将失去操作文件存储 CFS 资源的权限。
![](https://main.qcloudimg.com/raw/d96fded352eac57482a0aee78eaa8006.png)

