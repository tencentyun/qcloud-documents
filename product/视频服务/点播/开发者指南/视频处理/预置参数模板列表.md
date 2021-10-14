云点播支持使用参数模板代替复杂的参数集合，发起视频处理。针对不同视频处理的场合，云点播预置了一批参数模板。

## 视频转换类

视频转换类的预置参数模板包含了以下几种类型：
- 预置转码模板
- 预置转封装模板
- 预置转动图模板
- 预置指定时间点截图模板
- 预置采样截图模板
- 预置雪碧图模板
- 预置转自适应码流模板

[](id:transcoding)
### 预置转码模板
#### 转码视频格式

<table class="table auto-table"><tbody><tr><th colspan="1" rowspan="2">规格等级</th><th colspan="1" rowspan="2">模板 ID</th><th colspan="1" rowspan="2">封装格式（Format）</th><th colspan="4">视频参数</th><th colspan="4">音频参数</th></tr>
<tr><th colspan="1">分辨率（Resolution）</th><th colspan="1">码率（Bitrate）</th><th colspan="1">帧率（FPS）</th><th colspan="1">编码（Codec）</th><th colspan="1">码率（Bitrate）</th><th colspan="1">采样频率（SampleRate）</th><th colspan="1">音频声道数（SoundSystem）</th><th colspan="1">编码（Codec）</th></tr>
<tr><td colspan="1" rowspan="2">流畅（FLU）</td><td colspan="1">100010</td><td colspan="1">MP4</td><td colspan="1" rowspan="2">按比例缩放 × 360</td><td colspan="1" rowspan="2">400kbps</td><td colspan="1" rowspan="12">25</td><td colspan="1" rowspan="12">H.264</td><td colspan="1" rowspan="4">64 kbps</td ><td colspan="1" rowspan="12">44100Hz</td><td colspan="1" rowspan="12">双声道（Stereo）</td><td colspan="1" rowspan="12">AAC</td></tr>
<tr><td colspan="1">100210</td><td colspan="1">HLS</td></tr>
<tr><td colspan="1" rowspan="2">标清（SD）</td><td colspan="1">100020</td><td colspan="1">MP4</td><td colspan="1" rowspan="2">按比例缩放 × 540</td><td colspan="1" rowspan="2">1000kbps</td></tr>
<tr><td colspan="1">100220</td><td colspan="1">HLS</td></tr>
<tr><td colspan="1" rowspan="2">高清（HD）</td><td colspan="1">100030</td><td colspan="1">MP4</td><td colspan="1" rowspan="2">按比例缩放 × 720</td><td colspan="1" rowspan="2">1800kbps</td><td colspan="1" rowspan="4">128kbps</td></tr>
<tr><td colspan="1">100230</td><td colspan="1">HLS</td></tr>
<tr><td colspan="1" rowspan="2">全高清（FHD）</td><td colspan="1">100040</td><td colspan="1">MP4</td><td colspan="1" rowspan="2">按比例缩放 × 1080</td><td colspan="1" rowspan="2">2500kbps</td></tr>
<tr><td colspan="1">100240</td><td colspan="1">HLS</td></tr>
<tr><td colspan="1" rowspan="2">2K</td><td colspan="1">100070</td><td colspan="1">MP4</td><td colspan="1" rowspan="2">按比例缩放 × 1440</td><td colspan="1" rowspan="2">3000kbps</td><td colspan="1" rowspan="4">160kbps</td></tr>
<tr><td colspan="1">100270</td><td colspan="1">HLS</td></tr>
<tr><td colspan="1" rowspan="2">4K</td><td colspan="1">100080</td><td colspan="1">MP4</td><td colspan="1" rowspan="2">按比例缩放 × 2160</td><td colspan="1" rowspan="2">6000kbps</td></tr>
<tr><td colspan="1">100280</td><td colspan="1">HLS</td></tr></tbody></table>

#### 转码音频格式[](id:music)

<table>
    <tr>
        <th rowspan=1>
            模板 ID                
        </th>
        <th rowspan=1>
            封装格式（Format）
        </th>
        <th>
            音频码率（Bitrate）
        </th>
        <th>
            编码（Codec）
        </th>
        <th>
            声道数（SoundSystem）
        </th>
        <th>
            采样频率（SampleRate）
        </th>
    </tr>
 <tr>
        <td>
            1100
        </td>
        <td rowspan="5">
            M4A
        </td>
        <td>
            24kbps
        </td>
        <td rowspan="5">
            AAC
        </td>
        <td rowspan="7">
            双通道（Stereo）
        </td>
        <td rowspan="7">
            44100Hz
        </td>
    </tr>
 <tr>
        <td>
            1110
        </td>
        <td>
            48kbps
        </td>
    </tr>
    <tr>
        <td>
            1120
        </td>
        <td>
            96kbps
        </td>
    </tr>
     <tr>
        <td>
            1130
        </td>
        <td>
            192kbps
        </td>
    </tr>
    <tr>
        <td>
            1140
        </td>
        <td>
            256kbps
        </td>
    </tr>
    <tr>
        <td>
            1010
        </td>
        <td rowspan="2">
            MP3
        </td>
        <td>
            128kbps
        </td>
        <td rowspan="2">
            MP3
        </td>
    </tr>
    <tr>
        <td>
            1020
        </td>
        <td>
            320kbps
        </td>
    </tr>
</table>


### 预置极速高清模板

<table class="table auto-table"><tbody><tr><th colspan="1" rowspan="2">规格等级</th><th colspan="1" rowspan="2">模板 ID</th><th colspan="1" rowspan="2">封装格式（Format）</th><th colspan="4">视频参数</th><th colspan="4">音频参数</th></tr>
<tr><th colspan="1">分辨率（Resolution）</th><th colspan="1">最大码率（Bitrate）</th><th colspan="1">帧率（FPS）</th><th colspan="1">编码（Codec）</th><th colspan="1">码率（Bitrate）</th><th colspan="1">采样频率（SampleRate）</th><th colspan="1">音频声道数（SoundSystem）</th><th colspan="1">编码（Codec）</th></tr>
<tr><td colspan="1">同源（SAME）</td><td colspan="1" rowspan="">100800</td><td colspan="1" rowspan="5">MP4</td><td colspan="1">同源</td><td colspan="1" rowspan="5">无限制</td><td colspan="1" rowspan="5">25</td><td colspan="1" rowspan="5">H.264</td><td colspan="1">同源</td><td colspan="1" rowspan="5">44100Hz</td><td colspan="1" rowspan="5">双声道（Stereo）</td><td colspan="1" rowspan="5">AAC</td></tr></tr>
<tr><td colspan="1">流畅（FLU）</td><td colspan="1">100810</td><td colspan="1">按比例缩放 × 360</td><td colspan="1" rowspan="2">64 kbps</td></tr>
<tr><td colspan="1">标清（SD）</td><td colspan="1">100820</td><td colspan="1">按比例缩放 × 540</td></tr>
<tr><td colspan="1">高清（HD）</td><td colspan="1">100830</td><td colspan="1" rowspan="">按比例缩放 × 720</td><td colspan="1" rowspan="2">128kbps</td></tr>
<tr><td colspan="1">全高清（FHD）</td><td colspan="1">100840</td><td colspan="1">按比例缩放 × 1080</td></tr></tbody></table>


### 预置转封装模板

| 模板 ID | 转封装目标格式（Format） |
| ------- | ------------------------ |
| 875       | MP4                      |
| 876       | HLS                      |

[](id:cinemagraph)
### 预置转动图模板

| 模板 ID | 图片格式（Format） | 分辨率（Resolution） | 帧率（FPS） |
| ------- | ------------------ | -------------------- | ----------- |
| 20000   | GIF                | 同源                 | 2           |
| 20001   | WEBP               | 同源                 | 2           |

[](id:screenshot01)
### 预置指定时间点截图模板

| 模板 ID | 输出格式（Format） | 宽度（Width） | 高度（Height） | 填充方式（FillType） |
| ------- | ------------------ | ------------- | -------------- | -------------------- |
| 10      | JPG                | 同源          | 同源           | 拉伸                 |

[](id:screenshot02)
### 预置采样截图模板

| 模板 ID | 输出格式（Format） | 宽度（Width） | 高度（Height） | 采样方式（SampleType） | 截图间隔（Interval） | 填充方式（FillType） |
| ------- | ------------------ | ------------- | -------------- | ---------------------- | -------------------- | -------------------- |
| 10      | JPG                | 同源          | 同源           | 按百分比               | 10%                  | 拉伸                 |

[](id:screenshot03)
### 预置雪碧图模板

| 模板 ID | 输出格式（Format） | 小图宽度（Width） | 小图高度（Height） | 小图行数（Rows） | 小图列数（Columns） | 采样方式（SampleType） | 截图间隔（Interval） |
| ------- | ------------------ | ----------------- | ------------------ | ---------------- | ------------------- | ---------------------- | -------------------- |
| 10      | JPG                | 142               | 80                 | 10               | 10                  | 按时间间隔             | 10秒                 |

### 预置转自适应码流模板
#### 模板信息

<table border="0" >
 <tr>
  <th>模板 ID</td>
  <th>打包类型（PackageType）</td>
  <th>加密类型（EncryptionType）</td>
  <th>子流信息（SubstreamInfo）</td>
  <th >过滤“低分辨率转高分辨率” （DisableHigherResolution）</td>
 </tr>
 <tr>
  <td>10</td>
  <td>HLS</td>
  <td >不加密</td>
  <td >包含从“流畅”到“4K”共6个规格的子流</td>
  <td>是</td>
 </tr>
 <tr>
  <td>12</td>
  <td>HLS</td>
  <td>SimpleAES</td>
  <td >包含从“流畅”到“4K”共6个规格的子流</td>
  <td>是</td>
 </tr>
  <tr>
  <td>20</td>
  <td>MPEG-DASH</td>
  <td>	不加密</td>
  <td >包含从”流畅”到“4K“共6个规格的子流</td>
  <td>否</td>
 </tr>
</table>

#### 子流信息

<table border="0" >
 <tr>
  <th rowspan="2" >子流规格</td>
  <th colspan="4" >视频参数</td>
  <th colspan="4" >音频参数</td>
 </tr>
 <tr>
  <th>分辨率（Resolution）</th>
  <th>码率（Bitrate）</th>
  <th >帧率（FPS）</th>
  <th >编码（Codec）</th>
  <th>码率（Bitrate）</th>
  <th>采样频率（SampleRate）</th>
  <th>音频声道数（SoundSystem）</th>
  <th>编码（Codec）</td>
 </tr>
 <tr>
  <td>流畅</td>
  <td>按比例缩放 x 240</td>
  <td>256kbps</td>
  <td>24</td>
  <td>H.264</td>
  <td>48kbps</td>
  <td>44100Hz</td>
  <td>双声道（Stero）</td>
  <td>AAC</td>
 </tr>
 <tr>
  <td>标清</td>
  <td>按比例缩放 x 480</td>
  <td>512kbps</td>
  <td>24</td>
  <td>H.264</td>
  <td>48kbps</td>
  <td>44100Hz</td>
  <td>双声道（Stero）</td>
  <td>AAC</td>
 </tr>
 <tr>
  <td>高清</td>
  <td>按比例缩放 x 720</td>
  <td>512kbps</td>
  <td>24</td>
  <td>H.264</td>
  <td>48kbps</td>
  <td>44100Hz</td>
  <td>双声道（Stero）</td>
  <td>AAC</td>
 </tr>
 <tr>
  <td>全高清</td>
  <td>按比例缩放 x 1080</td>
  <td>1024kbps</td>
  <td>24</td>
  <td>H.264</td>
  <td>48kbps</td>
  <td>44100Hz</td>
  <td>双声道（Stero）</td>
  <td>AAC</td>
 </tr>
 <tr>
  <td>2K</td>
  <td>按比例缩放 x 1440</td>
  <td>3072kbps</td>
  <td>24</td>
  <td>H.264</td>
  <td>48kbps</td>
  <td>44100Hz</td>
  <td>双声道（Stero）</td>
  <td>AAC</td>
 </tr>
 <tr>
  <td>4K</td>
  <td>按比例缩放 x 2160</td>
  <td>6144kbps</td>
  <td>24</td>
  <td>H.264</td>
  <td>48kbps</td>
  <td>44100Hz</td>
  <td>双声道（Stero）</td>
  <td>AAC</td>
 </tr>
</table>


## 视频 AI 类

视频 AI 类的预置参数模板包含了以下几种类型：

* 预置视频内容审核模板
* 预置视频内容分析模板
* 预置视频内容识别模板

### 预置视频审核模板[](id:verify)


<table>
    <tr>
        <th rowspan=2>
            模板 ID                
        </th>
        <th colspan=3>
            视频画面
        </th>
        <th colspan=2>
            ASR 文字
        </th>
        <th colspan=2>
            OCR 文字
        </th>
    </tr>
 <tr>
        <th>
            令人反感的信息（Porn）
        </th>
        <th>
            令人不安全的信息（Terrorism）
        </th>
        <th>
            令人不适宜的信息（Political）
        </th>
        <th>
            令人反感的信息（Asr.Porn）
        </th>
        <th>
            令人不适宜的信息（Asr.Political）
        </th>
        <th>
            令人反感的信息（Ocr.Porn）
        </th>
        <th>
            令人不适宜的信息（Ocr.Political）
        </th>
    </tr>
    <tr>
        <td>
            10
        </td>
        <td>
            是
        </td>
        <td>
            是
        </td>
        <td>
            是
        </td>
        <td>
            否
        </td>
        <td>
            否
        </td>
        <td>
            否
        </td>
        <td>
            否
        </td>
    </tr>
    <tr>
        <td>
            20
        </td>
        <td>
            是
        </td>
        <td>
            是
        </td>
        <td>
            是
        </td>
        <td>
            是
        </td>
        <td>
            是
        </td>
        <td>
            是
        </td>
        <td>
            是
        </td>
    </tr>
</table>

### 预置视频内容分析模板

| 模板 ID | 智能分类（Classification） | 智能标签（Tag） | 智能封面（Cover） | 智能按帧标签（FrameTag） |
| -- | -- | -- | -- | -- |
| 10 | 是 | 是 | 是 | 否 |
| 20 | 是 | 是 | 是 | 是 |

### 预置视频内容识别模板

| 模板 ID | 人脸识别（Face） | 文本全文识别（OcrFullText） | 文本关键词识别（OcrWords） | 语音全文识别（AsrFullText） | 语音关键词识别（AsrWords） | 
| -- | -- | -- | -- | -- | -- |
| 10 | 是（使用默认人物库） | 否 | 否 | 否 | 否 |




## 历史转码类

### 历史预置转码模板

#### 转码视频格式

<table>
    <tr>
        <th rowspan=2>
            规格等级                
        </th>
        <th rowspan=2>
            模板 ID                
        </th>
        <th rowspan=2>
            封装格式（Format）
        </th>
        <th colspan=4>    
            视频参数
        </th>
        <th colspan=1>    
            音频参数
        </th>
    </tr>
    <tr>
        <th>
            分辨率（Resolution）
        </th>
        <th>
            码率（Bitrate）
        </th>
        <th>
            帧率（FPS）
        </th>
        <th>
            编码（Codec）
        </th>
        <th>
            编码（Codec）
        </th>
    </tr>
    <tr>
        <td rowspan=6>
            流畅（FLU）
        </td>
        <td>
            10
        </td>
        <td>
            MP4
        </td>
        <td>
            320 × 按比例缩放
        </td>
        <td>
            256kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            510
        </td>
        <td>
            MP4
        </td>
        <td>
            按比例缩放 × 240
        </td>
        <td>
            250kbps
        </td>
        <td>
            15
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            210
        </td>
        <td>
            HLS
        </td>
        <td>
            320 × 按比例缩放
        </td>
        <td>
            256kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            610
        </td>
        <td>
            HLS
        </td>
        <td>
            按比例缩放 × 240
        </td>
        <td>
            250kbps
        </td>
        <td>
            15
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            10046
        </td>
        <td>
            FLV
        </td>
        <td>
            320 × 按比例缩放
        </td>
        <td>
            256kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            MP3
        </td>
    </tr>
    <tr>
        <td>
            710
        </td>
        <td>
            FLV
        </td>
        <td>
            按比例缩放 × 240
        </td>
        <td>
            250kbps
        </td>
        <td>
            15
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td rowspan=6>
            标清（SD）
        </td>
        <td>
            20
        </td>
        <td>
            MP4
        </td>
        <td>
            640 × 按比例缩放
        </td>
        <td>
            512kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            520
        </td>
        <td>
            MP4
        </td>
        <td>
            按比例缩放 × 480
        </td>
        <td>
            600kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            220
        </td>
        <td>
            HLS
        </td>
        <td>
            640 × 按比例缩放
        </td>
        <td>
            512kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            620
        </td>
        <td>
            HLS
        </td>
        <td>
            按比例缩放 × 480
        </td>
        <td>
            600kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            10047
        </td>
        <td>
            FLV
        </td>
        <td>
            640 × 按比例缩放
        </td>
        <td>
            512kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            MP3
        </td>
    </tr>
    <tr>
        <td>
            720
        </td>
        <td>
            FLV
        </td>
        <td>
            按比例缩放 × 480
        </td>
        <td>
            600kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td rowspan=6>
            高清（HD）
        </td>
        <td>
            30
        </td>
        <td>
            MP4
        </td>
        <td>
            1280 × 按比例缩放
        </td>
        <td>
            1024kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            530
        </td>
        <td>
            MP4
        </td>
        <td>
            按比例缩放 × 720
        </td>
        <td>
            800kbps
        </td>
        <td>
            25
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            230
        </td>
        <td>
            HLS
        </td>
        <td>
            1280 × 按比例缩放
        </td>
        <td>
            1024kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            630
        </td>
        <td>
            HLS
        </td>
        <td>
            按比例缩放 × 720
        </td>
        <td>
            800kbps
        </td>
        <td>
            25
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            10048
        </td>
        <td>
            FLV
        </td>
        <td>
            1280 × 按比例缩放
        </td>
        <td>
            1024kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            MP3
        </td>
    </tr>
    <tr>
        <td>
            730
        </td>
        <td>
            FLV
        </td>
        <td>
            按比例缩放 × 720
        </td>
        <td>
            800kbps
        </td>
        <td>
            25
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td  rowspan=6>
            全高清（FHD）
        </td>
        <td>
            40
        </td>
        <td>
            MP4
        </td>
        <td>
            1920 × 按比例缩放
        </td>
        <td>
            2500kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            540
        </td>
        <td>
            MP4
        </td>
        <td>
            按比例缩放 × 1080
        </td>
        <td>
            1400kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            240
        </td>
        <td>
            HLS
        </td>
        <td>
            1920 × 按比例缩放
        </td>
        <td>
            2500kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            640
        </td>
        <td>
            HLS
        </td>
        <td>
            按比例缩放 × 1080
        </td>
        <td>
            1400kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            10049
        </td>
        <td>
            FLV
        </td>
        <td>
            1920 × 按比例缩放
        </td>
        <td>
            2500kbps
        </td>
        <td>
            24
        </td>
        <td>
            H.264
        </td>
        <td>
            MP3
        </td>
    </tr>
    <tr>
        <td>
            740
        </td>
        <td>
            FLV
        </td>
        <td>
            按比例缩放 × 1080
        </td>
        <td>
            1400kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td  rowspan=6>
            2K
        </td>
        <td>
            70
        </td>
        <td>
            MP4
        </td>
        <td>
            按比例缩放 × 1440
        </td>
        <td>
            3072kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            570
        </td>
        <td>
            MP4
        </td>
        <td>
            按比例缩放 × 1440
        </td>
        <td>
            2048kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            270
        </td>
        <td>
            HLS
        </td>
        <td>
            按比例缩放 × 1440
        </td>
        <td>
            3072kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            670
        </td>
        <td>
            HLS
        </td>
        <td>
            按比例缩放 × 1440
        </td>
        <td>
            2048kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            370
        </td>
        <td>
            FLV
        </td>
        <td>
            按比例缩放 × 1440
        </td>
        <td>
            3072kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.264
        </td>
        <td>
            MP3
        </td>
    </tr>
    <tr>
        <td>
            770
        </td>
        <td>
            FLV
        </td>
        <td>
            按比例缩放 × 1440
        </td>
        <td>
            2048kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td  rowspan=6>
            4K
        </td>
        <td>
            80
        </td>
        <td>
            MP4
        </td>
        <td>
            按比例缩放 × 2160
        </td>
        <td>
            6144kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            580
        </td>
        <td>
            MP4
        </td>
        <td>
            按比例缩放 × 2160
        </td>
        <td>
            4096kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            280
        </td>
        <td>
            HLS
        </td>
        <td>
            按比例缩放 × 2160
        </td>
        <td>
            6144kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.264
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            680
        </td>
        <td>
            HLS
        </td>
        <td>
            按比例缩放 × 2160
        </td>
        <td>
            4096kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
    <tr>
        <td>
            380
        </td>
        <td>
            FLV
        </td>
        <td>
            按比例缩放 × 2160
        </td>
        <td>
            6144kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.264
        </td>
        <td>
            MP3
        </td>
    </tr>
    <tr>
        <td>
            780
        </td>
        <td>
            FLV
        </td>
        <td>
            按比例缩放 × 2160
        </td>
        <td>
            4096kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.265
        </td>
        <td>
            AAC
        </td>
    </tr>
</table>

以上转视频模板中未注明的参数全部相同，分别是：

<table>
    <tr>
        <th style="width:18%">
            分类               
        </th>
        <th style="width:22%">
            参数/能力项
        </th>
        <th>
            说明
        </th>
    </tr>
    <tr>
        <td rowspan=4>
            视频参数
        </td>
        <td>
            编码档次
        </td>
        <td>
				    <ul>
				       <li>使用 H.264 编码时，编码档次为 High</li>
						   <li>使用 H.265 编码的，编码档次为 Main</li>
				    </ul>
        </td>
    </tr>
    <tr>
        <td>
            GOP 长度
        </td>
        <td>
            240帧
        </td>
    </tr>
    <tr>
        <td>
            颜色空间
        </td>
        <td>
            YUV420P
        </td>
    </tr>
    <tr>
        <td>
            码率控制方法
        </td>
        <td>
            动态比特率编码（VBR）
        </td>
    </tr>
    <tr>
        <td rowspan=3>
            音频参数
        </td>
        <td>
            采样率
        </td>
        <td>
            44100Hz
        </td>
    </tr>
    <tr>
        <td>
            码率
        </td>
        <td>
            48kbps
        </td>
    </tr>
    <tr>
        <td>
            声道数
        </td>
        <td>
            双通道（Stereo）
        </td>
    </tr>
</table>
