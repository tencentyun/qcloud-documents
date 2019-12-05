#### 1. 如何设置访问对象时直接显示，而不需要下载?
绑定用户自有域名（如需购买域名，可通过腾讯云 [注册域名](https://dnspod.cloud.tencent.com/?from=qcloudHpHeaderDnspod&fromSource=qcloudHpHeaderDnspod)）并开启静态网站功能即可。详情参考 [静态网站设置](/doc/product/436/6249)。
> <font color="#0000cc">**注意：** </font>
> 当前静态网站设置只适用于 COS V4 版本。

#### 2. 在 COS 控制台设置自定义域名失败，如何处理？
 1) 确认域名已备案；
 2) 确认域名的 DNS 解析正确（在 关闭 CDN 加速情况下，需要预先在 DNS 解析把域名 CNAME 到存储桶的 [默认域名](/doc/product/436/6252#.E9.BB.98.E8.AE.A4.E5.9F.9F.E5.90.8D)）。

#### 3. 开启了静态网站功能，但是仍无法显示图片？
1) 要实现访问 COS 时直接显示对象（图片），需要开启静态网站功能，不能通过设置对象头部的 Content-Disposition:inline 来实现。 
2) 检查是否有浏览器、CDN 缓存。可以通过 curl、wget 命令来避免浏览器缓存，CDN 地址可以在 [CDN 控制台](https://console.cloud.tencent.com/cdn) 进行清缓存操作。

#### 4. 用户绑定自有域名时，开启 CDN 加速和关闭 CDN 加速的区别？
- **开启 CDN 加速：**域名由 CDN 管理，和在 [CDN 控制台](console.cloud.tencent.com/cdn) 添加域名，源站选择 COS 是一样的效果。用户在解析域名时，需要使用 CDN 分配的 CNAME 记录。配置时，先添加域名再解析域名即可，解析域名参见 [云解析快速入门](/doc/product/302/3446)。
- **关闭 CDN 加速：**域名由 COS 管理，域名配置会下发到对应存储桶所属地域的所有下载接入机器上。用户在解析域名时，需要使用 存储桶的默认域名作为 CNAME 记录。配置时，需要先解析域名再添加自定义域名。

#### 5. 为什么设置了对象的自定义头部 Content-Disposition 后仍然不生效？
自定义头部中， 其他自定义头部，设置了就会生效，Content-Disposition 是特殊的。只有在开启静态网站功能，且用自定义域名访问时，该头部才生效。
