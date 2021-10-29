在开发 Dataway 时，对脚本进行调试和测试，以方便问题排查和结果验证，EIS 系统提供 Dataway 脚本的调试功能。该功能可通过手工定义输入参数 msg，单击测试后可以直接查看脚本运行结果、调试日志和错误信息。

**操作步骤：**
1. 打开 EIS 系统，新建一个组件，在 Dataway IDE 编辑框中输入表达式。
>?Dataway 调试模式下，支持在表达式中通过 print() 函数打印要观察的信息，运行结束后打印消息会显示在界面上。

<img src="https://main.qcloudimg.com/raw/48417aeac8c13654a1fd67e941cac43b/SetPayload%E7%BB%84%E4%BB%B6%E8%BE%93%E5%85%A5.png" alt="Transform组件输入" style="zoom:50%;" />
2. 单击 Dataway 表达式编辑框右上角“Debug”，弹出 msg 数据填写对话框，在对话框可以对 message 的 payload、vars 和 attrs 进行设置。设置完成后单击**开始测试**，系统会自动组装成一个 msg 参数，并作为脚本的输入传递到 dw_process 函数中。

![表达式单测框输入](https://main.qcloudimg.com/raw/b94d9160550295811b569ef85ffae0f7/%E8%A1%A8%E8%BE%BE%E5%BC%8F%E5%8D%95%E6%B5%8B%E6%A1%86%E8%BE%93%E5%85%A5.png)
3. 运行完成 dw_process 函数后，编辑框下方会弹出运行结果和 print 调试日志，如果运行错误会有 error 报错信息。
 - 输入代表 Dataway 表达式的运行结果，日志代表在脚本中使用 print 函数打印的调试日志，错误代表脚本运行错误，运行正确无错误显示绿色对勾标志。
![单测运行结果](https://main.qcloudimg.com/raw/2bfd0651bc3eabf7e3baa5061aa775f9/%E5%8D%95%E6%B5%8B%E8%BF%90%E8%A1%8C%E7%BB%93%E6%9E%9C.png)
![单测print日志](https://main.qcloudimg.com/raw/667d469c176ff66738d99d9f92b53ae1/%E5%8D%95%E6%B5%8Bprint%E6%97%A5%E5%BF%97.png)
4. 通过添加 print 日志和模拟请求 msg 参数的数据，可完成对 Dataway 表达式的调试和验证工作。
