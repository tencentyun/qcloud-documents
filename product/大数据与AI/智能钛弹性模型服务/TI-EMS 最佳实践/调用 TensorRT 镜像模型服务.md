### 准备内容
**1. 经典深度学习 inception 模型：**[inception_v3.tar](http://inception-v3-1255502019.coscd.myqcloud.com/inception_v3.tar)。
>?我们已经为您准备好了上述inception模型的cos访问地址：`cos://ti-ems-1255502019.cos.ap-beijing.myqcloud.com/models/tensorRT/inception_v3/1/`。您可以输入该 cos 地址，也可以将模型文件夹下载下来，解压上传到自己的 cos 存储桶中，并在【创建模型服务配置】页面选择相应的模型文件夹。

**2. 测试图片：**[imagenet_230.tar](http://ti-ems-1255502019.cosbj.myqcloud.com/test-data/imagenet_230.tar)（ImageNet label为230的图片）
### 创建模型服务配置
在模型服务配置页面单击【新建】，进入模型服务配置新建页面，输入配置名称：demo_tensorrt，单击【运行环境】，在弹出页面的【公共运行环境】栏选择 tensorrt。
![](https://main.qcloudimg.com/raw/2ec64b411f6aa2c671f51b93b65e4059.png)
单击【对象存储 cos 文件】，弹出 cos 文件选择页面，选择 inception_v3 模型文件夹所在的路径，单击【确定】。
![](https://main.qcloudimg.com/raw/bbec678b7252e153e5a5ccc1c622161f.png)
选择模型资源配置，单击【GPU 配置】，选择4核 CPU，8192MB内存，2TFLOPS 配置项。TensorRT 镜像一般要求：CPU 内存6GB以上，GPU 显存2G以上。模型服务配置创建完成之后，单击【确定】，进入模型服务配置页面。
![](https://main.qcloudimg.com/raw/66cc3e24d698d0738a0b69f4e036f5ea.png)
### 启动服务
在模型服务配置页面找到 demo_tensorrt 配置，单击配置卡片的【启动服务】，进入启动服务页面。
![](https://main.qcloudimg.com/raw/e7b2a5195603767ac22cf0814234ecc1.png)
在启动服务页面选择手动调节实例，实例数量设为1，单击【启动服务】，进入模型服务列表页面。
![](https://main.qcloudimg.com/raw/9cf83ec59d11d480bf7188d2e14c47c0.png)
### 获得访问地址和密钥
单击【启动模型服务】页面选择 demo_tensorrt 模型服务，在对应的【操作】列单击【调用】，即可获得 demo_tensorrt 模型服务的访问地址 IP 和密钥 TOKEN。
![](https://main.qcloudimg.com/raw/0d25e928082ab5ddf0f0a82d2ebb37f0.png)
### 获得模型元数据
以 Linux 系统为例，使用如下命令获取模型元数据：
```shell
curl -H "X-Auth-Token: TOKEN" IP:80/v1/models/m/metadata
```
**调用参数说明：**
TOKEN：通过点击模型服务页面的【服务调用】获取的密钥地址 token。
IP：通过点击模型服务页面的【服务调用】获取的服务访问地址。
### 调用模型服务接口
TI-EMS 模型服务支持以 gRPC 或 HTTP 访问，本示例使用 gRPC 访问模型服务。

- 下载服务调用示例脚本

```shell 
https://github.com/tencentyun/ti-ems-client-examples
```
```shell
cd client-examples
```

- 安装测试脚本依赖

测试脚本需要在 Python 环境下运行，运行前需要配置环境，requirements.txt 是运行测试脚本所需要的依赖库清单：
```shell
tensorflow-serving-api==1.13.0
tensorflow==1.13.1
grpcio==1.22.0
requests==2.22.0
numpy==1.16.3
opencv-python==4.1.0.25
```
使用如下命令行一键安装测试脚本所依赖的运行环境
```shell
pip install -r requirements.txt
```
请确保以上依赖安装成功。
- 运行客户端脚本

因为需要动态生成优化内核，TensorRT 镜像首次调用模型服务，根据模型大小不同可能需要等待0.5 - 5分钟。
```shell
python grpc_client.py --server IP --token TOKEN --data_dir DATA_DIR
```
IP：服务访问地址
TOKEN：服务密钥
DATA_DIR： 测试数据集所在路径
>?不同模型输入的数据类型、数据 shape 可能不同，或对数据预处理要求不同。请根据具体模型，设计相应的访问程序。了解更多 [客户端程序](https://github.com/tencentyun/ti-ems-client-examples) 。

TI-EMS 使用过程中如遇任何问题，欢迎加入 [智能钛 AI 开发者社区](https://cloud.tencent.com/developer/timl/ask)，与腾讯云 AI 专家和众多 AI 爱好者交流技术。
