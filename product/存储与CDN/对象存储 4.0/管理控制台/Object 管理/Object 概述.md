Object是腾讯云 COS 中存储的具体内容，使用 key-value 存储方式，专门用于存储任意多的数据。Object必须存储在一个或多个存储桶中，由以下基本内容组成：

键（Key）：Object名称。在 Bucket 中唯一标识一个Object
值（Value）：创建完 Bucket 后，可将本地任意类型的文件上传至 Bucket 中。每个 COS 的Bucket 都支持无限个数的文件存储，单文件简单上传最大支持 5G，单文件分块上传最大支持50T。
元数据（Metadata）：一组键值对，可用于存储有关Object的信息。可以参考[Object HTTP头设置](/doc/product/436/6258)。
访问控制信息 – 控制Object的访问权限信息。

## Object名称
腾讯云 COS 中上传的Object需具有合法的名称，它在 Bucket 中唯一地标识该 Object。在控制台Bucket Object 列表中可以遍历 Object 名称。Object 名称是采用 Unicode 字符，虽然可以在名称中使用任何 UTF-8 字符，但是每个应用程序对特殊字符的分析方式可能不同。以下原则有助于最大程度符合 DNS、Web 安全字符、XML 分析器和其他 API 的要求。

以下字符集通常可安全地用于键名称：

| 类型     | 详细内容                 |
| ------ | -------------------- |
| 字母数字字符 | [0-9 , a-z , A-Z]    |
| 特殊字符   | `!`、`-`、`_`、`.`、`* ` |
<font color="#FF0000"> 注意：Object 名称中不支持下列 ASCII 控制字符<br/>
字符上(↑)：CAN (24) <br/>
字符下(↓)：EM (25) <br/>
字符右(→)：SUB (26) <br/>
字符左(←)：ESC (27) <br/> </font>

以下是安全的Object名称示例：

my-organization
my.great_photos-2016/01/me.jpg
videos/2016/birthday/video1.wmv

需要注意的是，COS 的底层实现逻辑不存在Folder层次结构；但是用户可以在 COS 中创建Folder，并以分隔符标识文件层级结构。假设 Bucket 中包含具有以下名称的文件：

Vedio/mybday.mp4

Document/lesson1.mp4

report.pdf

控制台使用名称前缀（Vedio/、Document/）和分隔符（“/”）呈现FolderVedio和Document，而 report.pdf Object名没有前缀，因此这个Object在 Bucket 的根目录出现。

> COS 中没有层次结构。但是通过Object名称中的前缀和分隔符，COS 可以推断层次结构并引入Folder的概念。

## Object地址
Object的访问地址都是基于 Bucket 的访问地址和Object名称的，腾讯云的Object访问地址构成为 `Bucket域名+“/“+Object名称`，有关Bucket的域名可以参考 [Bucket 域名管理](/doc/product/436/6252)。


