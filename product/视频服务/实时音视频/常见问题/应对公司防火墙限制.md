因为有一些客户公司内部有外网访问限制，需要添加防火墙白名单才能访问，相关的规则如下：

## 客户端 Native SDK

防火墙端口：

|  TRTC SDK（Native） | 白名单项目 |
|---------|---------|
| TCP 端口 | 443 |
| UDP 端口 | 8000 |

域名白名单：

```
official.opensso.tencent-cloud.com

query.tencent-cloud.com

yun.tim.qq.com
```

 
## WebRTC

防火墙端口：

| WebRTC（H5） | 白名单项目 |
|---------|---------|
| TCP 端口 | 8687 |
| UDP 端口 | 8000；8800；843；443 |

域名白名单：

```
qcloud.rtc.qq.com
```


## 微信小程序

&lt;webrtc - room&gt; 域名白名单：

```
https://official.opensso.tencent-cloud.com

https://yun.tim.qq.com

https://cloud.tencent.com

https://webim.tim.qq.com
```


>! 因为腾讯云服务端 IP 地址是动态更新的，并不是固定的一批 IP 地址，所以我们无法提供固定的一组 IP 列表给您。
