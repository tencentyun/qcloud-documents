- 视频拖拽主要产生于视频点播场景中，当用户拖拽播放进度时，会向服务端发起类似如下请求： 
`http://www.test.com/test.flv?start=10`
此时会返回第10字节开始的数据，由于点播类视频文件均缓存在各 CDN 节点上，开启此项配置，各节点可直接响应此类请求。
- 开启视频拖拽时，需要同时开启过滤参数，且源站需要支持 range 请求。支持的文件格式为：mp4、flv、ts：

| 文件类型 | meta信息                                 | start 参数说明                               | 请求示例                     |
| ---- | -------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| MP4  | 源站视频的 meta 信息必须在文件头部，不支持 meta 信息在尾部的视频 | start 参数表示的是时间，单位是秒，支持小数以表示毫秒（如 start=1.01，表示开始时间是1.01s），CDN 会定位到 start 所表示时间的前一个关键帧（如果当前 start 不是关键帧） | ``` http://www.test.com/demo.mp4?start=10```  表示从第10秒开始播放 |
| FLV  | 源站视频必须带有 meta 信息                       | start 参数表示字节，CDN 会自动定位到 start 参数所表示的字节的前一个关键帧（如果 start 当前不是关键帧） | ``` http://www.test.com/demo.flv?start=10```  表示从第10个字节开始播放 |
| TS   | 无特殊要求                                  | start 参数表示的是时间，单位是秒，支持小数以表示毫秒（如 start=1.01，表示开始时间是1.01s），CDN 会定位到 start 所表示时间的前一个关键帧（如果当前 start 不是关键帧） | `http://www.test.com/demo.ts?start=10` 表示从第10秒开始播放 |

## 配置指引
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧目录中，单击【域名管理】，进入管理页面。
2. 在列表中，找到您需要编辑的域名所在行，单击操作栏的【管理】。
 ![](https://main.qcloudimg.com/raw/20cf381c1a66bfc5ccc76e84d7e6416f.png)
3. 单击【访问控制】选项卡，可以在 **视频拖拽** 模块进行配置。
默认情况下，视频拖拽配置为关闭状态。
 ![](https://main.qcloudimg.com/raw/1522e676ad303c787da9df2bfe648140.png)
4. 开启视频拖拽开关，若 [过滤参数配置](https://cloud.tencent.com/document/product/228/6291) 为关闭状态，开启视频拖拽会自动开启过滤参数。
![](https://main.qcloudimg.com/raw/3d16d61c33a1c5f2506c61849f7901c5.png)
