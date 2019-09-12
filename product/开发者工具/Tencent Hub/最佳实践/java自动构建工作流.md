本文主要叙述如何实践一条 Java 自动构建工作流。


### 操作页面
在项目仓库页面->工作流->新建工作流。

### 实践步骤
1.新建工作流，填写工作流基础设置信息。如还未绑定源代码授权，请参考 [源代码授权设置](https://cloud.tencent.com/document/product/857/18192)。
![](https://main.qcloudimg.com/raw/49d13fe45977263991a02491708274db.png)
   
2.新增一个 Stage，设置 Stage 信息。
![](https://main.qcloudimg.com/raw/32d74d45be5ef514f27cbdaea0b4d7d0.png)
   
   
3.新增一个 Job，设置 Job 信息，选择工作流组件。
![](https://main.qcloudimg.com/raw/c5c4a87049e19153119929f76aed6fdb.png)  

4.Tencent Hub 预置了一些工作流组件，并给这些组件都打上了关键词标签。可以通过组件标签来筛选出符合您需求的工作流组件。例如通过 Java 和 build 筛选出支持 Java 语言构建的工作流组件。 
![](https://main.qcloudimg.com/raw/0df89d295c62665551476ef64b9aa55d.png) 

5.填写组件需要的参数。
![](https://main.qcloudimg.com/raw/fefa3168c82bf139de319f41d27aca54.png)

6.参数的值可以输入填写，也可以使用环境变量。例如，组件需要的 GIT_CLONE_URL 参数，就可以使用工作流绑定了源代码授权后生成的环境变量`${_WORKFLOW_GIT_CLONE_URL}`。
![](https://main.qcloudimg.com/raw/b0f17ef56b3a80f9ba9c7e41a325212c.png) 

7.填写完成组件需要的参数，保存工作流。
![](https://main.qcloudimg.com/raw/ac8dee3bc4f5b003f6f59404e313e178.png)

8.运行工作流。
![](https://main.qcloudimg.com/raw/75de94e3d93be1d58bc8dc0cd888a54f.png)

9.运行成功后，可以看到项目仓库的文件管理下，自动生成了构建结果。
![](https://main.qcloudimg.com/raw/25435f92f272bb6141ac739ab8be142a.png)
![](https://main.qcloudimg.com/raw/d14f43f313bf519f7a5f8404323cbe74.png)
   
