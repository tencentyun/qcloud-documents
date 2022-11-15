

## 操作场景

常用的视频剪辑工具 Premiere、AE 等可以实现复杂的剪辑效果，在宣传视频制作、广告视频制作中被广泛应用。但在以下场景中，传统的视频剪辑工具或者模板化的视频处理软件无法满足**批量、自动化和可定制**的视频剪辑需求：
- 学校期望能在学生上完网课之后马上呈现所有学生学习过程中的精彩视频，搭配学校的 logo 和宣传语等，支持学生一键分享自己的成果。假设有 1 万个学生，则需要为每个学生制作唯一的视频，所以需要批量且自动化的完成 1 万个不同的视频剪辑。
- 某次营销活动中，需要为不同的用户生成不同的头像视频来吸引用户参与。每个用户的头像都不同，生成的视频也不同，用户可能成千上万，所以需要自动化完成。
- 网红运营公司期望能给所有主播生成统一的营业视频。可能有 100 个主播，专门找一个人剪辑 100 个视频好像勉强能接受，但如果每周都要剪一次不同的视频呢？所以需要自动化、批量和可定制化的剪辑。

这类视频剪辑场景还具有使用时段集中、计算量大的特点。单独购买高规格的服务器利用率很低，买低规格的服务器计算能力无法满足要求。Serverless 按量计费的特点，以及高性能的计算能力，完美匹配了这样的需求场景。既能达到 100% 的利用率，又能按量使用高性能计算能力。同时，Serverless 支持丰富的可编程环境，可支持不同开发习惯的开发者，灵活性更高。

## 前提条件

本文提到的所有视频剪辑的功能，均使用 [FFmpeg](http://ffmpeg.org/) 工具完成。

## FFmpeg 使用方法
[FFmpeg](http://ffmpeg.org/) 是一个用来做视频处理的开源工具，支持视频剪辑、视频转码、视频编辑、音频处理、添加文字、视频拼接、拉流推流直播等功能。通过不同的 FFmpeg 命令可以编程完成不同的视频剪辑功能，组合编排起来，即可应对各种批量自动化的场景。

常见的视频剪辑场景主要包含以下几种：
1. 视频转码
2. 视频裁剪
3. 视频加文字
4. 视频加图片
5. 视频拼接
6. 视频加音频
7. 视频转场
8. 视频特效
9. 视频加速慢速播放

### FFmpeg 命令

下文介绍了一些具体的 FFmpeg 命令，您可以本地 [安装 FFmpeg](http://ffmpeg.org/) 后进行测试。

```jsx
// 将 MOV 视频转成 mp4 视频
ffmpeg -i input.mov output.mp4
```
```jsx
// 将原视频的帧率修改为 24
ffmpeg -i input.mp4 -r 24 -an output.mp4
```
```jsx
// 将 mp4 视频转为可用于直播的视频流
ffmpeg -i input.mp4 -codec: copy -bsf:v h264_mp4toannexb -start_number 0 -hls_time 10 -hls_list_size 0 -f hls output.m3u8
```
```jsx
// 将视频分别变为 480x360，并把码率改 400
ffmpeg -i input.mp4 -vf scale=480:360,pad=480:360:240:240:black -c:v libx264 -x264-params nal-hrd=cbr:force-cfr=1 -b:v 400000 -bufsize 400000 -minrate 400000 -maxrate 400000 output.mp4
```
```jsx
// 给视频添加文字，例如字幕、标题等。
// `fontfile`是要使用的字体的路径，`text`是您要添加的文字，
// `fontcolor`是文字的颜色，`fontsize`是文字大小，`box`是给文字添加底框。
// `box=1`表示 enable，`0`表示 disable，`boxcolor`是底框的颜色，black@0.5 表示黑色透明度是 50%，`boxborderw`是底框距文字的宽度
// `x`和`y`是文字的位置，`x`和`y`不只支持数字，还支持各种表达式，具体可以去官网查看
ffmpeg -i input.mp4 -vf "drawtext=fontfile=/path/to/font.ttf:text='您的文字':fontcolor=white:fontsize=24:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2" -codec:a copy output.mp4
```
```jsx
// 给视频添加图片，例如添加 logo、头像、表情等。filter_complex 表示复合的滤镜，overlay 表示表示图片的 x 和 y，enable 表示图片出现的时间段，从 0-20 秒
ffmpeg -i input.mp4 -i avatar.JPG -filter_complex "[0:v][1:v] overlay=25:25:enable='between(t,0,20)'" -pix_fmt yuv420p -c:a copy output.mp4
```
```jsx
// 视频拼接，list.txt 里面按顺序放所有要拼接的视频的文件路径，如下。
// 注意，如果视频的分辨率不一致会导致拼接失败。
ffmpeg -f concat -safe 0 -i list.txt -c copy -movflags +faststart output.mp4
// list.txt 的格式如下
file 'xx.mp4'
file 'yy.mp4'
```
```jsx
// 视频加音频，stream_loop 表示是否循环音频内容，-1 表示无限循环，0 表示不循环。shortest 表示最短的 MP3 输入流结束时完成编码。
ffmpeg -y -i input.mp4 -stream_loop -1 -i audio.mp3 -map 0:v -map 1:a -c:v copy -shortest output.mp4
```
>? FFmpeg 也支持单独对音频进行编辑，具体使用方法可参考 [FFmpeg 官网](http://ffmpeg.org/)。

### 执行 FFmpeg 命令

本文以 Python 为例，可以参考以下代码示例执行 FFmpeg 命令。

```python
child = subprocess.run('./ffmpeg -i input.mov output.mp4',
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, close_fds=True, shell=True)
if child.returncode == 0:
	print("success:", child)
else:
	print("error:", child)
		raise KeyError("处理视频失败，错误：", child)
```

## 在 SCF 上使用 FFmpeg

1. 登录云函数控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
2. 在“函数服务”页面上方选择地域，并单击**新建**进入新建函数页面。
3. 设置以下参数信息，并单击**下一步**，如下图所示： 
   - **创建方式**：选择**模板创建**。
   - **模糊搜索**：输入“视频剪辑”，并进行搜索。
    单击模板中的**查看详情**，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。单击 github 地址可以访问模板源码，模板源码中可查看此 API 的调用参数和使用方式。
 ![](https://qcloudimg.tencent-cloud.cn/raw/55c67bbd72f15eca250985a4a5c3186e.png)
4. 在**基础配置**中，默认生成**函数名称**，可根据使用需求自行修改。按照引导配置异步执行和运行角色：
   - 异步执行：勾选“启用”
   - 运行角色：勾选“启用”，选择“配置并使用 SCF 模板运行角色”，将会自动创建并选择关联了 VOD 全读写权限的 SCF 模板运行角色，或选择“使用已有角色”，在下拉列表中选择包含上述权限的已有角色。本文以“配置并使用 SCF 模板运行角色”为例。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/cdb5533f5e64a9ab0646c60d0db4d131.png)
>! 示例需要授权 SCF 操作 VOD 的权限，已默认勾选“运行角色”并自动完成函数运行角色的创建和所需 VOD 操作权限策略 QcloudVODFullAccess 的关联，如需调整，请选择“使用已有策略”或取消“运行角色”勾选。
>
5. 在**触发器配置**中，选择“自动创建”，如下图所示： 
>! 如需使用已有 API 服务创建 API 网关触发器或修改触发器配置，请选择“自定义创建”。
>
   ![](https://qcloudimg.tencent-cloud.cn/raw/147755a39cc3ba2d60c97252a7b3c5a5.png)
6. 单击**完成**，即可完成函数和触发器创建并获得该函数的 HTTP 触发域名。

## 落地案例

某在线教育企业，需要在每次学生上完网课之后把网课录像制作成一段 30 秒的视频，作为学生的学习成果。此案例有几个关键的信息：
1. 通常一堂课有 200 个学生，需要同时制作 200 个视频。
2. 需要把 1 小时的上课视频剪辑成 30 秒。
3. 由于每个学生的上课屏幕有所不同，因此录制的视频都是不同的。
4. 最终的成果视频还需要加上学生的名字和头像。
5. 学生结束上课的时间很集中，因此制作视频时会有短时高并发。
6. 每次上完课的时候才会需要制作视频，时段比较固定且集中。

综合上述特点，用 Serverless 云函数来做这样的视频剪辑具有多个优势：
1. 解决了 200 个并发的问题，不需要自行搭建过多服务器。
2. 解决了只在发生时段使用的问题，其他时段都没有成本产生。
3. 解决了需要较强计算能力快速制作视频的问题。

案例的参考架构图如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/af379a5ef33a75bc6d1b7181f8604828.png)

## 总结

通过编排、组合、复用上面列举的各种音视频剪辑的场景，即可满足多种场景诉求。将视频剪辑中用来控制各种效果的参数，转成调用服务时传入的参数，即可实现各种效果的定制化。
