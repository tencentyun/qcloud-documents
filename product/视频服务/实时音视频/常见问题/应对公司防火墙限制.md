### 客户端 Native SDK 需要配置哪些端口或域名为白名单？

防火墙端口如下表所示：

|  TRTC SDK（Native） | 白名单项目 |
|---------|---------|
| TCP 端口 | 443、20166 |
| UDP 端口 | 8000、8080、16285、9000 |

域名白名单：

```
cloud.tim.qq.com
gz.file.myqcloud.com
avc.qcloud.com
yun.tim.qq.com
dldir1.qq.com
mlvbdc.live.qcloud.com
query.tencent-cloud.com
```

 
### WebRTC 需要配置哪些端口或域名为白名单？

防火墙端口如下表所示：

| WebRTC（H5） | 白名单项目 |
|---------|---------|
| TCP 端口 | 8687 |
| UDP 端口 | 8000；8080；8800；843；443；16285 |

域名白名单：

```
qcloud.rtc.qq.com
```


### 微信小程序需要配置哪些域名为白名单？

&lt;trtc-room&gt; 域名白名单：

```
https://official.opensso.tencent-cloud.com
https://yun.tim.qq.com
https://cloud.tencent.com
https://webim.tim.qq.com
https://query.tencent-cloud.com
```


>!因为腾讯云服务端 IP 地址是动态更新的，并不是固定的一批 IP 地址，所以我们无法提供固定的一组 IP 列表给您。
