## 简介

内容审核功能提供了自动冻结能力，可以将违规文件自动进行冻结处理。但由于冻结只会处理对象存储（Cloud Object Storage，COS）源站的数据，对于使用了 CDN 场景的用户，CDN 上的缓存无法在第一时间处理。

本文提供了一种通过云函数和 API 网关处理的方式，帮助用户解决 CDN 缓存无法及时冻结的问题。

## 操作步骤

1. 登录 [腾讯云云函数控制台](https://console.cloud.tencent.com/scf/list)，在**函数服务**页面，单击**新建**创建云函数。
2. 选择**从头开始**，并填写以下基础配置：
![img](https://qcloudimg.tencent-cloud.cn/raw/81535c1df37fd6a73e2504656b8c8940.png)
 - 函数类型：选择“事件函数”。
 - 函数名称：自定义一个函数名称。
 - 地域：选择您使用了审核功能的存储桶所在的地域。
 - 运行环境 选择“Python2.7”。
3. 函数代码按下述配置：
 - 提交方法：选择“本地上传 zip 包”或者“通过 cos 上传 zip 包”，zip 包可 [单击此处](https://cos5.cloud.tencent.com/cosbrowser/code/scf/cos_audit_cdn_refresh.zip) 进行下载。
 - 执行方法：填 index.main_handler。
4. 单击**高级配置**，配置**环境配置**，其中除环境变量外，其余配置可自行按需修改。
 - 资源类型：CPU
 - 内存：512MB
 - 初始化超时时间：65
 - 执行超时时间：30
 - 环境变量：
    - CI_AUDITING_CALLBACK：回调地址，这里填原本在内容审核的回调设置中的地址，设置回调地址则会进行回调，不设置不回调。
    - CDN_URL：CDN 地址，必选，设置 CDN 地址以刷新 CDN 缓存。
    - REGION：地域，必选，设置为 bucket 所在地域。
    - BUCKET_ID：存储桶 ID（即存储桶名称），必选，设置为存储桶 ID。存储桶 ID 用于查询图片样式，填写错误会导致样式查询出错。
    - IMAGE_STYLE_SEPARATORS：图片的样式分隔符，如果需要为图片刷新样式，则需要设置这个变量，多个分割符则连续写，不需要隔开。
    - CDN_REFRESH_TYPE：图片对象缓存刷新方式，默认为按 url 刷新，仅刷新样式，如设置为“path”，则会刷新按图片处理参数访问的缓存。注意，path 方式刷新会去除包含此文件名的更长的文件名的文件，请谨慎使用。
以上环境变量请确认正确填写，以确保缓存刷新符合预期，示例如下：
![img](https://qcloudimg.tencent-cloud.cn/raw/46dd95ef2105e62c2f68b7178b376524.png)
5. 权限配置勾选“运行角色”，单击**新建运行角色**，跳转到“新建自定义角色”页面。
6. 角色载体选择“云函数(scf)”，单击**下一步**。
![img](https://qcloudimg.tencent-cloud.cn/raw/845d7c142b0504c49f677564bc35294e.png)
7. 配置角色策略，选择 QcloudCDNFullAccess 和 QcloudCIReadOnlyAccess，单击**下一步**。
8. 为角色命名后，单击**完成**。
9. 自定义角色创建完毕后，回到云函数创建页面，刷新角色下拉表，选择刚才新建的角色。
10. 上述步骤完成后，单击**完成**，创建云函数。
11. 再进入 [API 网关控制台](https://console.cloud.tencent.com/apigateway/service)，开通 API 网关服务。
12. 您可以参考 [创建后端对接云函数 SCF 的 API](https://cloud.tencent.com/document/product/628/52201) 完成创建。
13. 在发布环境选择“发布”，然后单击“发布服务”。
14. 在数据万象“内容审核”页面，为图片或其他目标类型设置回调参数，回调 URL 设置为上一步创建的 API 网关的地址。
15. 回调设置完成后，CDN 上的资源将会自动根据审核回调结果进行缓存刷新。
