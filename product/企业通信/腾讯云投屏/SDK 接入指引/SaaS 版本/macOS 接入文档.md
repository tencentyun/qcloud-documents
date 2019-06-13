## 操作场景
本文档主要指导您在 macOS 操作系统下，对无线投屏独立安装包进行安装后的调用。

## 前提条件
- 请从线下销售经理获得无线投屏独立安装包，格式如：TencentCloudDisplay_corpid_version.dmg。
- 请确保系统版本最低支持：macOS 10.10。
- SaaS 方案是独立 App，用户通过系统 API 直接唤起 App。



## 操作步骤
1. 将安装包修改为一个统一的名字，存放 CDN 上，获取到 CDN 的链接。
2. 需要 macOS 的客户端将 App 唤起，如果 App 不存在，则下载：

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
