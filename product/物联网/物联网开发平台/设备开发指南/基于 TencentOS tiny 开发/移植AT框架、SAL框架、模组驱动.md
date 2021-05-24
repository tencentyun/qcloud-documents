本文将为您介绍 TencentOS tiny 接入腾讯物联网开发平台的框架、模组驱动移植相关操作。
## 步骤一：AT 框架、SAL 框架整体架构

AT 框架是我们编写的一个通用 AT 指令解析任务，使开发者只需调用 AT 框架提供的 API 即可处理与模组的交互数据，SAL 框架全称 Socket Abstract Layer，提供了类似 socket 网络编程的抽象层。基于 AT 框架实现 SAL 的底层函数叫做通信模组的驱动程序。

整体架构如下：

![](https://main.qcloudimg.com/raw/92ca691e35b66b052bbdbee2e6c8c8c6.png)

##  步骤二：移植 AT 框架

从 TencentOS-tiny 中复制以下五个文件到工程目录中，保持文件架构不变并删除多余文件。
1. 复制 `net\at` 目录下的 `tos_at.h` 和 `tos_at.c` 文件，两个文件实现了 TencentOS tiny AT 的框架。 
![](https://main.qcloudimg.com/raw/9948d5be6ddf3d45a88deaa939b4ec73.png)
2. 复制 `platform\hal\st\stm32l4xx\src` 目录下的 `tos_hal_uart.c` 文件，该文件为 TencentOS-tiny AT 框架底层使用的串口驱动 HAL 层。
![](https://main.qcloudimg.com/raw/5662ec84dc7329798974c61d97d6ef7b.png)
3. 复制 `kernel\hal\include` 目录下的 `tos_hal.h` 和 `tos_hal_uart.h` 文件，两个文件为 TencentOS-tiny AT 框架的部分头文件。
![](https://main.qcloudimg.com/raw/e53663baaba9c9859d2035a86f3a973c.png)

文件复制完成，接下来开始添加到工程中。
1. 将以上两个 `.c` 文件添加到 Keil 工程中。
![](https://main.qcloudimg.com/raw/a2b157526b43905bbbfc056ce61cc51f.png)
2. 将 `net\at` 和 `kernel\hal\include` 目录下两个头文件路径添加到 Keil MDK 中。
![](https://main.qcloudimg.com/raw/21d9140898a61a33d03a9448daa8e0dd.png)
3. 在串口中断中配置调用 AT 框架的字节接收函数，编辑 `stm32l4xx_it.c` 文件。
 1. 添加 AT 框架的头文件。
```c
/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "tos_at.h"
/* USER CODE END Includes */
```
 2. 在文件最后添加串口中断回调函数。
```c
/* USER CODE BEGIN 1 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
    extern uint8_t data;
    if (huart->Instance == LPUART1) {
        HAL_UART_Receive_IT(&hlpuart1, &data, 1);
        tos_at_uart_input_byte(data);
    }
}
/* USER CODE END 1 */
```
>!在回调函数中声明 data 变量在外部定义，这是因为 STM32 HAL 库的机制，需要在初始化完成之后先调用一次串口接收函数，使能串口接收中断，编辑 `usart.c` 文件。
>
    1. 在文件开头定义 data 变量为全局变量：
```c
/* USER CODE BEGIN 0 */
uint8_t data;
/* USER CODE END 0 */
```
    2. 在串口初始化完成之后使能接收中断：
```c
/* LPUART1 init function */
void MX_LPUART1_UART_Init(void)
{
    hlpuart1.Instance = LPUART1;
    hlpuart1.Init.BaudRate = 115200;
    hlpuart1.Init.WordLength = UART_WORDLENGTH_8B;
    hlpuart1.Init.StopBits = UART_STOPBITS_1;
    hlpuart1.Init.Parity = UART_PARITY_NONE;
    hlpuart1.Init.Mode = UART_MODE_TX_RX;
    hlpuart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
    hlpuart1.Init.OneBitSampling = UART_ONE_BIT_SAMPLE_DISABLE;
    hlpuart1.AdvancedInit.AdvFeatureInit = UART_ADVFEATURE_NO_INIT;
    if (HAL_UART_Init(&hlpuart1) != HAL_OK)
    {
    Error_Handler();
    }
    //手动添加，使能串口中断
    HAL_UART_Receive_IT(&hlpuart1, &data, 1);
}
```

因为此工程中只配置 LPUART1 和 USART2 两个串口，所以需要将 HAL 驱动中其余的串口屏蔽，否则将会报错。
![](https://main.qcloudimg.com/raw/b639b0f817feef905977ca167b2f38c2.png)

由于 AT 框架使用的缓冲区都是动态内存，所以需要将系统中默认动态内存池的大小至少修改为0x8000。
![](https://main.qcloudimg.com/raw/d9ddd86f9fad71827a34da2ab63b3fbd.png)

## 步骤三：移植 SAL 框架

1. TencentOS-tiny SAL 框架的实现在 `net\sal_module_wrapper` 目录下的 `sal_module_wrapper.h` 和 `sal_module_wrapper.c` 两个文件中，将这个文件夹从 TencentOS-tiny 官方仓库复制到工程目录下，并且保持原有架构不变。
![](https://main.qcloudimg.com/raw/82da4fb2d8a06f53cf2a3c50ed367c77.png)
2. 将 `sal_module_wrapper.c` 文件添加到 Keil MDK 工程中。
![](https://main.qcloudimg.com/raw/04f4163415c4ac939f4f606e4f7cc88f.png)
3. 将头文件 `sal_module_wrapper.h` 所在目录添加到 Keil MDK 中。
![](https://main.qcloudimg.com/raw/0bdb1543fbe89112950a27823e08592d.png)

## 步骤四：移植通信模组驱动

TencentOS-tiny 官方已提供大量的通信模组驱动实现 SAL 框架，覆盖常用的通信方式，例如2G、4G Cat.4、4G Cat.1、NB-IoT 等，在 `devices` 文件夹下,：
- air724
- bc26
- bc25_28_95
- bc35_28_95_lwm2m
- ec20
- esp8266
- m26
- m5310a
- m6312
- sim800a
- sim7600ce
- 欢迎贡献更多驱动...

因为这些驱动都是 SAL 框架的实现，所以这些通信模组的驱动可以根据实际硬件情况**选择一种加入到工程中**，这里以 Wi-Fi 模组 ESP8266 为例，演示如何加入通信模组驱动到工程中。

ESP8266 的驱动在 `devices\esp8266` 目录中，将此文件夹从 TencentOS-tiny 官方仓库复制到工程中，保持目录架构不变。
![](https://main.qcloudimg.com/raw/653b2f25919a1a41b055feae8be264b0.png)
1. 将 `esp8266.c` 文件加入到 Keil MDK 工程中。
![](https://main.qcloudimg.com/raw/1393d6d5b281df84d774682d06f699f9.png)
2. 将 `esp8266.h` 头文件所在路径添加到 Keil MDK 工程中，这样就移植完成。
![](https://main.qcloudimg.com/raw/fdcd3241a383e501ac20d2e4162f2505.png)

## 步骤五：测试网络通信

移植完成之后，修改 main.c，编写代码来测试网络通信是否正常。

添加头文件：
```c
#include "sal_module_wrapper.h"
#include "esp8266.h"
```

接着修改之前编写的 task1 的任务函数：
```c
#define RECV_LEN            1024
uint8_t recv_data[RECV_LEN];

void task1(void *pdata)
{
   int count = 1;
   int socket_id = -1;
   int recv_len = -1;
   
   /* 通信模组初始化 */
   esp8266_sal_init(HAL_UART_PORT_0);
   
   /* 入网 */
   esp8266_join_ap("Mculover666","mculover666");
    
   /* 发起socket连接 */
   socket_id = tos_sal_module_connect("117.50.111.72", "8001", TOS_SAL_PROTO_TCP);
    
   /* 发送一次数据 */
   tos_sal_module_send(socket_id, (uint8_t*)"hello,server!", 12);

   /* 接收一次数据 */
   recv_len = tos_sal_module_recv_timeout(socket_id, recv_data, sizeof(recv_data), 8000);
    
   if (recv_len < 0) {
        printf("receive error\n");
    } else if (recv_len == 0) {
        printf("receive none\n");
    } else {
        recv_data[recv_len] = 0;
        printf("receive len: %d\nmsg from remote: %s\n", recv_len, recv_data);
    }
    
   /* 关闭socket */
   tos_sal_module_close(socket_id);
    
   while(1)
   {
       printf("\r\nHello world!\r\n###This is task1 ,count is %d \r\n", count++);
       HAL_GPIO_TogglePin(LED_GPIO_Port,LED_Pin);
       osDelay(2000);
   }
}

```
>!初始化模组时指定的串口号即为 AT 通信模组所使用的串口，在 `tos_hal_uart.h` 中定义。
>
```c
typedef enum hal_uart_port_en {
    HAL_UART_PORT_0 = 0,    //对应LPUART1
    HAL_UART_PORT_1,        //对应USART1
    HAL_UART_PORT_2,        //依此类推
    HAL_UART_PORT_3,
    HAL_UART_PORT_4,
    HAL_UART_PORT_5,
    HAL_UART_PORT_6,
} hal_uart_port_t;
```
测试网络通信时需要的任务栈较大，所以增大 task1 的任务栈大小为512字节：
![](https://main.qcloudimg.com/raw/bb7c2cfb7aa0d27a07761b3993620a27.png)
同时，为了避免task2运行打印的信息对网络测试信息产生干扰，将创建 task2 的代码屏蔽：
![](https://main.qcloudimg.com/raw/cec0caae6c2c83d182408152d184e0c3.png)
>!TCP 测试服务器需要自己搭建或者使用一些小工具，此处不再详述。
>
编译程序，下载到开发板，在串口查看接收到服务端发送来的消息：
![](https://main.qcloudimg.com/raw/f617c49622ae49ca0d3a4ab30899f864.png)

至此，测试完成。

## 步骤六：下一步操作
请前往 [移植腾讯云 C-SDK](https://cloud.tencent.com/document/product/1081/47958) 进行内核移植操作。
