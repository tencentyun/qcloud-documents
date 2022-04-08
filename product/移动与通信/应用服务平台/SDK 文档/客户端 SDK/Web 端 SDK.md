`@cloudbase/js-sdk` 能让您可以在 Web 端（例如 PC Web 页面、微信公众平台 H5 等）使用 JavaScript 访问 Cloudbase 服务和资源。

## 安装

### 方式一：通过包管理器引入

```bash
#npm
npm install @cloudbase/js-sdk -S
# yarn
yarn add @cloudbase/js-sdk
```

### 方式二：通过 CDN 引入

通过 CDN 引入有两种方式：
<dx-codeblock>
:::  引入全量&nbsp;SDK
<script src="//imgcache.qq.com/qcloud/cloudbase-js-sdk/${version}/cloudbase.full.js"></script>
<script>
  const app = cloudbase.init({
    env: "your-env-id"
  });
</script>
:::
:::  按需引入功能模块
<!-- 内核 -->
<script src="//imgcache.qq.com/qcloud/cloudbase-js-sdk/${version}/cloudbase.js"></script>
<!-- 登录模块 -->
<script src="//imgcache.qq.com/qcloud/cloudbase-js-sdk/${version}/cloudbase.auth.js"></script>
<!-- 云函数模块 -->
<script src="//imgcache.qq.com/qcloud/cloudbase-js-sdk/${version}/cloudbase.functions.js"></script>
<!-- 云存储模块 -->
<script src="//imgcache.qq.com/qcloud/cloudbase-js-sdk/${version}/cloudbase.storage.js"></script>
<!-- 云数据库模块 -->
<script src="//imgcache.qq.com/qcloud/cloudbase-js-sdk/${version}/cloudbase.database.js"></script>
<!-- 实时推送模块，引入前必须首先引入云数据库模块 -->
<script src="//imgcache.qq.com/qcloud/cloudbase-js-sdk/${version}/cloudbase.realtime.js"></script>
<!-- 广告上报模块-->
<script src="//imgcache.qq.com/qcloud/cloudbase-js-sdk/${version}/cloudbase.analytics.js"></script>
<script>
  const app = cloudbase.init({
    env: "your-env-id"
  });
</script>
:::
</dx-codeblock>

>? 功能模块必须在内核之后引入，并且登录模块必须引入。


最新的版本号 version 可以前往 [NPM](https://www.npmjs.com/package/@cloudbase/js-sdk) 查看。


## 开发文档

- [初始化](https://docs.cloudbase.net/api-reference/webv2/initialization)

- [登录认证](https://docs.cloudbase.net/api-reference/webv2/authentication)

- [云函数](https://docs.cloudbase.net/api-reference/webv2/functions)

- [数据库](https://docs.cloudbase.net/api-reference/webv2/database)

- [文件存储](https://docs.cloudbase.net/api-reference/webv2/storage)

- [跨端开发](https://docs.cloudbase.net/api-reference/webv2/adapter)

>? 新版 JavaScript SDK 已更名 `@cloudbase/js-sdk`，旧版本 `tcb-js-sdk` 未来不再更新，详情请参见 [迁移指南](https://docs.cloudbase.net/api-reference/webv2/migrating)。


