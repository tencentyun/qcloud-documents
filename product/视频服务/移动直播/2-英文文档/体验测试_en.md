## Preparation for URLs
To experience the simplest 1v1 joint broadcasting, two pairs of URLs are needed: two LVB codes with each corresponding to a push URL livepush and a playback URL liveplay.
![](//mc.qcloudimg.com/static/img/fd615ac85e949617752130afd91b41a4/image.png)

As shown in the figure above, the LVB code of VJ A is 8888_streamA, and the LVB code of VJ B is 8888_streamB.

- VJ A needs to use the following livepush URL to push:
 
`rtmp://8888.livepush.myqcloud.com/live/8888_streamA?bizid=8888&txSecret=xxx&txTime=5C2A3CFF`

- VJ A uses the following liveplay URL to play VJ B's low-delay video:

`rtmp://8888.liveplay.myqcloud.com/live/8888_streamB?bizid=8888&txSecret=xxx&txTime=5C2A3CFF`

- VJ B needs to use the following livepush URL to push:

`rtmp://8888.livepush.myqcloud.com/live/8888_streamB?bizid=8888&txSecret=xxx&txTime=5C2A3CFF`

- VJ B uses the following liveplay URL to play VJ A's low-delay video:

`rtmp://8888.liveplay.myqcloud.com/live/8888_streamA?bizid=8888&txSecret=xxx&txTime=5C2A3CFF`

- **Note**:

During joint broadcasting, the primary and secondary VJs use the URLs of the rtmp protocol, that is, the URLs starting with rtmp://.
<a name="txsecret">&nbsp;</a>
## Hotlink Protection 
You may have noticed that all the four URLs above are under hotlink protection (txTime and txSecret in the URLs) to prevent malicious attacks.

Owing to hotlink protection, attackers cannot construct livepush push URLs and livepush playback URLs, which ensures that only the App authenticated by your server can perform push and prevents the traffic of your super linkages from being hacked.

- **Push Hotlink Protection (livepush)**
For more information on how to generate push hotlink protection, please see [DOC](https://cloud.tencent.com/document/product/454/7915#.E9.98.B2.E7.9B.97.E9.93.BE.E7.9A.84.E8.AE.A1.E7.AE.97.EF.BC.9F5). To put it simply:
```
LVB code = 8888_streamA
Encryption KEY = f3313e36c611150119f5d04ff1225b3e
txTime (it is recommended to be valid for 12 hours) = 2017.06.10 12:12:12 = 1497067932 = 593B719C (hexadecimal)
txSecret = MD5 (encryption KEY + LVB code + txTime) 
             = MD5(f3313e36c611150119f5d04ff1225b3e8888_streamA593B719C) 
             = 3bc85763bddab40be60c838174f53e03
```

- **Playback Hotlink Protection (liveplay)**
The calculation method of playback hotlink protection is the same as that of push hotlink protection, which also uses the encryption KEY of push hotlink protection. (tip: CDN has a specialized playback hotlink protection KEY with extremely high configuration costs, so we hardly use it.)

## Experience and Testing
Two (or more) mobile phones are needed for joint broadcasting, each of which must:
- push only one rtmp LVB stream to another (or several) mobile phone(s) for playback;
- play one (or more) rtmp LVB stream(s) to establish a two-way (or multi-way) video chat.

![](//mc.qcloudimg.com/static/img/56eec150834927ffba770bcd55779ff3/image.png)

- **Test Method**:
- Step 1: Set the local livepush push URL. For example, set the streamA mentioned at the beginning of this documentation, and click the start button to push.
- Step 2: Click the plus button in the figure to add a liveplay playback URL. For example, add the streamB mentioned at the beginning of this documentation.
- Step 3: To experience multi-way joint broadcasting, you can continue to click the plus button to add more liveplay playback URLs.

> If a long delay is found during the test, you may use a wrong URL. Only the super linkage supports low-delay playback. The ordinary CDN playback URL has a delay at least 2 seconds or more.

- **URLs for Testing**:
Obviously, the URLs mentioned at the beginning of this documentation cannot be used for testing. We have prepared groups of test URLs for your quick experience. Each group of URLs can only be used by one customer to test at a time. If all the URLs are occupied by other customers, please see the <a href="#txsecret">Hotlink Protection</a> in the middle of this documentation to generate URLs by yourself.

Group 1:
```
//3891_test001_A
rtmp://3891.livepush.myqcloud.com/live/3891_test001_A?bizid=3891&txSecret=70f6e3c168c95838cc1113410630f572&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test001_A?bizid=3891&txSecret=70f6e3c168c95838cc1113410630f572&txTime=5C2A3CFF

//3891_test001_B
rtmp://3891.livepush.myqcloud.com/live/3891_test001_B?bizid=3891&txSecret=c955e184a0aac1ba071d1980e7a42683&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test001_B?bizid=3891&txSecret=c955e184a0aac1ba071d1980e7a42683&txTime=5C2A3CFF
```

Group 2:
```
//3891_test002_A
rtmp://3891.livepush.myqcloud.com/live/3891_test002_A?bizid=3891&txSecret=8ac2f28aee6c0a9349e0aeb98842056e&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test002_A?bizid=3891&txSecret=8ac2f28aee6c0a9349e0aeb98842056e&txTime=5C2A3CFF

//3891_test002_B
rtmp://3891.livepush.myqcloud.com/live/3891_test002_B?bizid=3891&txSecret=6b9d205507aa6fcaea16d9bf7703b6d3&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test002_B?bizid=3891&txSecret=6b9d205507aa6fcaea16d9bf7703b6d3&txTime=5C2A3CFF
```

Group 3:
```
//3891_test003_A
rtmp://3891.livepush.myqcloud.com/live/3891_test003_A?bizid=3891&txSecret=76d429c4bb9a053426ada4657bb604d6&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test003_A?bizid=3891&txSecret=76d429c4bb9a053426ada4657bb604d6&txTime=5C2A3CFF

//3891_test003_B
rtmp://3891.livepush.myqcloud.com/live/3891_test003_B?bizid=3891&txSecret=a0070b11bba5af3108f02977d3d8c2b7&txTime=5C2A3CFF
rtmp://3891.liveplay.myqcloud.com/live/3891_test003_B?bizid=3891&txSecret=a0070b11bba5af3108f02977d3d8c2b7&txTime=5C2A3CFF
```




