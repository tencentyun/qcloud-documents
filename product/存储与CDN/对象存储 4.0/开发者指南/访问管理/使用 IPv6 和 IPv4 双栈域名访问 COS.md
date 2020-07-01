## 概述

随着互联网网络的蓬勃发展，IPv4 地址数量已经日益枯竭。由 IANA（Internet Assigned Numbers Authority，互联网数字分配机构）管理的 IPv4 位址，于2011年1月31日完全用尽。其他五个区域的可核发地址也将陆续枯竭，各大区域可分配的 IPv4 地址最迟于2020年底枯竭。

因此，IETF（Internet Engineering Task Force，互联网工作小组）规划了 IPv4的下一代网络协议，即 IPv6（Internet Protocol version 6）。经过近10年的讨论，最终于1998年12月以互联网标准规范（[RFC 2460](https://tools.ietf.org/html/rfc2460)）的方式正式公布。相比 IPv4，IPv6 具有以下两点显著的优势：

1. 具有更大的编码地址空间。IPv6 的编码地址空间为128位，IPv4 的编码地址空间为32位，消除了对网络地址转换的依赖，支持了更多设备接入互联网，对万物互联的发展起到基石作用。
2. 具有更安全的传输协议，强制要求加密传输，保障访问更加安全可靠。

IPv6 是未来扩展互联网地址的基础。然而，切换到 IPv6 地址存在较大的工作量，需要对路由器、防火墙、企业内部系统及相关应用程序等进行变更，目前主要技术演进路线均为采用双栈域名访问。预计在2025年以前 IPv4 仍会被支持，以便给新协议的修正留下足够的时间。基于此，COS 为用户提供了 IPv6 和 IPv4 的双栈域名，方便 IPv6 和 IPv4 客户端随时读写云上资源。

## 使用 IPv6 和 IPv4 双栈域名访问 COS

COS 目前已经提供了 IPv6 和 IPv4 双栈域名的支持。用户侧只需要将访问域名切换为双栈域名，即可在客户端以 IPv6 的方式访问 COS，获取存储在云端的资源。

目前 COS 已经对外提供上海地域双栈域名，可同时支持 IPv6 和 IPv4 客户端进行访问，访问域名格式如下：

```sh
<BucketName-APPID>.cos-dualstack.<Region>.myqcloud.com
```

上海地域双栈域名只需替换`<Region>`参数为`ap-shanghai`：

```sh
<BucketName-APPID>.cos-dualstack.ap-shanghai.myqcloud.com
```

以上海地域为例，假设用户新建了一个存储桶名为`camera_iotdevice_id-125000000000`，存储桶中存放的一个视频文件名为`record_hashid.mov`，则该文件的双栈域名格式如下：

```sh
https://camera_iotdevice_id-125000000000.cos-dualstack.ap-shanghai.myqcloud.com/record_hashid.mov
```
