## How to Use the Tool
1. Download the "[Windows Client Upload Tool](https://mc.qcloudimg.com/static/archive/ef1dec9f9a72cbafdc707915475a368e/upload.zip)" to the local computer, and decompress it to any folder. Note: The folder path should not include Chinese. After the decompression, the file directory structure is as follows:
![](https://mc.qcloudimg.com/static/img/716da8b5ece00ca2be062e2b637ff40d/1-1.png)

2. To ensure your data seucrity, you need to edit the configuration file etc\conf.json and enter your API key ([secretId and secretKey](https://cloud.tencent.com/help/%E4%BA%91API%E8%AE%BF%E9%97%AE%E5%AF%86%E9%92%A5%E5%9C%A8%E5%93%AA%E9%87%8C%E8%8E%B7%E5%8F%96%EF%BC%8C%E8%AE%BF%E9%97%AE%E5%AF%86%E9%92%A5%E6%9C%80%E5%A4%9A%E6%9C%89%E5%A4%9A%E5%B0%91%E4%B8%AA)) before uploading the backup. Be sure to keep your API key well to avoid leakage. To ensure a reliable transmission, this tool can resume upload from the breakpoint.
Note: Store the conf.json file in "UTF-8 without BOM" format. In Windows, it is recommended to use notepad++ to convert encoding)

![](https://mc.qcloudimg.com/static/img/8cd149b24b1be3df87371081fa8cad39/1-2.png)

3. Enter the Windows command line ("Start" ->"Search programs and files" > Enter "cmd")

![](https://mc.qcloudimg.com/static/img/57dadbb324f56172f7a5c0f825e91d9b/1-3.png)

4. In the Windows command line, enter the directory of the decompressed "Windows Client Upload Tool", and then call the upload-tool.exe under the bin directory to complete the upload. upload-tool.exe has two parameters: -r and -p. -p indicates the absolute path of the backup file in the local computer, and -r indicates the region where the transit storage is located (select the region where your Tencent Cloud Database resides in)
![](https://mc.qcloudimg.com/static/img/a4390e737e6367d860e2037c7b5068f3/1-4.png)

## Region Mapping

| Region | -r Parameter |
|---------|---------
| Guangzhou | gz | 
| Shanghai | sh |
| Hong Kong | hk | 
| Shanghai Finance | shjr | 
| Beijing | bj | 
| Shenzhen Finance | szjr | 

Note: The parameter is case sensitive
