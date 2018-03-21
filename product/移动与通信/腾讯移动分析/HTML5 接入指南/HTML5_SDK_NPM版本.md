### 安装
```
npm install mta-h5-analysis --save
```
### 引入上报

```
import MtaH5 from 'mta-h5-analysis';
```

### 相关代码

```
// 初始化
MtaH5.init({
  "sid":'********', //必填，统计用的appid
  "cid":'********',, //如果开启自定义事件，此项目为必填，否则不填
  "autoReport":0,//是否开启自动上报(1:init完成则上报一次,0:使用pgv方法才上报)
  "senseHash":0, //hash锚点是否进入url统计
  "senseQuery":0, //url参数是否进入url统计
  "performanceMonitor":0,//是否开启性能监控
  "ignoreParams":[] //开启url参数上报时，可忽略部分参数拼接上报
});

// 页面上报
MtaH5.pgv();

// 自定义事件上报
MtaH5.clickStat("ico_search", {"query":"特斯拉"});
```

