您可以编译不同的渠道包，用于运营数据的采集。如果您没有配置渠道，Analytics 仍然可以正常运行。

如果您想要配置渠道信息，可以在您工程的 `AndroidManifest` 文件中添加元数据信息：

```
<application>

<!-- 请将value改为app发布对应的渠道，不同的发布渠道使用不同的名字。-->
<meta-data android:name="com.tencent.tac.channel" android:value="xiaomi"/>
	
</application>
```
 
> **注意：**
> 若填写的渠道为纯数字字符串类型，请不要超过 int 表示的范围。
 
## gradle 自动生成渠道包

如果您是采用 gradle 编译，可以将您的 meta-data 设置为：

```
<meta-data
   	android:name="com.tencent.tac.channel"
	android:value="${tac_channel}" />
```

然后，在应用级的 build.gradle 文件里面设置多个产品，每个产品设置不同的 `tac_channel` 。这样当您通过 gradle 编译不同的包时，AndroidManifest 中元数据的 value 会自动替换成配置的值。例如下面的代码，定义了小米商店和应用宝两个不同的渠道包：

```
android {
	productFlavors {
        xiaomi {
            manifestPlaceholders = [tac_channel: "xiaomi"]
        }
        yingyongbao {
            manifestPlaceholders = [tac_channel: "yingyongbao"]
        }
    }
}
```
