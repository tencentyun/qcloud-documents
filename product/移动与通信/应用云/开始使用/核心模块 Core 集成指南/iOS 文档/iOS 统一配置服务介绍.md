通常我们在集成 SDK 的时候，需要对工程和 SDK 进行一些配置和初始化的操作。为了简化这两部分的工作，更加方便的集成配置 SDK，移动开发平台（MobileLine）实现了统一配置服务。
 
移动开发平台（MobileLine）支持通过脚本来配置工程需要的参数，同时也支持通过文件和程序配置 SDK。

一般情况下移动开发平台（MobileLine）的配置信息分成两类：
 
- 通过文件（满足正则条件：tac_services_configurations*.plist）来配置。
- 通过通过程序来配置。

### 通过引入脚本配置工程需要的参数

比如 QQ SDK 在集成的时候，需要您去设置回调的 scheme 之类的，这个我们通过脚本实现了。


### 通过文件进行配置 SDK

移动开发平台（MobileLine） SDK 统一配置服务，会读取所有位于您的 MainBundle 里面符合正则条件：`tac_services_configurations*.plist`，并合并其里面的内容，然后传递给配置服务，进行对应的服务配置。

例如以下文件名都是合法的配置文件：

```
tac_services_configurations.plist
tac_services_configurations_custom.plist
tac_services_configurations_payment.plist
....
```

在读取配置文件的时候，会按照字典顺序依次读取（ z > a ），并对所有的配置进行合并。如果在多个配置文件中存在多个重复的 Key，则会以顺序靠后的配置文件中的内容为准。

例如文件 `tac_services_configurations.plist` 与 `tac_services_configurations_custom.plist` 都存在以 `payment` 为 Key 的内容，则会用 `tac_services_configurations_custom.plist` 中的覆盖掉  `tac_services_configurations.plist` 中的。


通过这种多文件配置的方式，您可以对移动开发平台（MobileLine）的配置文件进行拆分和自定义操作。例如在不改变从官网下载的配置文件的基础上，实现自定义的参数配置。

### 通过程序进行配置 SDK

在您引入了需要配置的模块的头文件的时候，您可以在 `TACApplicationOptions` 的实例中看到对应模块的 `options`  配置，只需要修改对应的参数即可。
