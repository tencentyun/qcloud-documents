请确保您在执行此示例时，已经获得了 SCF 使用权限。申请内测权限请点击[这里](https://www.qcloud.com/act/apply/SCF)

```
注意：
1. 源 Bucket、目标 Bucket 和函数必须位于同一个地域下。在本教程中，我们将使用华南（广州）区域。
2. 必须使用两个COS Bucket。如果使用同一个 Bucket 作为源和目标，上传到源存储桶的每个缩略图都会再次触发函数，从而产生不必要的递归。
```
1) 登录腾讯云控制台，选择【对象存储服务】。

2) 点击【Bucket列表】选项卡下的【创建Bucket】按钮，新建源 COS Bucket。

3) 设置COS Bucket的名称如`srcmr`，选择地域为`华南`，设置访问权限为默认值`公有读私有写`并设置CDN加速为默认值`关闭`，点击【保存】按钮新建一个COS Bucket。

4) 按照相同的方式创建中间阶段 Bucket `middlestagebucket`和目标 Bucket `destmr`

5) 在源 Bucket（即srcmr）中，上传一个文本文件，本示例中使用了一个 [Serverless.txt](	http://srcmr-1251740579.cosgz.myqcloud.com/serverless.txt) 文本文件作为演示。（在实际关联 COS 前手动调用函数进行测试验证时，您要将包含该文件的示例数据传递给 SCF 函数，且 SCF 函数将根据该数据寻找相应的文件。因此您需要先创建此示例文件。）
![](//mc.qcloudimg.com/static/img/a80d72a80fe68e091109271f5cdba2b7/image.png)
