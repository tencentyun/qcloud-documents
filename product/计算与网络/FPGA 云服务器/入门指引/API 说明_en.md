## Enabling FPGA Image Classification

```
int FpgaClassifyOpen(const string& net_file,
                    const string& fc_net_file,
                    const string& train_file,
                    const string& mean_file,
                    const string& label_file);	
```
**Function:** This API is used to open the FPGA device, load the network structure, parameters, image mean and label files, and allocate resources.

**Parameters:**

- **[IN] net_file**: Path to Alexnet network structure file for classification. Note: Restrictions to Alexnet network structure are as follows:
 - Layer "Pool5" and the layers before it cannot be modified, added or deleted;
 - Layers after "Pool5" can be modified, added or deleted provided that the final output amount is equal to the number of labels of label files;
- **[IN] fc_net_file**: Path to fc_net file. fc_net is a file listed with all layers after "Pool5" in net_file. An input layer is added as the first layer. The parameters are set to (batch size x256x6x6).
- **[IN] train_file**: Path to model parameter file ;
- **[IN] mean_file**: Path to image mean file;
- **[IN] label_file**: Path to category label file;

**Returned value:**

- 0: Successful;
- Negative value: Error code

## Closing the FPGA Device

```
void FpgaClassifyClose(void);
```

**Function:** This API is used to close the FPGA device;
**Parameter:** None;
**Returned Value:** None.

## Classifying Images

```
int FpgaClassifyImage(const cv::Mat& image, float* scores)
```

**Parameters:**

- **[IN] image**: Image entered in the format of OpenCV cv::Mat;
- **[INOUT] scores**: The buffer pointer to receive the scoring results points to the float type. The number must be no less than the number of category labels, and the order of scores is the same as the label order in label_file;

**Returned value:**

- 0: Successful;
- Negative value: Error code.

## Error Code

```
enum FpgaClassifyErrCode {
    FPGA_RET_OK = 0,
    FPGA_RET_BUSY_RETRY = -10086,	//HW is busy, retry again.
    FPGA_RET_BAD_IMAGE,		// Decode image failed.
    FPGA_RET_ACLR_STOP      // HW accelerate service stop for some reason. e.g user interrupt or been killed.
};
```



