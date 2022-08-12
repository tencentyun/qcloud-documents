## 操作场景

本文介绍如何将 API 发布到 Kong 网关上，并实现 URL 重写。


## 前置条件
1. 已购买 Kong 网关实例，详情请参见 [网关实例管理](https://cloud.tencent.com/document/product/1364/72495)。
2. 进入 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)，并找到需要的实例。
3. 进入实例详情页后，在**配置管理**找到管理控制台的地址和访问方式。
<img src="https://qcloudimg.tencent-cloud.cn/raw/a02826888903fcff919d3f444b120241.jpg"> 
4. 访问 Konga 管理控制台。
<img src="https://qcloudimg.tencent-cloud.cn/raw/8390ff7dd93a80514c1096f5665cdd7f.jpg"> 

## 操作步骤

### 场景一：通过 Service 和 Route 配置实现 URL 前缀改写

<dx-alert infotype="explain" title="<b>示例：</b>">
原始 API 调用 URL 为 `http://<backend>/anything/api/<sub_path>` 
发布到 Kong 网关后，调用 URL 改写为 `http://<kong>/new/path/<sub_path>`
</dx-alert>

1. 单击 **ADD NEW SERVICE**创建 Service。
![](https://qcloudimg.tencent-cloud.cn/raw/80dac93dc57b6e4493dfbe52c7942dd8.jpg)
填写相应信息并设置 Path 为 `/anything/api`。
![](https://qcloudimg.tencent-cloud.cn/raw/ee31cae900b60d36642262df114c5c9c.png)
2. 单击 **ADD ROUTE** 在该 Service 上创建 Route，
![](https://qcloudimg.tencent-cloud.cn/raw/c41b7c48442668e50d4cf8d493d63f63.png)
设置 Path 为 `/new/path`，且开启 Strip Path 选项（默认开启）。
![](https://qcloudimg.tencent-cloud.cn/raw/2380aa7110551af00172ef6c287516b6.png)
3. 请求 `http://<kong>/new/path/user` 时，后端接收到的请求路径为 `/anything/api/user`。


### 场景二：通过 Request Transformer 插件实现完整 URL 改写
<dx-alert infotype="explain" title="<b>示例：</b>">
原始 API 调用 URL 为 `http://<backend>/anything/user_list` 
发布到 Kong 网关后，调用 URL 改写为 `http://<kong>/users`
</dx-alert>

1. 创建 Service，Path 可以任意设置。
2. 在该 Service 上创建 Route，设置 Path 为 `/users`。
3. 单击 **ADD PLUGIN** 新建插件。
![](https://qcloudimg.tencent-cloud.cn/raw/eb3ccfce6bdb59ec085830de13d2f924.png)
在该 Route 上创建 Request Transformer 插件。
![](https://qcloudimg.tencent-cloud.cn/raw/d585ce5662e34e423507e7663e2cd7e1.png)
并配置 `replace.uri` 为 `/anything/user_list`，该路径为后端接收到的实际请求路径。
![](https://qcloudimg.tencent-cloud.cn/raw/cbcd43b88e2e3aaa9218e115417ba947.png)
4. 请求 Route 后，后端接收到的请求路径为 `/anything/path`（原始 Service Path 配置被覆盖）。

### 场景三：通过 Request Transformer 插件实现部分 URL 改写

<dx-alert infotype="explain" title="<b>示例：</b>">
原始 API 调用 URL 为 `http://<backend>/anything/<user_id>/get`
发布到 Kong 网关后，调用 URL 改写为 `http://<kong>/user/<user_id>`
</dx-alert>

1. 创建 Service，Path 可以任意设置。
2. 在该 Service 上创建 Route，设置 Path 为 `/user/(?<user_id>\w+)`。
![](https://qcloudimg.tencent-cloud.cn/raw/a6568a1fdc258fc38f16b5581831d0ff.png)
3. 在该 Route 上创建 Request Transformer 插件。
![](https://qcloudimg.tencent-cloud.cn/raw/d585ce5662e34e423507e7663e2cd7e1.png)
并配置 `replace.uri` 为 `/anything/$(uri_captures['user_id'])/get`，该路径为后端接收到的实际请求路径。
![](https://qcloudimg.tencent-cloud.cn/raw/0c6660e1e14388f9a794a3a7053bcf4c.png)
4. 请求 `http://<kong>/user/user_a` 后，后端接收到的请求路径为 `/anything/user_a/get`。

## 相关参考
- [Kong 插件文档](https://docs.konghq.com/hub/kong-inc/request-transformer/)
