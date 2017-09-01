SSH密钥允许您在您的电脑和GitLab之间建立一个安全连接。

### 1. 生成SSH公钥
您可以按照如下命令生成SSH Keys：
```
ssh-keygen -t rsa -C "您的账号ID@git.cloud.tencent.com"
```
然后按三次回车即可生成SSH Key，并且会生成两个文件。其中id_rsa.pub文件中的内容便是公钥。
![](https://mc.qcloudimg.com/static/img/173699ee233a1116418c44a6044989f9/2017-08-28_114043.png)
![](https://mc.qcloudimg.com/static/img/171eecae63ecd839c349bca6d682952c/2017-08-28_114309.png)

> 以上操作在Windows平台下进行，Linux下命令不变，操作类似。

### 2. 添加SSH Keys
1. 首先，在TGit主页面里点击Profile Setting。
![](https://mc.qcloudimg.com/static/img/5522c138370e7c60d07018c345be3177/image.png)

2. 点击左边的SSH Keys，然后在点击Add SSH key。
![](https://mc.qcloudimg.com/static/img/b6df9f8393daac0b65a32e8c37ac2140/2017-08-28_140330.png)

3. 填写好Key和Title， 点击“Add key”按钮即可。
![](https://mc.qcloudimg.com/static/img/bd256c462aa81aa43a43627b12bdb26c/2017-08-28_114606.png)
