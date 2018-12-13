## 操作场景
BGP 高防包支持 CC 防护功能，当高防包统计的 HTTP 请求量超过设定的【http请求数阈值】时，自动触发 CC 防护。同时，BGP 高防包还支持 URL 白名单、IP 白名单和 IP 黑名单策略：
- 白名单中的 URL，其访问请求将无需执行 CC 攻击检测，直接被放行。
- 白名单中 IP，其 HTTP 访问请求将无需执行 CC 攻击检测，直接被放行。
- 黑名单中 IP，其 HTTP 访问请求将直接被拒绝。

用户可根据业务特点和防护需求，自定义防护策略实现更精准的 CC 攻击拦截。

## 操作步骤
1. 登录 [DDoS 防护（大禹）管理控制台](https://console.cloud.tencent.com/dayu/overview)，选择【BGP高防包】>【防护配置】。
2. 在【CC攻击防护】页签，选择目标实例，单击【CC防护】右侧的<img src="https://main.qcloudimg.com/raw/489e44ffdf057c2ae9a6b967236ccfa5.png"  style="margin:0;">开启 CC 防护。
3. 单击【http请求书阈值】右侧的下拉框选择合适的阈值。
>?
>- CC 防护默认关闭。当开启 CC 防护时，才可设置 HTTP 请求数阈值。
>- 推荐将 HTTP 请求阈值设置为业务量的**1.5**倍。

 ![](https://main.qcloudimg.com/raw/3cbe53d638041aa4f375d7fdd98bcf9f.png)
4. 选择【URL白名单】、【IP白名单】或【IP黑名单】页签，可根据实际业务需求添加或删除对应黑白名单。
