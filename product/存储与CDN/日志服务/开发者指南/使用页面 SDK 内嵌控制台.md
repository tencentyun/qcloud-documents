## 操作场景

日志服务（Cloud Log Service，CLS）提供独立的检索、仪表盘页面的 SDK 嵌入。相比较直接 iframe 嵌入控制台，iframe 嵌入控制台 SDK 页面更独立，不会出现登录态挤压问题，资源权限控制可以自定义控制，而 iframe 直接嵌入控制台的权限完全跟随角色，无法自定义控制。对于权限敏感，且对页面体验交互要求严格的用户，建议使用 SDK 方式嵌入。

| 嵌入方式      | 适用场景                                         | 
| ------------- | ------------------------------------------------ | 
| [控制台嵌入](https://cloud.tencent.com/document/product/614/45742)    | 实现免登录，无需资源权限控制、无严格交互体验要求 |
| SDK 嵌入 | 实现免登录，有资源权限控制、交互体验要求         |


## 场景示例

某统一运维运营门户，需要支持问题的一站化解决，因此集成 CLS 到指定菜单下。为保证体验性和权限管理，需要使用 SDK 嵌入。
<img src="https://qcloudimg.tencent-cloud.cn/raw/17480a26edf6cbafbcb9a40543d16e1e.png" style="width: 48%;" />

## 示例分析

该运维平台需要在可观测菜单下内嵌 CLS 日志检索页面，同时实现选择左侧服务列表中的某一个服务后，显示对应的日志主题。运维平台通过控制用户的服务可用权限，就能同时控制用户的日志主题可用权限。

![](https://qcloudimg.tencent-cloud.cn/raw/78cac68ce446e4db51a69d1c31ae0d91.png)

为达成业务对权限管控和页面集成的相关诉求，需要进行前端页面嵌入和后端接入层转发逻辑的开发工作，详情请参考 [独立运行环境接入文档](https://github.com/TencentCloud/cls-console-sdk/blob/main/sdk-modules/定制化开发.md)。

<img src="https://qcloudimg.tencent-cloud.cn/raw/ebd24648ac6eee89866b2355e352f0d3.png" style="width: 50%;" />

## 操作步骤

### 步骤1：获取页面 SDK

从 Github [cls-console-sdk](https://github.com/TencentCloud/cls-console-sdk) 下载源代码到本地。

本项目是基于 `sdk-modules` 文件夹，实现的**独立运行环境**快速体验样例。允许业务方将 CLS 控制台集成到自身页面，使用检索分析页面和仪表盘能力。


### 步骤2：部署页面 SDK

1. 在源代码下创建`./capi-forward/.env` 文件，填写 [密钥信息](https://console.cloud.tencent.com/cam/capi) 和环境密码。
```
# 环境变量区分大小写。secretId长度为36位，secretKey长度为32位。
secretId=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
secretKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 设置后支持密码鉴权，不设置则无任何鉴权
demoPassword=123456
```
2. 根据实际需求，进行项目部署。
<dx-tabs>
::: 容器化部署
1. 执行如下命令，构建最新镜像版本。
```
docker build . --tag=cls_web
```
2. 执行如下命令，运行容器。
```
docker run --env-file ./capi-forward/.env -p 3001:3001 cls_web
```
:::
::: Node.js 部署
1. 安装 pnpm，详情请参考  [安装](https://pnpm.io/zh/installation) 文档。
>? 如已安装 pnpm，请跳过此步骤。
>
2. 在项目根目录，执行如下命令，安装依赖。
```
pnpm recursive install --frozen-lockfile=true
```
>? 如遇到安装出错，请在项目根目录执行 `find . -name "node_modules" -type d -exec rm -rf '{}' +` 命令后再重新安装。
>
3. 在项目根目录，执行如下命令，完成项目构建。
```
npm run build
```
4. 在项目根目录，执行如下命令，启动项目。
```
npm run serve
```
>! 修改代码后需要重新进行构建。
>

:::
</dx-tabs>

### 步骤3：使用页面 SDK

<dx-tabs>
::: 通过浏览器访问
完成项目运行后，可在浏览器中打开相应页面。
```
# 检索分析页面：将以下网址中的 ${Region} 和 ${TopicId}，替换为对应的地域和日志主题ID，即可访问。${Query}为检索语句，可以为空。
http://localhost:3001/cls/search?region=${Region}&topic_id=${TopicId}&query=${Query}&time=now-h,now

# 检索分析页面: 将以下网址中的 ${Region} ${logset_name} ${topic_name}，替换为对应的地域、日志集名称、日志主题名称，即可访问。
http://localhost:3001/cls/search?region=${Region}&topic_name=${TopicName}&logset_name=${LogsetName}

# 仪表盘页面：将以下网址中的 ${dashboardId} 替换为仪表盘ID，即可访问。
http://localhost:3001/cls/dashboard/d?id=${dashboardId}&time=now-7d,now
```
地域参数格式为`ap-shanghai`, 检索页面参数设置请参考 [检索页面参数设置](https://cloud.tencent.com/document/product/614/39331) 文档。
:::
::: 通过 iframe 内嵌使用
在业务内部系统中，直接将此 SDK 控制台页面，作为 iframe 嵌入，通过路由参数完成与其他页面的结合。
```
// 一个快速查看效果的样例，请根据自身业务进行调整
function prepareSdkFrame(url) {
   var ifrm = document.createElement("iframe");
   ifrm.setAttribute("src", url);
   ifrm.style.width = "1280px";
   ifrm.style.height = "960px";
   document.body.appendChild(ifrm);
}
const url = 'http://localhost:3001/cls/search?region=${Region}&topic_id=${TopicId}&query=${Query}&time=now-h,now'

prepareSdkFrame(url)
```

:::
</dx-tabs>

