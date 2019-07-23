LoadBalance 团队在4月推出**公网应用型 CLB** 能力：自定义重定向。该能力可解决两大难题：
1. 强制 HTTPS
PC、手机浏览器等以 HTTP 请求访问 Web 服务，LoadBalance 代理后，返回 HTTPS 的 respond。默认强制以 HTTPS 访问网页。
2. 自定义重定向
当出现 Web 业务需要临时下线（如电商售罄、页面维护，更新升级时）会需要重定向能力。如果不做重定向，用户的收藏和搜索引擎数据库中的旧地址只能让访客得到一个 `404/503` 错误信息页面，降低了用户体验度，导致访问流量白白丧失。不仅如此，之前该页面积累的搜索引擎评分也浪费了。

## CLB 代理 HTTPS 请求
### nginx 的传统解决方案
#### 方案说明
1. 假定开发者购买了负载均衡器，后端绑定了100台 CVM，配置网站 `https://example.com`。开发者希望用户在浏览器中输入网址时，直接键入 `www.example.com` 即可通过 HTTPS 协议安全访问（即无论 HTTP / HTTPS 请求，都返回 HTTPS，强制使用加密能力）。
2. 此时用户输入的`www.example.com`请求转发流程如下：
该请求以 HTTP 协议传输，通过 VIP 访问 CLB 负载均衡监听器的80端口，并被转发到后端云服务器的 8080 端口。
3. 通过在腾讯云后端服务器的 nginx 上配置 rewrite 操作，该请求经过8080端口，并被重写到 `https://example.com` 页面。
4. 此时浏览器再次发送 `https://example.com` 请求到相应的 HTTPS 站点，该请求通过 VIP 访问负载均衡监听器的443端口，并被转发到后端云服务器的80端口。至此，请求转发完成。架构如下图所示：
![](https://mc.qcloudimg.com/static/img/b5d0efa20da5872ac3d29a41fd29d945/11.jpg)

#### 具体配置
1. 当用户请求的 HTTP 和 HTTPS 服务的域名一样时，且 HTTPS 端口默认为443时，为实现以上请求转发操作，用户可以直接对后端服务器做如下配置：
```
server {
    listen 80; 
    server_name example.com;

    location / {
        client_max_body_size 200m;
        rewrite ^/.(.*) https://$host/$1 redirect;   //在CVM上做rewrite配置
} 
}
```

2. 当用户请求的 HTTP 和 HTTPS 服务的域名不同，或者端口不是443时，为实现以上请求转发操作，用户需要指定具体的 URL 和端口，对后端服务器做如下配置：
```
server {
    listen 80; 
    server_name example.com;

    location / {
        client_max_body_size 200m;
        rewrite ^/.(.*) https://xxx.xxx.xx:10011/x redirect;   //在CVM上做rewrite配置
} 
}
```

#### CLB 代理 HTTPS
1. 上述架构中，CLB 的主要作用是对 HTTPS 进行代理，因此无论是 HTTP 还是 HTTPS 请求，到了 CLB 转发给后端 CVM 时，都是 HTTP 请求。此时，**客户端到 CLB 时如果为 HTTPS 协议，则采用加密传输的方式，但 CLB 到后端服务器依然是明文传输。**此时，开发者无法分辨出前端的请求是 HTTP 还是 HTTPS。
2. 为了解决这个问题，腾讯云 CLB 在将请求转发给后端 CVM 时，头部 header 会植入 X-Client-Proto，从而便于开发者依据 header 内容判断请求类型：
 - X-Client-Proto: HTTP （前端为 HTTP 请求）。
 - X-Client-Proto: HTTPS （前端为 HTTPS 请求）。

#### 存在问题
- 配置繁琐：假设客户有多个 domain + uri，有100台后端的 CVM 服务器，则需要在100台服务器上重复配置。且每增加一个 domain + uri，都需要在100台后端 CVM 上刷新一遍。
- 计算开销：重定向判断耗费后端 CVM 服务器的 CPU 资源。


### CLB 强制 HTTP 跳转方案
#### 方案说明
假定开发者需要配置网站`https://example.com` 。开发者希望用户在浏览器中输入网址时，直接键入`www.example.com`即可通过 HTTPS 协议安全访问。`www.example.com` 下，不仅仅是一个地址，后端关联的 URL 可能有数百的（用正则匹配），总的 real server 数量会有几百个，逐一配置难度太大。腾讯云支持一键式的，强制 HTTPS 跳转。
1. 请在 [腾讯云负载均衡控制台](https://console.cloud.tencent.com/loadbalance/index?rid=1) 完成 CLB 的 HTTPS 监听器的配置，搭建`https://example.com`的 Web 环境。
![](https://main.qcloudimg.com/raw/634b11258bfdfee45568062f8c3bf651.png)
2. 完成 HTTPS 配置后的结果如下图所示。
![](https://main.qcloudimg.com/raw/f11a1c39ea720f8476b29e97a57c3999.png)
3. 在 CLB 实例详情的“重定向配置”标签页中，单击【新建重定向配置】。
![](https://main.qcloudimg.com/raw/32adf5abcf5569e6986f2af645ae2eac.png)
4. 选择【自动重定向配置】，并选择已配置的 HTTPS 监听器和域名，单击【下一步：配置路径】。
![](https://main.qcloudimg.com/raw/9430331e893a5305c2d2ee930e215c97.png)
5. 单击【提交】即可完成配置。
![](https://main.qcloudimg.com/raw/ba728da9f4e0ecd9070f2f7a23763bd8.png)
6. 完成重定向配置后的结果如下图所示，可以看到已为 `HTTP:443` 监听器自动配置了 `HTTP:80` 监听器，且 HTTP 的流量均会被自动重定向到 HTTPS。
![](https://main.qcloudimg.com/raw/ece6f28f16456b72c73256e4de5335bc.png)

#### 方案优势
- 仅需1次配置：一个域名，一次配置即可完成强制 HTTPS。
- 更新：若 HTTPS 服务的 URL 有增减，只需要在控制台，重新使用该功能刷新一遍即可。

## 注意事项
- 会话保持：如 client 端访问了`example.com/bbs/test/123.html` ，且后端 CVM 开启了会话保持。 当启用重定向，将流量导到`example.com/bbs/test/456.html`时，原会话保持机制将失效。
- TCP / UDP 重定向：暂不支持 IP + Port 级别的重定向，后续版本将提供。
