## 操作场景
本文主要介绍管理工具合成所需的 ZMK。


## 操作步骤
1. 登录 VsmManager 客户端，单击**密钥管理** > **对称密钥管理**。
![](https://qcloudimg.tencent-cloud.cn/raw/3556f50d469f25598d2e8318bdaadec2.png)
2. 在对称密钥管理弹窗中，单击**成份合成密钥**。
![](https://qcloudimg.tencent-cloud.cn/raw/49917a9b76d7d87cfb5dbd4bc87a739b.png)
3. 在成份合成密钥弹窗中，配置相关参数，单击**下一页**。
![](https://qcloudimg.tencent-cloud.cn/raw/fa0807a0556b373f0bac950fdba3978a.png)
**参数说明：**
 - 密钥类型：000-KEK/ZMK。
 - 算法标识：R - 16字节 SM4。
 - 成份数目：以 2 个成份为例，可根据实际需求填写。
 - 密钥索引[1-2048]：1。
 - 密钥标签[0-16个字符]：根据实际需求填写。
4. 在成份合成密钥弹窗中，分别两次填写成份值，单击**完成**合成密钥成功，弹出“合成密钥成功”对话框。
![](https://qcloudimg.tencent-cloud.cn/raw/9c72eb1b9f744c7cf8b6a444db23582a.png)
