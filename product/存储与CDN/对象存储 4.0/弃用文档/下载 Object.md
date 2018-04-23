已经上传到存储桶 Bucket 中的 Object，可以通过访问地址进行下载。

进入 COS 管理控制台，点击 Object 所在的 Bucket，在 Object 列表右侧，点击 **文件信息** ：

![](https://mc.qcloudimg.com/static/img/e26cf2de168ba9dc1de75dc775e5f480/image.png)

此时会弹出 Object 信息窗口，点击下载按钮可直接下载 Object，您也可以复制 URL 地址粘贴至浏览器下载 ：

![](https://mc.qcloudimg.com/static/img/7325519a5253375d117cc779ce4f8d04/image.png)


若资源所属 Bucket 的属性为私有读写，此处复制的地址后会自动计算签名添加后缀，签名生成方法详情请参考 [签名算法](/doc/api/264/5993) 。

```
http://testbucket-10026302.file.myqcloud.com/test_uploadfile_1.txt?sign=eTgtgdjtdYm0fQ+5zGSLeQ9q3RdhPTEwMDI2MzAyJms9QUtJRG1tSURnYlk0a2h5YzJGVFZ0NjRZNUllZnd5WHhJb1VyJmU9MTQ2MjQzODA5NCZ0PTE0NTk4NDYwOTQmcj04ODYzOTQwOTkmZj0vdGVzdF91cGxvYWRmaWxlXzEudHh0JmI9dGVzdGJ1Y2tldA==
```

