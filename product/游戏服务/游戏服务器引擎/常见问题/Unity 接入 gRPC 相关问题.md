

### 将下载的 `grpc_unity_package.VERSION.zip` 文件解压到 Unity 项目中后，Unity Editor 报错 （例如[ 缺陷22251](https://github.com/grpc/grpc/issues/22251) 中描述）怎么处理？
**解决方案**：重新下载 v2.26 版本 [grpc_unity_package.2.26.0-dev.zip](https://packages.grpc.io/archive/2019/12/a02d6b9be81cbadb60eed88b3b44498ba27bcba9-edd81ac6-e3d1-461a-a263-2b06ae913c3f/index.xml) 并解压。

### 打包 MacOS 服务端程序，运行时出现 `error: grpc_csharp_ext` 错误怎么处理？
<img src="https://main.qcloudimg.com/raw/703dc0dd20342b4aff5d499f2ac1df85.png" style="width: 718px;"></img><br>
**解决方案**：重命名  `Assert/Plugins/Grpc.Core/runtimes/osx/x64 ` 路径下的  `grpc_csharp_ext.bundle` 文件为 `grpc_csharp_ext`，再将文件拷贝到路径 `YourUnityApp.app/Contents/Frameworks/MonoEmbedRuntime/osx` 下，路径中不存在的目录新建即可。

### 打包 Linux 服务端程序，运行时出现 `Unable to preload the following plugins: ScreenSelector.so` 错误怎么处理？
<img src="https://main.qcloudimg.com/raw/f2926b2ac676f2e1e1ce85b8bae397f1.png" style="width: 718px;"></img><br>
**解决方案**：Unity Editor 中，在 **File**>**Build Settings** 下勾选  **Server Build**，重新打包。
<img src="https://main.qcloudimg.com/raw/3ffa6a320c4269669c411f32cf7597f0.png" style="width: 718px;"></img>

### 打包 Windows 服务端程序，并使用 GSE 提供的 Windows Server 2012 R2 数据中心版64位英文版镜像创建服务器运行时，出现如下图所示的问题怎么处理？
![](https://main.qcloudimg.com/raw/aeb980b1528b7796481f2e552a340c64.png)
**解决办法**：创建生成包时请选择中文版镜像，上传代码勾选中文版镜像，如下图所示：
![](https://main.qcloudimg.com/raw/a38258c58300923e502906a2b128524d.png)
