SSH 密钥允许您在您的电脑和腾讯 Git 代码托管（工蜂）之间建立一个安全连接。

### 生成 SSH 公钥
您可以按照如下命令生成 SSH Keys：
```
ssh-keygen -t rsa -C "您的账号ID@git.cloud.tencent.com"
```

然后按三次回车即可生成 SSH Key，并且会生成两个文件。其中 id_rsa.pub 文件中的内容便是公钥。
![img](https://mc.qcloudimg.com/static/img/173699ee233a1116418c44a6044989f9/2017-08-28_114043.png)
![img](https://mc.qcloudimg.com/static/img/171eecae63ecd839c349bca6d682952c/2017-08-28_114309.png)

>!以上操作以 Windows 平台为例，Linux 下命令不变，操作类似。

### 添加 SSH Keys
1. 在腾讯工蜂主页上单击【Profile Settings】。
![img](https://main.qcloudimg.com/raw/1ec1095347512f2ab9a6a297ddf0a3de.png)
2. 单击左边的【SSH Keys】，然后再单击【Add SSH Key】。
![img](https://main.qcloudimg.com/raw/46ef2e9f5063bb5e6a671bf473f6bd37.png)
3. 复制公钥后粘贴到【Key】中，命名【Title】，单击【Add key】即可。
![img](https://main.qcloudimg.com/raw/f797bf0b74a9acb21daa8ec165c12f65.png)
