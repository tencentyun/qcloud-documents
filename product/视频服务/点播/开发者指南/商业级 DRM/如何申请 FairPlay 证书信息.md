要使用苹果的 FairPlay DRM（FPS），您需要先向苹果申请获得 FPS 部署包。本文手把手教您如何获得 FPS 部署包，和以下关键信息：

- FPS 证书文件（.cer）
- 私钥文件（.pem）
- 私钥密码
- ASK（Application Secret Key）

## 第一步：获取 FairPlay Streaming Deployment Package

1. 访问 [苹果 FairPlay 页面](https://developer.apple.com/streaming/fps/)，单击页面底部链接 `Request FPS Deployment Package` 后，您将看到一个表单页面。

>! 您需要拥有一个苹果开发者账号，成功登录后才能看到表单。
>![image-20220426181021189](https://qcloudimg.tencent-cloud.cn/raw/c8533ed9e4cf2b7961058eb9e5cd502a.png)

2. 填写页面申请表单，提交后等待苹果公司审批。

![image-20220426181021190](https://qcloudimg.tencent-cloud.cn/raw/5f905c0a865990ba4f1705fabdcdd652.png)

3. 当苹果公司通过申请后，您将得到一个 `FPS_Deployment_Package.zip` 压缩包 。

   > ? 在申请过程中，您将会被询问是否已完成密钥服务器模块（KSM）的实现和测试，对此可以回答： 
   >
   > ```
   > I am using a 3rd party DRM company and the company has already built and tested KSM
   > ```

## 第二步：创建私钥和证书签名请求（CSR，Certificate Signing Request）

解压 `FPS_Deployment_Package.zip` ，根据解压后的说明文档（.pdf），创建受密码保护的私钥以及证书签名请求（CSR）。

> !  需在执行下述过程的 PC 或服务器环境上安装 OpenSSL。 

1. 创建私钥文件（`privatekey.pem`），执行以下命令：

   ```shell
   openssl genrsa -aes256 -out privatekey.pem 2048
   ```

   在创建过程中，需要指定私钥密码，务必将私钥密码记录下来，后续步骤需要使用到。另外，建议私钥密码不要超过32个字符。

   ![image-20220421115813168](https://qcloudimg.tencent-cloud.cn/raw/c820dd647fb46eb6bbb57733f227b140.png)

2. 创建证书签名请求（`certreq.csr`），执行以下命令：

   ```shell
   openssl req -new -sha1 -key privatekey.pem -out certreq.csr -subj "/CN=SubjectName/OU=OrganizationalUnit/O=Organization/C=US"
   ```

   在创建过程中，需要输入在创建私钥文件时指定的私钥密码。

   ![image-20220421115929084](https://qcloudimg.tencent-cloud.cn/raw/25c7097a4633a2429b0f7173c0f255b6.png)

## 第三步：生成 FPS 证书（FairPlay Streaming Certificate）

访问 [苹果开发者页面](https://developer.apple.com/account)，获取 FPS 证书和 ASK。

1. 访问到 [苹果开发者页面](https://developer.apple.com/account)，单击左侧导航栏 `Certificates, Identifiers & Profiles`

   ![image-20220419113745847](https://qcloudimg.tencent-cloud.cn/raw/29e8bb1b63a60c877f17dd0c39d9e8d5.png)

2. 单击页面中的`+`按钮。

   ![image-20220419113637808](https://qcloudimg.tencent-cloud.cn/raw/4b88b93e4450b7171f09a3b75e2cb2bc.png)

3. 选择页面中的 `FairPlay Streaming Certificate` 选项，并单击 `Continue` 按钮。

   ![image-20220419114215512](https://qcloudimg.tencent-cloud.cn/raw/00fa1494b1256c9b4e1d769356450721.png)

4. 单击页面中的 `Choose File`按钮，选择在上一步中创建的 `certreq` 文件，并单击 `Continue` 按钮。

   ![image-20220419114506263](https://qcloudimg.tencent-cloud.cn/raw/52c2834bf36f4074e7f9f731aefc8948.png)

5. 将页面中的 `Application Secret Key (ASK)`  拷贝并备份，接着将 `ASK` 在下方输入栏中重新输入，并单击 `Continue ` 按钮。

   ![image-20220419114920781](https://qcloudimg.tencent-cloud.cn/raw/8e55fb6e817a2279f6b2cea3418506f7.png)

6. 上一步结束后，会出现一个弹框，让您再次确认是否已将 `ASK` 备份，确认已备份后，单击 `Generate` 按钮。

   >! 请务必确认已将 ASK 备份，此步骤完成后将无法再次查询 ASK。
   >![image-20220419115103618](https://qcloudimg.tencent-cloud.cn/raw/808347b36d824de46b6cbb84654d20c8.png)

7. 当以上步骤完成后，证书列表页面中将出现刚才所创建的 FPS 证书，并且证书类型为 `FairPlay Streaming`。

   ![image-20220419115340087](https://qcloudimg.tencent-cloud.cn/raw/ee831cfc5c26f37bdc09c9a50bab5ef5.png)

8. 单击 `Download` 按钮下载 FPS 证书（`fairplay.cer`）

   ![image-20220419115536031](https://qcloudimg.tencent-cloud.cn/raw/d7e7ad03c0168b61db084cfee762f6cc.png)

## 总结

至此，您已经完成了 `FairPlay` 证书信息的申请。
