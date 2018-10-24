## 文件上传

进入 COS 管理控制台，点击想要上传文件的 Bucket 名称，进入 Bucket 的【文件列表】页面：

![](https://mc.qcloudimg.com/static/img/d3e05e819435efc8be79044d3e3b4b9d/image.png)

点击页面上的 **上传文件** ，出现上传文件的对话框：

![](https://mc.qcloudimg.com/static/img/c6c29d0511ef2cfc59dd0d4dddf08f0b/image.png)

可以点击 **上传文件** 按钮或者 点击 **上传文件夹** ，选择多个本地文件或一个文件夹进行上传，部分浏览器支持拖拽多个文件或文件夹上传，已经选中文件到待上传文件列表后，列表区域仍然支持拖拽上传（下图红线框处出来的区域）：

![](https://mc.qcloudimg.com/static/img/39080355a65ed9728ec4fab3a7246053/image.png)

也可点击选择需要上传至的文件夹，或者创建一个新的文件夹，将 Object 上传至某个文件夹中。

## 任务管理

点击 **确认上传** 后，便会在任务管理列表里面创建相应的上传任务。用户可以在任务列表里面查看上传进度、终止未完成的任务、查看失败任务的原因。

![](https://mc.qcloudimg.com/static/img/e502373933234c93c1fcd7aa475fa040/image.png)

注意：控制台单个文件最大支持50G， 超过50G的文件将无法上传成功。同时，包含保留字（请参考文件夹创建命名规则）的文件夹名称也无法上传成功。



## 上传成功

在当前路径下，有文件成功上传后。页面会有刷新提醒，用户可以点击 **刷新** 按钮获取最新的文件列表。
![](https://mc.qcloudimg.com/static/img/dfa7880f6c2efacb9e8804420e38bcbd/image.png)


## 不完整文件 和 断点续传

上传中断的文件会以 “不完整的文件” 的形式存储下来。用户可以查看 “不完整的文件” 的文件信息，但无法下载、修改访问权限、设置自定义权限等。当用户用户下次上传相同文件时，不需要其他操作，文件会自动从断点部分继续上传。

![](https://mc.qcloudimg.com/static/img/f2e8982eaad79aab5e54a48c7b52237d/image.png)

