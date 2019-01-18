## Scenario Description
Cloud computing enables high performance computing (HPC) to use applications with higher bandwidth and higher computing capacity to address complex scientific, engineering and business issues.
But the problems solved by HPC are usually based on projects, with huge demands for the high scalability of the cloud platform. Compute node can be set into a scaling configuration (template) for the scaling group. By increasing the desired instance number, multiple compute nodes will be generated with one click for any calculation tasks. After saving the calculation results, you can delete the compute nodes for the task by modifying the desired instance number.

![Alt text](https://mc.qcloudimg.com/static/img/d7208378accfb11c320668ee5089a0c3/02.png)

## Tips on Usage
Create a scaling configuration for the nodes in the cluster, and place the computing cluster into the scaling group.

There are two ways to use the original data for high performance computing:

-  Save the data into snapshot, so that the CVM's expanded data disk is created based on the snapshot;

- Save the data into data server, so that all the compute nodes in the CVM can be read in the data server.


## Benefits of AS
- AS can greatly reduce the workload of manual preparation for the environment.

- There is no need to reserve long-term resources for temporary tasks.

## Applicability

- Weather forecast

- Gene sequencing

- Animation rendering, film and TV rendering

- Other industries that require high performance computing

