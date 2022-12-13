## 接口描述
- **描述：**调用 wemeet.app.shareOpenApp 唤起原生应用分享 UI。
- **客户端支持：**Win/Mac/IOS/Android
- **支持的版本：**3.3.0
- **是否需要鉴权：**否


**图例：**
![](https://qcloudimg.tencent-cloud.cn/raw/8e2323f6f5a475aa16309f50ebbea5b6.png)

## 代码示例
```plaintext
wemeet.app.shareOpenApp()   
   .then((res) => {     
       console.log('succ', res);   
   })   
   .catch((e) => {     
       console.error(e);  
    });

```
