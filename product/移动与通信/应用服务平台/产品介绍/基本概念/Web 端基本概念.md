
云开发为开发者提供的一站式后端云服务，可在需依赖后端服务的应用上使用云开发能力；云开发同样适用于网站开发。
Web 端是云开发中针对网站应用的统称，包含以下几个场景：
1. 普通网站应用（PC 端）。
2. 移动页面或者 H5 网页。
3. 公众号网页。



通过云开发支持网站应用开发，在支持的登录鉴权授权内，既微信登录方式、匿名登录方式、自定义登录方式（可对接任何第三方登录体系）下进行应用的访问授权，开发者若要开发网站应用，可根据需要选择不同的登录方式，可参考 [登录授权](https://cloud.tencent.com/document/product/876/41728)。

利用云开发的 Web 端能力进行开发时，主要有以下几个依赖概念：
- 应用关联，使应用可以正常使用云开发资源。
- 用户登录授权，在网站应用中接入登录方式。
- 域名授权，保障应用的来源安全。

### 应用关联
要使用云开发提供的云函数、云存储和云数据库的功能，需要先将云开发添加到网站应用中，即**应用关联。**
通过获取云开发提供的 Web 端 SDK 并关联到网站应用，才能操作后台资源，复制下方的代码片段，将其粘贴到 HTML 代码底部、其他 script 标记之前，即可将云开发添加至您的网站应用，示例：

```
<script src="https://imgcache.qq.com/qcloud/tcbjs/1.3.8/tcb.js"></script>
<script>
  var app = tcb.init({
    env: 'test1-1f2e36'
  })
</script>
```

其中 `https://imgcache.qq.com/qcloud/tcbjs/1.3.8/tcb.js` 中有版本信息，可根据需要获取 SDK 的版本：

**方式一：通过 npm 包**

通过 npm 包获取 tcb-js-sdk的版本，详细可参考 [npm tcb sdk包](https://www.npmjs.com/package/tcb-js-sdk)，如下：

![](https://main.qcloudimg.com/raw/5aaf5f8036cede5d75b3888391dbf734.jpg)


**方式二：通过 npm 安装后获取版本**

执行命令

```
# npm
npm install tcb-js-sdk -S

# info 
npm info tcb-js-sdk
```

打印结果后，可看到版本号。
![](https://main.qcloudimg.com/raw/59955c57dd8c259921106bbb562682c5.jpg)


### 登录授权
云开发的 Web 端开发支持的登录鉴权方式有：
1. 自定义登录授权。
2. 微信登录授权。
3. 匿名登录授权。

>!如果需要用到微信登录授权，开发者需要把网站应用注册到微信平台后，同时在腾讯云云开发控制台进行授权设置，即可接入微信登录方式。

微信开放平台授权方式请参考 [微信平台授权](https://open.weixin.qq.com/cgi-bin/frame?t=home/web_tmpl&lang=zh_CN)。
开发者可根据不同业务场景使用不同的登录方式，详细的登录授权方式可参考 [登录授权](https://cloud.tencent.com/document/product/876/41728)。


### 域名授权

云开发只允许授权过的域名下的页面使用 SDK 发起对发起的访问，开发者可自行添加安全来源的网站，将需设置的网站域名添加到安全验证的白名单中即可完成。
操作方式：登录 [云开发控制台](https://console.cloud.tencent.com/tcb/user) ，在 用户管理 > 登录设置 中添加授权域名。

>!若只添加域名安全白名单而不选定的登录方式作为鉴权，将无法正常使用客户端 SDK 调用资源，此两种安全校验需要搭配使用。

