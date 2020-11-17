SSH 密钥允许您在您的电脑和腾讯 Git 代码托管（工蜂）之间建立一个安全连接。

## 生成 SSH 公钥
您可以按照如下命令生成 SSH Keys：

```
ssh-keygen -t rsa -C "您的账号ID@git.code.tencent.com"
```

然后按三次回车即可生成 SSH Key，并且会生成两个文件。其中 id_rsa.pub 文件中的内容便是公钥。
![img](https://mc.qcloudimg.com/static/img/173699ee233a1116418c44a6044989f9/2017-08-28_114043.png)
![img](https://mc.qcloudimg.com/static/img/171eecae63ecd839c349bca6d682952c/2017-08-28_114309.png)

>!以上操作以 Windows 平台为例，Linux 下命令不变，操作类似。

## 添加 SSH Keys
1. 在腾讯工蜂主页上单击【个人设置】。
![img](https://main.qcloudimg.com/raw/e583fd886f24288e341a126299e7b07b.png)
2. 单击左边的【SSH 密钥】，然后再单击【添加 SSH 密钥】。
![img](https://main.qcloudimg.com/raw/ed0745ab6971117ef4b012cfef44a69b.png)
3. 复制公钥后粘贴到【Key】中，命名【Title】， 单击【Add key】即可。
![img](https://main.qcloudimg.com/raw/214bb0b888efd9bcffeeb2a94f2ff945.png)
