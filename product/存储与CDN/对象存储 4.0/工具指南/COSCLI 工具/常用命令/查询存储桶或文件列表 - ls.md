ls 命令用于查询所有存储桶列表、查询存储桶下的文件列表和文件夹下的文件列表。

## 命令格式

```plaintext
./coscli ls [cos://bucketAlias[/prefix/]]
```

>? 
>- 有关 bucketAlias 的说明，请参见 [下载与安装配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

ls 命令包含以下可选参数：

| 参数格式          | 参数用途       | 示例                 |
| ----------------- | -------------- | -------------------- |
| cos://bucketAlias | 指定存储桶     | cos://bucket1          |
| /prefix/          | 指定某一文件夹 | /picture/ |




## 操作示例


### 列出当前账号下所有存储桶

```plaintext
./coscli ls
```

### 列出文件

#### 列出 bucket1 存储桶中的所有文件

```plaintext
./coscli ls cos://bucket1
```

#### 列出 bucket1 存储桶中 picture 文件夹下的所有文件和文件夹

```plaintext
./coscli ls cos://bucket1/picture/
```


