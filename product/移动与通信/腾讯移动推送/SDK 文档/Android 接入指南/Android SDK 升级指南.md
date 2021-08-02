## TPNS Android SDK 1.2.5.0

###  1. 配置工程依赖环境（可选）

如果您在使用 SDK 依赖时遇到依赖拉取不到的情况，可以考虑在项目工程根目录 build.gradle 文件 allprojects.repositories 位置添加谷歌官方推荐镜像源 MavenCentral 和腾讯云镜像源。代码示例如下：
```
allprojects {
    repositories {
        google()
        // 谷歌推荐 MavenCentral 镜像源
        mavenCentral()
        jcenter()
        // 腾讯云镜像源
        maven { url 'https://mirrors.tencent.com/nexus/repository/maven-public/' }
    }
}
```

### 2. 新增配置（必需）
新增的标签查询接口，需要注意在继承 `XGPushBaseReceiver` 的实现类中增加实现方法 `onQueryTagsResult`。代码示例如下：
``` 
public class MessageReceiver extends XGPushBaseReceiver {

    // 其他回调接口
		// ...
		// 标签查询回调接口
    public void onQueryTagsResult(Context context, int errorCode, String data, String operateName) {
        Log.i(LogTag, "action - onQueryTagsResult, errorCode:" + errorCode + ", operateName:" + operateName + ", data: " + data);
    }
}
```
