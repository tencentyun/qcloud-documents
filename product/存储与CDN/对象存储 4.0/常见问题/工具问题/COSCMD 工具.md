### COSCMD 工具是否支持正则表达式？

不支持。

### 使用 COSCMD 工具，成功创建含有大写字符的存储桶，进行其他操作时使用大写字符报错？

COSCMD 工具会将大写字符自动转换为小写字符，存储桶名称只支持小写字母、数字、中划线及其组合，最多支持50个字符。更多限制信息，请参考 [规格与限制](https://cloud.tencent.com/document/product/436/14518) 文档。

### 使用 COSCMD 工具下载根目录文件，是否支持排除某个目录？

支持。可使用 `coscmd download --ignore /folder/*` 方式过滤。当忽略某一类后缀时，必须最后要输入`,` 或者加入`""`。


### 当需要传输大量文件时，如何提高传输速度？
可适当调整 MAX_THREAD 参数值，默认配置为5。线程数取决于机器性能，通常情况下设置为30，即可跑满带宽。例如将并发线程调整为30，执行命令行如下。
```plaintext
coscmd config -m 30
```


### COSCMD 工具是否支持使用 \* 号指定特定前缀对象的下载?

不支持。需要按照以下命令格式下载：
```plaintext
coscmd download prefix/ localpath/ -r
```
