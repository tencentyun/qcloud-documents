本示例提供了一个图像分类应用的样例，使用 OpenVINO 运行环境，帮助您快速熟悉使用 TI-EMS 发布模型服务的过程。此示例针对 ImageNet 标签为230的图像数据集，然后使用经典深度学习 inception-v4 的图像分类模型，将此模型部署为在线服务，部署完成后，用户可通过在线服务识别输入图片的图像种类。

开始使用示例前，请仔细阅读准备内容罗列的要求，提前完成准备工作。

### 准备内容
**1. 经典深度学习 inception 模型：**[inception_v4_ir.tar](http://inception-v4-ir-1255502019.file.myqcloud.com/inception_v4_ir.tar)。
>?我们已经为您准备好了上述 inception 模型的 COS 访问地址：`cos://ti-ems-1255502019.cos.ap-beijing.myqcloud.com/models/OpenVINO/inception_v4_ir/1/`。您可以输入该 COS 地址，也可以将模型文件夹下载下来，解压上传到自己的 COS 存储桶中，并在【创建模型服务配置】页面选择相应的模型文件夹。

**2. 测试图片：** [imagenet_230.tar](http://ti-ems-1255502019.cosbj.myqcloud.com/test-data/imagenet_230.tar)（ImageNet label 为230的图片）

### 创建模型服务配置
1. 在【模型服务配置】页面单击【新建】，进入【新建模型服务配置】页面
2. **输入配置名称**：demo_openvino。
3. **选择地域**：地域为模型文件夹所在 COS 地域。
>?为您提供的 COS 访问地址地域为北京，如已将模型文件夹上传至到自己的 COS 存储桶，可选择自己 COS 存储桶所在地域
4. **选择运行环境**：单击【运行环境】，在弹出页面的【公共运行环境】栏选择 openvino。
![](https://main.qcloudimg.com/raw/4cee79efc4e2e8ffd8e79f685c1ea15d.png)
5. **提供模型文件地址**：直接输入 COS 访问地址或单击【对象存储 COS 文件】，弹出【对象存储 COS 文件】选择页面，选择 inception_v3 模型文件夹所在的路径，单击【确定】。
![](https://main.qcloudimg.com/raw/01e1b8e1886bf9de9a238506625bb09e.png)
6. **完成模型服务配置**：单击【确定】。
![](https://main.qcloudimg.com/raw/0559373163238a3509b123e3b0f89071.png)

### 启动服务
在模型服务配置页面找到 demo_openvino 配置，单击配置卡片的【在线推理】，进入启动服务页面。
**输入服务名称**：输入启动的服务名称。
**选择资源组**：选择将要启动的资源组，这里选择已购买的专用资源组。
**选择实例配置**：选择【CPU 配置】，实例配置填写为2核4G。
**实例调节策略**：选择【手动调节】，实例数量设置为1。
**选择是否生成鉴权**：勾选生成鉴权按钮，生成服务访问地址的鉴权密钥。
全部设置完成后，单击【启动服务】，进行在线服务列表页面。

### 获得访问地址和密钥
单击【模型服务】>【在线推理】页面选择 openvino 模型服务，在对应的【操作】列单击【更多】>【调用】，选择公网地址访问，获得模型服务的公网访问地址和密钥 TOKEN。

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
git clone https://github.com/tencentyun/ti-ems-client-examples
```
```shell
cd ti-ems-client-examples
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
- 使用如下命令行一键安装测试脚本所依赖的运行环境
```shell
pip install -r requirements.txt
```
请确保以上依赖安装成功。
- 运行客户端脚本
```shell
python grpc_client_openvino.py --server IP --token TOKEN --data_dir DATA_DIR
```
IP：服务访问地址。
TOKEN：服务密钥。
DATA_DIR：测试数据集所在路径。
>?不同模型输入的数据类型、数据 shape 可能不同，或对数据预处理要求不同。请根据具体模型，设计相应的访问程序。了解更多 [客户端程序](https://github.com/tencentyun/ti-ems-client-examples) 。

TI-EMS 使用过程中如遇任何问题，欢迎加入 [腾讯云 TI 平台开发者社区](https://cloud.tencent.com/developer/timl/ask)，与腾讯云 AI 专家和众多 AI 爱好者交流技术。
