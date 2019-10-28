## 打开 FPGA 图片分类功能
```
int FpgaClassifyOpen(const string& net_file,
                    const string& fc_net_file,
                    const string& train_file,
                    const string& mean_file,
                    const string& label_file);	
```
#### 功能：
打开 FPGA 设备，载入网络结构、参数、图片均值和标签文件，分配资源。

#### 参数：

- **[IN]net_file**：分类用 alexnet 网络结构文件路径。
>!此处对 alexnet 的网络结构有以下限定：
 - 不可修改或增减 `Pool5 层`及其之前的各层。
 - 可以随意修改或增减 `Pool5 层`之后的各层，只需保证最终的输出维度与标签文件的标签数目相同即可。
- **[IN]fc_net_file**： `fc_net`的文件路径，`fc_net` 是 `net_file`中`pool5`层后的各层单独列为一个文件，并增加1个`input layer`作为第一层， 参数设置为（批量大小 x 256 x 6 x 6）。
- **[IN]train_file**:：模型参数文件路径。
- **[IN]mean_file**： 图片均值文件路径。
- **[IN]label_file**： 分类标签文件路径。

#### 返回值：
- 0：成功。
- 负值：错误码。

## 关闭FPGA设备
```
void FpgaClassifyClose(void);
```
#### 功能：
关闭 FPGA 设备。
#### 参数：
无。
#### 返回值：
无。

## 分类图片
```
int FpgaClassifyImage(const cv::Mat& image, float* scores)
```
#### 参数：
- **[IN]image**： 输入图片，使用`Opencv` 的 `cv::Mat`格式。
- **[INOUT]scores**：接收打分结果的`buffer 指针`，指向`float 类型`。数目不得低于分类标签的数目，分值的顺序与`label_file`里的标签顺序一致。

#### 返回值：
- 0：成功。
- 负值：错误码。

## 错误码
```
enum FpgaClassifyErrCode {
    FPGA_RET_OK = 0,
    FPGA_RET_BUSY_RETRY = -10086,	//HW is busy, retry again.
    FPGA_RET_BAD_IMAGE,		// Decode image failed.
    FPGA_RET_ACLR_STOP      // HW accelerate service stop for some reason. e.g user interrupt or been killed.
};
```
