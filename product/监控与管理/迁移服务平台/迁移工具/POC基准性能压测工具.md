## 镜像获取并导入

### 腾讯云导入

镜像地址：https://tool-release-1305426035.cos.ap-shanghai.myqcloud.com/benchtool-img-latest.raw

使用msp迁移到自己的cos中，或者下载下来上传到自己的cos桶中，使用镜像的导入功能从cos桶导入镜像。

![](https://qcloudimg.tencent-cloud.cn/raw/6bdbe21c94756d7dd2937dfe6217c128.png)

阿里云导入

镜像地址：https://tool-release.oss-cn-shanghai.aliyuncs.com/benchtoolimg_m-uf6bf66km21460pwjcj5_system.raw.tar.gz

下载下来上传到自己的oss桶中，使用镜像的导入功能从oss桶导入镜像,如下图所示，导入即可。

![](https://qcloudimg.tencent-cloud.cn/raw/3ee758f70b1715ea975e7940b8c7612a.png)

## 通过镜像创建服务器

- 如果测试云主机性能，创建需要测试对应规格的云主机。

- 如果测试数据库性能，建议创建高于数据库实例规格的云主机（例如数据库规格4核8G，建议测试服务器4核或8核），确保压力机性能高于被测实例。

从镜像创建实例后，使用浏览器直接访问8081端口，即可进入测试工具界面。

##  测试

1. ###### 进入主机测试界面，先添加测试项。![](https://qcloudimg.tencent-cloud.cn/raw/2690ea406143eccc03f3fdeb95341586.png)

2. 在“测试项”下拉菜单中，选择需要测试的项目（如需测试多个项目，可多次添加不同的测试项，同一个测试项也可以使用不同的测试参数添加多次）。![https://qcloudimg.tencent-cloud.cn/raw/7d21ee083a1945233bf0d7c99d72dd87.png](https://qcloudimg.tencent-cloud.cn/raw/7d21ee083a1945233bf0d7c99d72dd87.png)

3. 添加测试项时，工具会设置默认的测试参数值，可根据需要进行调整。![](https://qcloudimg.tencent-cloud.cn/raw/29226a057100df46820a7694a386f907.png)

4. 当需要测试的项目添加完成后，在测试项列表界面确认，确认无误点击“启动测试”。![](https://qcloudimg.tencent-cloud.cn/raw/935e7e968448e62943cbcc4d60a8d7be.png)

5. 在导航栏的“结果查询”中，可以查看测试任务的状态。![](https://qcloudimg.tencent-cloud.cn/raw/710848e2f3f1d22a6417a12a2d5c36f6.png)

6. 点击“测试组ID”，可查看该测试组（包含多个测试项的任务）详情。![](https://qcloudimg.tencent-cloud.cn/raw/8142a5f06ec6965a6fff5cc456505854.png)

7. 当测试任务执行完成后，可在测试组详情中查看测试结果，也可通过“查看日志”查看测试细节。![](https://qcloudimg.tencent-cloud.cn/raw/07694d3c80600fa144fb713f843dc9c2.png)

8. 其他产品（Redis、MySQL、CBS）测试均与主机测试方式相同。