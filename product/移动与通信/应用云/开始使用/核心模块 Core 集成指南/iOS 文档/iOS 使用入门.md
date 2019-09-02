移动开发平台（MobileLine）使用起来非常容易，只需要简单的 4 步，您便可快速接入。接入后，您即可获得我们提供的各项能力，减少您在开发应用时的重复工作，提升开发效率。

## 准备工作

为了使用移动开发平台（MobileLine）iOS 版本的 SDK，您首先需要一个 iOS 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用


在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

>!如果您已经在 MobileLine 控制台上创建过了项目和应用，请跳过此步。


## 第二步：添加配置文件

创建好应用后，您可以单击红框中的【下载配置】来下载该应用的配置文件的压缩包：

![](https://ws2.sinaimg.cn/large/006tNc79gy1fq0pubol92j31kw093gnw.jpg)

解压后将 tac_services_configurations.plist 文件集成进项目中。其中有一个  tac_services_configurations_unpackage.plist 文件，请将该文件放到您工程的根目录下面(**切记不要将该文件添加进工程中**)。 添加好配置文件后，继续单击【下一步】。


![](https://ws1.sinaimg.cn/large/006tNc79gy1forbnw3ijyj31bi11wnch.jpg)


>!请您按照图示来添加配置文件，`tac_service_configurations_unpackage.plist` 文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。




## 第三步：集成 SDK

>!无论您使用哪种代码集成方式，都请**配置程序需要脚本**。如果您选择手工集成，则需要先从：[下载地址](http://ios-release-1253960454.cossh.myqcloud.com/tac.zip),下载 移动开发平台（MobileLine）所需要的 SDK 集合文件。并仔细阅读文件中的 Readme.md 文档。

每一个 MobileLine 服务都是一个单独的 SDK，其中 `TACCore` 是其他所有模块的基础模块，因此您必须至少将 `analytics` 模块集成到您的 App 中，下表展示了 MobileLine 各种服务所对应的库。


以下库分别对应各种移动开发平台（MobileLine）的功能。

| 功能 | cocoapods | 服务名称 |
|:----|:-----------|:-----------|
| 腾讯移动分析（MTA） |  TACCore   |  analytics|
| 腾讯移动推送（信鸽）|  TACMessaging |  messaging  |
| 腾讯崩溃服务（bugly）|  TACCrash   |  crash      |
| 移动存储（Storage） |  TACStorage   |  storage   |
| 授权（Authorization）|  TACAuthorization   |  social  |
| 腾讯计费（米大师）|  TACPayment   |  payment  |


如果还没有 Podfile，请创建一个。

~~~
$ cd your-project directory
$ pod init
~~~

并在您的 Podfile 文件中添加移动开发平台（MobileLine）的私有源：

~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

如果您想集成我们的各种服务，那么您只需要在 Podfile 中添加对应的服务依赖即可：

例如，您只想集成 analytics 服务

```
pod 'TACCore'
```

如果您想集成 `messaging` 服务：

```
pod 'TACMessaging'
```

如果您想同时集成 `messaging` 和 `crash` 服务：

```
pod 'TACMessaging'
pod 'TACCrash'
```

>!控制台向导上默认您只集成最基础的 `analytics` 服务。


### 配置程序需要脚本

为了简化 SDK 的接入流程，我们使用 shell 脚本，帮助您自动化的去执行一些繁琐的操作，比如 crash 自动上报，在 Info.plist 里面注册各种第三方 SDK 的回调 scheme。因而，需要您添加以下脚本来使用我们自动化的加入流程。

脚本主要包括两个：

1. 在构建之前运行的脚本，该类型的脚本会修改一些程序的配置信息，比如在 Info.plist 里面增加 qqwallet 的 scheme 回调。
2. 在构建之后运行的脚本，该类型的脚本在执行结束后做一些动作，比如 Crash 符号表上报。

![](https://ws1.sinaimg.cn/large/006tNc79ly1fnttw83xayj317i0ro44j.jpg)

#### 自动添加所有程序需要脚本
自动添加脚本目前仅支持通过 Cocoapods 方式进行集成的用户。如果使用 Cocoapods 集成的话，在 Podfile 的最后一行后面**新起一行**，并且将以下代码粘贴进去以后，运行 `pod install` 即可，就完成了配置程序需要脚本这一步。

~~~
pre_install do |installer|
    puts "[TAC]-Running post installer"
    xcodeproj_file_name = "placeholder"
    Dir.foreach("./") do |file|
        if file.include?("xcodeproj")
            xcodeproj_file_name = file
        end
    end
    puts "[TAC]-project file is #{xcodeproj_file_name}"
    project = Xcodeproj::Project.open(xcodeproj_file_name)
    project.targets.each do |target|
        shell_script_after_build_phase_name = "[TAC] Run After Script"
        shell_script_before_build_phase_name = "[TAC] Run Before Script"
        puts "[TAC]-target.product_type is #{target.product_type}"
          if target.product_type.include?("application")
              should_insert_after_build_phases = 0
              should_insert_before_build_phases=0
              after_build_phase = nil
              before_build_phase = nil
              target.shell_script_build_phases.each do |bp|
                    if !bp.name.nil? and bp.name.include?(shell_script_after_build_phase_name)
                        should_insert_after_build_phases = 1
                        after_build_phase = bp
                    end
                    if !bp.name.nil? and bp.name.include?(shell_script_before_build_phase_name)
                        should_insert_before_build_phases = 1
                        before_build_phase = bp
                    end
              end


              if should_insert_after_build_phases == 1
                  puts "[TAC]-Build phases with the same name--#{shell_script_after_build_phase_name} has already existed"
              else
                  after_build_phase = target.new_shell_script_build_phase
                  puts "[TAC]-installing run afger build phases-- #{after_build_phase}"

              end
              after_build_phase.name = shell_script_after_build_phase_name
              after_build_phase.shell_script = "
              if [ -f \"${SRCROOT}/Pods/TACCore/Scripts/tac.run.all.after.sh\" ]; then
                  bash \"${SRCROOT}/Pods/TACCore/Scripts/tac.run.all.after.sh\"
              fi
              "
              after_build_phase.shell_path = '/bin/sh'
              if should_insert_before_build_phases == 1
                  puts "[TAC]-Build phases with the same name--#{shell_script_before_build_phase_name} has already existed"
                  else
                  before_build_phase = target.new_shell_script_build_phase
                  target.build_phases.insert(0,target.build_phases.pop)
                  puts "[TAC]-installing run before build phases-- #{before_build_phase}"

              end
              before_build_phase.name = shell_script_before_build_phase_name
              before_build_phase.shell_script = "
              if [ -f \"${SRCROOT}/Pods/TACCore/Scripts/tac.run.all.before.sh\" ]; then
                  bash \"${SRCROOT}/Pods/TACCore/Scripts/tac.run.all.before.sh\"
                  fi
                  "
              before_build_phase.shell_path = '/bin/sh'
         end
    end
    puts "[TAC]-Saving projects"
    project.save()
end

~~~

>!运行`pod install`以后，可以按照上面的图片打开项目里的 Build Phases 确认是否有 [TAC] 开头，与图上类似的 Build phases 。如果没有的话，可再次运行 `pod install`后检查即可。

#### 手动添加程序需要脚本

##### 添加构建之前运行的脚本

1. 在导航栏中打开您的工程。
2. 打开 Tab `Build Phases`。
3. 单击 `Add a new build phase` , 并选择 `New Run Script Phase`，您可以将改脚本命名 TAC Run Before

>!请确保该脚本在 `Build Phases` 中排序为第二。

4. 根据自己集成的模块和集成方式将代码粘贴入  `Type a script...` 文本框:。

需要黏贴的代码

~~~
#export TAC_SCRIPTS_BASE_PATH=[自定义执行脚本查找路径，我们会在该路径下寻找所有以“tac.run.all.before.sh”命名的脚本，并执行，如果您不需要自定义不用动这里]
${TAC_CORE_FRAMEWORK_PATH}/Scripts/tac.run.all.before.sh
~~~

其中 `THIRD_FRAMEWORK_PATH` 变量的取值根据您的安装方式而不同：

* 如果您使用 Cocoapods 来集成的则为 `${PODS_ROOT}/TACCore`，您需要黏贴的代码实例如下：

  ~~~
  ${SRCROOT}/Pods/TACCore/Scripts/tac.run.all.before.sh
  ~~~
* 如果您使用手工集成的方式则为 `您存储 TACCore 库的地址`，即您 TACCore framework 的引入路径，您需要黏贴的代码实例如下：

  ~~~
   export TAC_SCRIPTS_BASE_PATH=[自定义执行脚本查找路径，我们会在该路径下寻找所有以“tac.run.all.after.sh”命名的脚本，并执行，如果您不需要自定义不用动这里]
   [您存储 TACCore 库的地址]/TACCore.framework/Scripts/tac.run.all.before.sh
  ~~~




##### 添加构建之后运行的脚本

1. 在导航栏中打开您的工程。
2. 打开 Tab `Build Phases`。
3. 单击 `Add a new build phase` , 并选择 `New Run Script Phase`，您可以将改脚本命名 TAC Run Before。

>!请确保该脚本在 `Build Phases` 中排序需要放到最后。

4. 根据自己集成的模块和集成方式将代码粘贴入  `Type a script...` 文本框:。

需要黏贴的代码

~~~
#export TAC_SCRIPTS_BASE_PATH=[自定义执行脚本查找路径，我们会在该路径下寻找所有以“tac.run.all.after.sh”命名的脚本，并执行，如果您不需要自定义不用动这里]
${TAC_CORE_FRAMEWORK_PATH}/Scripts/tac.run.all.after.sh
~~~

其中 `THIRD_FRAMEWORK_PATH` 变量的取值根据您的安装方式而不同：

* 如果您使用 Cocoapods 来集成的则为 `${PODS_ROOT}/TACCore`，您需要黏贴的代码实例如下：

  ~~~
  ${SRCROOT}/Pods/TACCore/Scripts/tac.run.all.after.sh
  ~~~
* 如果您使用手工集成的方式则为 `[您存储 TACCore 库的地址]`，即您 TACCore framework 的引入路径，您需要黏贴的代码实例如下：

  ~~~
  #export TAC_SCRIPTS_BASE_PATH=[自定义执行脚本查找路径，我们会在该路径下寻找所有以“tac.run.all.after.sh”命名的脚本，并执行，如果您不需要自定义不用动这里]
  [您存储 TACCore 库的地址]/TACCore.framework/Scripts/tac.run.all.after.sh
  ~~~


## 第四步：初始化

集成好我们提供的 SDK 后，您需要在您自己的工程中添加初始化代码，从而让 MobileLine 服务在您的应用中进行自动配置。整个初始化的过程很简单。

### 步骤 1 在 UIApplicationDelegate 子类中导入移动开发平台（MobileLine）模块。

Objective-C 代码示例：

~~~
#import <TACCore/TACCore.h>
~~~
Swift 代码示例：

~~~
import TACCore
~~~


### 步骤 2 配置一个 TACApplication 共享实例，通常是在应用的 `application:didFinishLaunchingWithOptions:` 方法中配置。


######  使用默认配置

通常对于移动开发平台（MobileLine）的项目他的配置信息都是通过读取 tac_services_configuration.plist 文件来获取的。

Objective-C 代码示例：

~~~
[TACApplication configurate];
~~~

Swift 代码示例：

~~~
TACApplication.configurate();
~~~




###### 通过编程的方式自定义某些参数

您可能也有需求在程序运行时，去改变一些特定的参数来改变程序的行为。为了支持您的这种需求，我们增加了修改程序配置的接口，您可以仿照如下形式来修改移动开发平台（MobileLine）的配置。

Objective-C 代码示例：

~~~
TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
// 自定义配置
// opions.xxx= xxx
//
[TACApplication configurateWithOptions:options];
~~~

Swift 代码示例：

~~~
let options = TACApplicationOptions.default()
// 自定义配置
// opions.xxx= xxx
TACApplication.configurate(with: options);
~~~




### 启动服务

MobileLine iOS SDK 会自动帮您启动对应的服务，比如分析（Analytics）服务。有些服务比如Storage是按需启动，当您使用的时候，调用其接口即可。

| 功能 | 启动方式 | 服务名称 |
|:----|:-----------|:-----------|
| 腾讯移动分析（MTA） |  默认启动   |  analytics|
| 腾讯移动推送（信鸽）|  默认启动 |  messaging  |
| 腾讯崩溃服务（bugly）|  默认启动   |  crash      |
| 移动存储（Storage） | 按需使用   |  storage   |
| 授权（Authorization）|  按需使用   |  social  |
| 腾讯计费（米大师）|  按需使用   |  payment  |



## 后续步骤

### 了解 MobileLine：

- 查看 [MoblieLine 应用示例](https://ios-release-1253960454.cos.ap-shanghai.myqcloud.com/tac.zip)

### 向您的应用添加 MobileLine 功能：

- 借助 [Analytics](https://cloud.tencent.com/document/product/666/14822) 深入分析用户行为。
- 借助 [messaging](https://cloud.tencent.com/document/product/666/14826) 向用户发送通知。
- 借助 [crash](https://cloud.tencent.com/document/product/666/14824) 确定应用崩溃的时间和原因。
- 借助 [storage](https://cloud.tencent.com/document/product/666/14828) 存储和访问用户生成的内容（如照片或视频）。
- 借助 [authorization](https://cloud.tencent.com/document/product/666/14830) 来进行用户身份验证。
- 借助 [payment](https://cloud.tencent.com/document/product/666/14832) 获取微信和手 Q 支付能力
