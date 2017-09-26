SSH 密钥允许您在您的电脑和 GitLab 之间建立一个安全连接。

### 生成 SSH 公钥
您可以按照如下命令生成 SSH Keys：
```
ssh-keygen -t rsa -C "您的账号ID@git.cloud.tencent.com"
```
然后按三次回车即可生成 SSH Key，并且会生成两个文件。其中 id_rsa.pub 文件中的内容便是公钥。
![](https://mc.qcloudimg.com/static/img/173699ee233a1116418c44a6044989f9/2017-08-28_114043.png)
![](https://mc.qcloudimg.com/static/img/171eecae63ecd839c349bca6d682952c/2017-08-28_114309.png)

> 注意：
> 以上操作以 Windows 平台为例，Linux 下命令不变，操作类似。

### 添加 SSH Keys
1. 在 TGit 主页上单击【Profile Settings】。
![](https://mc.qcloudimg.com/static/img/5522c138370e7c60d07018c345be3177/image.png)

2. 单击左边的【SSH Keys】，然后再单击【Add SSH Key】。
![](https://mc.qcloudimg.com/static/img/b6df9f8393daac0b65a32e8c37ac2140/2017-08-28_140330.png)

3. 复制公钥后粘贴到【Key】中，命名【Title】， 单击【Add key】按钮即可。
![](https://mc.qcloudimg.com/static/img/bd256c462aa81aa43a43627b12bdb26c/2017-08-28_114606.png)
