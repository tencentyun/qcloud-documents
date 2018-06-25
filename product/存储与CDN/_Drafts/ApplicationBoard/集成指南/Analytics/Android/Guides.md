# 应用云 Analytics 服务 Android 接入指南

## 启动服务实例

Analytics 服务在使用前必须先启动，我们建议你放在 Application 的 onCreate 方法中执行该操作。

您可以调用 start(Context) 方法将启动 Analytics 服务：

```
TACAnalyticsService.getInstance().start(this);
```

## 上报页面访问

Analytics 默认会统计所有的页面访问，你不需要另外配置。如果需要独立上报页面访问，可以调用：

```
// 页面访问开始
TACAnalyticsService.getInstance().trackPageAppear(context, pageName);

// 页面访问结束
TACAnalyticsService.getInstance().trackPageDisappear(context, pageName);
```

## 上报自定义事件

自定义事件分为两种，单次事件和持续事件。普通事件是指单次事件，而持续事件除了事件本身的属性外，包含了事件的开始和结束时间。

上报单次事件，可以调用：

```
TACAnalyticsService.getInstance().trackEvent(context, TACAnalyticsEvent);

```

上报持续事件，可以调用：

```
// 事件开始
TACAnalyticsService.getInstance().trackEventDurationBegin(context, TACAnalyticsEvent);

// 事件结束
TACAnalyticsService.getInstance().trackEventDurationEnd(context, TACAnalyticsEvent);

```

