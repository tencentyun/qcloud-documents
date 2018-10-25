回源 HOST 是指 CDN 节点在回源过程中，在源站访问的站点域名。

源站与回源 HOST：源站配置的 IP/域名能够指引 CDN 节点回源时找到对应的源站服务器，服务器上可能存在若干 WEB 站点，回源 HOST 指明了资源所在的站点。
## 配置说明
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/f2f50e0d81eb0a8c0dcb61d2ee37e6c9/manage.png)
单击【基本配置】，您可以看到 **回源配置** 模块，配置回源 HOST。
![](https://mc.qcloudimg.com/static/img/5d584b6331baccd578f6e81edcf4bb71/backtosource.png)

### 默认配置
默认情况下，子域名的回源 HOST 为所配置的加速域名，泛域名回源 HOST 为访问域名，如：
+ 若您接入的加速域名为 ```www.test.com```，则此节点对此域名下资源发起回源请求时，Request HTTP Header 中 HOST 字段的值为 ```www.test.com```。
+ 若您接入的加速域名为泛域名，如 ```*.test.com```，若访问域名为 ```abc.test.com```，则回源 HOST 为 ```abc.test.com```。
![](https://mc.qcloudimg.com/static/img/90b1df3167dc3a089c7f09d0e3841e98/host-change.png)

### 自定义配置
> **注意**：
> 目前仅支持接入方式为 **自有源** 的域名配置回源 HOST。
> 请保证您配置的回源 HOST 域名能够支持访问，否则会导致回源失败的情况，影响您的业务。您可以根据自身业务情况配置自定义回源 HOST。

![](https://mc.qcloudimg.com/static/img/218190051523eac1377e36412c275909/host-change2.png)