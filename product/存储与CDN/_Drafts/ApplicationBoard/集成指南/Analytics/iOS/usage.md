## Analytics 编程使用指南

## 开始之前


如果这是您首次向应用添加 Analytics，请完成以下步骤：

在 应用云 控制台中关联您的应用

1. 安装 [应用云 SDK]()。
2. 在 [应用云 控制台]()中，将您的应用添加到您的 应用云 项目中。
3. 参考 [Analytics 配置文档]()，配置并初始化  Analytics


### 记录事件

事件可让您了解您的应用中发生了什么，例如用户操作、系统事件或错误。


> 在记录时间之前您需要先引入头文件 `#import <TACCore/TACCore.h>`

在配置好 TACAppliction 之后，您就可以 使用 `[TACAnalyticsService trackEvent:event]` 来记录事件了。

~~~
TACAnalyticsEvent* event = [TACAnalyticsEvent eventWithIdentifier:@"demo-appear-event"];
[TACAnalyticsService trackEvent:event];
~~~

为帮助您着手，Analytics SDK 定义了许多推荐的事件，这些事件可通用于各种应用类型，包括零售和电子商务、旅行以及游戏应用。比如常见的页面追踪，网络性能追踪等等

具体的使用可以参考：

~~~
TACAnalyticsService.h
~~~
