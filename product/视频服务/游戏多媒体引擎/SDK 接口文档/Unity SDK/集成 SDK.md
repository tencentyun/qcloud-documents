为方便 Unity 开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍适用于 Unity 开发的工程配置。


## 下载 SDK

1. 请先下载相关 Demo 及 SDK。详细下载链接请查看  [SDK 下载指引](https://cloud.tencent.com/document/product/607/18521)。
2. 在界面中找到 Unity 版本的 SDK 资源。
3. 单击**下载**。下载完的 SDK 资源解压后有以下几个部分。文件说明如下表：
<table>
<thead>
<tr>
<th>文件名</th>
<th align="center">说明</th>
<th>作用</th>
</tr>
</thead>
<tbody><tr>
<td>Plugins</td>
<td align="center">SDK 库文件</td>
<td>存放导出各个平台的库文件</td>
</tr>
<tr>
<td>GMESDK</td>
<td align="center">SDK 代码文件</td>
<td>提供 API 接口</td>
</tr>
</tbody></table>


<dx-alert infotype="explain" title="Unity SDK 平台支持">
Unity SDK 已同时集成 Windows、Mac、Android、iOS 平台架构。
</dx-alert>



## 工程配置步骤

### 步骤1：导入 Plugins 文件

将开发工具包中 Plugins 文件夹中的文件复制在 **Unity 工程**>**Assets**>**Plugins** 文件夹中，如图所示。
<img src="https://main.qcloudimg.com/raw/ce80710126e82b2af58090207a3ae077.png"  width="65%" /></img>



<dx-alert infotype="explain" title="">
如果不需要导出 win32 架构的可执行文件，请删除 Plugins 文件夹下的 x86 文件夹。
</dx-alert>




### 步骤2：导入代码文件

将开发工具包中 Scripts 文件夹中的文件复制在 Unity 工程中存放代码的文件夹中，如图所示：  
<img src="https://main.qcloudimg.com/raw/21e8b967c75ebdd2ea1686cfd434f89c.png"  width="65%" /></img>




## 音频设置

在 Unity 编辑器中，**Edit**>**Project Setting**>**Audio** 使用系统默认即可。如果进行修改，Unity 播放音效会因为在 iOS 上设置硬件缓存区受影响，表现为音效被打断。如图所示。
<img src="https://main.qcloudimg.com/raw/db8975fcaefa3dc71732ede1b5f979db.png"  width="50%" /></img>


<dx-alert infotype="forbid" title="Unity Audio Setting">
禁止设置 Project Setting 中的 Audio 模块。
</dx-alert>

若按照下图进行配置，则 Unity 播放音效会因为在 iOS 上设置硬件缓存区受影响，表现为音效被打断。如图所示。
![](https://main.qcloudimg.com/raw/0b1c09af7f42e39081cca1718baaede3.png)

## MacOS 平台使用操作

若在 MacOS 10.15.x 版本使用 Unity 集成 GME SDK，执行运行操作时报错显示文件已损坏，原因为 `com.apple.quarantine` 属性导致。
![](https://main.qcloudimg.com/raw/29aa9b69f32c13ffe3c6db4559c9ff17.png)
最直接的解决方案是删除 `com.apple.quarantine` 属性，具体操作步骤如下。
1. 通过终端执行 cd 命令快速定位到工程中的文件夹下：`Unity_OpenSDK_Audio/Assets/Plugins/`。
2. 执行以下命令。
```
$ xattr -d com.apple.quarantine gmesdk.bundle
```



<dx-alert infotype="explain" title="">
此操作有风险，建议使用低版本的 MacOS 进行接入。
</dx-alert>

