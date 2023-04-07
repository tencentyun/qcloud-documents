## 操作背景

CAM 于2022年7月14日（周四）09:00 - 2022年7月29日（周五）变更 ReadOnlyAccess 预设策略语法，剔除写接口，增加读接口，满足 ReadOnlyAccess 预设策略匹配所有支持接口级鉴权或资源级鉴权的云服务资产场景。

## 操作指引

### 写接口

剔除写接口列表如下，剔除之后，您的子账号将没有相关接口操作及调用权限，如您有调用该接口但未授权，请参考 [创建自定义策略 - 按策略语法创建](https://cloud.tencent.com/document/product/598/37739#.E6.8C.89.E7.AD.96.E7.95.A5.E8.AF.AD.E6.B3.95.E5.88.9B.E5.BB.BA) 给对应的子账号 [授权](https://cloud.tencent.com/document/product/598/10602) 即可。

<table>
<thead>
<tr>
<th width="30%">产品名</th>
<th width="20%">CAM 中简称</th>
<th width="50%">接口名</th>
</tr>
</thead>
<tbody><tr>
<td>工商注册</td>
<td>br</td>
<td>SendVerificationCode</td>
</tr>
<tr>
<td>负载均衡</td>
<td>clb</td>
<td>AutoRewrite</td>
</tr>
<tr>
<td>数字身份管控平台（员工版）</td>
<td>eiam</td>
<td>DoDefaultAction</td>
</tr>
<tr>
<td>弹性 MapReduce</td>
<td>emr</td>
<td>SubmitServiceParamsForMC</td>
</tr>
<tr>
<td>财务</td>
<td>finance</td>
<td>QcostUndoInvoice</td>
</tr>
<tr>
<td>数字身份管控平台</td>
<td>idam</td>
<td>LinkUserAndAccount</td>
</tr>
<tr>
<td>即时通信 IM</td>
<td>im</td>
<td>CreateSecretUserSig</td>
</tr>
<tr>
<td>密钥管理系统</td>
<td>kms</td>
<td>EnableWhiteBoxKey</td>
</tr>
<tr>
<td>云数据库 Memcached</td>
<td>memcached</td>
<td>DestroyInstance</td>
</tr>
<tr>
<td rowspan="10">云数据库 MongoDB</td>
<td rowspan="10">mongodb</td>
<td>AssignProject</td>
</tr>
<tr>
<td>AutoRenew</td>
</tr>
<tr>
<td>BackupInstance</td>
</tr>
<tr>
<td>BuyInstance</td>
</tr>
<tr>
<td>FormalDBInstance</td>
</tr>
<tr>
<td>RestartInstance</td>
</tr>
<tr>
<td>Restorable</td>
</tr>
<tr>
<td>RestoreAllInstance</td>
</tr>
<tr>
<td>RestoreTableInstance</td>
</tr>
<tr>
<td>UpgradeInstance</td>
</tr>
<tr>
<td rowspan="2">云数据库 Redis</td>
<td rowspan="2">redis</td>
<td>DestroyPostpaidInstance</td>
</tr>
<tr>
<td>DestroyPrepaidInstance</td>
</tr>
<tr>
<td rowspan="2">云函数</td>
<td rowspan="2">scf</td>
<td>CopyFunction</td>
</tr>
<tr>
<td>TerminateAsyncEvent</td>
</tr>
<tr>
<td rowspan="8">金融资源聚合平台</td>
<td rowspan="8">solar</td>
<td>ApproveFlow</td>
</tr>
<tr>
<td>CopyActivityChannel</td>
</tr>
<tr>
<td>DenyFlow</td>
</tr>
<tr>
<td>FreezeActivityChannel</td>
</tr>
<tr>
<td>OffLineProject</td>
</tr>
<tr>
<td>OfflineActivityChannel</td>
</tr>
<tr>
<td>ReExecuteFlow</td>
</tr>
<tr>
<td>UnfreezeActivityChannel</td>
</tr>
<tr>
<td rowspan="7">云数据库 SQL Server</td>
<td rowspan="7">sqlserver</td>
<td>CompleteExpansion</td>
</tr>
<tr>
<td>OfflineDBInstance</td>
</tr>
<tr>
<td>RecoveryPostInstance</td>
</tr>
<tr>
<td>RestartDBInstance</td>
</tr>
<tr>
<td>RunMigration</td>
</tr>
<tr>
<td>TerminateDBInstance</td>
</tr>
<tr>
<td>UpgradeDBInstance</td>
</tr>
<tr>
<td>SSL 证书</td>
<td>ssl</td>
<td>VerifyManager</td>
</tr>
<tr>
<td rowspan="2">腾讯云 TI 平台 TI-ONE</td>
<td rowspan="2">tione</td>
<td>CopyFlow</td>
</tr>
<tr>
<td>CopyUserCosFile</td>
</tr>
<tr>
<td>容器服务</td>
<td>tke</td>
<td>UpgradeClusterAuthorizationMode</td>
</tr>
<tr>
<td>微服务平台 TSF</td>
<td>tsf</td>
<td>RunMsApi</td>
</tr>
<tr>
<td>增值电信</td>
<td>vat</td>
<td>SendVerificationCode</td>
</tr>
<tr>
<td>语音消息</td>
<td>vms</td>
<td>DeleteTemplate</td>
</tr>
<tr>
<td rowspan="5">云点播</td>
<td rowspan="5">vod</td>
<td>ConfirmEvents</td>
</tr>
<tr>
<td>ConfirmManualReviewResult</td>
</tr>
<tr>
<td>ConvertVodFile</td>
</tr>
<tr>
<td>Relay</td>
</tr>
<tr>
<td>WeChatMiniProgramPublish</td>
</tr>
</tbody></table>

### 读接口

增加读接口列表如下，增加之后，您的子账号将拥有相关接口查看及调用权限。

<table>
<thead>
<tr>
<th width="30%">产品名</th>
<th width="20%">CAM 中简称</th>
<th width="50%">接口名</th>
</tr>
</thead>
<tbody><tr>
<td rowspan="3">语音识别</td>
<td rowspan="3">asr</td>
<td>DownloadAsrVocab</td>
</tr>
<tr>
<td>DownloadCustomization</td>
</tr>
<tr>
<td>DownloadModel</td>
</tr>
<tr>
<td>智能创作</td>
<td>cme</td>
<td>AccessWeb</td>
</tr>
<tr>
<td rowspan="19">主机安全</td>
<td rowspan="19">cwp</td>
<td>ExportAttackLogs</td>
</tr>
<tr>
<td>ExportBaselineEffectHostList</td>
</tr>
<tr>
<td>ExportBaselineList</td>
</tr>
<tr>
<td>ExportBashEvents</td>
</tr>
<tr>
<td>ExportBruteAttacks</td>
</tr>
<tr>
<td>ExportEventlog</td>
</tr>
<tr>
<td>ExportIgnoreBaselineRule</td>
</tr>
<tr>
<td>ExportIgnoreRuleEffectHostList</td>
</tr>
<tr>
<td>ExportMaliciousRequests</td>
</tr>
<tr>
<td>ExportMalwares</td>
</tr>
<tr>
<td>ExportNonlocalLoginPlaces</td>
</tr>
<tr>
<td>ExportPrivilegeEvents</td>
</tr>
<tr>
<td>ExportProtectDirList</td>
</tr>
<tr>
<td>ExportReverseShellEvents</td>
</tr>
<tr>
<td>ExportSecurityTrends</td>
</tr>
<tr>
<td>ExportTasks</td>
</tr>
<tr>
<td>ExportVulEffectHostList</td>
</tr>
<tr>
<td>ExportVulList</td>
</tr>
<tr>
<td>ExportWebPageEventList</td>
</tr>
<tr>
<td>数据连接器</td>
<td>eis</td>
<td>DownloadMessage</td>
</tr>
<tr>
<td rowspan="5">游戏多媒体引擎</td>
<td rowspan="5">gme</td>
<td>DownloadApplicationData</td>
</tr>
<tr>
<td>DownloadFile</td>
</tr>
<tr>
<td>DownloadKey</td>
</tr>
<tr>
<td>DownloadRecordFileUrlList</td>
</tr>
<tr>
<td>DownloadScanData</td>
</tr>
<tr>
<td>即时通信 IM</td>
<td>im</td>
<td>DownloadAuthenticateMutually</td>
</tr>
</tbody></table>
