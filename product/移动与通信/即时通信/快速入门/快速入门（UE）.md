## 腾讯云 IM UE5 Plugin 集成

### 步骤1：在腾讯云 IM 控制台创建应用

登录到 [腾讯云IM控制台](https://console.cloud.tencent.com/im)，如图所示创建 IM 应用：
<img src="https://qcloudimg.tencent-cloud.cn/raw/160fc987f2094c2bd10047f994ce139d.png" style="width:550px;" />  

在应用 [基础信息页面](https://console.cloud.tencent.com/im/detail)，记录应用 sdkappid 和密钥，在后续使用 [初始化](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#aecee922675b671cd979d68604a4be1bb) 和 [登录](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html#a6a9c19be21327ace77ab75657d2944b3) 接口时会用到。

### 步骤2：安装 UE5 并创建新项目

1. 安装 [Epic games Luncher](https://store.epicgames.com/en-US/download)，并且通过 Epic 安装 Unreal Engine 5.0.0+版本，安装好如图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c806cbcb84a52bfd27fdd45ee3a96569.png)
2. 启动 UE5，创建 UE5 应用，如图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6c3a54e5e95942427f51a5b78925ddee.png)
其中项目默认设置中蓝图和 C++、目标平台的配置，可根据业务方自己的需求进行配置，腾讯云 IM UE5 Plugin 对此没有限制。
3. 创建好后应用后，项目目录如图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/4fd00ac65805977017125748b465ab86.png" style="width:250px;" />  


### 步骤3：下载 Plugin

```shell
// 将插件从GitHub下来
git clone https://github.com/TencentCloud/chat-plugin-ue5.git
```



### 步骤4： Plugin 引入

在项目根目录创建插件目录，命名问 Plugins，将步骤三中下载的插件包（Plugins/下的 TencentCoudChat 文件夹）引入其中，引入后可在 UE5 Editor 的编辑 > 插件模块查看到如图所示插件安装：
![](https://qcloudimg.tencent-cloud.cn/raw/b09deaa84f6509ecf2429fc5a7e4d3cf.png)

插件引入后，在项目主模块中的 Build.cs 文件中，引入插件模块，如图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4b2a9ca77489615a9aa7cbec3366a95d.png)

### 步骤5：头文件引入

在业务 CPP 文件中引入 TencentCloudChat.h 后，开始使用腾讯云 IM UE5 Plugin 提供的能力。

### 步骤6：测试验证

验证代码如图所示：

![](https://qcloudimg.tencent-cloud.cn/raw/63e91f86f3194b3529993271dd2b995b.png)

其中初始化用到的 sdkappid 由在步骤一种获得，登录使用到的 usersig，可在 [控制台辅助工具](https://console.cloud.tencent.com/im/tool-usersig) 生成。在生产环境， usersig 由业务侧后台生成。本篇入门教程只演示了初始化、登录、注册消息监听事件的 API 调用，完整的 API 文档可以查看 [此处](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html)。UE5各个平台均集成的是 C++ SDK，且所有接口一致。

在 UE5 控制台中见到如下日志，代表 plugin 集成成功：

![](https://qcloudimg.tencent-cloud.cn/raw/0f3cf5aa62cfc4e015c5862f393b1315.png)

![](https://qcloudimg.tencent-cloud.cn/raw/52231b764244ce2fa560dd591ce0a6fe.png)
## 相关文档

- [API 文档](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMManager.html)
- [UE5 官方文档](https://docs.unrealengine.com/5.0/zh-CN/)

## 常见问题

1. 在 mac 调试环境，如遇到提示文件已经损坏，可执行如下命令修复：
<dx-codeblock>
:::  sh
 sudo xattr -r -d com.apple.quarantine $pathToframgeWork 
:::
</dx-codeblock>
2. 初始化传入的日志和 db 目录，需要应用有读写权限。
3. 插件暂不支持win32和Mac M1进行调试和编译。
