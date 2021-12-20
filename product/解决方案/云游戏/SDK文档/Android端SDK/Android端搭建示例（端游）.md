## 接入步骤
1. 将 `tcgsdk-1.1.7.348_20210607_1955_release.aar` 拷贝到 libs 目录下。
2. 在应用模块的 `build.gradle` 中加入：
```
repositories {
   flatDir {dirs 'libs'}
}
dependencies {
   implementation fileTree(include: ['*.jar'], dir: 'libs')
   // 云游sdk依赖的网络库(大小50k)
   implementation 'com.android.volley:volley:1.2.1'
   // 云游sdk
   implementation(name: "tcgsdk-1.1.7.348_20210607_1955_release.aar", ext: 'aar')
}
```
3. 进行混淆配置。
  由于 native 层代码需要反射调回 java，需要确保 SDK 内的代码都不被混淆，请在 proguard 中添加以下配置：
```
-keep class org.twebrtc.** {*;}
-keep class com.tencent.tcgsdk.** {*;}
```
4. AndroidManifest 配置：
``` java
<uses-feature android:glEsVersion ="0x00020000" android:required="true" />
```


## 调用示例
```
public class SimpleSample extends BaseActivity {
  private GameView mGameView;
  private ITcgSdk mSDK;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    initView();
    initSdk();
  }

  /**
   * 创建游戏画面视图
   */
  private void initView() {
    mGameView = new GameView(this);
    setContentView(mGameView);
  }

  /**
   * 初始化SDK
   */
  private void initSdk() {
    // 创建Builder
    TcgSdk2.Builder builder = new TcgSdk2.Builder(
        this.getApplicationContext(),
        APP_ID,
        mTcgLifeCycleImpl,
        mGameView.getSurfaceRenderer());

    // 设置日志级别
    builder.logLevel(LogLevel.VERBOSE);

    // 通过Builder创建SDK接口实例
    mSDK = builder.build();

    // 给游戏视图设置SDK实例
    mGameView.setSDK(mSDK);
  }


  /**
   * TcgSdk生命周期回调
   */
  private final ITcgListener mTcgLifeCycleImpl = new ITcgListener() {
    @Override
    public void onConnectionTimeout() {
      // 云游戏连接超时, 用户无法使用, 只能退出
    }

    @Override
    public void onInitSuccess(String clientSession) {
      // 初始化成功
      start(clientSession);
    }

    @Override
    public void onInitFailure(int errorCode) {
      // 初始化失败, 用户无法使用, 只能退出
    }

    @Override
    public void onConnectionFailure(int errorCode, String errorMsg) {
      // 云游戏连接失败
    }

    @Override
    public void onConnectionSuccess() {
      // 云游戏连接成功, 所有SDK的设置必须在这个回调之后进行(包括ITcgSdk.sendGamePadConnected及其他按键事件)
    }

    @Override
    public void onDrawFirstFrame() {
      // 游戏画面首帧回调
    }
  };

  /**
   * 启动云游戏, 云端实例启动成功后会回调onStartExperience
   *
   * @param clientSession 用于云端初始化的client session
   * @see SimpleSample#onStartExperience(String)
   */
  protected void start(String clientSession) {
    // 以下请求ServerSession的后端支持是云游团队的体验服务
    // 客户端接入时需要在自己的业务后台返回ServerSession
    // 业务后台的API请参考:
    // https://cloud.tencent.com/document/product/1162/40740
    super.startExperience(clientSession);
  }

  @Override
  void onStartExperience(String serverSession) {
    //　启动游戏
    mSDK.start(serverSession);
  }
}
```
- 客户端获取的 clientSession 作为参数传递给 App 后台（传递方式业务方可以自行实现），业务后台请求云 API 锁定机器并创建会话，拿到 serverSession。
- 客户端通过 serverSession 启动游戏。其中，客户端传递 clientSession，App 后台返回 serverSession，传递方式 App 可自行实现。
- SDK 启动游戏之后会通过 ITcgListener 接口把启动过程中的回调告知给客户端，游戏启动后与远端的交互可通过 ITcgSdk 进行。
