# Android应用接入初始化与验证

## 1、初始化

在您的Application类中初始化TMFBase，TMFBase相关定义请参见[基础库API](../进阶指南/基础库API.md)。

> ![注意](../img/注意.png)注意：
>
> 1. TMF不支持多进程，请您只在主进程进行初始化TMFBase。
> 2. 初始化TMFBase需要您指定buildNo, buildNo是TMF引入的应用版本号，一般为6-7位数字，是应用更新、热修复判断版本更新的重要依据，具体使用规则请参见[buildNo](../../../06应用发布/应用发布/接入Android/使用.md#buildno) 。

```java
public class MyApplication extends Application {

    @Override
    public void onCreate() {
        //TMF不支持多进程，如果有多进程情况，需做进程判断，只在主进程做初始化
        initBase(this);
    }
}

private void initBase(Application context) {
	 TMFBaseConfig config = new TMFBaseConfig.Builder()  
					.buildNo(1000001) // 必须，buildNO是应用更新、热修复判断版本更新的重要依据
					.debug(true) // 日志开关，true表示打开日志输出
					.build();  
	 TMFBase.init(context, config);
}
```

## 2、接入验证

可以通过获取guid来验证TMF是否接入成功，如果成功获取guid则表示接入成功。

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

![guid获取成功](../img/guid获取成功.png)