假设用户某个CLB下有两个域名：login.qcloud.com和img.qcloud.com，此时希望login.qcloud.com有会话保持，而img.qcloud.com没有会话保持。则可以在开启会话保持配置中选择“cookie植入”的方式，并在后端服务器内进行配置。

若后端服务器为nginx服务器，先启用ngx_http_upstream_session_sticky_module模块；该模块是一个负载均衡模块，通过cookie实现客户端与后端服务器的会话保持, 在一定条件下可以保证同一个客户端访问的都是同一个后端服务器。

![](//mccdn.qcloud.com/static/img/300b92cca97bbe8fdbf3fd902cb9200e/image.png)

配置说明：
- cookie设置用来记录会话的cookie名称 
- domain设置cookie作用的域名，默认不设置 
- path设置cookie作用的URL路径，默认不设置 
- maxage设置cookie的生存期，默认不设置，即为session cookie，浏览器关闭即失效
- mode设置cookie的模式
insert：通过Set-Cookie头直接插入相应名称的cookie。 
prefix：不会生成新的cookie，但会在响应的cookie值前面加上特定的前缀，当浏览器带着这个有特定标识的cookie再次请求时，模块在传给后端服务前先删除加入的前缀，后端服务拿到的还是原来的cookie值，这些动作对后端透明。
rewrite: 使用服务端标识覆盖后端设置的用于会话保持的cookie。如果后端服务在响应头中没有设置该cookie，则认为该请求不需要进行会话保持。使用这种模式，后端服务可以控制哪些请求需要会话保持，哪些请求不需要。
- option设置用于会话保持的cookie的选项，可设置成indirect或direct。indirect不会将cookie传送给后端服务，该cookie对后端应用完全透明。direct则与indirect相反。 
- maxidle设置session cookie的最长空闲的超时时间 
- maxlife设置session cookie的最长生存期 
- fallback设置是否重试其他机器，当会话保持的后端服务器宕机后，是否需要尝试其他机器 
- hash设置cookie中server标识是用明文还是使用md5值，默认使用md5。