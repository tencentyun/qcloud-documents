## Mastodon 文件存储总览
首先介绍下 Mastodon 默认会在本地存些啥资源，这里先把对接在 COS 上的文件目录贴出来。
![](https://qcloudimg.tencent-cloud.cn/raw/239095d6d0dca42582ef3e6c7ae4be24.png)

如图所示，Mastodon 会创建四个文件夹，accounts、cache、media_attachments、site_uploads

1. accounts：包含在 Mastodon 上注册用户的 avatars 和 headers，就是头像和自定义头图。
2. cache：应用程序缓存，内含 accounts，custom_emojis，media_attachments，preview_cards 四个文件夹，顾名思义是账户，自定义表情，媒体附件（音频 + 视频资源），账户信息预览卡片。
3. media_attachments：包含用户上传的媒体附件（视频+音频+图片）例如图片最终目录下有 original 和 small 两个文件夹，里面分别是用户发帖的原始图片以及缩略图。
4. site_uploads：与 Mastodon 整站设置相关的素材，例如·整站的背景图等。

以上这些资源默认会存储于本地硬盘，内容量最大的属 media_attachments 文件夹，内含视频+音频+图片，建议对接至 COS。

这里列出几点用 COS 而不是本地存储的优点：
- 不再依赖本地硬盘，不会因为本地硬盘的问题导致存储服务不可用（例如磁盘满），并且迁移的时候也无需挪动本地文件。
- 使用本地存储进行资源分发依赖于主机的外网带宽，远远小于 COS 分发的下行速度。
- COS 提供了图片处理服务，使用图片压缩后可以提高加载速度并节省下行带宽费用。

## Mastodon 接入 COS
1. 在 File storage 章节，可知存储源有本地存储或者 S3 兼容存储，默认配置为本地存储。请参见 [File storage](https://github.com/mastodon/documentation/blob/master/content/en/admin/config.md#file-storage-cdn)。
![](https://qcloudimg.tencent-cloud.cn/raw/e129d6552717631d35078bbaff20f68f.png)
2. 腾讯云 COS 是支持 S3 的，于是使用 Amazon S3 and compatible 的方式进行接入。
3. 腾讯云 COS 文档中也有关于 S3 对接的介绍：[在兼容 S3 的第三方应用中使用 COS 的通用配置](https://cloud.tencent.com/document/product/436/41284?from=10680)。
4. 只需修改 .env.production 配置文件，添加 S3 相关的配置项，就不再会存储至本地硬盘了。
```
# File storage (optional)
# -----------------------
S3_ENABLED=true
S3_BUCKET=mastodon-<rm>
AWS_ACCESS_KEY_ID=<rm>
AWS_SECRET_ACCESS_KEY=<rm>
S3_ENDPOINT=https://cos.ap-beijing.myqcloud.com
S3_ALIAS_HOST=mastodon-<rm>.cos.ap-beijing.myqcloud.com
S3_FORCE_SINGLE_REQUEST=true

```
 - S3_ENABLED：开启 S3 存储，不使用本地存储。
 - S3_BUCKET：填写腾讯云 COS 的 bucket 名称，需要后面包含的 appid。
 - AWS_ACCESS_KEY_ID：填写访问密钥的 SecretId。
 - AWS_SECRET_ACCESS_KEY：填写访问密钥的 SecretKey。
 - S3_ENDPOINT：填写腾讯云 COS 存储桶对应区域的端点，自己是北京区的，其他区如下表。
5. 例如：`https://cos.ap-beijing.myqcloud.com`，用实际的地域简称替换 `ap-beijing`。
6. S3_ALIAS_HOST：填写上表中的默认域名，用实际的存储桶名称，同样需要后面包含的 appid，这里打码掉了
7. 之前用的是万象优图的域名，现在直接使用 COS 域名也能调用万象优图图片处理的相关能力了。
```
S3_ALIAS_HOST=mastodon-<rm>.picbj.myqcloud.com
```
8. S3_FORCE_SINGLE_REQUEST：兼容 Mastodon 应用程序，设置为 true。
9. 最后，在 COS 的 CORS 设置好来源域名（多了个 localhost 是为了本地预览 blog 可以正常输出图片）
![](https://qcloudimg.tencent-cloud.cn/raw/dfa54dabaaa8d6f4e509ff536746f9de.png)
10. 访问 Mastodon 看到图片的地址都是 S3_ALIAS_HOST 开头的，也就是从 COS 而不是轻量机的域名，最后完成对接。
![](https://qcloudimg.tencent-cloud.cn/raw/bd3f6d889673209d22359f9da59c9b3a.png)


## COS 其他设置
这里再贴几张其他的设置项，非必需，仅供参见：

1. 例如开启**防盗链**，控制盗刷流量。
![](https://qcloudimg.tencent-cloud.cn/raw/f92e7ba7c41946d00b093b5b5d023110.png)
2. 开启**服务端加密**，保护数据安全。
![](https://qcloudimg.tencent-cloud.cn/raw/a4594d79e7871cce6bae774532fe1f21.png)
3. 访问权限自己使用的「公有读私有写」，如需更严格的权限可以分配成「私有读写」，不过这样在读的时候需要算好签名参数。
![](https://qcloudimg.tencent-cloud.cn/raw/ac06affdf4fe67af3f7cc4b5d3f8a39a.png)
4. 开启**日志存储**，便于后期溯源访问详情。
![](https://qcloudimg.tencent-cloud.cn/raw/515e0b9ecf22e0573b66a4cdd91f786d.png)
5. 图片处理，可以设置**图片处理样**式，减小图片大小以节省流量，原本就是万象优图的能力。
![](https://qcloudimg.tencent-cloud.cn/raw/011267c72048026bb2797e0ad0b6fbe8.png)

## 统计分析
tootctl media usage 统计如下：
```
[root@cn-tx-bj7-c8 mastodon]# docker-compose run --rm web tootctl media usage
[+] Running 5/5
 ⠿ Network mastodon-internal_network  Created                                                                                                                                                                                                        2.5s
 ⠿ Network mastodon-external_network  Created                                                                                                                                                                                                        1.7s
 ⠿ Container mastodon_db_1            Recreated                                                                                                                                                                                                      0.9s
 ⠿ Container mastodon_redis_1         Recreated                                                                                                                                                                                                      0.9s
 ⠿ Container mastodon_es_1            Recreated                                                                                                                                                                                                      1.5s
[+] Running 3/3
 ⠿ Container mastodon-redis-1  Started                                                                                                                                                                                                               0.7s
 ⠿ Container mastodon-es-1     Started                                                                                                                                                                                                               0.7s
 ⠿ Container mastodon-db-1     Started                                                                                                                                                                                                               0.7s
Attachments:    8.77 GB (8.77 GB local)
Custom emoji:   16.7 KB (0 Bytes local)
Preview cards:  5.38 MB
Avatars:        1.23 MB (1.02 MB local)
Headers:        2.51 MB (771 KB local)
Backups:        0 Bytes
Imports:        0 Bytes
Settings:       1.39 MB

```

根据 COS 的统计可以看出今年初创建的存储桶，截至今天马上 9 个月，已经存放了 2.3w 张图片，占用量不到 10G。
![](https://qcloudimg.tencent-cloud.cn/raw/5ca0c1218557a671e7a92478bbc9d6c3.png)
每天请求量在 2K 左右：
![](https://qcloudimg.tencent-cloud.cn/raw/9b55b63b791aac990b75565c9a315eb7.png)
