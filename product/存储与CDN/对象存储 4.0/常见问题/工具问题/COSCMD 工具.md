### COSCMD 工具是否支持正则表达式？

不支持。

### 使用 COSCMD 工具，成功创建含有大写字符的存储桶，进行其他操作时使用大写字符报错？

COSCMD 工具会将大写字符自动转换为小写字符，存储桶名称只支持小写字母、数字、中划线及其组合，最长 40 字符。更多限制信息，请参考 [规格与限制](https://cloud.tencent.com/document/product/436/14518)。

### 使用 COSCMD 工具下载根目录文件，是否支持排除某个目录？

支持。可使用 `coscmd download -ignore /xxx/*` 方式过滤。
