## 操作场景
Service Mesh 应用支持在 Sidecar 上运行用户自定义的 Lua 脚本的能力。用户可以自定义一些业务逻辑放在 Sidecar 上执行，来实现一些自定义的业务逻辑（例如在请求头中添加参数、设置服务路由规则等）。配置 Sidecar 过滤器可以大大加强 Mesh 应用的灵活性。


## 操作步骤
### 新建过滤器
1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)，在左侧导航栏单击**应用管理**。
2. 在应用管理列表页，单击目标应用的 ID，进入应用详情页。
3. 访问 Sidecar过滤器 页面，新建过滤器。
   - 填写过滤器名称以及备注。
   - 填写过滤器作用位置。
     - 作为服务端是指：该脚本将在部署组运行启动的微服务作为服务端时生效。
     - 作为客户端是指：该脚本将在部署组运行启动的微服务作为客户端的时候生效。当选择过滤器位置为客户端时，需要填写被调用的微服务的名称。仅当调用被调服务的时候，过滤器会生效。
   - 填写脚本内容。脚本需要严格按照 Lua 脚本的格式进行书写。

>?
- Lua 脚本最大为65535字节。
- 已经下线的过滤器才能删除。
- 编辑后的 Lua 脚本，需要再次发布之后才能生效。

以下为微服务作为客户端时，向请求头中添加两个字段并返回请求体大小的示例：
```
function envoy_on_request(request_handle)
    request_handle:headers():add("foo", "bar")
end
function envoy_on_response(response_handle)
    body_size = response_handle:body():length()
    response_handle:headers():add("response-body-size", tostring(body_size))
end
```

有关 Lua 脚本更多的书写原则，可以参考 [Envoy 使用文档](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/lua_filter)。


### 发布过滤器
创建好的过滤器需要发布才能生效。当前 TSF 支持将同一个过滤器发布到多个部署组上，或将某一个过滤器下线。过滤器也可以发布在离线状态的部署组上，当部署组启动时会将过滤器加载。








