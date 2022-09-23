
## 生成 CSR 文件

生成 Certificate Signing Request(CSR)：
 <img src="//main.qcloudimg.com/raw/76c59ee727f1147693f6da95bc1db070.png" width=640 />
 
填写您的邮箱（这个邮箱是申请 AppID 的付费帐号）和常用名称（一般默认是计算机名，不用更改），并选择保存到硬盘：
 <img src="//main.qcloudimg.com/raw/12c80d3cb45d44e6b9fb8f63bc616347.png" width=640 />
 
单击继续： 
 <img src="//main.qcloudimg.com/raw/b393d5662e94646b24aa14979c17b3c3.png" width=640 />
 
 已经在本地生成了一个 TXIMDemoAPS.certSigningRequest 的 CSR 文件。

## 生成 App ID

登录 developer.apple.com，选择 Member Center ：
<img src="//main.qcloudimg.com/raw/d39160bb0713cd67fd78377328c3928a.png" width=640 />

进入后选择 Certificates，Identifiers & Profiles：
<img src="//main.qcloudimg.com/raw/4f6fb2c58856d47a3fdce33d0b446bc1.png" width=640 />

再选择 Identifiers 进行到 Identifiers 管理页：
<img src="//main.qcloudimg.com/raw/bfbe4ef16748542215a203268395638f.png" width=640 />

生成 App ID：
Identifiers 的右侧列表中，如果您已经配置您的应用，跳到第3步，否则单击“+”号添加 App ID。
<img src="//main.qcloudimg.com/raw/8c18cf7548705e9557f77fb76637a465.png" width=640 />

输入您的 App ID 描述信息，可以输入工程名；Bunble ID（在工程的 General 信息中），一般格式为 com.youcompany.youprojname，选择需要支持 Push Notification，Continue：
<img src="//main.qcloudimg.com/raw/dca8a2cda77581eeeda92882fce90119.png" width=640 />

Submit 提交：
<img src="//main.qcloudimg.com/raw/b24c07c8ad8f70e4aa0eb878a8d8dfeb.png" width=640 />

## 创建 App 的 APS 证书

回到 App IDs 选择您需要推送的 App。展开单击“Edit”：
<img src="//main.qcloudimg.com/raw/11b2213530dc164d45f2da2293cce07f.png" width=640 />

找到最底部的 Push Notifications，单击“Create Cerifcate…”创建 push 证书，这里**开发环境的证书和发布环境的证书需要分别创建，也就是相同的流程要走两遍**：
<img src="//main.qcloudimg.com/raw/257aa0f4d8ebcb3ff3e2bb5f327a5edd.png" width=640 />

单击 Continue 继续：
<img src="//main.qcloudimg.com/raw/359899fa7fead219335499a42ca01a82.png" width=640 />

上传创建好 CSR 文件（参照第一节）xxx.certSigningRequest（例子为：TXIMDemoAPS.certSigningRequest），单击“Generate”：
<img src="//main.qcloudimg.com/raw/5ce5ec899e22ee7361efdd3b052d70a6.png" width=640 />

aps 证书创建成功了，单击 Download 下载到本地。（文件名：开发版本为 aps_development.cer，发布版本为 aps.cer）：
<img src="//main.qcloudimg.com/raw/8949831833544f35b1eb8c749b420edf.png" width=640 />

单击 Done，您会发现该环境的 push 配置状态已经 Enabled：
<img src="//main.qcloudimg.com/raw/67910c40b8e8b84ba81bd6f84fe16a58.jpg" width=640 />

注意：有的 App ID 的 Apple Push Notification service 列是灰色的，并且不允许使用 Configure 按钮，这是因为 APNS 不支持带通配符的 App ID。

## 生成 Push 证书

导入证书
双击上一节下载的文件（aps_development.cer 和 aps.cer）将其安装到电脑，在“钥匙串访问”中，可以看到已经导入的证书。
<img src="//main.qcloudimg.com/raw/51b99080f9f479319ee6d742aedd3a3a.png" width=640 />

右键选择导出为 p12 文件, （例：存储为 TXIMDemoAPS.p12）：
<img src="//main.qcloudimg.com/raw/af2ead9db94586c2e18bf2b59b2151ec.png" width=640 />

注意：开发版本证书只有在 debug 模式下开发的时候会生效，正式发布版本的证书，一定要使用正式版本的证书。

## 生成 Provisioning Profile 文件（PP 文件）
生成对应的描述文件，这里演示开发版描述文件的创建（发布版本的创建流程一样，用户可以自行操作），单击"Continue"
<img src="//main.qcloudimg.com/raw/6c4eff074f24e0ae1b3bb73dda9dea26.png" width=640 />

选择3.3步骤中创建推送证书那个 App ID，单击"Continue"，
<img src="//main.qcloudimg.com/raw/ec5fd56e7269a9f75299e636dd644d58.png" width=640 />

选择3.3中创建的开发版推送证书（创建发布版描述文件时，选择3.3中创建的发布版推送证书），单击"Continue"，
<img src="//main.qcloudimg.com/raw/12e2e9dd0820f4e7e7f5ee4f9580fb02.png" width=640 />

选择需要加入开发的设备，只有加入了的设备才能进行真机调试，创建发布版本时没有这个步骤，单击"Continue",
<img src="//main.qcloudimg.com/raw/10742a7703b04984bf94a1386a9642c9.png" width=640 />

输入 PP 文件的名称，这里以 IMDevPP 为例
<img src="//main.qcloudimg.com/raw/405ac56131c2c38d4f98cda13c5327e2.png" width=640 />

生成 PP 文件完成
<img src="//main.qcloudimg.com/raw/e21aca45d642de8050605073e9f3a942.png" width=640 />


注：以上所有的步骤，除了生成 p12 文件时必须要下载证书安装到本地，其它生成的文件都可以不下载到本地。

检查生成的 PP 文件
查看 pp 文件的状态一定要为 Active
<img src="//main.qcloudimg.com/raw/fe957f8e017d22e4e4812eea046e5e45.png" width=640 />

单击 PP 文件进入详细资料页面，状态也要是 Active
<img src="//main.qcloudimg.com/raw/20ec87d3caac9cb8d0119762e0d53da5.png" width=640 />

## Xcode 中的配置
新版 Xcode 已经不需要手动配置证书和描述文件了，只需在 General 中选择正确的 Team，Fix Issue 即可，这也是上面所说的不用下载证书到本地安装的原因
<img src="//main.qcloudimg.com/raw/22db4c59af9d26d562f916e87e10fbc2.png" width=640 />

