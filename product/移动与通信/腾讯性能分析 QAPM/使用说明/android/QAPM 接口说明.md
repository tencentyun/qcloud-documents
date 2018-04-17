### 初始化 QAPM
```
public static QAPM getInstance(Application app, String key, String ver)
```
参数如下
app： 当前应用的 app 对象
key：为 [获取项目 app_key](https://cloud.tencent.com/document/product/683/15220) 中项目分配的 key
ver：产品版本号
### 设置 QAPM 相关参数。
```
public static QAPM set(String key, Object value)
```
  <table width="1037" border="0" cellpadding="0" cellspacing="0" style='width:777.75pt;border-collapse:collapse;table-layout:fixed;'>
   <col width="249" class="xl65" style='mso-width-source:userset;mso-width-alt:7968;'/>
   <col width="788" style='mso-width-source:userset;mso-width-alt:25216;'/>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl66" height="40" width="249" style='height:30.00pt;width:186.75pt;' x:str>参数名</td>
    <td class="xl66" width="788" style='width:591.00pt;' x:str>解释</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>key<span style='mso-spacerun:yes;'>&nbsp;</span></td>
    <td x:str>可选为&quot;uuid&quot;、&quot;uin&quot;、&quot;host&quot;、&quot;debug&quot;、&quot;leakfix&quot;、&quot;listener&quot;。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="120" rowspan="3" style='height:90.00pt;' x:str>value - uuid：string 类型</td>
    <td x:str>设置上报数据里的 UUID，用于标记该版本被混淆堆栈的 mapping。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td x:str>因此，建议采用“产品 ID + 版本号”作为入参的方式生成 UUID，具体生成函数各产品可以自行决定。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td x:str>建议最终生成 UUID 格式的字符串（格式类似 e6ae1282-ceb8-4237-89bd-2d23d00a8e33）。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>uin: string 类型</td>
    <td x:str>设置上报数据里附带的 QQ 号。即上报的用户账号。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>debug: bool 类型</td>
    <td x:str>是否开启调试日志，true 为开启，false 为不开启，默认为 false。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>leakfix: bool 类型</td>
    <td x:str>是否开启自动泄漏修复。true 为开启，false 为不开启，默认为false。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>listener</td>
    <td x:str>可为 InspectorListener/MemoryCellingListener/BatteryReportListener 类型，用于设置相关监听回调用。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>返回值</td>
    <td x:str>QAPM 对象。</td>
   </tr>
   <![if supportMisalignedColumns]>
    <tr width="0" style='display:none;'>
     <td width="249" style='width:187;'></td>
     <td width="788" style='width:591;'></td>
    </tr>
   <![endif]>
  </table>
	


### 启动监控。
```
public boolean run(int func)
```
>注意：
>默认全开为63（QAPM.ALL），正式发布的版本，建议以 run(24)来启动，因为下述三个功能（1、2、4）对应用性能都略有影响。

<table width="531" border="0" cellpadding="0" cellspacing="0" style='width:398.25pt;border-collapse:collapse;table-layout:fixed;'>
   <col width="72" span="2" style='width:54.00pt;'/>
   <col width="387" style='mso-width-source:userset;mso-width-alt:12384;'/>
   <tr height="18" style='height:13.50pt;'>
    <td class="xl65" height="18" width="72" style='height:13.50pt;width:54.00pt;' x:str>参数</td>
    <td class="xl65" width="72" style='width:54.00pt;' x:str>含义</td>
    <td class="xl65" width="387" style='width:290.25pt;' x:str>解释</td>
   </tr>
   <tr height="18" style='height:13.50pt;'>
    <td class="xl66" height="126" rowspan="7" style='height:94.50pt;border-right:none;border-bottom:none;' x:str>func</td>
    <td class="xl67" rowspan="7" style='border-right:none;border-bottom:none;' x:str>功能表</td>
    <td x:str>1：内存泄漏(QAPM.LEAKINSPECTOR)</td>
   </tr>
   <tr height="18" style='height:13.50pt;'>
    <td x:str>2：文件 IO(QAPM.IO)</td>
   </tr>
   <tr height="18" style='height:13.50pt;'>
    <td x:str>4：数据库 IO(QAPM.DB)</td>
   </tr>
   <tr height="18" style='height:13.50pt;'>
    <td x:str>8：卡顿(QAPM.LOOPER)</td>
   </tr>
   <tr height="18" style='height:13.50pt;'>
    <td x:str>16：触顶(QAPM.CEILING)</td>
   </tr>
   <tr height="18" style='height:13.50pt;'>
    <td x:str>32：电量(QAPM.BATTERY)</td>
   </tr>
   <tr height="18" style='height:13.50pt;'>
    <td x:str>63：开启以上全部监控(QAPM.ALL)</td>
   </tr>
   <tr height="18" style='height:13.50pt;'>
    <td class="xl68" height="18" style='height:13.50pt;' x:str>返回值</td>
    <td class="xl67" x:str>无</td>
    <td></td>
   </tr>
   <![if supportMisalignedColumns]>
    <tr width="0" style='display:none;'>
     <td width="387" style='width:290;'></td>
    </tr>
   <![endif]>
  </table>