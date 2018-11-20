1) Log in to Tencent Cloud console, and select SCF.

2) Click **Create Function** button under **Guangzhou** region, to enter the new function page.

3) Enter the function name as `hello-world` and leave all other configuration options unchanged.

4) Click **Next** button, to enter function code edit page, select default **Online Edit**, and select `Hello World` template in **Template**. At this time, execution method and code will be entered with the default values in template:

 - Execution method is `index.main_handler`. SCF console stores this piece of code as `index.py` file automatically, and uploads the file that is compressed to SCF platform to create cloud function.
 - The following code fragments are displayed in the function code:

```
print('Start Hello World function')
def main_handler(event, context):
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    return event['key1']  #return the value of key "key1"
```
This sample code acquires the following form of data from the parameter `event`:
```
{
  "key1": "test value 1",
  "key2": "test value 2"
}
```

5) Click **Next** to enter triggering method page. You don't need to configure any trigger for this sample code, so you can simply click **Complete** button.

6) At this point, the console will generate a code package automatically and upload it to SCF platform to create cloud function. Click the `hello-world` function you just created in the cloud function list page, to enter the cloud function details page.


