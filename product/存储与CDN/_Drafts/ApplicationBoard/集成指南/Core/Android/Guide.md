# 应用云Android接入指南

## 绑定用户标识

应用云的很多服务，例如 Analytics、Messaging，都可以在上报信息时带上用户标识，这样后台可以查看数据的时候，可以定位到具体的用户。如果您需要带上这样的信息，可以在用户模块登录之后，调用 bindUserId 方法，绑定您的用户标识：

```
TACApplication.bindUserId(customId)
```

如果您是通过微信或者qq等三方登录模块，可以调用 useOpenId：

```
TACApplication.useOpenId(openId)
```

当你绑定之后，我们会自动通知所有服务，后续上报信息时，自动带上用户的id。