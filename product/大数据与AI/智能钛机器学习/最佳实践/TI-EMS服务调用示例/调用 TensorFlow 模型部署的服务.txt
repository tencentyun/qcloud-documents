# 调用 TensorFlow 模型部署的服务
## 准备内容

1.经典深度学习 inception 模型：[inception_model.zip](http://ti-ems-1255502019.cosbj.myqcloud.com/tfserving/inception/inception_model.zip)

> 注：我们已经为您准备好了上述inception模型的cos访问地址：
>  cos://ti-ems-1255502019.cos.ap-beijing.myqcloud.com/tfserving/inception/1556451336。您可以输入该cos地址，也可以将模型文件夹下载下来，解压上传到自己的cos存储桶中，并在【创建模型服务配置】页面选择相应的模型文件夹。

2.测试图片: [image.encode](http://ti-ems-1255502019.cosbj.myqcloud.com/tfserving/inception/image.encode)

![](pics2/测试图片.png)

> 我们将上图测试花朵图片按照inception模型定义的JSON数据格式`{"instances":[{"b64": 图片 base64 编码}]}`进行编码，将jpg转换成base64。`image.encode`为经过编码的测试图片数据。

- base64编码

base 64 命令行工具可以将二进制图片编码为ASCII文本数据，大多数开发环境都包含原生base 64 命令行工具，要对图片文件进行编码，请执行以下操作：

Linux环境下

```shell 
base64 input.jpg > output.txt 
```
Mac  OSX环境下

```shell 
base64 -i input.jpg -o output.txt
```

## 环境配置

**模型运行环境:**  tfserving 环境

**资源配置：** 1CPU核2G内存


## 调用测试
单击【模型调用】，可获得当前服务的访问地址IP和密钥token。

![](/pics2/调用地址.jpg)

模型服务可以直接生成采用 POST 方法的服务接口，以供外界调用。这里使用 curl 工具为例，展示用户如何调用服务接口：

```shell
	curl -H "Content-Type: application/json" \
	-H "x-Auth-Token: TOKEN" \
	-X POST IP/v1/models/m:predict -d "@image.encode"
```

- 调用参数说明

TOKEN：通过点击模型服务页面的【服务调用】获取的密钥地址token

IP：通过点击模型服务页面的【服务调用】获取的服务访问地址

返回结果：

```shell
{
		"predictions:" [
			{
			   "probabilities": [5.39647e-07, 1.25255e-05, 0.99991, 3.78369e-06, 7.35335e-05],
			   "classes": "roses",
			   "class_idx": 2
			}
		]
	}
```

可以看出模型服务运行正常，并且正确的对发送的花朵进行了分类。

参考

TensorFlow 模型服务文档
