NVIDIA GPU 系列实例提供了监控 GPU 使用率，显存使用量，功耗以及温度等参数的能力。
## GPU 监控工作条件

GPU监控是通过在GPU云服务上部署安装相关 [GPU 驱动](https://cloud.tencent.com/document/product/560/8048)和[云服务器监控组件](https://cloud.tencent.com/document/product/248/6211)来实现的，使用不同的镜像需要不同的处理方式：

1. 使用公共镜像：公共镜像默认包含云服务器监控组件，只需安装GPU驱动
2. [使用镜像市场GPU驱动预装镜像](https://cloud.tencent.com/document/product/560/30129)：无需任何安装
3. 使用导入镜像：需手动安装云服务器监控组件和GPU驱动

## 查看 GPU 工作参数

1. 访问控制台GPU实例的监控页面，GPU监控展示如下，移动鼠标到指标曲线上将显示对应GPU设备的BDF和监控数据

   ![](https://main.qcloudimg.com/raw/13ae6f53519093601fbeba86971ec7a0.jpg)

 2. 指标解释

    | 指标名称      | 含义                                       | 单位   | 维度    |
    | ------------- | ------------------------------------------ | ------ | ------- |
    | GPU使用率     | 评估负载所消耗的计算能力，非空闲状态百分比 | %      | per-GPU |
    | GPU显存使用量 | 评估负载对显存占用                         | MBytes | per-GPU |
    | GPU功耗       | 评估GPU耗电情况                            | W      | per-GPU |
    | GPU温度       | 评估GPU散热状态                            | 摄氏度 | per-GPU |

    

## 无监控数据原因

1. 只支持NVIDIA GPU实例
2. 只支持Linux操作系统
3. 没有安装GPU驱动或监控组件
4. [其他原因分析](https://cloud.tencent.com/document/product/248/17468)