LoadBalance 团队在 4 月推出**公网应用型 LB**独家能力：自定义重定向。该能力可解决两大难题：
1. 强制 HTTPS
PC、手机浏览器等以 HTTP 请求访问 Web 服务，LoadBalance 代理后，返回 HTTPS 的 respond。默认强制以 HTTPS 访问网页。
2. 自定义重定向
当出现 Web 业务需要临时下线（如电商售罄、页面维护，更新升级时）会需要重定向能力。如果不做重定向，用户的收藏和搜索引擎数据库中的旧地址只能让访客得到一个 `404/503` 错误信息页面，降低了用户体验度，导致访问流量白白丧失。不仅如此，之前该页面积累的搜索引擎评分也浪费了。

## 一、CLB 代理 HTTPS 请求
### nginx 的传统解决方案
#### 方案说明
1. 假定开发者购买了负载均衡器，后端绑定了 100 台 CVM，配置网站 https://example.com 。开发者希望用户在浏览器中输入网址时，直接键入www.example.com 即可通过 HTTPS 协议安全访问（即无论 HTTP / HTTPS 请求，都返回 HTTPS，强制使用加密能力）。
2. 此时用户输入的 www.example.com 请求转发流程如下：
该请求以 HTTP 协议传输，通过 VIP 访问 CLB 负载均衡监听器的 80 端口，并被转发到后端云服务器的 8080 端口。
3. 通过在腾讯云后端服务器的 nginx 上配置 rewrite 操作，该请求经过 8080 端口，并被重写到 https://example.com 页面。
4. 此时浏览器再次发送 https://example.com 请求到相应的 HTTPS 站点，该请求通过 VIP 访问负载均衡监听器的 443 端口，并被转发到后端云服务器的 80 端口。至此，请求转发完成。架构如下图所示：
![](https://mc.qcloudimg.com/static/img/b5d0efa20da5872ac3d29a41fd29d945/11.jpg)

#### 具体配置
1. 当用户请求的 HTTP 和 HTTPS 服务的域名一样时，且 HTTPS 端口默认为 443 时，为实现以上请求转发操作，用户可以直接对后端服务器做如下配置：
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

2. 当用户请求的 HTTP 和 HTTPS 服务的域名不同，或者端口不是 443 时，为实现以上请求转发操作，用户需要指定具体的 URL 和端口，对后端服务器做如下配置：
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
1. 上述架构中，CLB 的主要作用是对 HTTPS 进行代理，因此无论是 HTTP 还是 HTTPS 请求，到了 CLB 转发给后端 CVM 时，都是 HTTP 请求。此时，**客户端到LB 时如果为 HTTPS 协议，则采用加密传输的方式，但 LB 到后端服务器依然是明文传输。**此时，开发者无法分辨出前端的请求是 HTTPS 还是 HTTPS。
2. 为了解决这个问题，腾讯云 CLB 在将请求转发给后端 CVM 时，头部 header 会植入 X-Client-Proto，从而便于开发者依据 header 内容判断请求类型：
 - X-Client-Proto: HTTP （前端为 HTTP 请求）。
 - X-Client-Proto: HTTPS （前端为 HTTPS 请求）。

#### 存在问题
- 配置繁琐：假设客户有多个 domain + uri，有 100 台后端的 CVM 服务器，则需要在 100 台服务器上重复配置。且每增加一个 domain + uri，都需要在 100 台后端 CVM 上刷新一遍。
- 计算开销：重定向判断耗费后端 CVM 服务器的 CPU 资源。


### CLB 强制 HTTP 跳转方案
#### 方案说明
假定开发者需要配置网站 https://example.com 。开发者希望用户在浏览器中输入网址时，直接键入www.example.com 即可通过 HTTPS 协议安全访问。www.example.com 下，不仅仅是一个地址，后端关联的 URL 可能有数百的（用正则匹配），总的 real server 数量会有几百个，逐一配置难度太大。腾讯云支持一键式的，强制 HTTPS 跳转。
1. 第一步，先在 [腾讯云负载均衡控制台](https://console.cloud.tencent.com/loadbalance/index?rid=1) 将 LB 的 HTTPS 监听器配置好，也就是将 https://example.com 的 Web 环境搭建好。
 ![](https://mc.qcloudimg.com/static/img/61a723a69c581968a46fe86447f1473a/1111.jpg)
2. 第二步，到应用型负载均衡器控制台处启用重定向能力，目前支持域名级别，整体跳转。
 ![](https://mc.qcloudimg.com/static/img/e066362fed8d3cf7740dd50c49c6004b/2222.jpg)

#### 方案优势
- 仅需 1 次配置：一个域名，一次配置即可完成强制 HTTPS。
- 更新：若 HTTPS 服务的 URL 有增减，只需要在控制台，重新使用该功能刷新一遍即可。

## 二、注意事项
- 会话保持：如 client 端访问了 example.com/bbs/test/123.html ，且后端 CVM 开启了会话保持。 当启用重定向，将流量导到 example.com/bbs/test/456.html 时，原会话保持机制将失效。
- TCP / UDP 重定向：暂不支持 IP + Port 级别的重定向，后续版本将提供。
