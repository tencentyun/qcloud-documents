本文档将指导用户在 Mac OS 系统中安装信任证书。

## 操作场景
运维用户使用本地自签发证书认证登录堡垒机时，运维用户需要在 Mac OS 系统中安装信任证书。
## 操作步骤
1. 使用 Safari 浏览器访问堡垒机网站，Safari 会提示该网站证书存在问题，单击【显示详细信息】，将出现风险提示。
![](https://main.qcloudimg.com/raw/2a1d555046e6ea1fd92374bef7bb6f86.png)
2. 在出现风险提示框中，单击【访问此网站】，将弹出确认框。
![](https://main.qcloudimg.com/raw/672e3792b7473a0aa87fe3eb8090370b.png)
3. 在确认框中，单击【访问网站】，将弹出验证框。
![](https://main.qcloudimg.com/raw/512bae3f279a2eb6bfe9f64bd6222125.png)
4. 在验证框中，输入用户名及密码。
![](https://main.qcloudimg.com/raw/b849183188961d766aeab9ecb5321c2e.png)
5. 确认完成后，在 Mac OS 的实用工具中，打开钥匙串访问应用。
![](https://main.qcloudimg.com/raw/084aafded27a8faece1db1721686df5c.png)
6. 在登录选项卡中，找到网站的证书，双击证书。
![](https://main.qcloudimg.com/raw/db9ca78cd4f5726fcdb72fbc65bbec63.png)
7. 在信认选项中，改为始终信任。
![](https://main.qcloudimg.com/raw/f070b3883c5f05998694649e3e204d4f.png)
8. 再次在弹出的验证框中，输入密码，将成功信任该网站的证书。
