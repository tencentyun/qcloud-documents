### 步骤一：初始化
在您的 Application 类中初始化 TMFBase，TMFBase 相关定义请参见[ 基础库 API](https://cloud.tencent.com/document/product/1034/85319)。
>!
> - TMF 不支持多进程，请您只在主进程进行初始化 TMFBase。
> - 初始化 TMFBase 需要您指定 buildNo，buildNo 是 TMF 引入的应用版本号，一般为6-7位数字，是应用更新、热修复判断版本更新的重要依据，具体使用规则请参见[ buildNo](https://cloud.tencent.com/document/product/1034/33148#buildNo)。
> - 由于灰度时未正式发布新版，新包版本号仍为旧版本号，此时使用 buildNo 仍然可以比较版本大小，定向对灰度用户进行升级。
> 
```java
public class MyApplication extends Application {
    @Override
    public void onCreate() {
        //TMF 不支持多进程，如果有多进程情况，需做进程判断，只在主进程做初始化
        initBase(this);
    }
}
private void initBase(Application context) {
	 TMFBaseConfig config = new TMFBaseConfig.Builder()  
					.buildNo(1000001) // 必须，buildNO 是应用更新、热修复判断版本更新的重要依据
					.debug(true) // 日志开关，true 表示打开日志输出
					.build();  
	 TMFBase.init(context, config);
}
```

### 步骤二：接入验证
可以通过获取 guid 来验证 TMF 是否接入成功，如果成功获取 guid 则表示接入成功。
```java
TMFBase.getShark().getGuidAsyn(new IGuidCallback() {
                    @Override
                    public void onCallback(int retCode, String guid) {
                        if (!TextUtils.isEmpty(guid)) {
                            Log.d("TMFDemo_test", "guid: " + guid + " 获取成功!!!!");
                        } else {
                            Log.d("TMFDemo_test", "获取GUID失败，guid: " + guid + " retCode: " + retCode);
                        }
                    }
                });
```
![](https://qcloudimg.tencent-cloud.cn/raw/5be71db0a4b4a4132021a051e625c068.png)
