## TMFBaseConfig
TMFBaseConfig 构建器
```java
public static class Builder {  
	/**  
	 * 网关实例，如果用户需要自行创建Shark实例来代替内置Shark, 则调用该接口进行设置替换
	 * @param shark  
	 */  
	public Builder shark(IShark shark)

	/**  
	 * 从Assets加载配置文件
	 * @param assetName 默认值: tmf_configurations.json  
	 */  
	public Builder configAssetName(String assetName)

	/**  
	 * 从文件加载配置文件
	 * @param configFile  
	 */  
	public Builder configFile(File configFile)

	/**  
	 * 指定渠道号， 非必须
	 * @param channel 默认值：android  
	 * @return  
	 */  
	public Builder channel(String channel)

	/**  
	 * TMF平台build号(必须)，用于Shark、应用更新、热修复
	 * @param buildNo  
	 */  
	public Builder buildNo(int buildNo)

	/**  
	 * 如果涉及到环境切换，请设置该值 
	 * @param migrateType  
	 */  
	public Builder migrateType(MigrateType migrateType)

	/**  
	 * 设置日志上报相关信息 
	 * @param colorLogConfig  
	 */  
	public Builder colorLogConfig(ColorLogConfig colorLogConfig)
	 
	/**  
	 * 在该回调中调整内置shark默认配置项 
	 * @param sharkConfigAdjustCallback  
	 */  
	public Builder sharkConfigAdjustCallback(ISharkConfigAdjustCallback callback)
	
	/**  
	 * 在该回调中调整内置shark默认配置项
	 */
	public interface ISharkConfigAdjustCallback {  
		void onAdjust(TMFSharkConfigInfo sharkConfigInfo);  
	}
  	/**
     * 构建TMFBaseConfig
     * @return
     */
    public TMFBaseConfig build() 
}
```

## TMFBase
```java
public class TMFBase {  
	/**  
	 * 获取TMFBaseConfig
	 */  
	 public static TMFBaseConfig getsConfig()

	/**  
	 * 获取内置Shark实例 
	 */  
	 public static IShark getShark()

	/**  
	 * 获取buildNo 
	 */  
	 public static int getBuildNo()

	/**  
	 * 初始化（base初始化完成前，不允许使用组件功能）
	 * @param application 上下文  
	 * @param config 配置  
	 */ 
	 public static void init(Application application, TMFBaseConfig config)
}
```

## 内置 Shark 实例配置调整
基础库初始化时根据指定配置文件创建了内置 shark 实例，如果用户需要调整内置 shark 参数配置，可以参照如下方法进行：
```java
TMFBaseConfig config = new TMFBaseConfig.Builder()
                .buildNo(BuildConfig.BUILD_NO) // 必须，网关, 热更等模块需要使用
                .debug(true) //是否开启log
				//设置配置调整回调
				.sharkConfigAdjustCallback(new ISharkConfigAdjustCallback() {  
						@Override  
					 public void onAdjust(TMFSharkConfigInfo sharkConfigInfo) {  
							//在此调整配置信息
							sharkConfigInfo.ipPassThrough = SharkSp.getInstance().getIpPathThrough();  
					 }  
				})
                .build();

TMFBase.init(this, config);
```

SharkConfigInfo说明请参考[ 移动网关 > 接入Android > API](../../../05后台服务/移动网关/接入Android/API.md#sharkconfiginfo)

## SSLPinCfg
Http 通道服务端证书绑定校验相关设置，支持两种绑定校验：
1. 指定信任的证书文件，对证书文件进行完整校验，服务端返回的证书链中有证书校验通过，则校验通过，否则不通过。
2. 设置信任证书公钥，只校验证书文件的公钥信息，服务端返回的证书链中有证书公钥可信，则校验通过，否则不通过。
```java
//SSLPinCfg Builder
public static class Builder{
	/**  
	 * 绑定证书公钥的sha256, 只校验公钥部分，证书链中包含指定公钥则通过校验
	 *
	 * @param sha256 证书公钥sha256的base64字符串  
	 * @return  
	 */  
	public Builder addSHA256OfPublicKey(String sha256);
	
	/**  
	 * 绑定放在assets中的证书文件（pem/der/crt），证书链中包含指定证书则通过校验
	 *
	 * @param assetName 证书文件的asset名字
	 * @return  
	 */  
	public Builder addAssetNameOfCert(String assetName);
	
	/**
	 * 构建SSLPinCfg
	 */
	public SSLPinCfg build();
}

//证书绑定校验设置示例
TMFBaseConfig config = new TMFBaseConfig.Builder()  
		//...
		.sharkConfigAdjustCallback(new ISharkConfigAdjustCallback() {  
			@Override  
			public void onAdjust(TMFSharkConfigInfo sharkConfigInfo) {  
				//...
				sharkConfigInfo.sslPinCfg = new SSLPinCfg.Builder()  
						.addAssetNameOfCert("certs/selfsigned.cert")  
						.addAssetNameOfCert("tbbank.cer")  
						.addSHA256OfPublicKey("Ye0tdZMsVzzUD8GYr4hV+2ywj8UPMT6wexK0gudQ6DQ=")  
						.addSHA256OfPublicKey("jzqM6/58ozsPRvxUzg0hzjM+GcfwhTbU/G0TCDvL7hU=")  
						.build();  
				//域名校验回调
				sharkConfigInfo.hostnameVerifier = new HostnameVerifier() {  
					@Override  
					public boolean verify(String hostname, SSLSession session) {  
						return true;  
					}  
				};
			}  
		})  
		.build();

TMFBase.init(CommonApp.get().getApplication(), config);
```
