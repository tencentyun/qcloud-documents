## 绑定用户标识

移动开发平台（MobileLine）的多项服务（如 Analytics、Messaging 等）都可以在上报信息时带上用户标识，这样通过后台查看数据的时候，可以定位到具体的用户。
- 您可在用户模块登录之后，调用 bindUserId 方法，绑定用户标识：

`TACApplication.bindUserId(userId)`

- 如果通过微信或者 QQ 等三方登录模块，可调用 useOpenId 方法，绑定用户标识：

`TACApplication.useOpenId(openId)`

绑定用户标识后，我们会自动通知所有服务，后续上报信息时，自动带上用户的 ID。
