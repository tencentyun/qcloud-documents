## 操作场景
本文档使用了腾讯云开发者工具套件（SDK）3.0及云 API 接口，实现在销毁包年包月云服务器实例时，同时销毁已挂载至该实例的所有包年包月云硬盘。本文档适用于销毁仅含有包年包月云硬盘的包年包月云服务器，提供 Python 及 Go 两种语言的示例代码，请您结合实际情况进行使用。
 
<dx-alert infotype="notice" title="">
销毁/退还云服务器实例及云硬盘所造成的影响请参见 [相关影响](https://cloud.tencent.com/document/product/213/4930#.E7.9B.B8.E5.85.B3.E5.BD.B1.E5.93.8D)。
</dx-alert>



## 前提条件
- 已具备计费模式为包年包月的云服务器实例，且该实例已挂载云硬盘。
- 已前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取 SecretID 及 SecretKey。


## 操作步骤
### 安装依赖环境及 SDK
请根据您实际使用的开发语言，安装对应依赖环境及 SDK：
<dx-tabs>
::: Go
1. 安装 Go 1.9 或其以上版本，并设置 GOPATH 等所需环境变量。详情请参见 [Golang 官网](https://golang.org/)。
2. 执行以下命令，安装 GO SDK。更多信息请参见 [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)。
```
go get github.com/tencentcloud/tencentcloud-sdk-go@latest
```
:::
::: Python
1. 安装 Python 3.6 - 3.9 版本，详情请参见 [Python 官网](https://www.python.org/)。
2. 执行以下命令，安装 Python SDK。更多信息请参见 [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)。
```
pip install --upgrade tencentcloud-sdk-python
```
:::
</dx-tabs>


### 运行示例代码
示例代码如下，您可根据实际情况进行使用：

<dx-tabs>
::: Go
main 程序示例代码：
<dx-codeblock>
:::  Golang
package main

import (
	"termins"	// 导入package
)

func main() {
	var id = "xxxxxx"  // 请替换为实际使用的 SecretID
	var key = "xxxxxx"	// 请替换为实际使用的 SecretKey
	var region = "ap-beijing"
	ins := "ins-irmer45l"
	termins.NewTerminateInstancesAndCbs(id, key, region).Process(ins)   
}
:::
</dx-codeblock>
销毁实例及云硬盘示例代码：
<dx-codeblock>
:::  Golang
package termins

import (
	"fmt"
	cbs "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cbs/v20170312"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	cvm "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm/v20170312"
	"strings"
	"time"
)

type TerminateInstancesAndCbs struct {
	Credential \*common.Credential
	Region string
	CbsClient \*cbs.Client
	CvmClient \*cvm.Client
}

func NewTerminateInstancesAndCbs(secretId string, secretKey string, region string) \*TerminateInstancesAndCbs {
	credential := common.NewCredential(secretId, secretKey)

	cpfCbs := profile.NewClientProfile()
	cpfCbs.HttpProfile.Endpoint = "cbs.tencentcloudapi.com"
	cbsClient, _ := cbs.NewClient(credential, region, cpfCbs)

	cpfCvm := profile.NewClientProfile()
	cpfCvm.HttpProfile.Endpoint = "cvm.tencentcloudapi.com"
	cvmClient, _ := cvm.NewClient(credential, region, cpfCvm)

	return &TerminateInstancesAndCbs{Credential: credential, Region: region, CbsClient: cbsClient, CvmClient: cvmClient}
}

func (c \*TerminateInstancesAndCbs) TerminateInstance(instanceId string) (cvmApiErrors []string){
	request := cvm.NewTerminateInstancesRequest()
	request.InstanceIds = common.StringPtrs([]string{instanceId})

	for i := 0; i < 5; i ++ {
		response, err := c.CvmClient.TerminateInstances(request)
		if \_, ok := err.(\*errors.TencentCloudSDKError); ok {
			cvmApiErrors = append(cvmApiErrors, fmt.Sprintf("Got API error when terminating %s: %s", instanceId, err))
			time.Sleep(3 \* time.Second)
			continue
		}
		if err != nil { // 非SDK错误
			panic(err)
		}
		fmt.Printf("TerminateInstance: %s, resp: %s", instanceId, response.ToJsonString())
		return []string{}
	}
	return cvmApiErrors
}

func (c \*TerminateInstancesAndCbs) DescribeDisksForInstances(instanceId string) ([]string, error) {
	request := cbs.NewDescribeDisksRequest()
	request.Filters = []\*cbs.Filter {
		{
			Values: common.StringPtrs([]string{instanceId}),
			Name:   common.StringPtr("instance-id"),
		},
	}
	response, err := c.CbsClient.DescribeDisks(request)
	if \_, ok := err.(\*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return []string{}, err
	}
	if err != nil {
		panic(err)
	}
	var cbsIds []string
	for \_, disk := range response.Response.DiskSet {
		if \*disk.DiskUsage == "DATA_DISK" {
				cbsIds = append(cbsIds, \*disk.DiskId)
		}
	}
	return cbsIds, nil
}

func (c \*TerminateInstancesAndCbs) CheckTerminateInstanceSuccess(instanceId string) (result bool, cvmApiErrors []string){
	request := cvm.NewDescribeInstancesRequest()
	request.InstanceIds = common.StringPtrs([]string{instanceId})

	for i := 0; i < 30; i ++ {
		response, err := c.CvmClient.DescribeInstances(request)

		if err != nil { // 非SDK错误
			panic(err)
		}
		if \_, ok := err.(\*errors.TencentCloudSDKError); ! ok {
			fmt.Printf("Describe instance %s: resp: %s", instanceId, response.ToJsonString())
			// 后付费实例
			if \*response.Response.TotalCount == 0 {
				return true, []string{}
			}
			// 预付费实例
			if *response.Response.TotalCount == 1 && \*response.Response.InstanceSet[0].InstanceState == "SHUTDOWN" {
				return true, []string{}
			}
		} else {
			cvmApiErrors = append(cvmApiErrors, fmt.Sprintf("Got API error when describing %s: %s", instanceId, err))
		}
		time.Sleep(6 \* time.Second)
	}
	return false, cvmApiErrors
}

func (c \*TerminateInstancesAndCbs) DetachDisks(diskIds []string) (result bool, cbsApiErrors []string){
	request := cbs.NewDetachDisksRequest()
	request.DiskIds = common.StringPtrs(diskIds)

	for i := 0; i < 5; i ++ {
		response, err := c.CbsClient.DetachDisks(request)
		if \_, ok := err.(\*errors.TencentCloudSDKError); ! ok {
			return true, []string{}
		}
		if err != nil {	// 非SDK错误
			panic(err)
		}
		fmt.Printf("Detach Disks: %s, resp: %s", strings.Join(diskIds, ","), response.ToJsonString())
		cbsApiErrors =  append(cbsApiErrors, fmt.Sprintf("Got API error when detaching disks: %s", err))
		time.Sleep(3 \* time.Second)
	}
	return false, cbsApiErrors
}

func (c \*TerminateInstancesAndCbs) CheckDisksDetached(diskIds []string) (result bool, cbsApiErrors []string) {
	second := 60 * 3
	count := len(diskIds)

	request := cbs.NewDescribeDisksRequest()
	request.DiskIds = common.StringPtrs(diskIds)

	for ; second > 0; second -= 3 {
		response, err := c.CbsClient.DescribeDisks(request)
		if \_, ok := err.(\*errors.TencentCloudSDKError); ! ok {
			// 检查是否所有磁盘都已经解挂
			cnt := count
			for \_, disk := range response.Response.DiskSet {
				if \*disk.Attached == false {
					cnt -= 1
				}
			}
			if cnt == 0 {
				return true, []string{}
			}
		}
		if err != nil { // 非SDK错误
			panic(err)
		}
		cbsApiErrors = append(cbsApiErrors, fmt.Sprintf("Got API error when terminating disks: %s", err))
		time.Sleep(3 \* time.Second)
	}
	return false, []string{}
}

func (c \*TerminateInstancesAndCbs) TerminateDisks(diskIds []string) (result bool, cbsApiErrors []string){

	request := cbs.NewTerminateDisksRequest()
	request.DiskIds = common.StringPtrs(diskIds)

	for i := 0; i < 10; i ++ {
		response, err := c.CbsClient.TerminateDisks(request)
		if \_, ok := err.(\*errors.TencentCloudSDKError); ! ok {
			return true, []string{}
		}
		if err != nil {	// 非SDK错误
			panic(err)
		}
		fmt.Printf("TerminateDisks: %s, resp: %s", strings.Join(diskIds, ","), response.ToJsonString())
		cbsApiErrors = append(cbsApiErrors, fmt.Sprintf("Got API error when terminating disks: %s", err))
		time.Sleep(6 \* time.Second)
	}
	return false, cbsApiErrors
}

func (c \*TerminateInstancesAndCbs) Process(instanceId string) {
	// 从cvm实例中获取磁盘实例id
	cbsIds, desDiskError := c.DescribeDisksForInstances(instanceId)
	if desDiskError != nil {
		panic(desDiskError)
	}

	// 销毁实例
	termInsErrors := c.TerminateInstance(instanceId)
	if len(termInsErrors) != 0 {
		panic(termInsErrors)
	}

	// 检查实例是否处于shutdown状态
	checkTermInsRes, checkTermInsErrors := c.CheckTerminateInstanceSuccess(instanceId)
	if ! checkTermInsRes {
		panic(checkTermInsErrors)
	}

	// 解挂磁盘
	if len(cbsIds) == 0 {
		return
	}
	detachDisksRes, detachDisksError := c.DetachDisks(cbsIds)
	if ! detachDisksRes {
		panic(detachDisksError)
	}

	// 检查磁盘是否已经解挂
	checkDetachDisksRes, checkDetachDisksErrors := c.CheckDisksDetached(cbsIds)
	if ! checkDetachDisksRes {
		panic(checkDetachDisksErrors)
	}

	// 销毁磁盘
	termDisksRes, termDisksErrors := c.TerminateDisks(cbsIds)
	if ! termDisksRes {
		panic(termDisksErrors)
	}
}
:::
</dx-codeblock>
:::
::: Python
main 程序示例代码：
<dx-codeblock>
:::  python
# -*- coding: utf-8 -*-
import sys
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from TerminateTotalInstance import TerminateTotalInstance

if __name__ == '__main__':
    try:
        id = "xxxxxx"  // 请替换为实际使用的 SecretID
        key = "xxxxxx"	// 请替换为实际使用的 SecretKey
        region = "ap-beijing"
        ins = "ins-irmer45l"
        TerminateTotalInstance(sid, skey, region=region).process(instance_id=instance_id)
        print("done!")
    except TencentCloudSDKException as e:
        print(e)
    except Exception as e:
        print("failed")
:::
</dx-codeblock>
销毁实例及云硬盘示例代码：
<dx-codeblock>
:::  python
# -*- coding: utf-8 -*-
import logging
import time

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.cvm.v20170312 import cvm_client, models as cvm_models
from tencentcloud.cbs.v20170312 import cbs_client, models as cbs_models


class TerminateTotalInstance(object):
    def __init__(self, sid, skey, region):
        self.sid = sid
        self.skey = skey
        self.cred = credential.Credential(self.sid, self.skey)
        self.cbs_client = self.__create_cbs_client(region)
        self.cvm_client = self.__create_cvm_client(region)

    def get_cred(self):
        # 如果是根据token获取的身份， 这里需要判断一下token是否有效
        # 如果无效， 重新获取cred
        if not self.cred:
            self.cred = credential.Credential(self.sid, self.skey)
        return self.cred

    def process(self, instance_id):
        # 获取云盘
        cbs_ids = self.describe_disks_for_instance(instance_id)

        # 退还实例
        cvm_resp, cvm_api_errors = self.terminate_instance(instance_id)
        if cvm_api_errors:
            raise Exception(cvm_api_errors)

        # 确认子机退还成功
        is_succ, cvm_api_errors = self.check_terminate_instance_success(instance_id)
        if not is_succ:
            raise Exception(cvm_api_errors)

        # 解挂并批量退还云盘
        if not cbs_ids:
            return
        cbs_resp, cbs_api_errors = self.detach_disks(cbs_ids)
        if cbs_api_errors:
            raise Exception(cbs_api_errors)

        cbs_resp, cbs_api_errors = self.terminate_disks_for_instance(cbs_ids)
        if cbs_api_errors:
            raise Exception(cbs_api_errors)

    def terminate_instance(self, instance_id):
        # 调用失败历史
        cvm_api_errors = []

        for i in range(0, 5):
            try:
                req = cvm_models.TerminateInstancesRequest()
                params = '{"InstanceIds":["%s"]}' % instance_id
                req.from_json_string(params)
                resp = self.cvm_client.TerminateInstances(req)
                cvm_api_errors.clear()
                return resp, cvm_api_errors

            except TencentCloudSDKException as e:
                # 失败重试，记录报错
                cvm_api_errors.append(e)
                logging.error(e)
            time.sleep(3)

        return None, cvm_api_errors

    def check_terminate_instance_success(self, instance_id):
        # 调用失败历史
        cvm_api_errors = []

        for _ in range(0, 30):
            try:
                req = cvm_models.DescribeInstancesStatusRequest()
                params = '{"InstanceIds":["%s"]}' % instance_id
                req.from_json_string(params)
                resp = self.cvm_client.DescribeInstancesStatus(req)
                cvm_api_errors.clear()
                if resp.TotalCount > 0:
                    if resp.InstanceStatusSet[0].InstanceState == "SHUTDOWN":
                        return True, cvm_api_errors
                    else:
                        logging.error(resp)

            except TencentCloudSDKException as e:
                # 失败重试，记录报错
                cvm_api_errors.append(e)
                logging.error(e)
            time.sleep(6)

        return False, cvm_api_errors

    def describe_disks_for_instance(self, instance_id):
        # 获取绑定在子机上的数据盘
        req = cbs_models.DescribeDisksRequest()
        params = '{"Filters": [ { "Name": "instance-id", "Values": [ "%s" ]}]}' % instance_id
        req.from_json_string(params)
        disks = self.cbs_client.DescribeDisks(req)
        if hasattr(disks, "DiskSet"):
            cbs_ids = [disk.DiskId for disk in disks.DiskSet if disk.DiskUsage == "DATA_DISK"]
        else:
            cbs_ids = list()
        return cbs_ids

    def detach_disks(self, cbs_ids):
        # 解挂数据盘
        cbs_api_errors = []
        for _ in range(0, 5):
            try:
                req = cbs_models.DetachDisksRequest()
                req.DiskIds = cbs_ids
                resp = self.cbs_client.DetachDisks(req)
                cbs_api_errors.clear()
                return resp, cbs_api_errors

            except TencentCloudSDKException as e:
                # 失败重试，记录报错
                cbs_api_errors.append(e)
                logging.error(e)
            time.sleep(3)

        return None, cbs_api_errors

    def terminate_disks_for_instance(self, cbs_ids):
        # 退还数据盘
        cbs_api_errors = []
        for _ in range(0, 10):
            try:
                req = cbs_models.TerminateDisksRequest()
                req.DiskIds = cbs_ids
                resp = self.cbs_client.TerminateDisks(req)
                cbs_api_errors.clear()
                return resp, cbs_api_errors

            except TencentCloudSDKException as e:
                # 失败重试，记录报错
                cbs_api_errors.append(e)
                logging.error(e)
            time.sleep(6)
        return None, cbs_api_errors

    def __create_cbs_client(self, region):
        http_profile = HttpProfile()
        http_profile.endpoint = "cbs.tencentcloudapi.com"

        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile
        return cbs_client.CbsClient(self.get_cred(), region, client_profile)

    def __create_cvm_client(self, region):
        http_profile = HttpProfile()
        http_profile.endpoint = "cvm.tencentcloudapi.com"

        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile
        return cvm_client.CvmClient(self.get_cred(), region, client_profile)
:::
</dx-codeblock>

:::
</dx-tabs>

	
	
