Windows云硬盘扩容有以下两种场景：

- 对于新增的容量空间，建立独立的新分区，老的分区保持不变。
- 扩容旧的分区至新增的空量空间，并且保持老分区的数据不丢失。

以上两种场景在您的windows云硬盘升级成功之后（看到云硬盘容量变化），都可以通过 Windows 下的分区扩容工具分区助手完成分区扩容，并且保证原数据不会丢失。

## 前提条件
- 用户需要先完成 [扩容实体云硬盘](/doc/product/362/5747) 操作。
- 若此云硬盘上没有经过格式化和创建文件系统，直接在原有空白云硬盘基础上增加了容量，用户可以直接参考 [Windows 系统分区、格式化及创建文件系统](https://cloud.tencent.com/document/product/362/6734
)相关操作。

## 新空间格式化成一个独立分区
打开分区助手可以看到新扩容未使用的磁盘空间：
![](//mccdn.qcloud.com/static/img/8bb1180fb58f1dba376084eca29502e7/image.png)

右键选中未使用的磁盘空间，选择【创建分区】：
![](//mccdn.qcloud.com/static/img/2c9c621debf86e7ae91e55fdf42216fe/image.png)

在弹出框中，输入需要的分区大小、盘符和文件系统，然后点击【确定】按钮：
![](//mccdn.qcloud.com/static/img/2279a58dff1ecf399f53a660f46612f8/image.png)

在左上角点击【提交】任务按钮：
![](//mccdn.qcloud.com/static/img/e406a9ab0a907fc9f33708beaad45feb/image.png)

在弹出框中，确认格式分区的信息无误后，点击【执行】按钮：
![](//mccdn.qcloud.com/static/img/0eb80f57d7ade8eec8b86b9bc82a8f92/image.png)

再次确认格式分区的信息无误后，在弹出框中点击【是】按钮：
![](//mccdn.qcloud.com/static/img/b31c86dcc8e38644a8fe5835d2f676f5/image.png)

创建完成后，点击【确认】按钮：
![](//mccdn.qcloud.com/static/img/f424d22f58089ecf0712173484008945/image.png)

打开【我的电脑】可以看到新创建的磁盘分区(此例中新创建的是E盘)：
![](//mccdn.qcloud.com/static/img/f53c99dd35ec9f9af00eb2d1960522ef/image.png)

## 新空间增加到已有分区空间中
右键点击需要扩容的分区，选择【调整/移动分区(R)】：
![](//mccdn.qcloud.com/static/img/aacac81271ba88f35ea0dd6e25314977/image.png)

在弹出框中，如图所示，向右拖动小箭头调整分区需要的空间大小，然后点击【确认】按钮：
![](//mccdn.qcloud.com/static/img/d548f0c5f75f9171612581c77cad072b/image.png)

在左上角点击【提交】按钮：
![](//mccdn.qcloud.com/static/img/0b4e4e270c6b1e9ab43a747553119746/image.png)

在弹出框中，确认分区扩容信息正确无误后，点击【确认】按钮：
![](//mccdn.qcloud.com/static/img/aab479952f267a19585c789a9511cd84/image.png)

再次确认分区扩容信息后，点击【是】按钮：
![](//mccdn.qcloud.com/static/img/d9c99392f4542bebc1087f9d6790e722/image.png)

等待分区扩容完成后，点击【确定】：
![](//mccdn.qcloud.com/static/img/b06ca48c96f5c2230077b9e3430b779a/image.png)

打开【我的电脑】，可以查看到扩容后的分区变化(此例中扩容的是D盘，由60G扩容至109G)：
![](//mccdn.qcloud.com/static/img/cfb207b4364adc4e59cea68ad700271b/image.png)