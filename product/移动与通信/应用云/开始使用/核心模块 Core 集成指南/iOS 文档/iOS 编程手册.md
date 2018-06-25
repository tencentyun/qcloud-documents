

## 绑定用户唯一标记

为了方便追踪用户信息，您可以绑定用户的唯一标记：

Objective-C:

~~~
[[TACApplication defaultApplication] bindUserIdentifier:@"uuid-11"];
~~~

Swift:

~~~
TACApplication.default().bindUserIdentifier("xxxx");
~~~

当您调用该功能后，我们会周知所有需要用户唯一 ID 的模块，绑定该 ID。

> 备注：使用支付模块的时候，您必须设置该ID。该在使用信鸽账号推送的时候，也需要先设置该标记。
