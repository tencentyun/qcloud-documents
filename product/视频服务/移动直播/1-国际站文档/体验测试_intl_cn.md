## 地址的准备
体验最简单的1v1连麦，也需要两对地址，即两个直播码，每个直播码对应一路 livepush 推流地址 和 一路 liveplay 播放地址。
![](//mc.qcloudimg.com/static/img/fd615ac85e949617752130afd91b41a4/image.png)

如上图中 主播A 的直播码为 8888_streamA， 如上图中 主播B 的直播码为 8888_streamB，

- 主播 A 需要使用如下的 livepush 地址推流：
 
`rtmp://8888.livepush.myqcloud.com/live/8888_streamA?bizid=8888&txSecret=xxx&txTime=5C2A3CFF`

- 主播 A 使用如下的 liveplay 地址播放主播 B 的低延迟视频：

`rtmp://8888.liveplay.myqcloud.com/live/8888_streamB?bizid=8888&txSecret=xxx&txTime=5C2A3CFF`

- 主播 B 需要使用如下的 livepush 地址推流：

`rtmp://8888.livepush.myqcloud.com/live/8888_streamB?bizid=8888&txSecret=xxx&txTime=5C2A3CFF`

- 主播 B 使用如下的 liveplay 地址播放主播 A 的低延迟视频：

`rtmp://8888.liveplay.myqcloud.com/live/8888_streamA?bizid=8888&txSecret=xxx&txTime=5C2A3CFF`

- <font color='red'>**特别提醒**</font>：

连麦中大小主播使用的地址都是 rtmp 协议的地址，即 rtmp:// 打头的 URL。
<a name="txsecret">&nbsp;</a>
## 防盗链保护 
您可能注意到了，上述的四条 URL 全部都有防盗链保护（即地址中的 txTime 和 txSecret），这是为了防止恶意攻击。

有了防盗链保护，攻击者就无法轻易构造出 livepush 推流地址，从而保证只有通过您服务器鉴权的 App 才能推流。有了防盗链保护，攻击者亦无法轻易构造出 livepush 播放地址，从而保证您的超级链路不会被攻击者盗用流量。

- **推流防盗链（livepush）**
推流防盗链的生成办法可以参考 [DOC](https://cloud.tencent.com/document/product/454/7915#.E9.98.B2.E7.9B.97.E9.93.BE.E7.9A.84.E8.AE.A1.E7.AE.97.EF.BC.9F5)， 简单描述即：
```
直播码 = 8888_streamA
加密KEY = f3313e36c611150119f5d04ff1225b3e
txTime（推荐设置12小时过期） = 2017.06.10 12:12:12 = 1497067932 = 593B719C(16进制)
txSecret = MD5(加密KEY + 直播码 + txTime) 
             = MD5(f3313e36c611150119f5d04ff1225b3e8888_streamA593B719C) 
             = 3bc85763bddab40be60c838174f53e03
```

- **播放防盗链 ( liveplay）**
播放防盗链的计算办法跟推流防盗链的计算方法完全相同，而且使用的也是推流防盗链的加密KEY（扩展知识：CDN 是有专门的播放防盗链 KEY 的，不过配置成本很高，所以我们就不去折腾它了。）

## 体验和测试
体验连麦需要两台（或两台以上）的手机，每台手机都要：
- 推一路（且仅有一路） rtmp 直播流，以供另外一台（或几台）手机播放。
- 播一路（或多路）rtmp 直播流，这样才能构成双向（或多向）视频通话。

![](//mc.qcloudimg.com/static/img/56eec150834927ffba770bcd55779ff3/image.png)

- **测试方法**：
- 第一步：设置本地的 livepush 推流地址，比如文章开始的 steamA，并点击按时按钮启动推流。
- 第二步：按图中的加号添加一路 liveplay 播放地址，比如文章开始的 streamB。
- 第三步：如果要体验多路连麦，可以继续点击加号按钮增加更多的 liveplay 播放地址。

> 如果测试中发现延迟很大，可能是用错地址了，<font color='red'>只有超级链路才支持低延迟播放</font>，普通的 CDN 播放地址延迟至少在 2 秒以上。

- **测试地址**：
文章开始的地址显然是不能用的，我们准备了几组测试地址，方便您快速体验。但是每组地址<font color='red'>同时只能供一个客户测试</font>，所以，如果您发现地址都被其他客户占用了，可以参考文章中间部分介绍的 <a href="#txsecret">防盗链保护</a> 自行生成。

第一组：
```
//3891_test001_A
rtmp://3891.livepush.myqcloud.com/live/3891_test001_A?bizid=3891&txSecret=70f6e3c168c95838cc1113410630f572&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test001_A?bizid=3891&txSecret=70f6e3c168c95838cc1113410630f572&txTime=5C2A3CFF

//3891_test001_B
rtmp://3891.livepush.myqcloud.com/live/3891_test001_B?bizid=3891&txSecret=c955e184a0aac1ba071d1980e7a42683&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test001_B?bizid=3891&txSecret=c955e184a0aac1ba071d1980e7a42683&txTime=5C2A3CFF
```

第二组：
```
//3891_test002_A
rtmp://3891.livepush.myqcloud.com/live/3891_test002_A?bizid=3891&txSecret=8ac2f28aee6c0a9349e0aeb98842056e&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test002_A?bizid=3891&txSecret=8ac2f28aee6c0a9349e0aeb98842056e&txTime=5C2A3CFF

//3891_test002_B
rtmp://3891.livepush.myqcloud.com/live/3891_test002_B?bizid=3891&txSecret=6b9d205507aa6fcaea16d9bf7703b6d3&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test002_B?bizid=3891&txSecret=6b9d205507aa6fcaea16d9bf7703b6d3&txTime=5C2A3CFF
```

第三组：
```
//3891_test003_A
rtmp://3891.livepush.myqcloud.com/live/3891_test003_A?bizid=3891&txSecret=76d429c4bb9a053426ada4657bb604d6&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test003_A?bizid=3891&txSecret=76d429c4bb9a053426ada4657bb604d6&txTime=5C2A3CFF

//3891_test003_B
rtmp://3891.livepush.myqcloud.com/live/3891_test003_B?bizid=3891&txSecret=a0070b11bba5af3108f02977d3d8c2b7&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test003_B?bizid=3891&txSecret=a0070b11bba5af3108f02977d3d8c2b7&txTime=5C2A3CFF
```



