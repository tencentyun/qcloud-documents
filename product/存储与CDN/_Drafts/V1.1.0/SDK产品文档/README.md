
润色说明：

## 流程

1. 在_Draft下面，修改相关文档
2. 没有问题后再迁移到发布目录


## 关于标记

需要润色的SDK文档会在该SDK目录上面标记**待润色**。润色完成后，请修改为润色完成，并rtx:[stonedong](rtx://open?action=chat&member=stonedong)
## 检查部分


1. 检查错别字
2. 检查格式错误

## 文档左侧规则

每一个SDK都是如此

文档拆成了两个部分：

1. 入门文档
2. 接口文档

在整理的时候，按照这两个文档整理。


## 需要填充的部分

检查文档中是否有关于secretid、secretkey、bucket如何获取的说明，如果没有，则在合适的位置添加如下内容：


> 关于SecretID、SecretKey、Bucket等名称的含义和获取方式请参考:[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)


