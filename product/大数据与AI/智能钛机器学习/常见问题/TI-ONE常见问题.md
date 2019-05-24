**1.初次新建工程时需进行COS一键授权，若授权失败，如何手动进行COS授权？**
 登录此链接https://console.cloud.tencent.com/cam/role
点击【新建角色】-选择【腾讯云产品服务】，![](https://main.qcloudimg.com/raw/6923e6ee8d03ed121f05e8879e1c1ab0.png)



勾选中【智能钛自动机器学习】，点击【下一步】，

![](https://main.qcloudimg.com/raw/260463bd14d36fc4dc03dfc30b4bdf76.png)



在【策略列表】中搜索【QcloudAccessForTIRole】，并选中，点击【下一步】，

![](https://main.qcloudimg.com/raw/4f179a7087115fa560a2005d6189d4a1.png)



在【角色名称】填写【TI_QCSRole】，【角色描述】选填【腾讯智能钛(TI)操作权限含列举对象存储(COS)文件，读取、删除、添加、修改文件内容等 】。点击【完成】，即手动完成COS授权。

![](https://main.qcloudimg.com/raw/a7d9ab99a0635eba0b751b7ccd3fce1a.png)



创建完成显示如下图：

![](https://main.qcloudimg.com/raw/da5c133ee42abd41987da5ace84305d8.png)



**2.当在创建模型或部署模型过程中报错“无法访问COS资源的权限”时怎么办？**

登录<https://console.cloud.tencent.com/cam/role>，检查是否完成COS授权给智能钛产品。

若检查结果为已授权，存在角色：TI_QCSRole，建议删除此角色，重新手动授权。

![](https://main.qcloudimg.com/raw/fdb404218a807890762516fd399c844d.png)



如不存在角色：TI_QCSRole，需手动进行COS授权，请参照手动授权。



**3.为什么平台内置demo没有运行按钮？**

内置demo需复制到自己的的工程中方可运行，操作步骤如下：

1. 在 【我的工程】-【典型任务流】中，单击【复制】

2. 选择工程名称，单击【保存】，复制成功。

   ![](https://main.qcloudimg.com/raw/2dc05379b4cd6a7b22b2b90f820f2fc7.png)

3. 单击复制的工作流，进入画布。

4. 单击如下图标，开始运行任务流。

![](https://main.qcloudimg.com/raw/75e4f97f9ebcd1eb3f45be97654bb0b7.png)



**4.COS上传数据太慢怎么办？**

建议使用COS客户端，具体操作可参考：<https://cloud.tencent.com/document/product/436/11366>



**5.每个账号创建工作流的数量是否有限制？**

目前没有限制



**6.智能钛机器学习平台的资源配置是怎样的？**

一般情况下：10CPU,1GPU,内存20G。



**7.在智能钛平台训练好的模型是否可以下载到线下使用？**

在平台训练好的模型支持导出，可下载到线下使用。右键【模型图标】，点击【模型操作】-【导出模型】即可。

![](https://main.qcloudimg.com/raw/d6f7d14804a1c7204c4d9e3196630304.png)



**8.智能钛机器学习平台是否支持从外部导入模型？**

支持，在【模型仓库】页，单击页面上方【导入模型】，可以将外部的模型导入平台进行统一管理，支持来源为用户的 COS 路径与本地上传，支持的格式为 PMML/ANGEL/TFServing。

![](https://main.qcloudimg.com/raw/f2100380fd6edd1eca95cd2ef6e7f6c9.png)



**9.模型部署时如何选择正确的运行环境？**

目前平台支持3种运行环境：

1. pmml，一般使用机器学习时选择此运行环境；
2. tfserving，一般使用深度学习时选择此运行环境；
3. angel，此环境一般针对angel算法，后续会支持此种算法。



![img](https://qqadapt.qpic.cn/txdocpic/0/e132808aabeb7db38d8ab08b2c390879/0)



**10.智能钛机器学习平台的机器学习算法是可以分布式运行的吗？**	

平台基于spark和angel开发的，都是分布式的。



**11.智能钛机器学习平台是用的spark的mlib吗，不是sklearn？**

使用组件，您也可以写基于sklearn的代码来跑。



**12.使用组件的话，需要上传numpy这些吗？**

Tensorflow的组件自带numpy的。



**13.智能钛机器学习平台的中间运算，代码格式是什么，用什么语法？**

机器学习是基于spark的，同时支持scala和python（pyspark）。



**14.智能钛机器学习平台的SQL语法支持哪些，DDL,DML,完全兼容ANSI SQL 2003么？**

目前暂不支持SQL语法。



**15.智能钛机器学习平台Tensorflow组件是否支持导入python的pyd文件**？

支持，但是pyd文件无法放在压缩包中导入，应该单独放在依赖文件(不能压缩)或者放在cos上， 然后在程序依赖中填入cos路径即可。

![](https://main.qcloudimg.com/raw/ae2e6d59c92400f9be925f7f136dfcaa.png)



**16.为什么有时python代码很简单，但Tensorflow任务却需要运行很长时间？**

原因可能是您在“程序依赖”中填了一个cos路径， 这个路径下面不止包含python的依赖文件，还包含大量的数据文件。 Tensorflow组件把这些数据文件当做依赖导入，所以耗时很久。

![](https://main.qcloudimg.com/raw/891c846834a58bed1923d5e81633d895.png)