### 创建 Notebook 时等待时间较长，是怎么回事？
目前创建时间在6分钟以内均为正常状态，还请您耐心等待。

### Notebook 运行到一半变为失败状态，是怎么回事？
- 若 Notebook 使用过程中出现内存或磁盘溢出，Notebook 会被停止，需要调大资源后重启下。
- 注意在使用 Notebook 中合理控制内存开销，同时关注磁盘大小。额外添加的存储资源挂载在 /home/tione/notebook 下面，尽量往该目录下存放数据和结果。
- 针对内存溢出，建议减小 batch size，数据分批读内存。

###  停止 Notebook 实例失败，长时间停止不成功，该怎么办？
如遇此种情况，可多次刷新页面，查看 Notebook 实例状态，若长时间停止不成功，请及时联系  [售后在线支持](https://cloud.tencent.com/online-service?from=connect-us) 进行处理。

###  运行中的 Notebook 支持修改相关配置信息吗？
支持的，但需要先停止 Notebook ，修改保存后，再重新启动。

### 如何在 Notebook 中查看已有依赖包以及安装第三方库。
请见官方文档：[安装第三方库](https://cloud.tencent.com/document/product/851/40119)。

### 若重启 Notebook 任务，之前自定义的安装包是否还存在？
不存在，需要重新进行安装。但可以通过生命周期脚本，使得重启后依赖包依然可用，详情请见官方文档：[使用生命周期脚本配置 Notebook 实例](https://cloud.tencent.com/document/product/851/43140)。

### 如何在 Notebook 中 切换 tione 账户 到 root 账户？
Notebook 中默认用 tione 账户运行，如果在使用中需要切换到 root 账户，则需要做以下操作：
1. 创建 Notebook 时选择开启 root 权限。
2. 在笔记本或者终端里通过 "sudo su -" 切换成 root。 
![img](https://main.qcloudimg.com/raw/d7a7a51ffbc2d4a5ef280b8829d28613.png)

###  Notebook 中使用 GPU 资源时，如何查看 CUDA 的版本信息？
进入 Notebook 实例内部，在 Terminal 中执行 `nvidia-smi` 命令进行查看，如下图所示： 
![img](https://main.qcloudimg.com/raw/8183b761851987a0cad28e68da219de9.png)

### 如何在 Notebook 终端里面切换内核？
可以通过 source activate 命令切换，支持以下内核：mxnet_py2、mxnet_py3、python2、python3、pytorch_py2 、pytorch_py3、tensorflow2_py3、tensorflow_py2、tensorflow_py3。例子：source activate tensorflow2_py3
