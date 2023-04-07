## 前置条件
- 已经创建 iOS 开发工程。
- 工程已经使用 Cocoapods 管理或工程通过 IDE 工具创建。

## 初始化步骤
1. 修改 `Podfile` 文件，添加 TM F基础库 `TMFBase`。将 `TMFBase` 及其依赖库导入至工程中。
```ruby
   target 'TMFDemo' do
   	pod 'TMFBase'
   end
```
2. 在命令行执行 `pod install` 命令接入相关 TMF SDK。
3. 从控制台下载配置文件 `tmf-ios-configurations.json`，并将文件导入工程目录下。  
   <img src="https://qcloudimg.tencent-cloud.cn/raw/4b3832474790ccc0685c275f68df0f1d.png" width=50% style="border: 1.5px solid">
4. 在工程的 `AppDelegate` 文件中引入 `TMFBase.h` 头文件和 `TMFSharkCenter.h`。然后在 `-application:didFinishLaunchingWithOptions:` 方法中进行 TMFBase 的初始化。

## 接入验证
查看控制台日志是否有 “GUID” 信息。如果 GUID 生成正常表示 TMF 环境初始化成功，反之初始化失败。  
<img src="https://qcloudimg.tencent-cloud.cn/raw/f2ee7d3d4a866614fb2dfa700fce917b.png" width=70% style="border: 1.5px solid">
