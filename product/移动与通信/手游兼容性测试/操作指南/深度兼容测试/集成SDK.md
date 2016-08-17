SDK只在测试版本中集成，正式版本无需集成。
支持的游戏引擎以及版本号：

| 引擎 | SDK支持（已测试）版本号 |
|---------|---------|
| Unity3D | 4.3, 4.5, 4.6, 5.0 |


### 一、添加SDK
下载地址：
[WTSDK（Unity3d_NGUI）](http://cdn.wetest.qq.com/com/c/wetest_unity_ngui.zip)
[ WTSDK（Unity3d_UGUI）](http://cdn.wetest.qq.com/com/c/wetest_unity_ugui.zip)

包含三个组件：u3dautomation.dll、u3dautomation.jar、和libcrashmonitor.so
1、将u3dautomation.dll放到Assets\Scripts下面。
2、U3dautomation.jar与libcrashmonitor.so
把这两个jar包和so库一起编译到游戏中的地方，不需要调用其中的函数，例如可以放到Builds\Plugin\Android\下面（或是Assets\Plugins\Android），不同游戏位置可能不一样。

### 二、初始化测试代码

1、到Unity编辑器中，选择第一个启动的Scene，然后在根结节新建一个空的GameObject，名字可随便定义：
![](//mccdn.qcloud.com/static/img/fdfc5c5723c16357ac799901a434122c/image.png)

2、在GameObject的脚本上调用如下代码进行初始化
```
this.gameObject.AddComponent<WeTest.U3DAutomation.U3DAutomationBehaviour>();
```

![](//mccdn.qcloud.com/static/img/c518efef239143c4b081e97c841d84c5/image.png)

说明：
CI集成的，可以通过控制`<ProjectPath>/Assets/smcs.rsp`、`<ProjectPath>/Assets/smcs.rsp`来控制是否集成wetest。通常在debug版本集成，release上线版本不可集成

### 三、编译

1、建议在设置Unity的Optimization优化选项时：
（1）将Api Compatibility Level选项设置为.NET 2.0 Subset， StrippingLevel为四个选项内随机选择；
（2）如果必须将Api Compatibility Level设置为.NET 2.0，则建议StrippingLevel设置为Disable。主要是为了保证SDK合入后的稳定性，避免由于选项的问题，导致编译后APK有时不能正常运行的情况。
![](//mccdn.qcloud.com/static/img/eaa495316efa58a2aa16bcebb3e5ba6e/image.png)
2、按游戏的编译流程，拿到apk包即可。 
 如果SDK集成成功后，拉起游戏后，会输出日志：U3DAutomationinit ... 




