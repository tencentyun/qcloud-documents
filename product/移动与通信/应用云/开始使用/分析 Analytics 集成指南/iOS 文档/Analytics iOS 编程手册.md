# 应用云 Analytics iOS 编程手册

## 开始之前


如果这是您首次向应用添加 Analytics，请完成以下步骤：

在应用云控制台中关联您的应用

1. 安装 [应用云 SDK](https://console.cloud.tencent.com/tac)。
2. 在 [应用云 控制台](https://console.cloud.tencent.com/tac)中，将您的应用添加到您的应用云项目中。
3. 参考 [Analytics 配置文档](https://console.cloud.tencent.com/tac)，配置并初始化  Analytics。


### 记录事件

事件可让您了解您的应用中发生了什么，例如用户操作、系统事件或错误。

>**注意：** 
>在记录时间之前您需要先引入头文件 `#import <TACCore/TACCore.h>`。

在配置好 TACAppliction 之后，您就可以使用 `[TACAnalyticsService trackEvent:event]` 来记录事件了。

~~~
TACAnalyticsEvent* event = [TACAnalyticsEvent eventWithIdentifier:@"demo-appear-event"];
[TACAnalyticsService trackEvent:event];
~~~

为帮助您着手，Analytics SDK 定义了许多推荐的事件，这些事件可通用于各种应用类型，包括零售和电子商务、旅行以及游戏应用，比如常见的页面追踪。

### 统计事件时长

事件时长可以统计某个事件的时长，比如用户访问某个页面的时长

~~~
- (void)viewDidLoad {
    [super viewDidLoad];
    TACAnalyticsEvent* event = [TACAnalyticsEvent eventWithIdentifier:@"duration-event"];
    _durationEvent = event;
    // Do any additional setup after loading the view from its nib.
}
- (IBAction)durationStart:(id)sender
{
    [TACAnalyticsService trackEventDurationBegin:_durationEvent];
}

- (IBAction)durationEnd:(id)sender
{
    [TACAnalyticsService trackEventDurationEnd:_durationEvent];
}
~~~

### 控制自动页面追踪

默认我们会对用户使用时的页面跳转进行埋点，如果您不希望使用改功能可以关闭该功能

~~~
 TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
 options.analyticsOptions.autoTrackPageEvents = NO;
     ....
[TACApplication configurateWithOptions:options];
~~~


## 其他功能

其他功能请参考 TACAnalyticsService.h 中的定义
