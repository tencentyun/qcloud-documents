## 场景背景

图像分类是深度学习算法的一个典型应用，本案例的内容是训练深度学习模型用来对花朵的照片进行分类。

我们使用的训练数据包括 5 类花朵的照片，分别是：

菊花（Daisy，633 张）
![](https://main.qcloudimg.com/raw/dda11f7c4e82f05f3826bd3c08acb30b.png)

蒲公英（Dandelion，375 张）
![](https://main.qcloudimg.com/raw/95c67051a0c6a0b1fd2a7a5477b3b21b.png)

玫瑰（Rose，641 张）
![](https://main.qcloudimg.com/raw/8bddd4618aeaa57c8d010cb1abd33d13.png)

向日葵（Sunflower，675 张）
![](https://main.qcloudimg.com/raw/40ef12639358fd175a89b04b2c73ab31.png)

郁金香（Tulip，766 张）
![](https://main.qcloudimg.com/raw/1cc5578aa6f248f4297d63f5e7912bc3.png)

在本场景中，我们用 tensorflow 中的 CNN 网络训练模型，训练完成后部署发布，发布后的模型可以用 http 的方式调用，识别传入的图像，返回分类的结果。

## 案例相关材料
相关材料下载链接：
 - [LICENSE.txt](https://main.qcloudimg.com/raw/bf4914e86227a9b374866bfb04cc87d7/LICENSE.zip)
 - [Daisy.zip](https://main.qcloudimg.com/raw/dbaa773d5421b0476217ed21661bd7f0/daisy.zip)
 - [Dandelion.zip](https://main.qcloudimg.com/raw/e7f584e36b553d5626e23971c3022b1a/dandelion.zip)
 - [Rose.zip](https://main.qcloudimg.com/raw/221a005375287a1f9b727dcf2a6e96b8/roses.zip)
 - [Sunflower.zip](https://main.qcloudimg.com/raw/1c4a629c2ce06f4ade99b169897acec5/sunflowers.zip)
 - [Tulip.zip](https://main.qcloudimg.com/raw/2f8824a9fb5efeb583041a07760fecad/tulips.zip)

## 整体流程

该 Demo 的整体流程如下图所示：
![](https://main.qcloudimg.com/raw/cb0c8d4fa83b22903a9a9a6d5acafec8.png)

包含 4 个环节，分别是：

1.  [指定存储图片的 COS 位置](#jump1)
2.  [将数据拆分成训练集和测试集](#jump2)
3.  [对数据做特征处理](#jump3) 
4.  [训练花朵分类的深度神经网络模型](#jump4) 


## 流程详解

### 新建工程和工作流
1. 登录 [TI-ONE](https://tio.cloud.tencent.com)控制台，进入 TI-ONE 项目列表页。单击【+新建工程】。
    ![](https://main.qcloudimg.com/raw/632a3f15ff510e33dbb90061371a7db9.png)

2. 填写工程名称和工程描述等相关信息。
    ![](https://main.qcloudimg.com/raw/e8b2d533ede8e55b24c63c96ade15825.png)

3. 登录腾讯云 [对象存储控制台](https://console.cloud.tencent.com/cos)，单击【储存桶列表】>【创建储存桶】。
    ![](https://main.qcloudimg.com/raw/e4cdfaa79d7881d63df4e88f80cdfce2.png)

4. 创建成功后在新建工程页下拉列表处选取储存桶。
    ![](https://main.qcloudimg.com/raw/645d2203a91e7ea715d41769a964dc74.png)

5. 单击新建工程页面的 API 密钥管理链接，进入 COS 控制台，单击【密钥管理】>【云 API 密钥链接】进入密钥界面。
    ![](https://main.qcloudimg.com/raw/3697b0510ed3e6403150e0b4ce3632f2.png)

6. 单击新建密钥进行密钥创建-复制创建好的 SecretId 和 Secretkey，在新建工程页面粘贴，单击保存。
    ![](https://main.qcloudimg.com/raw/51d455f62142ca9d18f5ee623e6221ef.png)

7. 完成新建工程后，单击“+号”新建工作流。
    ![](https://main.qcloudimg.com/raw/11c67f72ffef272fafcf5554284fee42.png)

8. 输入工作流名称。
    ![](https://main.qcloudimg.com/raw/a73d5ff291b45b391da2e0fbc3b4e0d9.png)

9. 单击确认，进入画布。
    ![](https://main.qcloudimg.com/raw/39115fe695132ca714a34d2019b60cea.png)

<span id = "jump1"></span>
### 设置数据源

1. 本案例的训练样本是图片，数据量比较大（约 200 M），因此我们先将训练样本上传 COS，在工作流中通过引入 COS 数据源。
![](https://main.qcloudimg.com/raw/3fcd8910a2aea840315ec57fd884ac92.png)

2. 左边栏选择：输入>数据源>COS 数据源。

3. 拖入画布，填写参数：
	- COS 数据路径：填写 COS 上保存训练样本的路径，加`\${cos}`前缀，在本例中填写`\${cos}/flower/data/`。
![](https://main.qcloudimg.com/raw/e0b9da0c6b55a9dee7200d6f35aaca13.png)

<span id = "jump2"></span>
### 拆分数据

1. 使用 splitdataset 组件拆分数据，将图像文件拆分成用于训练和测试的两个 part，输出路径中保存 3 个文件，label_map.txt、train.txt 和 valid.txt，label_map.txt 记录类目到 label 的映射，train.txt 记录训练集索引（图片文件名），valid.txt 记录测试集索引（图片文件名）。
> **注意:**
> 本案例中使用到的路径都要提前在 COS 中创建好。

2. 左边栏选择：输入>数据转换>Split dataset。

3. 右键重命名：拆分数据。

4. 填写参数：
 - 图像存储路径：`\${cos}/flower/data/`
 - 输出路径自动生成，支持修改。
 - 分类or检测任务：Classification
 - 验证集比例：0.2
 - GPUs：0
 - CPUs：1
 - Memory(m)：1024
![](https://main.qcloudimg.com/raw/580610939ec6445e696a780449be772b.png)

<span id = "jump3"></span>
### 特征处理

1. 使用 image>tfrecord 从图像文件中提取特征。

2. 左边栏选择：输入>数据转换>image>tfrecord (Image Classification)。

3. 右键重命名：特征处理。

4. 填写参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 图像存储路径：`\${cos}/flower/data/`
 - 是否分类任务：True
 - images/split（每份record文件所含图像数，在数据集较大时将存储成多份文件）：1000
 - GPUs：0
 - CPUs：1
 - Memory(m)：1024
![](https://main.qcloudimg.com/raw/e053fcfd373053bb1c13e8a88a8745ef.png)

<span id = "jump4"></span>
### 花朵分类模型训练

1. 选择 AlexNet 作为本次训练花朵分类模型的算法，AlexNet 是一种 CNN 算法。

2. 左边栏选择：算法>深度学习算法>计算机视觉>AlexNet。

3. 右键重命名：花朵分类模型。

4. 填写参数:
 - 输入数据根据连线自动生成。
 - 测试数据若未生成，则需要用户手动将上一组件与本组件相连，重新点开参数配置栏，测试集数据根据连线自动生成。
 - 可视化文件存储路径：`\${cos}/flower0513/out`
 - 初始化模型（基础模型输入，如没有则填 0）：0
 - 类别数：5
 - 类别标签映射文件：`\${cos}/flower0513/out/label_map.txt`。
 - 批量处理大小：16
 - 迭代次数：100
 - 初始学习率：0.01
 - 学习率衰减步数：1000
 - 学习率衰减因子：0.1
 - 正则化因子：0.0005
 - GPUs：1
 - CPUs：3
 - 其余使用默认值。
![](https://main.qcloudimg.com/raw/0025454c3634ed17e6e68b48e102d80d.png)


## 操作说明

### 保存工作流

单击工具条上的磁盘图标，保存工作流。
![](https://main.qcloudimg.com/raw/0e21a190a359c58c5d3648d290938b5f.png)

### 运行完整流程

单击工具条上的“三角”箭头，运行完整的流程。
![](https://main.qcloudimg.com/raw/9d18c789ac2294f365cec1f17f45f804.png)


### 从指定环节开始运行

右键单击要运行的环节，选择“起点运行”，从该环节开始向下执行：
![](https://main.qcloudimg.com/raw/941f880096f68bf340fcd6750bcb8bcd.png)


### 部署模型

1. TI-ONE 平台支持将模型部署后发布为服务对外服务，可以方便地使用训练好的模型。
![](https://main.qcloudimg.com/raw/bf49617dc11c1311ed72cc07b5f4925a.png)

2. 模型训练运行成功后，右键单击模型左侧的尾巴，选择“模型操作”>“模型部署”。

3. 填写部署参数

 -  模型组：选择需要部署的模型组，如果没有可选的模型组需要事先在“模型管理”菜单里新建模型组。

 -  实例类型：选择实例运行的配置，本例中选择“GPU”。

 -  实例数：1

 -  服务分类：根据模型类型选择，本例中选择“深度学习”。

 -  部署版本：实例的版本，本例中选择“新增版本”。

    ![](https://main.qcloudimg.com/raw/f448443a2065b32c9c5d52bc62b7ff55.png)

4. 单击确定开始部署模型。
![](https://main.qcloudimg.com/raw/072e37dff69204d95b85ab108672c857.png)

5. 单击服务中的模型，可以获取服务详情。
![](https://main.qcloudimg.com/raw/6ce468ee9d872a7a807308f06b66bda0.png)



### 调用模型

1. 您可以使用命令行或在线调试工具调用模型服务，例如，使用 postman 来测试服务调用。[postman 下载地址>>](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=zh-CN)

2. 输入参数：
 - 服务地址：可从服务详情中获取。
 - 服务调用类型选择 post。
 - 参数选择“file”，输入需要上传的图片文件地址。
![](https://main.qcloudimg.com/raw/67e6d676f4f760ba9fb87ce6a124a586.png)

3. 单击【send】，发送调用请求，查看返回结果。

4. 返回结果解读：服务会返回模型对图片的分类结果，结果按照评分返回 top n 的类别，在本例中返回了 top 2 的结果，分别是蒲公英（Dandelion）和向日葵（Sunflower）。
```
{
		key: "classes"
		value {
			dtype: DT_STRING
			tensor_shape {
				dim {
					size: 1
				}
				dim {
					size: 2
				}
			}
			string_val: "dandelion"
			string_val: "sunflowers"
		}
	}
outputs {
		key: "scores"
			value {
			dtype: DT_FLOAT
			tensor_shape {
				dim {
					size: 1
				}
				dim {
					size: 2
				}
			}
			float_val: 0.000917751691304
			float_val: 0.000570954522118
		}
}
```


### 异常处理

当环节节点上出现感叹号，说明流程出现异常。鼠标悬浮于组件，可以查看失败原因。
![](https://main.qcloudimg.com/raw/0c308dac4a3d3a39519370e0a3739609.png)

右键单击该环节选择“TensorFlow 控制台”> “App 详情”查看日志，可以查看具体错误原因。
![](https://main.qcloudimg.com/raw/065542347f4c537a9d748cb1a9628ceb.png)

