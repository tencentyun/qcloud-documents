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
