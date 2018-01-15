## Overview

Batch provides the instances of a task with the task-related environment variable information, to allow user program to execute different computing tasks based on the environment variables.

## Details

| Variable Name | Meaning | Description |
|---------|---------|---------|
| BATCH_JOB_ID | Job ID | ID of a job to which instances belong. It is included in the returned result after the job is submitted. For example: job-n4ohivif |
| BATCH_TASK_NAME | Task name | Name of a task to which instances belong. It is specified when the job is submitted. For example, `"TaskName": "Task1"` |
| BATCH_TASK_INSTANCE_NUM | Total number of instances of a task | The total number of instances requested to run concurrently in a task to which the instances belong. For example, `"TaskInstanceNum": 5"` |
| BATCH_TASK_INSTANCE_INDEX | Task instance index | The index of an instance in a task to which instances belong. For example, 5 instances are specified to run concurrently in a task, and the indices of these instances are 0, 1, 2, 3, 4 respectively. |


