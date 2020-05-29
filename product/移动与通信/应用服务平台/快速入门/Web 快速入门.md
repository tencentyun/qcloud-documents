本文主要介绍如何从零开始创建一个 Web 项目并开启本地开发环境。

### 准备工作
1. 注册 [腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2Fproduct%2Flvb)，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 参考 [开通环境](https://cloud.tencent.com/document/product/876/41391) 创建云开发环境，获得 环境 ID。
3. 参考 [Node.js 官网](https://nodejs.org/en/) 下载安装 Node.js。
4. 参考 [安装 CLI 工具](https://cloud.tencent.com/document/product/876/41392)  安装 Cloudbase CLI。

### 步骤1： 创建初始项目

#### MacOS或Linux

使用命令行创建目录 my-cloudbase-app，和其下的两个文件。

```shell
mkdir my-cloudbase-app && cd my-cloudbase-app && touch index.html && touch cloudbaserc.json
```

该目录下存在两个文件：`index.html` 与 `cloudbaserc.json`

```
├── cloudbaserc.json
└── index.html
```

#### Windows

1. 创建 `my-cloudbase-app` 文件夹
2. 在此文件夹下，创建两个空白文件 `index.html` 与 `cloudbaserc.json`

#### 填充文件内容

以下是 index.html 内容，我们尝试登录云开发，如果成功，那么产生一个弹窗：
```
<html>
  <head>
    <script src="https://imgcache.qq.com/qcloud/tcbjs/1.3.5/tcb.js"></script>
    <script>
      const app = tcb.init({
        env: '您的环境ID'  // 此处填入您的环境ID
      });
      app.auth().signInAnonymously().then(() => {
        alert('登录云开发成功！')
      });
    </script>
  </head>
  <body>
    Hello Cloudbase!
  </body>
</html>
```
以下是 cloudbaserc.json 的内容：
```
{
    "envId": "此处填入您的环境ID"
}

```




### 步骤2： 添加安全域名
登录腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb)，单击需要配置的环境，选择左侧菜单栏【环境】>【环境设置】，单击【安全配置】，将域名添加到【Web安全域名】中。
例如：把 `localhost:5000` 加入到安全域名中，让此域名下的页面可以使用 SDK 访问云开发服务。

![](https://main.qcloudimg.com/raw/0ef6eeaccb59ae6091081c7e2dd4f6e5.png)


### 步骤3：开启匿名登录
开启匿名登录操作请参考登录授权 - [匿名登录](https://cloud.tencent.com/document/product/876/41729) 文档。


### 步骤4： 开启本地开发环境
在项目根目录运行：
```
$ npx serve
```
即可打开一个本地静态服务器，然后访问：http://localhost:5000。如果 SDK 成功使用匿名身份登录，那么您应该可以看到一个弹窗。

登录成功后，便可以访问和使用云开发的各类资源，详情请参阅 Web SDK 文档：

- [登录授权](https://cloud.tencent.com/document/product/876/34660)。
- [云函数](https://cloud.tencent.com/document/product/876/34661)。
- [数据库](https://cloud.tencent.com/document/product/876/34662)。
- [文件存储](https://cloud.tencent.com/document/product/876/34663)。

### 步骤5：使用云开发部署静态页面
1. 登录腾讯云云开发控制台，开通 [静态网站服务](https://console.cloud.tencent.com/tcb/hosting)。
2. 在项目根目录下运行：
```
cloudbase hosting:deploy
```
命令上传网站文件（如 html/css/图片等）。

3. 使用 envId.tcloudbaseapp.com 访问您的网站。
详情请参考 [静态网站托管](https://cloud.tencent.com/document/product/876/40271) 相关文档
