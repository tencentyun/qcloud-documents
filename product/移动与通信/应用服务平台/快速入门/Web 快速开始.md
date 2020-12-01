## 准备工作

1. [注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985)；
2. **务必** [创建云开发环境](https://cloud.tencent.com/document/product/876/41391)，获得 **环境 ID**；
3. 安装 [Node.js](https://nodejs.org/en/)；
4. 安装 [Cloudbase CLI](https://cloud.tencent.com/document/product/876/41539#.E5.AE.89.E8.A3.85-cloudbase-cli)。
```sh
npm install -g @cloudbase/cli
```

>? 如果 `npm install -g @cloudbase/cli` 失败，您可能需要 [修改 npm 权限](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)，或者以系统管理员身份运行：
> 
> ```sh
> sudo npm install -g @cloudbase/cli
> ```
> 

## 第 1 步：创建初始项目

**"MacOS 或 Linux"**

使用命令行创建目录 my-cloudbase-app，和其下的两个文件。

```shell
mkdir my-cloudbase-app && cd my-cloudbase-app && touch index.html && touch cloudbaserc.json
```

该目录下存在两个文件：`index.html` 与 `cloudbaserc.json`

```
├── cloudbaserc.json
└── index.html
```

**Windows**

1. 创建 `my-cloudbase-app` 文件夹。
2. 在此文件夹下，创建两个空白文件 `index.html` 与 `cloudbaserc.json`。

以下是 `index.html` 内容，我们尝试登录云开发，如果成功，那么产生一个弹窗：

```html
<html>
  <head>
    <script src="https://imgcache.qq.com/qcloud/tcbjs/1.3.5/tcb.js"></script>
    <script>
      const app = tcb.init({
        env: "您的环境ID" // 此处填入您的环境ID
      });
      app
        .auth()
        .signInAnonymously()
        .then(() => {
          alert("登录云开发成功！");
        });
    </script>
  </head>
  <body>
    Hello Cloudbase!
  </body>
</html>
```

以下是 `cloudbaserc.json` 的内容：

```json
{
  "envId": "此处填入您的环境ID"
}
```

## 第 2 步：添加安全域名

1. 登录腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb)，单击已创建的环境，进入环境页面。
2. 选择左侧菜单栏【环境】>【安全配置】，进入安全配置页面。
3. 单击【添加域名】，将域名添加到【WEB 安全域名】。
![](https://main.qcloudimg.com/raw/41f33bb17b5f809bc596c04cb042a2d5.jpg)
>? 这里我们将 `localhost:5000` 加入到安全域名中，让此域名下的页面可以使用 SDK 访问云开发服务。

## 第 3 步：开启匿名登录

请参见 [开启匿名登录授权](https://cloud.tencent.com/document/product/876/41729#.E5.BC.80.E5.90.AF.E5.8C.BF.E5.90.8D.E7.99.BB.E5.BD.95.E6.8E.88.E6.9D.83) 文档。

## 第 4 步：开启本地开发环境

在项目根目录运行：

```plaintext
npx serve
```

即可打开一个本地静态服务器，然后访问 `http://localhost:5000`。

>? 如果 SDK 成功使用匿名身份登录，那么您应该可以看到一个弹窗。

登录成功后，便可以访问和使用云开发的各类资源，详情请参见 [Web SDK 文档](https://docs.cloudbase.net/api-reference/web/authentication.html)。

- [登录认证](https://docs.cloudbase.net/api-reference/web/authentication.html)
- [云函数](https://docs.cloudbase.net/api-reference/web/functions.html)
- [数据库](https://docs.cloudbase.net/api-reference/web/database.html)
- [文件存储](https://docs.cloudbase.net/api-reference/web/storage.html)

## 第 5 步（可选）：使用云开发部署静态页面

1. 开通 [静态网站服务](https://console.cloud.tencent.com/tcb/hosting)。
2. 在项目根目录下运行以下命令，上传网站文件：
```plaintext
cloudbase hosting:deploy index.html
```
>? 在运行 `cloudbase hosting:deploy` 之前，请先登录命令行工具：
> 
> ```sh
> cloudbase login
> ```
3. 使用 `_envId_.tcloudbaseapp.com` 访问您的网站。详情请参见 [静态网站托管](https://cloud.tencent.com/document/product/876/40270) 相关文档。
