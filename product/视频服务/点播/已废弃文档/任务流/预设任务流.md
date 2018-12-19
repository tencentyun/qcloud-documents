## 简介

预设任务流是点播系统内置的通用化的任务流模板，目前暂时只有QCVB_SimpleProcessFile。

注意：任务流的概念以及用法可以参见[任务流综述](/document/product/266/10263)。

## 内置任务流列表
| 任务流名称 | 任务流功能 |
|---------|---------|
| QCVB_SimpleProcessFile | 转码，设置水印，采样截图，使用截图设置视频封面|

## QCVB_SimpleProcessFile

简单的ProcessFile，支持转码，水印，设置封面，采样截图。
QCVB_SimpleProcessFile(transcodeDefinition, watermarkDefinition, coverBySnapshotDefinition, sampleSnapshotDefinition)

## 参数说明

| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| transcodeDefinition | 是 |Integer/Array | 转码模板号，参见[转码参数模板](/document/product/266/8098)。 |
| watermarkDefinition | 是 |Integer  | 水印模板号，参见[水印参数模板](/document/product/266/9647) |
| coverBySnapshotDefinition | 是 |Integer | 使用截图设置视频封面模板号，参见[截图参数模板](/document/product/266/8097)。 |
| sampleSnapshotDefinition | 是 |Integer | 采样截图模板号，参见[采样截图参数模板](/document/product/266/9050) |

## 使用示例

### 获取元信息示例

```
QCVB_SimpleProcessFile()
```
以下示例的含义是：
1. 对视频获取元信息，即视频的长、宽、码率等数据；

### 使用控制台配置的规格转码示例
```
QCVB_SimpleProcessFile(1, 1, 10, 10)
```
以下示例的含义是：
1. 对视频进行转码，转码模板为控制台配置的模板；
1. 转码过程需要设置水印，水印模板号为1，即默认模板；
1. 对视频设置封面，封面图片为视频首帧，截图模板号为10；
1. 对视频进行采样截图，采样截图的模板号为10；


### 指定视频规格转码示例
```
QCVB_SimpleProcessFile({210,220}, 10, 10, 10)
```
以下示例的含义是：
1. 对视频文件进行转码，目标输出模板为210，220；
1. 转码过程需要设置水印，水印模板号为10；
1. 对视频设置封面，封面图片为视频首帧，截图模板号为10；
1. 对视频进行采样截图，采样截图的模板号为10；

## 获取结果
1. 任务流状态变更（或者处理完成）会触发[事件通知-任务流状态变更通知](/document/product/266/9636)。APP后台可据此监听任务流的执行状态。
2. 任务流执行完毕之后，任务结果可以从[GetVideoInfo](/document/product/266/8586)中获取。 
