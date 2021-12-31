ls 命令用于查询所有存储桶列表、查询存储桶下的文件列表和文件夹下的文件列表。

## 命令格式

```plaintext
./coscli ls [cos://bucketAlias[/prefix/]] [flag]
```

>? 有关 bucketAlias 的说明，请参见 [配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>

ls 命令包含以下可选参数：

| 参数格式          | 参数用途       | 示例                 |
| ----------------- | -------------- | -------------------- |
| cos://bucketAlias | 指定存储桶     | cos://bucket1          |
| /prefix/          | 指定某一文件夹 | /picture/ |

ls 命令包含以下可选 flag：

| flag 简写 | flag 全称   | flag 用途                            |
| --------- | ----------- | ------------------------------------ |
| -h        | --help      | 输出帮助信息                         |
|     无      | --include   | 包含特定模式的文件                   |
|     无       | --exclude   | 排除特定模式的文件                   |
| -r        | --recursive | 是否递归地遍历文件夹，并列出所有文件 |

>? 
> - `--include` 和`--exclude`支持标准正则表达式的语法，您可以使用它来过滤出符合特定条件的文件。
> - 使用 zsh 时，您可能需要在 pattern 串的两端加上双引号。
```plaintext
./coscli ls cos://bucket1 -r --include ".*.mp4"
```

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

#### 递归列出 bucket1 存储桶中 picture 文件夹下的所有文件

```plaintext
./coscli ls cos://bucket1/picture/ -r
```

#### 递归列出 bucket1 存储桶中所有的 .mp4 类型文件

```plaintext
./coscli ls cos://bucket1 -r --include .*.mp4
```



#### 递归列出 bucket1 存储桶中的所有不是 .mp4 类型的文件

```plaintext
./coscli ls cos://bucket1 -r --exclude .*.mp4
```

#### 递归列出 bucket1 存储桶中 picture 文件夹下所有以 test 开头并且类型不是 .jpg 的文件

```plaintext
./coscli ls cos://bucket1/picture -r --include ^picture/test.* --exclude .*.jpg
```
