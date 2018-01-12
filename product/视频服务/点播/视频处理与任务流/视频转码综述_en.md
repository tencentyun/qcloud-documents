Video transcoding is to convert a video stream into another one to adapt to different network bandwidths, terminal processing capabilities, and user requirements. Generally, VOD transcoding is called offline transcoding, and LVB transcoding is called instant transcoding.

Typical application scenarios of offline transcoding include:

- **Terminal adaptation**: Convert videos in specific formats to videos with better terminal adaption for distribution on the widest range of terminals. For example, you can transcode AVI videos (unfriendly network playback) to MP4 (supported by almost all web players) for distribution over the Internet.
- **Bandwidth adaptation**: Transcode videos at different bitrates (such as Ultra HD, HD, and SD) for you to choose based on your network bandwidth.
- **Friendly playback**: Optimize the video container format for better playback. For example, the MOOV head of some MP4 files may be at the file end, so some players must download the entire MP4 file before starting playing. To solve this problem, you can move the MOOV head to the file head by transcoding, so that the player can start playing without downloading the entire file.
- **Watermarking**: Add copyright-related images, such as TV station logo, into the video to declare the video copyright.
- **Reduced distribution bandwidth**: An advanced video encoding method is used to reduce the video bitrate while ensuring the image quality, thus saving bandwidth. For example, perform H.265 encoding for originally H.264 encoded videos.
- **Reduced storage costs**: Directly storing original videos for the purpose of archive may result in high storage costs. You can transcode them into videos of low bitrates to dramatically reduce storage costs.

The following is an offline transcoded video example with multi-bitrate videos and an APNG dynamic watermark:

<iframe src="https://playvideo.qcloud.com/vod/4564972818712033224/iplayer.html?appid=1253131631&fileid=4564972818712033224&autoplay=0&sw=1280&sh=720" frameborder="0" width="70%" height="360" scrolling="no"></iframe> <!-- iframe code is used multiple times in the page, but the JS code behind them only needs to be used once (to adjust the height of iframe) --> 
<script src="//imgcache.qq.com/open/qcloud/video/h5/fixifmheight.js" charset="utf-8"></script>

## Video Transcoding

### Transcoding Capability Overview

<table>
    <tr>
        <th style="width:18%">
            Category               
        </th>
        <th style="width:22%">
            Parameter/Controlled Item
        </th>
        <th>
            Description
        </th>
    </tr>
    <tr>
        <td rowspan=5>
            <a href="https://cloud.tencent.com/document/product/266/11732##.E5.B0.81.E8.A3.85.E6.A0.BC.E5.BC.8F(format)">Container format</a>
        </td>
        <td>
            Input format
        </td>
        <td>
            <li>AVI: The file extension is AVI;</li>
            <li>QuickTime: The file extension is MOV;</li>
            <li>MPEG: The file extension can be MPG, MPEG, MPE, DAT, VOB, ASF, 3GP, or MP4;</li>
            <li>WMV: The file extension can be WMV or ASF;</li>
            <li>Real: The file extension can be RM or RMVB;</li>
            <li>Flash: The file extension can be FLV or F4V;</li>
            <li>Matroska: The file extension is MKV.</li>
        </td>
    </tr>
    <tr>
        <td>
            Output format
        </td>
        <td>
            Video:
            <li>MP4</li>
            <li>HLS</li>
            <li>FLV</li>
            Audio:
            <li>MP3</li>
            <li>AAC</li>
            <li>OGG</li>
            <li>FLAC</li>
            Dynamic image:
            <li>GIF</li>
        </td>
    </tr>
    <tr>
        <td>
            Audio-only output
        </td>
        <td>
            Audio-only output is supported. That is, video streams are deleted.
        </td>
    </tr>
    <tr>
        <td>
            Video-only output
        </td>
        <td>
            Video-only output is supported. That is, audio streams are deleted.
        </td>
    </tr>
    <tr>
        <td>
            Re-wrapping
        </td>
        <td>
            Video re-wrapping is supported, with three output formats of MP4, HLS, and FLV.
        </td>
    </tr>
    <tr>
        <td rowspan=8>
            Video encoding parameters
        </td>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E7.BC.96.E7.A0.81.E6.96.B9.E5.BC.8F(codec)">Encoding method (Codec)</a>
        </td>
        <td>
            <li>H.264</li>
            <li>H.265</li>
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E7.A0.81.E7.8E.87(bitrate)">Bitrate</a>
        </td>
        <td>
            Output bitrate range: 10-50,000 Kbps.
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E5.B8.A7.E7.8E.87(frame-rate)">Frame rate</a>
        </td>
        <td>
            The following three frame rates are supported:
            <li>24 fps</li>
            <li>25 fps</li>
            <li>30 fps</li>
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E5.88.86.E8.BE.A8.E7.8E.87(resolution)">Resolution</a>
        </td>
        <td>
            <li>Width range: 128-4,096</li>
            <li>Height range: 128-4,096</li>
        </td>
    </tr>
    <tr>
        <td>
            Auto Zoom
        </td>
        <td>
            <li>Scaling proportionally to the width is supported</li>
            <li>Scaling proportionally to the height is supported</li>
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#gop(group-of-pictures)">GOP </a>duration
        </td>
        <td>
            GOP duration: 1-10 seconds.
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E7.BC.96.E7.A0.81.E6.A1.A3.E6.AC.A1(profile)">Encoding grade (Profile)</a>
        </td>
        <td>
            <li>H.264: Baseline, Main, High;</li>
            <li>H.265: Main only.</li>
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E9.A2.9C.E8.89.B2.E7.A9.BA.E9.97.B4(color-space)">Color Space</a>
        </td>
        <td>
            YUV420P.
        </td>
    </tr>
    <tr>
        <td rowspan=4>
            Video processing parameters
        </td>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E8.A7.86.E9.A2.91.E9.99.8D.E5.99.AA">Video noise reduction</a>
        </td>
        <td>
            Supported
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E5.8E.BB.E9.9A.94.E8.A1.8C.E6.89.AB.E6.8F.8F">Deinterlacing</a>
        </td>
        <td>
            Supported
        </td>
    </tr>
    <tr>
        <td>
            Bitrate control method
        </td>
        <td>
            The following bitrate control methods are supported:
            <li>Variable Bit Rate (VBR);</li>
            <li>Constant Bit Rate (CBR);</li>
            <li>Constant Rate Factor (CRF).</li>
        </td>
    </tr>
    <tr>
        <td>
            Video compression mode
        </td>
        <td>
            OnePass and TwoPass are supported.
        </td>
    </tr>
    <tr>
        <td rowspan=4>
            Audio encoding parameters
        </td>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E7.BC.96.E7.A0.81.E6.A0.BC.E5.BC.8F(codec)">Encoding method (Codec)</a>
        </td>
        <td>
            <li>MP3</li>
            <li>AAC</li>
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E9.87.87.E6.A0.B7.E7.8E.87(sample-rate)">Sampling Rate</a>
        </td>
        <td>
            The following audio sampling rates are supported:
            <li>44,100 HZ</li>
            <li>48,000 HZ</li>
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E7.A0.81.E7.8E.87(bitrate)2">Bitrate</a>
        </td>
        <td>
            The following audio bitrates are supported:
            <li>48 Kbps</li>
            <li>64 Kbps</li>
            <li>128 Kbps</li>
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11732#.E5.A3.B0.E9.81.93(sound-channel)">Channel</a>
        </td>
        <td>
            <li>MP3: mono, dual-channel</li>
            <li>AAC: mono, dual-channel</li>
        </td>
    </tr>
    <tr>
        <td rowspan=3>
            Transcoding control
        </td>
        <td>
            HLS MasterPlayList
        </td>
        <td>
            HLS MasterPlayList output is supported.
        </td>
    </tr>
    <tr>
        <td>
            Avoidance of converting bitrate/resolution from a low value to a high value
        </td>
        <td>
            The following two methods are supported:
            <li>If the bitrate/resolution of a target transcode template is higher than that of the source video, the transcoding for this specification is not performed. For example, the source video's bitrate is 600 Kbps, and three transcoding outputs are specified, with the respective bitrates of 256 Kbps, 512 Kbps and 1024 Kbps, only transcoding results for 256 Kbps and 512 Kbps are output if this option is enabled.</li>
            <li>If the bitrate/resolution of the target transcoding template is greater than that of the source video, the output bitrate/resolution is the same as that of the source video after transcoding. For example, a source video's bitrate is 600 Kbps, and three channels of transcoding outputs are specified, with respective bitrate of 256 Kbps, 512 Kbps and 1024 Kbps. If this option is enabled, the transcoded output bitrate for the third channel is still 600 Kbps, but other parameters of this channel are still output based on the parameters specified in the transcoding template.</li>
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81">Programmable transcoding process</a>
        </td>
        <td>
            Transcoding process can be flexibly controlled via Lua programs.
        </td>
    </tr>
    <tr>
        <td rowspan=1>
            Video content security
        </td>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/9638">Video encryption</a>
        </td>
        <td>
            HLS standard video encryption is supported.
        </td>
    </tr>
</table>

### Transcoding Template

Video processing involves many parameters, so VOD system uses transcoding templates to contain various transcoding parameters. You can simply specify a transcoding template to complete the video processing.

VOD system provides a set of preset transcoding templates for developers. For more information, please see [Preset Transcoding Templates](#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF). If the preset templates do not meet the demands, developers can customize transcoding templates as needed.

### Managing Transcodeing Templates through Console
Available soon.

### Managing Transcoding Templates with Server APIs
For more information, please see:
- Server API: [CreateTranscodeTemplate](https://cloud.tencent.com/document/product/266/9910)
- Server API: [UpdateTranscodeTemplate](https://cloud.tencent.com/document/product/266/9911)
- Server API: [QueryTranscodeTemplate](https://cloud.tencent.com/document/product/266/9912)
- Server API: [QueryTranscodeTemplateList](https://cloud.tencent.com/document/product/266/9913)
- Server API: [DeleteTranscodeTemplate](https://cloud.tencent.com/document/product/266/9914)


### Initiating Transcoding

#### Initiating Transcoding in the VOD Console
The document is to be completed.

#### Initiating Transcoding with Server APIs
For more information, please see:
- [Process Videos Using Task Flows](https://cloud.tencent.com/document/product/266/11700#.E4.BD.BF.E7.94.A8.E4.BB.BB.E5.8A.A1.E6.B5.81.E5.A4.84.E7.90.86.E8.A7.86.E9.A2.91)
- Server API: [ConvertVodFile](https://cloud.tencent.com/document/product/266/7822)

> Note:
> When you transcode a video by calling server APIs, it is recommended to use a task flow instead of a separate video transcoding API.

## Video Re-wrapping
Video re-wrapping is to change the video container format while keeping the video encoding method unchanged. For example, you can re-wrap an HLS video as MP4 for local downloading and editing.

Re-wrapping can be considered as a special transcoding. You can initiate video re-wrapping in the same way as initiating video transcoding. For more information, please see [Initiating Transcoding](#.E5.8F.91.E8.B5.B7.E8.BD.AC.E7.A0.81).

VOD system provides a set of re-wrapping templates. For more information, please see [Preset Re-wrapping Templates](#.E9.A2.84.E7.BD.AE.E8.BD.AC.E5.B0.81.E8.A3.85.E6.A8.A1.E6.9D.BF).

## Video Watermark

Video watermark is to add copyright-related images, such as TV station logo, into the video to declare the video copyright. In the process of video transcoding, you can specify a [Watermark Template](#.E6.B0.B4.E5.8D.B0.E6.A8.A1.E6.9D.BF) to add a watermark into the output video file.

### Watermark Type

VOD system supports two types of watermarks:
- **Static watermark**: The watermark is an image that is placed at a fixed position in the video, and displays from the beginning to the end of the video. JPG and PNG are supported, but it is recommended to use the PNG format;
- **Dynamic watermark**: The watermark is an [APNG](https://zh.wikipedia.org/wiki/APNG) dynamic image that is played on a loop at a fixed position of the video.

### Watermark Position

The position of a watermark is determined by parameters `left`, `top`, `width`, and `height`, as shown below:

![Diagram of Watermark Position Parameters](//mc.qcloudimg.com/static/img/c030e8efdcdda7c6abbd7875dbc68d7c/image.png)

The parameter descriptions are as follows:
- `left`: The distance from the left side of the watermark to the left side of the video;
- `top`: The distance from the top of the watermark to the top of the video;
- `width`: The watermark image width;
- `height`: The watermark image height.

All the four parameters support the following two calculation methods:

1. Calculation in pixels;
2. Calculation based on the watermark width/height percentage in the video width/height, that is:
    (1) `left` and ` width` are calculated based on the percentage of video width;
    (2) `top` and ` height` are calculated based on the percentage of video height.

If only `width` is specified and `height` is not specified, the aspect ratio of the original watermark image is used.

For example:
> Suppose a video file with a resolution of 1280×720 needs to add a watermark with a resolution of 100×100:
> - `left` = 100 px, indicating that the left side of the watermark is 100 pixels to the left side of the video;
> - `top` = 10%, indicating that the distance from the top of the watermark to the top of the video is 10% of the video height, i.e. 128 pixels (1280×10%=128);
> - If `width` is 5% and `height` is not specified, the watermark width is 64 pixels (1280×5%=64), and the height is 64 pixels (because the aspect ratio of the watermark image is 1:1, the height and width are same, i.e. 64 pixels).

For multi-bitrate transcoding, if the size and position of watermarks at different bitrates should remain the same, it is recommended to calculate based on percentage.

### Watermark Template

Video watermark involves many parameters, so VOD system uses watermark templates to contain various watermark parameters. You can simply specify a watermark template to add a video watermark in the process of transcoding.

Developers can manage watermark templates through the console and server APIs. For now, you can only set the watermark position based on the width/height percentage instead of pixel offset in the console, and watermark size setting is not supported. Complete watermark management features in the console will be available soon.

### Managing Watermark Templates through the Console
The document is to be completed.

### Managing Watermark Templates with Server APIs

A watermark template can be created in three steps with server APIs:
1. Call the API [ApplyUploadWatermark](https://cloud.tencent.com/document/product/266/11607) to request the upload URL of the watermark file;
2. Use the HTTP PUT method to upload the watermark file to the URL returned in step 1. The request body is the binary data of the watermark image;
3. Call the API [CreateWatermarkTemplate](https://cloud.tencent.com/document/product/266/11599) to create a watermark template.

> The following example shows how to upload a watermark file in step 2:
> Suppose the URL returned by the API ApplyUploadWatermark is `http://123.test.com/123.png&sign=abcd` and the local watermark file to upload is `123.png`, the curl command used to upload the watermark file is as follows:
> 
> <pre>
> curl 'http://123.test.com/123.png&sign=abcd' --upload-file 123.png
> </pre>

For more information, please see:
- Server API: [ApplyUploadWatermark](https://cloud.tencent.com/document/product/266/11607)
- Server API: [CreateWatermarkTemplate](https://cloud.tencent.com/document/product/266/11599)
- Server API: [UpdateWatermarkTemplate](https://cloud.tencent.com/document/product/266/11605)
- Server API: [QueryWatermarkTemplate](https://cloud.tencent.com/document/product/266/11606)
- Server API: [QueryWatermarkTemplateList](https://cloud.tencent.com/document/product/266/11608)
- Server API: [DeleteWatermarkTemplate](https://cloud.tencent.com/document/product/266/11604)

## Preset Transcoding Template

### Preset Transcoding Template
<table>
    <tr>
        <th rowspan=2>
            Grade                
        </th>
        <th rowspan=2>
            Template ID                
        </th>
        <th rowspan=2>
            Container Format
        </th>
        <th colspan=4>    
            Video Parameter
        </th>
        <th colspan=1>    
            Audio Parameter
        </th>
    </tr>
    <tr>
        <th>
            Resolution
        </th>
        <th>
            Bitrate
        </th>
        <th>
            Frame rate (FPS)
        </th>
        <th>
            Encoding (Codec)
        </th>
        <th>
            Encoding (Codec)
        </th>
    </tr>
    <tr>
        <td rowspan=6>
            Fluent (FLU)
        </td>
        <td>
            10
        </td>
        <td>
            MP4
        </td>
        <td>
            320 × Scaling proportionally
        </td>
        <td>
            256 Kbps
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
            Scaling proportionally × 240
        </td>
        <td>
            250 Kbps
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
            320 × Scaling proportionally
        </td>
        <td>
            256 Kbps
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
            Scaling proportionally × 240
        </td>
        <td>
            250 Kbps
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
            320 × Scaling proportionally
        </td>
        <td>
            256 Kbps
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
            Scaling proportionally × 240
        </td>
        <td>
            250 Kbps
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
            Standard Definition (SD)
        </td>
        <td>
            20
        </td>
        <td>
            MP4
        </td>
        <td>
            640 × Scaling proportionally
        </td>
        <td>
            512 Kbps
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
            Scaling proportionally × 480
        </td>
        <td>
            600 Kbps
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
            640 × Scaling proportionally
        </td>
        <td>
            512 Kbps
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
            Scaling proportionally × 480
        </td>
        <td>
            600 Kbps
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
            640 × Scaling proportionally
        </td>
        <td>
            512 Kbps
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
            Scaling proportionally × 480
        </td>
        <td>
            600 Kbps
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
            High Definition (HD)
        </td>
        <td>
            30
        </td>
        <td>
            MP4
        </td>
        <td>
            1280 × Scaling proportionally
        </td>
        <td>
            1024 Kbps
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
            Scaling proportionally × 720
        </td>
        <td>
            800 Kbps
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
            1280 × Scaling proportionally
        </td>
        <td>
            1024 Kbps
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
            Scaling proportionally × 720
        </td>
        <td>
            800 Kbps
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
            1280 × Scaling proportionally
        </td>
        <td>
            1024 Kbps
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
            Scaling proportionally × 720
        </td>
        <td>
            800 Kbps
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
            Full High Definition (FHD)
        </td>
        <td>
            40
        </td>
        <td>
            MP4
        </td>
        <td>
            1920 × Scaling proportionally
        </td>
        <td>
            2,500 Kbps
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
            Scaling proportionally × 1080
        </td>
        <td>
            1,400 Kbps
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
            1920 × Scaling proportionally
        </td>
        <td>
            2,500 Kbps
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
            Scaling proportionally × 1080
        </td>
        <td>
            1,400 Kbps
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
            1920 × Scaling proportionally
        </td>
        <td>
            2,500 Kbps
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
            Scaling proportionally × 1080
        </td>
        <td>
            1,400 Kbps
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
            Scaling proportionally × 1440
        </td>
        <td>
            3,072 Kbps
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
            Scaling proportionally × 1440
        </td>
        <td>
            2,048 Kbps
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
            Scaling proportionally × 1440
        </td>
        <td>
            3,072 Kbps
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
            Scaling proportionally × 1440
        </td>
        <td>
            2,048 Kbps
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
            Scaling proportionally × 1440
        </td>
        <td>
            3,072 Kbps
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
            Scaling proportionally × 1440
        </td>
        <td>
            2,048 Kbps
        </td>
        <td>
            30
        </td>
        <td>
            H.265
        </td>
        <td>
            aac
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
            Scaling proportionally × 2160
        </td>
        <td>
            6,144 Kbps
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
            Scaling proportionally × 2160
        </td>
        <td>
            4,096 Kbps
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
            Scaling proportionally × 2160
        </td>
        <td>
            6,144 Kbps
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
            Scaling proportionally × 2160
        </td>
        <td>
            4,096 Kbps
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
            Scaling proportionally × 2160
        </td>
        <td>
            6,144 Kbps
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
            Scaling proportionally × 2160
        </td>
        <td>
            4,096 Kbps
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

The following parameters of the above transcoding templates are the same:

<table>
    <tr>
        <th style="width:18%">
            Category               
        </th>
        <th style="width:22%">
            Parameter/Controlled Item
        </th>
        <th>
            Description
        </th>
    </tr>
    <tr>
        <td rowspan=3>
            Video encoding parameters
        </td>
        <td>
            Encoding grade
        </td>
        <td>
            H.264 is High; H.265 is Main
        </td>
    </tr>
    <tr>
        <td>
            GOP duration
        </td>
        <td>
            240 frames
        </td>
    </tr>
    <tr>
        <td>
            Color space
        </td>
        <td>
            YUV420P
        </td>
    </tr>
    <tr>
        <td rowspan=3>
            Video processing parameters
        </td>
        <td>
            Video noise reduction
        </td>
        <td>
            Disabled
        </td>
    </tr>
    <tr>
        <td>
            Deinterlacing
        </td>
        <td>
            Disabled
        </td>
    </tr>
    <tr>
        <td>
            Bitrate control method
        </td>
        <td>
            VBR encoding
        </td>
    </tr>
    <tr>
        <td rowspan=3>
            Audio encoding parameters
        </td>
        <td>
            Sampling rate
        </td>
        <td>
            44,100 HZ
        </td>
    </tr>
    <tr>
        <td>
            Bitrate
        </td>
        <td>
            48 Kbps
        </td>
    </tr>
    <tr>
        <td>
            Number of channels
        </td>
        <td>
            Dual-channel
        </td>
    </tr>
</table>

### Preset Re-wrapping Template
| Output Format | Template ID |
|---------|---------|
| MP4 | 9 |
| HLS | 6 |
