堡垒机系统默认使用静态口令方式进行登录，若要使用 AD 域方式进行登录认证，您可查看本文档指引进行登录。

## 前提条件
管理员需要已完成 [配置域服务](https://cloud.tencent.com/document/product/1025/32132)。
## 操作步骤
1. 登录 [堡垒机控制台](https://console.cloud.tencent.com/cds/dasb)，找到需要操作的堡垒机，在右侧操作栏单击【管理】，进入堡垒机登录页面，也可以直接在浏览器中，输入访问地址`https://IP`，进入登录页面。 
2. 使用管理员账号登录堡垒机，在上方导航中，单击【用户管理】，在用户管理页面找到需要生成个人证书的运维用户，在编辑栏，单击“用户编辑”图标。
![](https://main.qcloudimg.com/raw/fc62c26f976d8ace9b35b91f9521022b.png)
3. 在用户编辑页面，单击【设置认证方式】，选择“静态口令认证”及“ AD 域认证”，单击【保存】即完成设置。
![](https://main.qcloudimg.com/raw/cd751e695dc24cfc8f983ee86ba62d57.png)
4. 返回堡垒机登录页面，在登录堡垒机界面输入运维用户名、密码后，正确拖动滑块，单击【登录】，即可使用 AD 域登录堡垒机。
![](https://main.qcloudimg.com/raw/8df4f740ab207356be7a3159f982b3e3.png)
