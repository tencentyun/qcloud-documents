## 简介
回源设置主要用于数据的热迁移、特定请求的重定向等场景。例如当存储桶中没有用户请求的对象时、或者需要对特定的请求进行重定向时，设置回源地址可以有效满足用户需求。

截至 2017 年 7 月，回源设置支持源站为电信、移动、联通、长城宽带的 IP 段，其他运营商支持持续新增中。
![回源设置1](//mc.qcloudimg.com/static/img/c6e4e6281c47210b8dd97ba3a2a7cb9f/image.png)
## 设置步骤
1. 登录 [对象存储桶控制台](https://console.cloud.tencent.com/cos4/index)，选择左侧菜单栏【 Bucket 列表】，进入 Bucket 列表页面。单击需要配置回源的存储桶（如 example），进入存储桶。
![访问权限1](//mc.qcloudimg.com/static/img/b51d5a77d53c3416324ea3eb283c788c/image.png)
2. 单击【基础配置】，进入存储桶的基础配置页，找到回源设置，单击【编辑】进入可编辑模式。
![回源设置2](//mc.qcloudimg.com/static/img/5cd4e9d94d871eb4b58714c0d993fe52/image.png)
3. 修改当前状态为开启，输入回源地址（如 abc.example.com），单击【保存】即可。
![回源设置3](//mc.qcloudimg.com/static/img/31950daad98cbfc7dbbbedf4673ac221/image.png)

> **注意：**
- **用户设置回源状态为开启后，必须填入需要回源的域名或者 IP 地址，否则无法保存。**
-  **填入地址时只需填入域名或 IP 地址，无需带前缀“ http:// ”。亦支持以“ :[port] ”方式填写对应的端口号，“ : ”使用英文字符。**
```
例如（以下示例仅供参考，无实际意义。）：
abc.example.com
abc.example.com:8080
10.10.10.10
10.10.10.10:8080
```
- **截至 2017 年 7 月，控制台只支持 HTTP 回源，不支持 HTTPS。**

## 示例
**背景**
APPID 为 1250000000 的用户创建名为 example 的存储桶，并开启了 CDN 加速访问域名：
```
example-1250000000.file.myqcloud.com```
设置存储桶回源地址为:
```
abc.example.com
```
在源站（ `http://abc.example.com`）存放图片 1.jpg。

**客户端首次访问：**
```
http://example-1250000000.file.myqcloud.com/1.jpg
``` 
COS 发现无法命中对象时，对客户端返回 302 HTTP 状态码并跳转至 
```
http://abc.example.com/1.jpg
``` 
此时对象由源站提供给客户端，保证访问。同时 COS 从源站复制 1.jpg 并保存至存储桶 example 的根目录中。

**第二次访问**
```
http://example-1250000000.file.myqcloud.com/1.jpg
``` 
COS 直接命中根目录下 1.jpg 对象并返回给客户端。
