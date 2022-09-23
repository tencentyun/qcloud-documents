## 创建子账号
- 使用主账号登录腾讯云 [访问管理控制台](https://console.cloud.tencent.com/cam)，单击**新建用户**即可创建子账号，包括子用户和协作者。
![](https://main.qcloudimg.com/raw/003a3abb5e0cf5565b32ae7b38b1c8a7.png)
- 创建成功后，CAM 会为该子账号生成登录信息，可单击**查看用户详情**后选择**安全** 并进行密码重置。
![](https://main.qcloudimg.com/raw/96800bd699e659d154c2ac8eca926f59.png)
![](https://main.qcloudimg.com/raw/526d659cb961da70abe06e9074231e24.png)
>?如果您需要多人协同开发，请为其他协作成员创建 CAM 子账号。

## 子账号授权
如果您需要给 CAM 子账号授予创建项目、定义数据资产分类目录的权限，需要给其授权 WeDataFullAccess 策略。若不需要赋予子账号以上权限，可略过此部分内容。
1. 在“用户列表”页面下，选择子账号，在操作列中点击**授权**。搜索选择 QcloudWeDataFullAccess 策略。
![](https://qcloudimg.tencent-cloud.cn/raw/722bda6b7aca32da5215a5b2e2b996e8.png)
2. 单击**确定**，即可授权子账号 WeData 权限。
