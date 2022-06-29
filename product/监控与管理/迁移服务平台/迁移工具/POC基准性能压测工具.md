## 步骤1：导入镜像

### 腾讯云导入镜像

1. 获取镜像。
镜像下载地址：[镜像地址](https://tool-release-1305426035.cos.ap-shanghai.myqcloud.com/benchtool-img-latest.raw)
2. 根据实际需求，选择不同操作进行导入：
 - 使用迁移服务平台（Migration Service Platform，MSP）将已获取的镜像迁移到对象存储（Cloud Object Storage，COS）bucket 中。
 - 自行将已获取的镜像上传到 bucket，并导入镜像。具体操作可参见 [导入镜像](https://cloud.tencent.com/document/product/213/4945#.E5.AF.BC.E5.85.A5.E6.AD.A5.E9.AA.A4) 文档。


### 阿里云导入镜像

1. 获取镜像。
镜像下载地址：[镜像地址](https://tool-release.oss-cn-shanghai.aliyuncs.com/benchtoolimg_m-uf6bf66km21460pwjcj5_system.raw.tar.gz)
2. 将已获取的镜像上传到 OSS 桶中，并导入镜像。具体操作可参见 [阿里云文档](https://help.aliyun.com/?spm=5176.19720258.J_3207526240.32.e9392c4awzPjR4)。

## 步骤2：通过镜像创建服务器

- 如果测试云主机性能，创建需要测试对应规格的云服务器。
- 如果测试数据库性能，建议创建高于数据库实例规格的云服务器（例如数据库规格4核8G，建议测试服务器4核或8核），确保压力机性能高于被测实例。

通过镜像创建实例后，使用浏览器直接访问8081端口，即可进入测试工具界面。

## 步骤3：测试

1. 进入主机测试界面，单击**添加测试项**。
![](https://qcloudimg.tencent-cloud.cn/raw/2690ea406143eccc03f3fdeb95341586.png)
2. 在弹出的窗口中，单击“测试项”下拉菜单，选择需要测试的项目（如需测试多个项目，可多次添加不同的测试项，同一个测试项也可以使用不同的测试参数添加多次）。
![](https://qcloudimg.tencent-cloud.cn/raw/aa94c5ffabbd54cfc031a5bddbc6a2ae.png)
3. 根据实际需要，调整测试参数，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/53273bdd176b64b96f027403fd3c8be8.png)
4. 待需要测试的项目添加完成后，确认测试项信息，单击**启动测试**。
![](https://qcloudimg.tencent-cloud.cn/raw/935e7e968448e62943cbcc4d60a8d7be.png)
5. 在左侧导航栏中，单击**结果查询**，查看测试任务的状态。
![](https://qcloudimg.tencent-cloud.cn/raw/710848e2f3f1d22a6417a12a2d5c36f6.png)
您可以对测试任务进行如下操作：
 - 单击**测试组ID**，查看该测试组（包含多个测试项的任务）详情。
![](https://qcloudimg.tencent-cloud.cn/raw/8142a5f06ec6965a6fff5cc456505854.png)
 - 单击**查看日志**，查看测试细节。
![](https://qcloudimg.tencent-cloud.cn/raw/ce3ba9b3c2a8111d5bfc48f5266a4c41.png)

其他产品（Redis、MySQL、CBS）测试均与主机测试方式相同。
