如果您不希望在腾讯云进行视频录制，可以通过本地拉流录制的方式将视频保存到本地。ffmpeg 本地拉流录制的步骤如下：

### 1. 下载并安装 ffmpeg
通过使用 ffmpeg 工具 ，可以完成直播流的录制。
>您可以在 [ffmpeg官网](https://www.ffmpeg.org/) 下载并安装ffmpeg 工具 。

``` shell
wget http://www.ffmpeg.org/releases/ffmpeg-3.4.tar.gz
tar -zxvf ffmpeg-3.4.tar.gz
cd ffmpeg-3.4
./configure
make
make install
```
### 2. 拉流录制
以混流后的直播码 `8525_d1965300f23315789ded4e49ce831d10` 为例，根据直播码获得的推流地址：`rtmp://8525.liveplay.myqcloud.com/live/8525_d1965300f23315789ded4e49ce831d10.flv` 进行拉流录制。
示例：
``` shell
./ffmpeg  -i "rtmp://8525.liveplay.myqcloud.com/live
/8525_d1965300f23315789ded4e49ce831d10.flv" 
-codec copy -f mp4 test.mp4
```

### 3. 拉流录制中
![上传进行中](http://docs-1253488539.cossh.myqcloud.com/recording.png)

### 4. 拉流下载完成
![下载完成](http://docs-1253488539.cossh.myqcloud.com/record-done.png)

