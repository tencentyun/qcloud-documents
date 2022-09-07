## 操作场景
本文介绍如何在视频增强型实例 GN7vi 服务器上进行视频编解码和 AI 画质增强。视频增强型实例 GN7vi 提供了视频编解码功能和 AI 画质增强功能，使用方式和开源 FFmpeg 完全兼容，您可以参考本文完成视频画质处理。


## 操作步骤

### 实例环境准备
参考 [创建 NVIDIA GPU 实例](https://cloud.tencent.com/document/product/560/30211) 创建一台实例。其中：
 - **实例**：根据对 GPU 和内核数量的需求，参考 [视频增强型 GN7vi](https://cloud.tencent.com/document/product/560/19700#GN7vi) 选择。
 - **镜像**：可参考表格中的 [可用镜像](https://cloud.tencent.com/document/product/560/19700#.E8.AE.A1.E7.AE.97.E5.9E.8B.E5.AE.9E.E4.BE.8B.E6.80.BB.E8.A7.88) 进行选择。
 - **驱动**：CUDA 及 cuDNN 的自动安装并非本次部署的必选项，您可根据实际情况选择。可选择如下安装方式：
<dx-tabs>
::: 创建实例时自动安装

部分镜像支持自动安装驱动，通过勾选“后台自动安装GPU驱动”进行安装。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/51947eb1013c53a045a33342003291e9.png)
若您所选的镜像版本不支持自动安装驱动，可参考手动安装步骤登录实例进行安装。

:::
::: 创建实例后手动安装

1. 参考 [使用标准方式登录 Windows 实例](https://cloud.tencent.com/document/product/213/57778)，登录已创建的 GPU 云服务器。
2. 执行以下命令，实现 GPU 驱动、CUDA、cuDNN 的自动安装。
<dx-alert infotype="explain" title="">
环境版本配置为 GPU 驱动460.106.00、CUDA11.2.2和 cuDNN8.2.1。若您有其他版本需要，可通过 [联系我们](#contact) 咨询。
</dx-alert> ```shell
wget https://gpu-related-scripts-1251783334.cos.ap-guangzhou.myqcloud.com/gpu-auto-install/gpu_auto_install_220823.sh && wget https://gpu-related-scripts-1251783334.cos.ap-guangzhou.myqcloud.com/gpu-auto-install/driver460_cuda11.2.2.txt && sudo bash ./gpu_auto_install_220823.sh install --config_file=./driver460_cuda11.2.2.txt && source /etc/bash.bashrc && source ${HOME}/.bashrc
```

:::
</dx-tabs>



### 文件总览
依次执行以下命令，进入 tscsdk-center 查看当前目录下的所有文件。
```shell
cd /usr/local/qcloud/tscsdk-center
```
```shell
ls -l
```
返回结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b95500646122d69983e86bcce2563ffb.png)
说明如下：
<table>
<tr>
<th>文件名</th>
<th>说明</th>
</tr>
<tr>
<td>fflib_gpu</td>
<td>画质处理程序的运行依赖库。</td>
</tr>
<tr>
<td>ffmpeg</td>
<td>已经嵌入画质处理功能的 ffmpeg 程序。</td>
</tr>
<tr>
<td>tenmodel</td>
<td>画质处理使用的 AI 模型。</td>
</tr>
<tr>
<td>videos</td>
<td>内置的样例视频。</td>
</tr>
</table>


### 开始使用
1.依次执行以下命令，设置环境变量。
```shell
cd /usr/local/qcloud/tscsdk-center
```
```shell
export LD_LIBRARY_PATH=./fflib_gpu:$LD_LIBRARY_PATH
```
2. 在 tscsdk-center 目录下，依次执行以下命令，生成经画质处理之后的样例输出视频。
 - 低清视频处理：低清视频一般指分辨率小于或等于720p的视频，该命令使用了 tenfilter 中均衡模式下的标准超分辨率模型以及 unsharp 锐化处理。
```shell
./ffmpeg -i ./videos/input1.mp4 -vf tenfilter=mag_filter=1:mag_sr=2:mag_sr_stre=balance,unsharp -c:v libten264 -ten264opts crf=26:vbv-maxrate=2000 -y output1.mp4
```
 - 高清视频处理：高清视频一般指分辨率大于720p的视频。该命令使用了 tenfilter 中的高质量超分辨率模型。
```shell
./ffmpeg -i ./videos/input2.mp4 -vf tenfilter=mag_srgan=1 -c:v libten264 -ten264opts crf=26:vbv-maxrate=2000 -y output2.mp4
```
 - 快速处理模型：以下命令使用了 tenfilter 中的去压缩伪影、正常模式下的标准超分辨率模型以及 unsharp 锐化处理。
```shell
./ffmpeg -i ./videos/input1.mp4 -vf tenfilter=af=auto,tenfilter=mag_filter=1:mag_sr=2:mag_sr_stre=normal,unsharp -c:v libten264 -ten264-params crf=26:vbv-maxrate=2000 -y fast_output1.mp4
```
```shell
./ffmpeg -i ./videos/input2.mp4 -vf tenfilter=af=auto,tenfilter=mag_filter=1:mag_sr=2:mag_sr_stre=normal,unsharp -c:v libten264 -ten264-params crf=26:vbv-maxrate=2000 -y fast_output2.mp4
```
<dx-alert infotype="explain" title="">
同一模型的运行速度会受到输入分辨率的影响，分辨率越大运行速度越慢。初次运行特定 AI 模型时，会耗费较长的时间初始化模型，后续重复执行相同命令时速度会有明显提升。如需评估运行速度，请参考重复执行时的结果。
</dx-alert>
ffmpeg 命令中的部分参数含义如下表：
<table>
<tr>
<th>参数内容</th>
<th>参数含义</th>
</tr>
<tr>
<td><code>-i videos/input1.mp4</code></td>
<td>指定输入视频文件。</td>
</tr>
<tr>
<td><code>-vf tenfilter=mag_srgan=1</code></td>
<td>指定视频处理滤镜（filter） 图，各参数含义请参见 <a href="#ai">视频处理 AI 模型功能清单</a>。</td>
</tr>
<tr>
<td><code>-c:v libten264</code></td>
<td>指定编码器为腾讯自研的 Ten264 或 Ten265 视频编码器。</td>
</tr>
<tr>
<td><code>-ten264opts crf=26:vbv-maxrate=2000</code></td>
<td>设置视频编码器的相关参数，各参数含义请参见 <a href="#videoEncoder">视频编码器功能清单</a>。</td>
</tr>
<tr>
<td><code>-y output.mp4</code></td>
<td>指定输出视频文件，自动覆盖已有文件。</td>
</tr>
</table>
3. 等待程序运行结束后，可将输出视频文件下载到本地进行查看，建议使用 xshell、MobaXterm 等工具。以下为执行上述命令输出的4个视频文件截图，以用作对比验证。
<dx-tabs>
::: output1.mp4
截图时间：01分15秒
![](https://qcloudimg.tencent-cloud.cn/raw/9773d6f0790e5e1ceedf3a2bf5c958ee.png)
:::
::: fast_output1.mp4
截图时间：01分15秒
![](https://qcloudimg.tencent-cloud.cn/raw/12da44d281de1acf74cd823acbcc0f44.png)
:::
::: output2.mp4
截图时间：00分10秒
![](https://qcloudimg.tencent-cloud.cn/raw/891787f7ed4754ee10a97ac74e2d7eba.png)
:::
::: fast_output2.mp4
截图时间：00分10秒
![](https://qcloudimg.tencent-cloud.cn/raw/108db7750a9ee26e7661ff621af2b1c5.png)
:::
</dx-tabs>


## 功能清单

tscsdk-center 包含 [视频处理 AI 模型](#ai) 和 [腾讯自研视频编码器](#videoEncoder) 两部分视频能力的支持。
视频处理 AI 模型利用 FFmpeg 的滤镜（filter）机制进行集成，使相关 filter 能够将 AI 推理能力嵌入到视频编解码和处理流程中，提升硬件设备的利用效率和吞吐能力，结合腾讯自研的视频编码器，可以在视频画质增强的基础上带来更高的视频编码压缩率。


### 视频处理 AI 模型功能清单[](id:ai)
视频处理 AI 模型全部集成在一个名为 tenfilter 的滤镜中。通过 `"-vf tenfilter=name1=value1:name2=value2"` 的方式实现调用和配置。在单个 tenfilter 中可以开启一个 AI 模型，多个 tenfilter 之间可以任意组合。
所有 AI 模型的详细描述如下表：

<table>
<tr>
<th>模型或功能名称</th>
<th>参数</th>
<th>使用示例</th>
</tr>
<tr>
<td>通用参数</td>
<td>
<ul class="params">
<li>mdir：模型配置文件路径。默认值为 "./tenmodel/tve-conf.json"。</li>
<li>gpu：tenfilter 所用的 GPU 编号。</li>
</ul>
</td>
<td>tenfilter=mdir=./tenmodel/tve-conf.json:gpu=1</td>
</tr>
<tr>
<td>去压缩伪影</td>
<td>af：去压缩伪影强度。当前仅支持 auto。</td>
<td>tenfilter=af=auto</td>
</tr>
<tr>
<td>人脸保护</td>
<td>
<ul class="params">
<li>face_protect_enable：为1时开启人脸保护逻辑。</li>
<li>face_af_ratio：人脸区域去噪弱化系数。</li>
<li>face_sp_ratio：人脸区域锐化强化系数。</li>
</ul>
</td>
<td>tenfilter=face_protect_enable=1:face_af_ratio=0.5:face_sp_ratio=0.5</td>
</tr>
<tr>
<td>视频插帧</td>
<td>
<ul class="params">
<li>mag_fps：为1时开启视频插帧。</li>
<li>fps：目标帧率。</li>
</ul>
</td>
<td>tenfilter=mag_fps=1:fps=60</td>
</tr>
<tr>
<td>色彩增强</td>
<td>
<ul class="params">
<li>mag_filter：需要设置为1。</li>
<li>cebb：为1时开启色彩增强。</li>
</ul>
</td>
<td>tenfilter=mag_filter=1:cebb=1</td>
</tr>
<tr>
<td>标准超分辨率</td>
<td>
<ul class="params">
<li>mag_filter：需要设置为1。</li>
<li>mag_sr：超分辨率比率，当前仅支持2倍超分辨率。</li>
<li>mag_sr_stre：超分辨率模式。可设置为正常模式（normal）或均衡模式（balance）。</li>
</ul>
</td>
<td>tenfilter=mag_filter=1:mag_sr=2:mag_sr_stre=normal</td>
</tr>
<tr>
<td>高质量超分辨率</td>
<td>mag_srgan：为1时开启高质量超分辨率模型。</td>
<td>tenfilter=mag_srgan=1</td>
</tr>
<tr>
<td>视频去噪声</td>
<td>
<ul class="params">
<li>mag_filter：需要设置为1。</li>
<li>dn：去噪声强度，当前仅支持3。</li>
</ul>
</td>
<td>tenfilter=mag_filter=1:dn=3</td>
</tr>
<tr>
<td>视频画质增强<br>
人脸增强<br>
字体增强<br>
（支持多模型）</td>
<td>
<ul class="params">
<li>mag_filter：需要设置为1。</li>
<li>eh：为1时开启画质增强。</li>
<li>faceeh：为1时开启人脸增强。</li>
<li>fonteh：为1时开启字体增强。</li>
<li>prior：AI 模型执行优先级，例如 "faceeh-eh-fonteh"，需同时开启对应模型。添加 "-parally" 时开启并行优化。</li>
</ul>
</td>
<td>
<ul class="params">
<li>单模型：
tenfilter=mag_filter=1:eh=1</li>
<li>多模型：
tenfilter=mag_filter=1:eh=1:faceeh=1:prior=faceeh-eh-parally</li>
</ul>
</td>
</tr>
</table>




### 腾讯自研视频编码器[](id:videoEncoder)

tscsdk-center 包含 Ten264 和 Ten265 两个腾讯自研的视频编码器。编码器类型以及编码器参数可以在视频处理时通过命令参数进行设置。
每种编码器的指定和设置方式如下：

<table>
<thead>
<tr>
<th>编码器名称</th>
<th>指定方式</th>
<th>设置方式</th>
</tr>
</thead>
<tbody><tr>
<td>Ten264</td>
<td>-vcodec libten264-c:v libten264</td>
<td>-ten264opts name1=value1:name2=value2</td>
</tr>
<tr>
<td>Ten265</td>
<td>-vcodec libten265-c:v libten265</td>
<td>-ten265-params name1=value1:name2=value2</td>
</tr>
</tbody></table>

每种编码器的具体参数及其详细说明如下：

<dx-tabs>
::: Ten264 编码器


<table>
<thead>
<tr>
<th width="15%">参数名称</th>
<th>参数说明</th>
</tr>
</thead>
<tbody><tr>
<td>preset</td>
<td>指定编码器编码参数集合的配置。<br>0："ultrafast"，1："superfast"，2："veryfast"，3："faster"，4："fast"，5："medium"，6："slow"，7："slower"，8："veryslow"，9："placebo"。</td>
</tr>
<tr>
<td>bitrate</td>
<td>ABR 模式下面的输出视频的码率。</td>
</tr>
<tr>
<td>crf</td>
<td>CRF 模式下面的 CRF 数值。</td>
</tr>
<tr>
<td>aq-mode</td>
<td>0：关闭 aqmode，1：开启 aqmode，2：基于方差的aqmode，3：基于方差的 aqmode 并且偏向于暗场景。<br>默认2会产生更好的 ssim 结果。</td>
</tr>
<tr>
<td>vbv-maxrate</td>
<td>vbv 的最大码率。默认情况下该数值和配置的码率相同。</td>
</tr>
<tr>
<td>vbv-bufsize</td>
<td>vbv 缓冲 buffer 的大小。默认情况下该数值是配置的码率的四倍。</td>
</tr>
<tr>
<td>rc-lookahead</td>
<td>lookahead 长度。</td>
</tr>
<tr>
<td>scenecut</td>
<td>是否开启场景切换。默认开启，一般不建议关闭。</td>
</tr>
<tr>
<td>keyint</td>
<td>关键帧最长间隔。默认是256，可以根据实际业务情况配置，一般配置为2 - 5s的时间间隔的帧数。</td>
</tr>
<tr>
<td>threads</td>
<td>使用的线程池的线程数。</td>
</tr>
<tr>
<td>lookahead-threads</td>
<td>预分析，lookahead 使用线程数。</td>
</tr>
<tr>
<td>profile</td>
<td>"baseline"，"main"，"high"，"high422"，"high444"。</td>
</tr>
</tbody></table>


:::
::: Ten265 编码器


<table>
<thead>
<tr>
<th width="15%">参数名称</th>
<th>参数说明</th>
</tr>
</thead>
<tbody><tr>
<td>preset</td>
<td>指定编码器编码参数集合的配置。<br>-1：ripping，0：placebo，1：veryslow，2：slower，3：slow，4：universal，5：medium，6：fast，7：faster，8：veryfast，9：superfast。</td>
</tr>
<tr>
<td>rc</td>
<td>码率控制方式。<br>0：CQP，1：ABR_VBV，2：ABR，3：CRF_VBV，4：CRF。</td>
</tr>
<tr>
<td>bitrate</td>
<td>ABR 模式下面的输出视频的码率。</td>
</tr>
<tr>
<td>crf</td>
<td>CRF 模式下面的 CRF 数值，取值范围：[1,51]。</td>
</tr>
<tr>
<td>aq-mode</td>
<td>0：关闭 aqmode，1：开启 aqmode，2：基于方差的 aqmode，3：基于方差的 aqmode 并且偏向于暗场景。<br>默认2会产生更好的 ssim 结果。</td>
</tr>
<tr>
<td>vbv-maxrate</td>
<td>vbv 的最大码率。默认情况下该数值和配置的码率相同。</td>
</tr>
<tr>
<td>vbv-bufsize</td>
<td>vbv 缓冲 buffer 的大小。默认情况下该数值是配置的码率的四倍。</td>
</tr>
<tr>
<td>rc-lookahead</td>
<td>lookahead 长度。</td>
</tr>
<tr>
<td>scenecut</td>
<td>场景切换阈值，取值范围[0,100]。0表示关闭。默认开启，一般不建议关闭。</td>
</tr>
<tr>
<td>open-gop</td>
<td>是否开启 open gop。<br>0：关闭，1：开启。默认开启，在直播场景中为了支持随机接入，建议关闭这个功能。</td>
</tr>
<tr>
<td>keyint</td>
<td>关键帧最长间隔。默认是256，可以根据实际业务情况配置，需要大于50且是8的倍数。</td>
</tr>
<tr>
<td>ltr</td>
<td>是否要支持长期参考帧 。0：关闭，1:：开启。默认开启，如果播放 HEVC 视频的硬件设备比较差，建议关闭这个功能。</td>
</tr>
<tr>
<td>pool-threads</td>
<td>WPP 使用的线程池的线程数。默认和 CPU 的核数相同，如果想减少 CPU 占用，可以降低这个数目。</td>
</tr>
</tbody></table>


:::
</dx-tabs>





## 使用建议
- tscsdk-center 支持每个 AI 模型的灵活控制，如果有特殊的需求和应用场景，可以通过设置每项功能的开关和组合顺序，以达到更好的适配和视频处理效果。
- tscsdk-center 提供了两种超分辨率模型。其中，标准超分辨率模型相对适合于分辨率较低的老片源，高质量超分辨率模型相对适合于高清片源，建议结合片源类型对这两种超分辨率模型的实际效果进行评估。
- tscsdk-center 提供 AI 模型需要运行在 GPU 上，而视频编码器只运行在 CPU 上。大部分情况下，在 GPU 算力跑满后，CPU 还会存在一定的空闲。此时可以合理安排一些只需运行在 CPU 上的视频处理任务（例如视频转码）以充分利用各类硬件资源。


## 联系我们[](id:contact)
欢迎扫码下方二维码加入视频增强型实例 GN7vi 用户交流群，如有关于视频增强型实例 GN7vi 使用咨询和问题反馈，欢迎在交流群中进行咨询。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ab62199eb349efb7fcb629ea24af8b48.png" style="width:250px">





<style>
 .params{margin-bottom:0px !important}
</style>
