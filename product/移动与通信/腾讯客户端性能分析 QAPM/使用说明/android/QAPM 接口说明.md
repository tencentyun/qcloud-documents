### 设置 QAPM 相关参数
```
(1)  public static QAPM setProperty(int key, String value)
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
    <td x:str>可选为&quot;PropertyKeyAppId&quot;、&quot; PropertyKeyUserId&quot;、&quot; PropertyKeyAppVersion&quot;、&quot; PropertyKeySymbolId&quot;、 &quot;PropertyKeyDebug&quot;。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> PropertyKeyAppId </td>
    <td x:str>产品 ID 为“产品密钥-产品 ID”模式，可从邮件中获取。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> PropertyKeyUserId </td>
    <td x:str>用户账号（比如 QQ 号、微信号等）。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> PropertyKeyAppVersion </td>
    <td x:str>产品版本（以类似“7.3.0.141.r123456”格式填写，后台可以解析出大版本号和 revision）。</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> PropertyKeySymbolId </td>
    <td x:str>UUID，用于拉取被混淆堆栈的 mapping ,用于做堆栈翻译用<br/>
   </td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> PropertyKeyDebug </td>
    <td x:str>是否开启调试日志（“true”开启，“false”不开启，默认后者）。</td>
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
	


### 启动监控
```
(2) public static boolean beginScene(String sceneName, int mode)
```
<table width="1037" border="0" cellpadding="0" cellspacing="0" style='width:777.75pt;border-collapse:collapse;table-layout:fixed;'>
   <col width="249" class="xl65" style='mso-width-source:userset;mso-width-alt:7968;'/>
   <col width="788" style='mso-width-source:userset;mso-width-alt:25216;'/>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl66" height="40" width="249" style='height:30.00pt;width:186.75pt;' x:str>参数名</td>
    <td class="xl66" width="788" style='width:591.00pt;' x:str>解释</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> sceneName </td>
    <td x:str>被监控的场景名</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>mode<span style='mso-spacerun:yes;'>&nbsp;</span></td>
    <td x:str>可选为&quot;ModeAll&quot;、&quot;ModeStable&quot;、&quot;ModeResource&quot;、&quot; ModeDropFrame&quot;</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> ModeAll </td>
    <td x:str>开启全部监控，包括内存泄漏、文件 IO、数据库 IO、卡顿、触顶、电量、区间性能、流畅度</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> ModeStable </td>
    <td x:str>开启适合外网使用的监控，包括卡顿、区间性能、流畅度</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> ModeResource </td>
    <td x:str>区间性能监控</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> ModeDropFrame </td>
    <td x:str>流畅度采集</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>返回值</td>
    <td x:str>布尔值，表示监控是否开启成功。</td>
   </tr>
   <![if supportMisalignedColumns]>
    <tr width="0" style='display:none;'>
     <td width="249" style='width:187;'></td>
     <td width="788" style='width:591;'></td>
    </tr>
   <![endif]>
  </table>

>注意：<br/>
>A. 正式版建议开启 QAPM.ModeStable，研发流程内版本建议开启 QAPM.ModeAll。 <br/>
>B. 确实需要定制开启个别功能时，可使用 ModeLeakInspector、ModeFileIO、ModeDBIO、ModeLooper、ModeCeiling、ModeBattery 中一个到多个，多个使用时采用按为或方式即可，如 ModeLeakInspector | ModeFileIO | ModeDBIO。<br/>
> C. 上述定制功能开启后，不能通过 endScene 关闭。

<br />

```
(3) public static boolean beginScene(String sceneName, String extraInfo, int mode)
```
<table width="1037" border="0" cellpadding="0" cellspacing="0" style='width:777.75pt;border-collapse:collapse;table-layout:fixed;'>
   <col width="249" class="xl65" style='mso-width-source:userset;mso-width-alt:7968;'/>
   <col width="788" style='mso-width-source:userset;mso-width-alt:25216;'/>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl66" height="40" width="249" style='height:30.00pt;width:186.75pt;' x:str>参数名</td>
    <td class="xl66" width="788" style='width:591.00pt;' x:str>解释</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> sceneName </td>
    <td x:str>见(2)</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> extraInfo <span style='mso-spacerun:yes;'>&nbsp;</span></td>
    <td x:str>可选以下项<br /> 用户定制 —— 若存在未调用 endScene 即再调用 beginScene 的场景，需要填 extraInfo 以区分</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> mode </td>
    <td x:str>见(2)</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>返回值</td>
    <td x:str>见(2)</td>
   </tr>
   <![if supportMisalignedColumns]>
    <tr width="0" style='display:none;'>
     <td width="249" style='width:187;'></td>
     <td width="788" style='width:591;'></td>
    </tr>
   <![endif]>
  </table>


### 结束监控
```
(4) public static boolean endScene(String sceneName, int mode)
```
<table width="1037" border="0" cellpadding="0" cellspacing="0" style='width:777.75pt;border-collapse:collapse;table-layout:fixed;'>
   <col width="249" class="xl65" style='mso-width-source:userset;mso-width-alt:7968;'/>
   <col width="788" style='mso-width-source:userset;mso-width-alt:25216;'/>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl66" height="40" width="249" style='height:30.00pt;width:186.75pt;' x:str>参数名</td>
    <td class="xl66" width="788" style='width:591.00pt;' x:str>解释</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> sceneName </td>
    <td x:str>见(2)</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>mode<span style='mso-spacerun:yes;'>&nbsp;</span></td>
    <td x:str>可选为&quot;ModeResource&quot;、&quot; ModeDropFrame&quot;</td>
   </tr>
  <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> ModeResource </td>
    <td x:str>区间性能监控</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> ModeDropFrame </td>
    <td x:str>流畅度采集</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>返回值</td>
    <td x:str>布尔值，表示监控是否终止成功。</td>
   </tr>
   <![if supportMisalignedColumns]>
    <tr width="0" style='display:none;'>
     <td width="249" style='width:187;'></td>
     <td width="788" style='width:591;'></td>
    </tr>
   <![endif]>
  </table>


<br />

```
(5) public static boolean endScene(String sceneName, String extraInfo, int mode)
```
<table width="1037" border="0" cellpadding="0" cellspacing="0" style='width:777.75pt;border-collapse:collapse;table-layout:fixed;'>
   <col width="249" class="xl65" style='mso-width-source:userset;mso-width-alt:7968;'/>
   <col width="788" style='mso-width-source:userset;mso-width-alt:25216;'/>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl66" height="40" width="249" style='height:30.00pt;width:186.75pt;' x:str>参数名</td>
    <td class="xl66" width="788" style='width:591.00pt;' x:str>解释</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> sceneName </td>
    <td x:str>见(2)</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> extraInfo <span style='mso-spacerun:yes;'>&nbsp;</span></td>
    <td x:str>可选以下项:<br /> 用户定制 —— 见(2)<br/>APPLAUNCH —— 用户定制 App 启动的结束点</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str> mode </td>
    <td x:str>见(4)</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" style='height:30.00pt;' x:str>返回值</td>
    <td x:str>见(4)</td>
   </tr>
   <![if supportMisalignedColumns]>
    <tr width="0" style='display:none;'>
     <td width="249" style='width:187;'></td>
     <td width="788" style='width:591;'></td>
    </tr>
   <![endif]>
  </table>

