数据湖计算 DLC 具备完善的数据访问权限机制，DLC 的权限分为操作权限和数据权限。操作权限由访问管理 CAM 服务进行管理，数据权限由 DLC 权限模块进行管理。
- 主账号默认拥有 DLC 全部操作权限和数据权限。
- 若子用户被授予 DLC 数据权限管理的操作权限，则该子用户可以将数据权限授予给其他子用户，可以将该类用户视作“管理员”。
- 若子用户被授予数据读写权限，则该子用户可以运行有权限数据的查询任务，其数据权限是被“管理员”进行分配。
- 除主账号外的所有子用户的数据权限都是靠“管理员”进行分配。用户不能查询没有权限的数据。

主账户默认拥有 DLC 全部操作权限。主账号通过访问管理 CAM 将 DLC 的访问权限授予给子用户，使子用户拥有对应的 DLC 操作权限。
## 操作步骤
1. 创建子用户并授权
 在 CAM 控制台创建子用户，并授予对应的权限。具体可参见 [子账户授权](#jump)。
 - 预设策略 QcloudDLCFullAccess：DLC 的全部操作权限。
 - 自定义策略：DLC 指定的操作权限。
2. 子用户登录数据湖计算 DLC 控制台并验证权限。
若子用户登录控制台并执行授权操作成功，则授权生效。


## 操作权限分类
如下表所示，按照 DLC 接口，将 DLC 操作分类如下，具体可参见 [API 文档](https://cloud.tencent.com/document/product/1342/53787)。

| 权限类型   | 说明                                | 
| ---------- | ----------------------------------- |
| 元数据管理 | 操作 DLC 管理的数据库和表的元数据信息 |
| 任务管理   | 提交和查看 DLC 任务                   |
| 权限管理   | 管理用户的数据访问权限              |
| 系统配置   | DLC 服务基础配置                     |

[](id:jump)
## 子账户授权
如果您使用主账号访问数据湖计算 DLC，可以跳过该步骤。
1. 创建子账户的操作步骤，可参见 [创建子账号并授权](https://cloud.tencent.com/document/product/598/54458)。
2. 创建自定义策略。
 - 在访问管理控制台的 [策略](https://console.cloud.tencent.com/cam/policy) 页面，单击**新建自定义策略**新建策略。
 - 在弹出的选择策略创建方式中，单击**按策略语法创建**，进入编辑策略页面。
 - 在按策略语法创建页面中，选择**空白模板**，单击**下一步**。
 - 在模板中，输入策略名称和描述（建议策略名称为 DLCDataAccess），将如下复制策略粘贴至**策略内容**。填写完成后，单击**完成**，即可成功创建自定义策略。拥有该自定义策略权限的子用户，可以登录数据湖计算 DLC 控制台执行 SQL 任务。但无法操作数据权限管理。具体可参见 [账号和权限管理]()。
```json
{
	 "version": "2.0",
	 "statement": [
		 {
			 "effect": "allow",
			 "action": [
				 "dlc:DescribeStoreLocation",
				 "dlc:DescribeTable",
				 "dlc:DescribeViews",
				 "dlc:CancelTask",
				 "dlc:CreateDatabase",
				 "dlc:CreateScript",
				 "dlc:CreateTable",
				 "dlc:CreateTask",
				 "dlc:DeleteScript",
				 "dlc:DescribeDatabases",
				 "dlc:DescribeScripts",
				 "dlc:DescribeTables",
				 "dlc:DescribeTasks",
				 "dlc:DescribeQueue"
			 ],
			 "resource": [
				 "*"
			 ]
		 }
	 ]
}
```
![](https://main.qcloudimg.com/raw/f623bbe2304ee557940b46ca017211a3.png)
5. 将预设策略或者自定义策略绑定给访问数据湖计算 DLC 的子账户后，该子账户可以登录和访问数据湖计算 DLC，具体可参见 [子用户权限设置](https://cloud.tencent.com/document/product/598/36256)。
 - 预设策略：QcloudDLCFullAccess。
 - 自定义策略：依据上述步骤自定义创建的数据湖计算 DLC 访问策略。
