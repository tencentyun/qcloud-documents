## 简介
本实践将引导您在使用腾讯云对象存储 COS 上传对象时，借助无服务器云函数 SCF 实现自动刷新在 CDN 上指定的缓存文件，让其自动获取到更新后的资源。

>!使用此功能将遵循 CDN 相关 API 调用次数的限制，详情请查阅 [缓存刷新](https://cloud.tencent.com/document/product/228/6299#url-.E5.88.B7.E6.96.B0) 文档。

## 实践背景

当静态内容需要更新时，通常会往 COS 覆盖上传一个更新版本的资源或删除该资源。若您配置的 CDN 缓存过期时间较长，则 CDN 的某些边缘节点可能会仍然缓存旧资源。缓存过期时间太短，则会影响到加速的效果。具体详情请参见 [缓存过期配置](https://cloud.tencent.com/document/product/228/6290) 的相关信息。

根据上述情况，您需要使用 CDN 控制台上的 [缓存刷新](https://cloud.tencent.com/document/product/228/6299) 功能，对指定 URL 进行手动刷新操作，实现删除无效缓存文件或者更新资源。

本文将结合 COS 和 SCF 的功能特性，在 COS 文件更新时，实现自动刷新 CDN 缓存的效果。

## 准备工作

1. 腾讯云账户，需具备 COS、CDN、SCF 等产品的访问权限。
2. 创建存储桶，并在该存储桶上绑定了 CDN 加速域名。
3. 确保 COS 的存储桶的所属地域支持 SCF 产品功能，暂不支持跨地域调用。
4. 准备好可调用 CDN 刷新接口的云 API 密钥，以及下载 [SCF 刷新 CDN 示例代码](https://main.qcloudimg.com/raw/757b646eb68e9b9a5b2fc4bf0fed2492/scf_about_cdn_refresh.zip)。

## 实践步骤

> 本实践案例以 Node.js 语言示例代码为例。

### 1. 创建 SCF 函数
>!您创建的函数所属地域需与 COS 存储桶的地域保持一致。

1）登录 [SCF 控制台](https://console.cloud.tencent.com/scf/)，单击函数服务，选择与静态内容相同的地域并创建函数。如下图所示：
![](https://main.qcloudimg.com/raw/332edc2828575a4c802a9af9cb233b08.png)
2）在 “新建函数” 页面，选择 “空白函数”，输入函数名称（如 refresh_cdn），设置运行环境（示例代码使用 Node.js 语言，因此运行环境设置为  Nodejs 6.10）。确认配置无误后单击【完成】即可。如下图所示：
![](https://main.qcloudimg.com/raw/70e9dbae0471dd8cd50ffa724eb089f4.png)

### 2. 配置函数

空白函数创建完成后，需添加对应的函数代码，并设定触发方式，使函数可以正常工作。

#### 2.1 配置函数代码

1）下载  [SCF 刷新 CDN 示例代码](https://main.qcloudimg.com/raw/757b646eb68e9b9a5b2fc4bf0fed2492/scf_about_cdn_refresh.zip)。
2）解压所有文件，找到其中的 index.js 文件并打开。
3）在代码里修改替换成您的具备调用 CDN 刷新接口权限的 SecretId、SecretKey 和需要刷新的域名。如下图所示：
![](https://main.qcloudimg.com/raw/b2b0eba560e3229fc402490f0737712b.png)
4）如需调用刷新绑定在腾讯云海外 CDN 上的域名，请将代码中的 `RefreshCdnUrl` 修改为 `RefreshCdnOverSeaUrl`。

#### 2.2 上传函数代码

1）将修改好的代码和其他文件重新压缩打包为 zip 格式。
2）在 SCF 控制台中，选择 "函数代码" 页签，将 "提交方法" 设置为 "本地上传 zip 包"，并选择刚压缩的 zip 格式文件，单击【上传】。如下图所示：
![](https://main.qcloudimg.com/raw/9672da05b98748a5ef06da393ec64d04.png)

#### 2.3 添加触发方式

1）在 SCF 控制台中，选择 "触发方式" 页签，单击【添加触发方式】。
2）将 “触发方式” 设置为  "COS 触发"，并选择需刷新 COS 资源的存储桶。如下图所示：
![](https://main.qcloudimg.com/raw/8f3b5efab6a30b008fd1b8e12eafb1e0.png)
3）根据实际需求，设置事件类型。
- 如果您仅需要自动刷新 CDN 访问覆盖上传到 COS 的对象，则需将 "事件类型" 设置为 "文件上传"。
- 如果您同时需要对删除行为也进行自动刷新，则需再添加一种触发方式，并将 "事件类型" 设置为 "文件删除"。

4）勾选立即启用。
5）最后确认配置信息无误后，单击【保存】。

### 3. 测试
>!由于 CDN 是异步操作，查询操作时，请稍等片刻。

完成配置后，可在对应存储桶中上传一个新对象进行验证。
1）在 COS 控制台中，上传一个同名的更新文件。如下图所示：
具体操作请查阅 [上传对象](https://cloud.tencent.com/document/product/436/13321) 文档。
![](https://main.qcloudimg.com/raw/66ba3a7ea298f2f4e240f76ebe76df03.png)
2）完成上传后，即可在 SCF 控制台的 "运行日志" 查询到调用成功的日志。如下图所示：
![](https://main.qcloudimg.com/raw/99b84dec0d0d3599fbffecef2d8e4d95.png)
3）在 CDN 控制台的 “缓存刷新 - 操作记录” 中，可查询到自动调用刷新的记录。

4）以上测试通过后，即可访问 CDN 加速后的 URL 获取到最新的资源。
