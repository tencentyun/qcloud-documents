
如果您不再需要存储对象和文件，请先删除Object并彻底清空Bucket，最后删除Bucket。

### 1.删除 Object

- 进入 COS 管理控制台，进入要删除的文件所属 Bucket ，点击文件右侧操作栏中**删除**

![](//mc.qcloudimg.com/static/img/4972523a52c04f76023067bee1cfacb9/image.png)

- 点击**确认**，即可删除文件，删除后的文件原有的URL将立即失效。

> 注：目前Bucket管理控制台暂未支持批量删除功能，如需批量删除，请转到[开发者工具](https://cloud.tencent.com/document/product/436/7212)下载相关工具。


### 2.删除 Bucket

- 进入 COS 管理控制台，点击需要删除的 Bucket， 右侧操作栏中**删除**

![](//mc.qcloudimg.com/static/img/933169d4141d0c2dec0b3e35184bdbe5/image.png)

- 点击**确认删除** ，即可完成删除操作。

> 注：删除 Bucket 时，需保证其中没有任何文件、目录，否则将无法删除。


下一步:**流程结束**