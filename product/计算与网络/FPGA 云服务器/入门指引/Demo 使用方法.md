## Demo 简介
本文档主要介绍基于 FPGA Alexnet 模型做图片分类的 Demo，其主要组成部分和使用方法。

## Demo 目录
FPGA 云服务器入门指引 Demo 放置在`/data/fpga_classify_demo`目录下，Demo 目录如下：
- bin
- build
- src
- include
- lib
	- caffe
	- fpga_classify
- test
 - script

>!FPGA 中做 Alexnet 图片分类的 API 放在 Demo 的`lib/fpga_classify`目录下。

## 图片目录
FPGA 云服务器入门指引图片目录放置在 `/data/images` 目录下，保存了10764张测试图片。
## 模型目录
FPGA 云服务器入门指引模型目录放置在 `/data/models` 目录下，保存了在 ImageNet LSVRC-2012 比赛中使用的 Alexnet 的网络结构、模型参数文件、图片均值文件和标签文件等。
## Demo 使用说明
1.	进入 Demo 目录下的`build`目录，运行 `./build`。
2.	进入`test/script`目录，运行`./test_demo.sh`。
3.	结果保存在当前目录下`fpga_res.txt`文件中，文件内容为`/data/images`目录下所有图片的分类结果。本文档展示的 Alexnet 模型结果为千分类，仅展示概率最高的3种分类。
取其中2行分类结果如下所示：
```
n03978966_12321 : ["n03595614 jersey, T-shirt, tee shirt", 0.9920]	["n04370456 sweatshirt", 0.0047]	["n04532106 vestment", 0.0026]
n04127633_18545 : ["n04252225 snowplow, snowplough", 0.1553]	["n03384352 forklift", 0.1499]	["n03649909 lawn mower, mower", 0.0640]
```

#### 说明：
-  第1列表示图片名。
- 其他每一列用中括号分隔，表示该图片分类得到的标签及标签对应的得分值。得分值表示图片属于这个标签的概率，范围在[0.0,1.0]之间，0.0 表示完全不可能，1.0 表示100%。
-  所有标签的得分值总和为1.0。
-  分类标签按得分降序排列。

#### 该结果表明：
FPGA 云服务器经过 Alexnet 模型分类后，
图片  n03978966_12321：属于类别标签 jersey， T-shirt， tee shirt 的概率为99.20%，属于类别标签 sweatshirt 的概率为0.47%，属于类别标签 vestment 的概率 0.26%。
图片 n04127633_18545：属于类别标签 snowplow, snowplough 的概率为15.53% ，属于类别标签 forklift  的概率为14.99%，属于类别标签 lawn mower, mower 的概率为6.4%。
