### MRP 中 Cloud Shell 与普通 Linux 系统提供的 Shell 有什么不同？
与普通 Linux 的 Shell 相比，Cloud Shell 登录不需要密码。Cloud Shell 中还封装了一套与 MRP 的可视化操作相适应的 mrp 命令，能够更方便、高效地处理 MRP 中的实验，如编辑、导入、提交、取消和删除等操作。
	
### Cloud Shell 中找不到实验列表页中显示的实验，如何解决？
请在 Cloud Shell 中执行 tefs sync 命令即可。
	
### Cloud Shell 中 tefs 相关命令不能正常使用，如何解决？	
请使用 tefs upgrade --force 进行强制升级。
