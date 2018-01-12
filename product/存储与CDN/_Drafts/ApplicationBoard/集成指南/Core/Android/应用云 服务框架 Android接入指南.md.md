## 应用云服务框架 Android 配置指南

### 集成配置文件

请从[控制台]()下载 tac.json 文件，并放到你应用模块的 assets 文件夹下。应用云服务框架自动会读取配置文件，作为服务的默认参数。

### 配置服务框架

应用云所有服务都必须在服务框架配置完成之后才能正常使用。因此，我们建议你在 Application onCreate方法中执行该操作。你可以有两种方式配置，默认配置和高级配置。如果你没有特殊需求，使用默认配置即可。


#### 使用默认配置

如果你要直接使用默认配置，可以使用以下方法：

```
TACApplication.configure(context);
```

应用云会自动读取你集成的json文件作为参数，配置好框架。


#### 使用高级配置

如果你需要在代码中修改配置，或者你使用的子服务强制需要额外配置参数，可以使用以下方法：

```
// 获取一个新的默认配置实例
TACApplicationOptions applicationOptions = TACApplicationOptions.newDefaultOptions(this);

// 修改子服务的参数，具体配置项请参考每个子服务的开发文档
...

// 用修改之后的配置参数设置框架
TACApplication.configureWithOptions(this, applicationOptions);
```


### 获取当前配置

配置之后，你可以使用以下方法获取当前的配置参数：

```
TACApplicationOptions currentOptions = TACApplication.options();

```


