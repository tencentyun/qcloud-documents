如果您不希望在腾讯云进行视频录制，可以通过本地拉流录制的方式将视频保存到本地。ffmpeg 本地拉流录制的步骤如下。

## 1. 下载并安装 ffmpeg
通过使用 [ffmpeg](https://www.ffmpeg.org/) 工具的使用 ，可以完成直播流的录制。
在 [ffmpeg官网](https://www.ffmpeg.org/) 下载并安装
``` shell
wget http://www.ffmpeg.org/releases/ffmpeg-3.4.tar.gz
tar -zxvf ffmpeg-3.4.tar.gz
cd ffmpeg-3.4
./configure
make
make install
```
## 2. 拉流录制
<<<<<<< HEAD
以混流后的直播码 `8525_d1965300f23315789ded4e49ce831d10` 为例，根据获得的推流地址为：`rtmp://8525.liveplay.myqcloud.com/live/8525_d1965300f23315789ded4e49ce831d10.flv` 进行拉流录制。
=======
根据拿到混流后直播码的推流地址：
[rtmp://8525.liveplay.myqcloud.com/live/8525_d1965300f23315789ded4e49ce831d10.flv]() 进行拉流录制。
>>>>>>> d11e5df6f9b4f6aeab0c250a7efde39e6c8735e6
``` shell
./ffmpeg  -i "rtmp://8525.liveplay.myqcloud.com/live
/8525_d1965300f23315789ded4e49ce831d10.flv" 
-codec copy -f mp4 test.mp4
```

## 3. 拉流录制中
![上传进行中](http://docs-1253488539.cossh.myqcloud.com/recording.png)

## 4. 拉流下载完成
![下载完成](http://docs-1253488539.cossh.myqcloud.com/record-done.png)

