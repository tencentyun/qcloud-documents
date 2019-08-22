key、keyid、iv、content id 等数据可通过 DescribeKeys 接口获取。

## Widevine 加密

推荐加密工具：
[ shaka packager](https://google.github.io/shaka-packager/html/index.html)
 加密命令：
```
$ ./packager-linux in={input filename},stream=audio,output={output filename} in={input filename},stream=video,output={output filename} --enable_raw_key_encryption --keys label={label}:key_id={key_id}:key={key},label={label}:key_id={key_id}:key={key} --pssh {pssh} --mpd_output {output mpd name}
```

>?Widevine 方案，音频和视频需使用不同的加密 key。
>
更多用法，请参考 [shaka packager 文档](https://google.github.io/shaka-packager/html/index.html)。

## 准备 Fairplay 材料
以下四项材料需用户使用自己的 Apple 开发者帐户从 Apple 官方处获取，**材料不可复用**。
- 获取 FPS_Deployment_Package.zip 文件。
- 参照解压的 FPS_Deployment_Package 文档生成公私钥对。
- 提交生成的公钥给 Apple，获取 Apple 返回的公钥证书。
- 提交 Apple 返回的公钥证书后，获取网页显示的 Ask。

## Fairplay 加密

推荐加密工具：
[bento4 mp42hls](https://www.bento4.com/)
加密命令：

```
$ ./mp42hls --encryption-mode SAMPLE-AES --encryption-key {key+iv} --encryption-iv-mode fps --output-single-file --encryption-key-uri skd://{content id} --encryption-key-format com.apple.streamingkeydelivery --encryption-key-format-versions 1 --index-filename {output m3u8 filename} --segment-duration 10 {input filename}
```

更多用法，请参考 [bento4 文档](https://www.bento4.com/)。
