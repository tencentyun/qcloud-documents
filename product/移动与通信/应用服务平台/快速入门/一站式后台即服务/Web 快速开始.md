## 准备工作

1. 拥有 [腾讯云账号](https://cloud.tencent.com/document/product/876/41391)。
2. **务必** [创建云开发环境](https://cloud.tencent.com/document/product/876/41391)，获得 **环境 ID**。
3. 安装 [Node.js](https://nodejs.org/en/)。
4. 安装 [Cloudbase CLI](https://cloud.tencent.com/document/product/876/41392)。
```sh
npm install -g @cloudbase/cli
```

<dx-alert infotype="explain" title="">
如果 `npm install -g @cloudbase/cli` 失败，您可能需要 [修改 npm 权限](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)，或者以系统管理员身份运行：
 ```sh
 sudo npm install -g @cloudbase/cli
 ```
</dx-alert>


## 步骤1：创建初始项目
<dx-tabs>
::: MacOS&nbsp;或&nbsp;Linux
使用命令行创建目录 `my-cloudbase-app`，和其下的两个文件。
```sh
mkdir my-cloudbase-app && cd my-cloudbase-app && touch index.html && touch cloudbaserc.json
```
该目录下存在两个文件：`index.html` 与 `cloudbaserc.json`：
```
├── cloudbaserc.json
└── index.html
```
:::
::: Windows
1. 创建 `my-cloudbase-app` 文件夹。
2. 在此文件夹下，创建两个空白文件 `index.html` 与 `cloudbaserc.json`。
:::
</dx-tabs>
 
 - 以下是 `index.html` 内容，我们尝试登录云开发，如果成功，那么产生一个弹窗：
<dx-codeblock>
:::  html
<html>
  <head>
    <meta charset="utf-8" />
    <script src="https://imgcache.qq.com/qcloud/cloudbase-js-sdk/1.5.0/cloudbase.full.js"></script>
    <script>
      const app = cloudbase.init({
        env: "您的环境ID" // 此处填入您的环境ID
      });
      app
        .auth()
        .anonymousAuthProvider()
        .signIn()
        .then(() => {
            alert("登录云开发成功！");
        });
    </script>
  </head>
  <body>
    Hello Cloudbase!
  </body>
</html>
:::
</dx-codeblock>

- 以下是 `cloudbaserc.json` 的内容：
<dx-codeblock>
:::  json
{
  "envId": "此处填入您的环境ID"
}
:::
</dx-codeblock>


## 步骤2：添加安全域名
登录 [云开发 CloudBase 控制台](https://console.cloud.tencent.com/tcb)，在 [安全配置](https://console.cloud.tencent.com/tcb/env/safety) 页面中，将域名添加到 Web 安全域名中。
>? 这里我们把 `localhost:5000` 加入到安全域名中，让此域名下的页面可以使用 SDK 访问云开发服务。

## 步骤3：开启匿名登录
请参考：[开启匿名登录授权](https://cloud.tencent.com/document/product/876/41729#step1)。

## 步骤4：开启本地开发环境
在项目根目录运行：
```sh
npx serve
```

即可打开一个本地静态服务器，然后访问 `http://localhost:5000`。

>? 如果 SDK 成功使用匿名身份登录，那么您应该可以看到一个弹窗。

登录成功后，便可以访问和使用云开发的各类资源，详情请参见 [Web SDK 文档](https://docs.cloudbase.net/api-reference/webv2/initialization)。

- [登录认证](https://docs.cloudbase.net/api-reference/webv2/authentication)
- [云函数](https://docs.cloudbase.net/api-reference/webv2/functions)
- [数据库](https://docs.cloudbase.net/api-reference/webv2/database)
- [文件存储](https://docs.cloudbase.net/api-reference/webv2/storage)

## 第 5 步（可选）：使用云开发部署静态页面
1. 开通 [静态网站服务](https://console.cloud.tencent.com/tcb/hosting)。
2. 在项目根目录下运行以下命令，上传网站文件：
<dx-codeblock>
:::  sh
cloudbase hosting deploy index.html
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
在运行 `cloudbase hosting deploy` 之前，请先登录命令行工具：
<dx-codeblock>
:::  sh
cloudbase login
:::
</dx-codeblock>
</dx-alert>
3. 使用 `_envId_-_instanceId_.tcloudbaseapp.com` 访问您的网站，其中 `envId` 与 `instanceId` 是您 CloudBase 环境的标识符。详情请参见 [静态网站托管](https://cloud.tencent.com/document/product/876/40270)。



## 查看更多示例

- [示例：登录与用户](https://tdemo-1258016615.tcloudbaseapp.com/auth/)
- [示例：云函数](https://tdemo-1258016615.tcloudbaseapp.com/functions/)
- [示例：云数据库](https://tdemo-1258016615.tcloudbaseapp.com/database/)
- [示例：云存储](https://tdemo-1258016615.tcloudbaseapp.com/storage/)
