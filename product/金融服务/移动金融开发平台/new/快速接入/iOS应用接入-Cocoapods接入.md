# iOS应用接入-Cocoapods接入

iOS平台使用[CocoaPods](https://cocoapods.org/)来接入TMF SDK，具体接入步骤如下：

## 前置条件

- 已安装 CocoaPods 1.0.0 及以上版本，并确保接入的工程是 CocoaPods 工程。

## 接入步骤

1. 打开工程中的`Podfile`文件，添加TMF SDK 的`source`。  
   <img src="../img/podfile.png" width=60% style="border: 1.5px solid">

   TMF SDK的`source`如下：

   ```rust
   source 'https://git.code.tencent.com/TMF-SDK/tmf-repo.git'
   ```

2. 根据需要，向其中添加相应组件。例如：添加`TMFShark`组件 。   
   <img src="../img/podfile2.png" width=60% style="border: 1.5px solid">

3. 在命令行执行 `pod install` 命令即可完成接入。

