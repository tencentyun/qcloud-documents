

# iOS应用初始化及接入验证

## 1、前置条件

- 已经创建 iOS 开发工程。
- 工程已经使用 Cocoapods 管理或工程通过 IDE 工具创建。

## 2、初始化步骤

1. 修改`Podfile`文件，添加TMF基础库`TMFBase`。将`TMFBase`及其依赖库导入至工程中。

   ```ruby
   target 'TMFDemo' do
   	pod 'TMFBase'
   end
   ```

2. 在命令行执行 `pod install` 命令接入相关 TMF SDK。

3. 从[控制台下载配置文件](../../在控制台创建应用/下载配置文件.md)`tmf-ios-configurations.json`，并将文件导入工程目录下。  
   <img src="../img/file.png" width=50% style="border: 1.5px solid">

4. 在工程的`AppDelegate`文件中引入`TMFBase.h`头文件和`TMFSharkCenter.h`。然后在`-application:didFinishLaunchingWithOptions:`方法中进行TMFBase的初始化：

## 3、接入验证

查看控制台日志是否有“GUID”信息。如果GUID生成正常表示TMF环境初始化成功，反之初始化失败。  
<img src="../img/guid.png" width=70% style="border: 1.5px solid">