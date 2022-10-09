UGCKit 可以让您自由修改预置的文字、颜色和图标。

[](id:write)
## 文字
UGCKit 默认提供中英文两套语言包，其中所有的本地化字符串均在 `UGCKit/UGCKitResources/Localizable.strings` 中，以默认的标准的本地化字符串格式存储，您可以通过替换其中的文本来修改默认的字符串，或者增加新的语言。

以动效名称为例，其中文内容位于 `UGCKit/UGCKitResources/zh-Hans.lproj/Localizable.strings`，内容示例如下:
```swift
"UGCKit.Edit.VideoEffect.DynamicLightWave" = "动感光波";
"UGCKit.Edit.VideoEffect.DarkFantasy" = "暗黑幻境";
"UGCKit.Edit.VideoEffect.SoulOut" = "灵魂出窍";
"UGCKit.Edit.VideoEffect.ScreenSplit" = "画面分裂";
"UGCKit.Edit.VideoEffect.Shutter" = "百叶窗";
"UGCKit.Edit.VideoEffect.GhostShadow" = "鬼影";
"UGCKit.Edit.VideoEffect.Phantom" = "幻影";
"UGCKit.Edit.VideoEffect.Ghost" = "幽灵";
"UGCKit.Edit.VideoEffect.Lightning" = "闪电";
"UGCKit.Edit.VideoEffect.Mirror" = "镜像";
"UGCKit.Edit.VideoEffect.Illusion" = "幻觉";
```
如果需要修改 "幻觉"效果为“幻像”，只需修改最后一行为
```swift
"UGCKit.Edit.VideoEffect.Illusion" = "幻像";
```

[](id:color)
## 颜色
UGCKit 中所有界面的颜色获取方法均在 UGCKitTheme 类中定义，您可以通过修改对应属性的值来进行修改，具体资源的名请查看 `UGCKitTheme.h` 中的注释。
以 App 界面背景颜色为例:
```swift
UGCKitTheme *theme = [[UGCKitTheme alloc] init];
theme.backgroundColor = [UIColor whiteColor]; // 改为白色背景
UGCKitEditViewController *editViewController = [[UKEditViewController alloc] initWithMedia:media config:nil theme:theme]; // 使用自定义主题创建控制器
```

[](id:icon)
## 图标
UGCKit 中所有界面的图标均在 `UGCKit.xcassets` 资源中，您可以自由替换。具体图标的文件名可以在 `UGCKitTheme.h` 中查看，图标资源的命名与其中的属性方法名相同，界面上的每个图标在其中均有定义，以录制界面为例，图中的标注为对应图标在 UGCKitTheme 中的属性名，也是在 `UGCKit.xcassets` 中的资源名称。
![](https://main.qcloudimg.com/raw/6c44a90aa35af122fdc013c1354a4b9d.jpg)
UGCKit 更换图标有以下两种方式：
- 直接替换换 UGCKitTheme.xcassets 中的图标。
- 通过代码向 UGCKitTheme 对象赋值来进行修改。

使用代码修改录制界面图标的示例如下：
```swift
UGCKitTheme *theme = [[UGCKitTheme alloc] init];
theme.nextIcon = [UIImage imageName:@"myConfirmIcon"]; // 修改完成按钮图标
theme.recordMusicIcon = [UIImage imageName:@"myMusicIcon"]; // 设置“音乐”功能图标
theme.beautyPanelWhitnessIcon = [UIImage imageNamed:@"beauty_whitness"]; // 设置”美白“效果图标
UGCKitRecordViewController *viewController = [[UGCKitRecordViewController alloc] initWithConfig:nil theme:theme]; // 使用自定义主题创建控制器
```