When launching a CVM instance for the first time, you can pass user data to the CVM by passing a text and execute the text.
This document uses Windows CVM as an example to describe how to output "Hello Tencent Cloud" by passing a PowerShell script when launching the CVM for the first time.
## Notes
* A command can be executed by passing a text only on the first time of launching a CVM.
* The passed text must be encoded with Base64.
* Adding these tasks to the startup of the CVM will increase its startup time. Wait a few minutes until the tasks complete, and then test whether they are executed successfully.
* In this example, specify the Windows PowerShell script using PowerShell label. For example:
```
<powershell>
"Hello Tencent Cloud." | Out-File .\tencentcloud.txt
</powershell>
```

## Step 1: Write PowerShell script
```
<powershell>
"Hello Tencent Cloud." | Out-File .\tencentcloud.txt
</powershell>
```

## Step 2: Encode the script file with Base64
```
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Script)
$EncodedText =[Convert]::ToBase64String($Bytes)

# The encoded result:
PABwAG8AdwBlAHIAcwBoAGUAbABsAD4AIAAiAEgAZQBsAGwAbwAgAFQAZQBuAGMAZQBuAHQAIABDAGwAbwB1AGQALgAiACAAfAAgAE8AdQB0AC0ARgBpAGwAZQAgAC4AXAB0AGUAbgBjAGUAbgB0AGMAbABvAHUAZAAuAHQAeAB0ACAAPAAvAHAAbwB3AGUAcgBzAGgAZQBsAGwAPgA=
```

## Step 3: Pass the text
### Passing on the official website or the console
When you create a CVM on the official website or the console, select **Advanced Configuration** in **4. Set Security Group and CVM** step. Enter the encoded result of the step 2 in user defined data item. Finish the creation and launch the CVM.
For example, the encoded result in this example is as follows:
```
PABwAG8AdwBlAHIAcwBoAGUAbABsAD4AIAAiAEgAZQBsAGwAbwAgAFQAZQBuAGMAZQBuAHQAIABDAGwAbwB1AGQALgAiACAAfAAgAE8AdQB0AC0ARgBpAGwAZQAgAC4AXAB0AGUAbgBjAGUAbgB0AGMAbABvAHUAZAAuAHQAeAB0ACAAPAAvAHAAbwB3AGUAcgBzAGgAZQBsAGwAPgA=
```
### Passing via API
When creating a CVM via API, you can pass the text by assigning the value of the encoded result of step 2 to UserData parameter of RunInstances API. The following is an example of the parameter of CVM creation request with UserData.
```
https://cvm.tencentcloudapi.com/?Action=RunInstances
  &Version=2017-03-12
  &Placement.Zone=ap-guangzhou-2
  &ImageId=img-pmqg1cw7
  &UserData=PABwAG8AdwBlAHIAcwBoAGUAbABsAD4AIAAiAEgAZQBsAGwAbwAgAFQAZQBuAGMAZQBuAHQAIABDAGwAbwB1AGQALgAiACAAfAAgAE8AdQB0AC0ARgBpAGwAZQAgAC4AXAB0AGUAbgBjAGUAbgB0AGMAbABvAHUAZAAuAHQAeAB0ACAAPAAvAHAAbwB3AGUAcgBzAGgAZQBsAGwAPgA=
  &<Common request parameters>
```

