## 操作场景
本文档主要指导您在 macOS 操作系统下，对无线投屏独立安装包进行安装后的调用。SaaS 方案是独立 App，用户通过系统 API 直接唤起 App。

## 前提条件
- 请从线下销售经理获得无线投屏独立安装包，格式如：TencentCloudDisplay_corpid_version.dmg。
- 请确保 macOS 系统为10.10或以上版本。



## 操作步骤
1. 请客户自行部署内网并配置服务器。
2. 需要 macOS 客户端将无线投屏 App 唤起，如果无线投屏 App 不存在，跳转客户公司内网下载。下面附上下载无线投屏 App 和唤起无线投屏 App 的代码。

```
if (![[NSWorkspace sharedWorkspace] launchAppWithBundleIdentifier:@"com.tencent.wecast" options:NSWorkspaceLaunchWithoutActivation additionalEventParamDescriptor:NULL launchIdentifier:nil]) {

// 拉起失败，下载安装包

NSString *message = @"在应用程序中未找到无线投屏，如已安装请手动启动";

NSAlert *alert = [NSAlert new];

[alert addButtonWithTitle:@"下载"];

[alert addButtonWithTitle:@"取消"];

[alert setMessageText:message];

[alert setAlertStyle:NSAlertStyleWarning];

[alert beginSheetModalForWindow:[self window] completionHandler:^(NSModalResponse returnCode) {

if(returnCode == NSAlertFirstButtonReturn) {

NSString *dmgPath = @"www.qq.com"; //这里放置macOS安装包下载地址

[[NSWorkspace sharedWorkspace] openURL:[NSURL URLWithString:dmgPath]];

}

else if(returnCode == NSAlertSecondButtonReturn)

 {

// 取消
        }

else {

// 取消
}
}];
}

```
