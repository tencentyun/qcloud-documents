bucket-tagging 命令用于创建（修改）、获取、删除存储桶标签。

## 命令选项
bucket-tagging 命令包含以下可选 flag：

|flag 简写|flag 全称| flag 用途|
|----|----|----|
|-m|--method|指定需要进行的操作，包括 put、get、delete   |

>? 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

## 添加或修改存储桶标签

存储桶标签用一组健值对（Key-Value）来表示，只有存储桶所有者及拥有 PutBucketTagging 权限的用户才可以添加或修改存储桶标签，否则会返回错误码 403 AccessDenied。

### 命令格式

```plaintext
./coscli bucket-tagging --method put cos://<BucketName-APPID> key1#value1 key2#value2
```
其中，`key#value`表示标签键值对 Key-Value，key 和 value 之间以`#`分割。若存储桶未设置标签，此命令将为存储桶添加指定的标签；若存储桶已设置标签，此命令将覆盖原有的标签。

### 操作示例

为存储桶 exmaplebucket-1250000000 配置两组标签，其中一组标签的 key 为1，value 为111，一组标签的 key 为2，value 为222。命令如下：

```plaintext
./coscli bucket-tagging --method put cos://exmaplebucket-1250000000 1#111 2#222
```

## 查询存储桶标签
### 命令格式

```plaintext
./coscli bucket-tagging --method get cos://<BucketName-APPID>
```

### 操作示例

```plaintext
./coscli bucket-tagging --method get cos://exmaplebucket-1250000000
```

以下输出结果表明 exmaplebucket-1250000000 配置了两组标签，其中一组标签的 key 为1，value 为111，一组标签的 key 为2，value 为222。

```plaintext
  KEY | VALUE  
------+--------
    1 |   111  
    2 |   222 
```

## 删除存储桶标签

### 命令格式
```plaintext
./coscli bucket-tagging --method delete cos://<BucketName-APPID>
```


### 操作示例

```plaintext
./coscli bucket-tagging --method delete cos://exmaplebucket-1250000000
```
