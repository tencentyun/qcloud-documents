> 回源 HOST 是指 CDN 节点在回源过程中，在源站访问的站点域名。请保证您配置的回源 HOST 域名能够支持访问，否则会导致回源失败的情况，影响您的业务。您可以根据自身业务情况配置自定义回源 HOST。
>
> 源站与回源 HOST：源站配置的 IP/域名能够指引 CDN 节点回源时找到对应的源站服务器，服务器上可能存在若干 WEB 站点，回源 HOST 指明了资源所在的站点。
>
> 根据有关部门规定，源站为腾讯云CVM的加速域名，回源 HOST 配置的域名需要在腾讯云备案。

## 配置指引

### 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】：
![](https://mc.qcloudimg.com/static/img/1f2cb594cd614b62b589cb20a20ed362/basic-config-1.png)
单击【基本配置】，在最下方可以看到回源 HOST配置：
![](https://mc.qcloudimg.com/static/img/8da29875fe47392f6e67839e02f36d65/origin-config-3.png)

默认情况下，子域名的回源 HOST 为所配置的加速域名，泛域名回源 HOST 为访问域名：
+ 若您接入的加速域名为 ```www.test.com```，则此节点对此域名下资源发起回源请求时，Request HTTP Header 中 HOST 字段的值为 ```www.test.com```。
+ 若您接入的加速域名为泛域名，如 ```*.test.com```，若访问域名为 ```abc.test.com```，则回源 HOST 为 ```abc.test.com```。

### 修改回源Host

点击【编辑】可以对回源host配置进行调整：![](https://mc.qcloudimg.com/static/img/36e6b93488f46f08759244ae09553c29/origin-config-4.png)

## 配置案例

用户访问域名为```www.test.com```，源站配置为域名```origin.test.com```，```origin.test.com``` 对应的A记录为```1.1.1.1```

用户请求为：```http://www.test.com/1.jpg```。

若配置如下：![](https://mc.qcloudimg.com/static/img/36e6b93488f46f08759244ae09553c29/origin-config-4.png)

默认情况下，回源 host 为加速域名，回源时实际请求发往```1.1.1.1```

获取的资源为：```http://www.test.com/1.jpg```。

若配置如下：![](https://mc.qcloudimg.com/static/img/1888f327603bbdfe15c332d489b1f4c1/origin-host-demo.png)

回源 host 为```origin.test.com```，回源时实际请求发往```1.1.1.1```

获取的资源为：```http://origin.test.com/1.jpg```。