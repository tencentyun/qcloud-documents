CDN 支持多项自定义配置，您可以根据自身业务需要进行设置，优化您的 CDN 加速效果。

## 基本配置
| 配置名称                                     | 功能描述                |
| ---------------------------------------- | ------------------- |
| [基本信息](https://cloud.tencent.com/doc/product/228/7864) | 支持修改域名所属项目、域名对应业务类型 |
| [源站配置](https://cloud.tencent.com/doc/product/228/6289) | 支持热备源站配置、源站修改，保障回源  |
| [回源 HOST 配置](https://cloud.tencent.com/doc/product/228/6293) | 指定 CDN 回源到源站时的访问域名  |

## 访问控制
| 配置名称                                     | 功能描述                      |
| ---------------------------------------- | ------------------------- |
| [过滤参数配置](https://cloud.tencent.com/doc/product/228/6291) | 指定节点是否忽略用户的访问 URL 中"?"之后的参数 |
| [防盗链配置](https://cloud.tencent.com/doc/product/228/6292) | 配置 HTTP referer 黑白名单      |
| [IP 黑白名单配置](https://cloud.tencent.com/doc/product/228/6298) | 支持设置 IP 黑白名单，进行访问控制       |
| [IP 访问限频配置](https://cloud.tencent.com/doc/product/228/6420) | 支持单 IP 单节点访问限频配置          |
| [视频拖拽配置](https://cloud.tencent.com/doc/product/228/8111) | 支持开启视频拖拽配置                |


## 缓存过期配置
| 配置名称                                     | 功能描述              |
| ---------------------------------------- | ----------------- |
| [缓存过期配置](https://cloud.tencent.com/doc/product/228/6290) | 配置指定资源内容的缓存过期时间规则 |
| [状态码缓存配置](https://cloud.tencent.com/doc/product/228/6290) | 404状态码缓存时间配置     |
| [HTTP 头部缓存](https://cloud.tencent.com/doc/product/228/6290) | 头部缓存策略配置          |

## 回源配置
| 配置名称                                     | 功能描述                 |
| ---------------------------------------- | -------------------- |
| [中间源配置](https://cloud.tencent.com/doc/product/228/6294) | 指定是否使用中间源            |
| [Range 回源配置](https://cloud.tencent.com/doc/product/228/7184) | 开启/关闭 Range 分片回源     |
| [回源跟随302配置](https://cloud.tencent.com/doc/product/228/7183) | 开启/关闭源站返回302时，是否跟随跳转 |

## 安全配置

| 配置名称                                     | 功能描述      |
| ---------------------------------------- | --------- |
| [鉴权配置](https://cloud.tencent.com/document/product/228/33115) | 配置 URL 鉴权 |

## 高级配置

| 配置名称                                     | 功能描述                             |
| ---------------------------------------- | -------------------------------- |
| [带宽封顶配置](https://cloud.tencent.com/doc/product/228/7541) | 对域名设置带宽封顶阈值，超出阈值时关闭 CDN 服务，访问回源站 |
| [HTTPS 设置](https://cloud.tencent.com/doc/product/228/6295) | 配置 HTTPS 实现安全加速，支持 HTTPS 强制跳转    |
| [SEO 优化配置](https://cloud.tencent.com/doc/product/228/6297) | 开启 SEO 优化配置，保证搜索引擎权重稳定性          |
| [HTTP Header 配置](https://cloud.tencent.com/doc/product/228/6296) | 添加 HTTP Header 配置                |

## 跨国专线配置
| 配置名称                                     | 功能描述                        |
| ---------------------------------------- | --------------------------- |
| [跨国专线配置（内测中）](https://cloud.tencent.com/doc/product/228/7854) | 境外 CDN 加速时，开启/关闭跨国专线，保障回源质量 |
