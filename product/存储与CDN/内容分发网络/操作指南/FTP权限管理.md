>!目前 FTP 托管源不再对新用户开放，存量用户可继续使用。

由于同一个腾讯云账号下，可能出现多个项目并行的情况，为了预防各项目间的信息泄漏，使用 FTP 托管源的用户，腾讯云支持每个项目、目录分配不同权限的托管源账号管理方案。

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧【托管源管理】菜单，选择【FTP 托管源权限管理】，进入托管源权限管理页面。
![](https://mc.qcloudimg.com/static/img/394f0b09f9b8a4cf9a705c326c06635e/1.png)
### 创建子账号
单击【添加子账号】按钮，可创建一个新的 FTP 子账号。
![](https://mc.qcloudimg.com/static/img/e364f6d1831d4bd662f97640b3a7517b/create_account.png)
可进行子账号的账号、密码、授权项目、授权目录设置。
> **注意**：
> + 账号为用户自定义的账号名称，前缀数字统一固定为云服务账号。
> + 可以不指定授权目录，此时授予指定项目的所有权限。
> + 指定授权的目录必须为已经存在的 FTP 目录，否则会导致添加子账号失败。

### 修改子账号密码
在子账号列表中，单击需要修改的子账号右侧的【重置密码】，可对其登录密码进行修改。
![](https://mc.qcloudimg.com/static/img/6abef77ccfe2bbc1934d7644473087cb/reset_password.png)

### 删除子账号
在子账号列表中，单击需要删除的子账号右侧的【删除】，可删除子账号，删除操作需要填充该子账号对应密码。
![](https://mc.qcloudimg.com/static/img/45a1090cbfcf19879b2321a1393bdd5e/del_account.png)
