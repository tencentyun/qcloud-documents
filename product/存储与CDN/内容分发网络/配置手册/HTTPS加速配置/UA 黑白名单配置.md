
## 配置场景

腾讯云 CDN 支持通过配置 User-Agent 黑白名单规则实现访问控制。
通过对用户 HTTP 请求头中的 User-Agent 进行规则判断，按需放行或拒绝用户访问。

## 配置指南



### 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可进入域名配置页面，第二栏【访问控制】中可看到 UA 黑白名单配置，默认情况下为关闭状态：
![](https://main.qcloudimg.com/raw/5105eca56650c784e3e5965172619322.png)

### 新增规则
单击【新增规则】，可按需逐条添加黑(白)名单：
![](https://main.qcloudimg.com/raw/74bae0674238aa3f37bc9853c823e62f.png)


 
#### 配置约束

- 仅支持全部设置为黑名单或全部设置为白名单，不支持同时设置黑、白名单规则。
- 最多可配置 10 条黑或白名单规则。
- 规则内容支持通配符`*`，多个值情况下使用 `|`分隔。
- 生效类型支持全部文件、文件类型、文件目录、指定文件路径四种模式，暂不支持正则匹配。

>!
>1. 仅支持通配符`*`，暂时不支持其他正则表达式。
>2. 无`*`情况下，其他字符均为完全匹配。


## 配置示例

若加速域名`cloud.tencent.com`的 UA 黑白名单配置如下：
![](https://main.qcloudimg.com/raw/7ac57bc6f16087aad95c0844c6053f75.png)
当 HTTP Request Header 中 User-Agent 如下时：

```
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
```

命中黑名单，将直接返回403。

