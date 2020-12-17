# 组件化集成

## 介绍

`yj-player`是基于【视频合成协议】的web播放器组件，方便预览当前协议合成效果。

`yj-player-helper`是对【视频合成协议】的一个基础封装，仅协助组装，校验协议。提供少量通用业务场景`helper`方法，协助串联【云媒资】到合成协议。

关于【视频合成协议】，请参考[文档](./protocolIntro.md)。


## 快速开始

```html
<html>
  <head>
    <!--cdn形式引入我们的sdk--->
    <script src="https://vs-cdn.tencent-cloud.com/sdk/yj-player-1.3.3.js"></script>
    <script src="https://vs-cdn.tencent-cloud.com/sdk/yj-player-helper-1.3.0.js"></script>
    <!-- 我们还支持npm方式引入:-->
    <!-- npm install yj-player --save -->
    <!-- npm install yj-player-helper --save -->
  </head>
  <body>
    <div id='container'>
    </div>
  </body>
  <script>
    /**
     * 
     * import { Track, CMEUtils } from "yj-player-helper";
     * import YJPlayer from "yj-player";
     * 
     * 模块化引入，或直接取全局对象
     * */

    /**
     * @auth 登录方法，保证可以调用CME，WebAPI。
     *    @param sign {{string}} 签名串。
     **/
    CMEUtils.auth({
        sign:"your_sign"
      }).then(()=>{
        console.log('登录成功')
        /**
         * 创建一个轨道数据
         */
        const videoTrack = Track.create({
          type: "video",
        });

        console.log(videoTrack);

        /***
         * 从云媒资获取一个视频类型素材。
         * 使用append助手方法往轨道添加元素。
         */
        CMEUtils.createtrackitem("video_asset_id").then((videoItem) => {
          Track.append(videoTrack, videoItem);
          
          videoItem.duration = 8000  //调整播放时长为8秒
          const data = [videoTrack];
          let player = new YJPlayer({
            mode: "preiew",
            container: document.getElementById("container"),
            aspectRatio: "16:9",
            data: { tracks: data },
          });
          player.play()
        });
      }).catch(err=>{
        console.error('登录异常')
      })
  
  </script>
</html>
```

<!-- 完整`demo`体验请点击👉 &nbsp;[下载demo](https://video-caster-sdk-1258344699.cos.ap-guangzhou.myqcloud.com/examples/yunjian-player-sdk-demo.zip) -->
