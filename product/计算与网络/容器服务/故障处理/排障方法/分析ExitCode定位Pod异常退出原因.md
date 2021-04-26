本文介绍如何根据 Pod 异常状态信息中的 Exit Code 进一步定位问题。

## 查看 Pod 异常状态信息
执行以下命令，查看异常 Pod 状态信息。
```
kubectl describe pod <pod name>
```
返回结果如下：
```bash
Containers:
  kubedns:
    Container ID:  docker://5fb8adf9ee62afc6d3f6f3d9590041818750b392dff015d7091eaaf99cf1c945
    Image:         ccr.ccs.tencentyun.com/library/kubedns-amd64:1.14.4
    Image ID:      docker-pullable://ccr.ccs.tencentyun.com/library/kubedns-amd64@sha256:40790881bbe9ef4ae4ff7fe8b892498eecb7fe6dcc22661402f271e03f7de344
    Ports:         10053/UDP, 10053/TCP, 10055/TCP
    Host Ports:    0/UDP, 0/TCP, 0/TCP
    Args:
      --domain=cluster.local.
      --dns-port=10053
      --config-dir=/kube-dns-config
      --v=2
    State:          Running
      Started:      Tue, 27 Aug 2019 10:58:49 +0800
    Last State:     Terminated
      Reason:       Error
      Exit Code:    255
      Started:      Tue, 27 Aug 2019 10:40:42 +0800
      Finished:     Tue, 27 Aug 2019 10:58:27 +0800
    Ready:          True
    Restart Count:  1
```
在返回结果的容器列表 `Last State` 字段中， `Exit Code` 为程序上次退出时的状态码，该值不为0即表示程序异常退出，可根据退出状态码进一步分析异常原因。

## 退出状态码说明

* 状态码需在0 - 255之间。
* 0表示正常退出。
* 若因外界中断导致程序退出，则状态码区间为129 - 255。例如，操作系统给程序发送中断信号 `kill -9` 或 `ctrl+c`，导致程序状态变为 `SIGKILL` 或 `SIGINT`。
* 通常因程序自身原因导致的异常退出，状态码区间在1 - 128。在某些场景下，也允许程序设置使用129 - 255区间的状态码。
- 若指定的退出状态码不在0 - 255之间（例如，设置 `exit(-1)`），此时将会自动执行转换，最终呈现的状态码仍会在0 - 255之间。
若将退出时状态码记为 `code`，则不同情况下转换方式如下：
    * 当指定的退出时状态码为负数，转换公式为：
```text
256 - (|code| % 256)
```
    * 当指定的退出时状态码为正数，转换公式为：
```text
code % 256
```

## 常见异常状态码
* **137**：表示程序被 `SIGKILL` 中断信号杀死。异常原因可能为：
 * 通常是由于 Pod 中容器内存达到了其资源限制（`resources.limits`）。例如，内存溢出（OOM）。由于资源限制是通过 Linux 的 cgroup 实现的，当某个容器内存达到资源限制， cgroup 就会将其强制停止（类似于 `kill -9`），此时通过 `describe pod` 可以看到 Reason 是 `OOMKilled`。
 * 宿主机本身资源不够用（OOM），则内核会选择停止一些进程来释放内存。
>?无论是 cgroup 限制，还是因为节点机器本身资源不够导致的进程停止，都可以从系统日志中找到记录。方法如下：
>Ubuntu 系统日志存储在目录 `/var/log/syslog`，CentOS 系统日志存储在目录 `/var/log/messages` 中，两者系统日志均可通过 `journalctl -k` 命令进行查看。
>
 * livenessProbe（存活检查）失败，使得 kubelet 停止 Pod。
 * 被恶意木马进程停止。
* **1和255**：通常表示一般错误，具体原因需要通过容器日志进一步定位。例如，可能是设置异常退出使用 `exit(1)` 或 `exit(-1)`导致的，而-1将会根据规则转换成255。



## Linux 标准中断信号

Linux 程序被外界中断时会发送中断信号，程序退出时的状态码为中断信号值加128。例如， `SIGKILL` 的中断信号值为9，那么程序退出状态码则为9 + 128 = 137。更多标准信号值参考如下表：

<table>
	<tr>
	<th>信号 Signal</th> <th>状态码 Value</th> <th>动作 Action</th> <th>描述 Comment</th>
	</tr>
	<tr>
	<td><code>SIGHUP</code></td> <td>1</td> <td>Term</td>
	<td>Hangup detected on controlling terminal or death of controlling process</td>
	</tr>
	<tr>
	<td><code>SIGINT</code></td> <td>2</td> <td>Term</td>
	<td>Interrupt from keyboard</td>
	</tr>
	<tr>
	<td><code>SIGQUIT</code></td> <td>3</td> <td>Core</td>
	<td>Quit from keyboard</td>
	</tr>
	<tr>
	<td><code>SIGILL</code></td> <td>4</td> <td>Core</td>
	<td> Illegal Instruction</td>
	</tr>
	<tr>
	<td><code>SIGABRT</code></td> <td>6</td> <td>Core</td>
	<td>Abort signal from abort(3)</td>
	</tr>
	<tr>
	<td><code>SIGFPE</code></td> <td>8</td> <td>Core</td>
	<td> Floating-point exception</td>
	</tr>
	<tr>
	<td><code>SIGKILL</code></td> <td>9</td> <td>Term</td>
	<td>Kill signal</td>
	</tr>
	<tr>
	<td><code>SIGSEGV</code></td> <td>11</td> <td>Core</td>
	<td>Invalid memory reference</td>
	</tr>
	<tr>
	<td><code>SIGPIPE</code></td> <td>13</td> <td>Term</td>
	<td>Broken pipe: write to pipe with no readers; see pipe(7)</td>
	</tr>
	<tr>
	<td><code>SIGALRM</code></td> <td>14</td> <td>Term</td>
	<td>Timer signal from alarm(2)</td>
	</tr>
	<tr>
	<td><code>SIGTERM</code></td> <td>15</td> <td>Term</td>
	<td>Termination signal</td>
	</tr>
	<tr>
	<td><code>SIGUSR1</code></td> <td>30,10,16 </td> <td>Term</td>
	<td>User-defined signal 1</td>
	</tr>
	<tr>
	<td><code>SIGUSR2</code></td> <td>31,12,17</td> <td>Term</td>
	<td>User-defined signal 2</td>
	</tr>
	<tr>
	<td><code>SIGCHLD</code></td> <td>20,17,18</td> <td>Ign</td>
	<td>Child stopped or terminated</td>
	</tr>
	<tr>
	<td><code>SIGCONT</code></td> <td>19,18,25</td> <td>Cont</td>
	<td> Continue if stopped</td>
	</tr>
	<tr>
	<td><code>SIGSTOP</code></td> <td>17,19,23</td> <td>Stop</td>
	<td>Stop process</td>
	</tr>
	<tr>
	<td><code>SIGTSTP</code></td> <td>18,20,24</td> <td>Stop</td>
	<td>Stop typed at terminal</td>
	</tr>
	<tr>
	<td><code>SIGTTIN</code></td> <td>21,21,26</td> <td>Stop</td>
	<td>Terminal input for background process</td>
	</tr>
	<tr>
	<td><code>SIGTTOU</code></td> <td>22,22,27</td> <td>Stop</td>
	<td>Terminal output for background process</td>
	</tr>
</table>



## C/C++ 退出状态码

`/usr/include/sysexits.h` 中进行了退出状态码标准化（仅限 C/C++），如下表：

<table>
	<tr>
	<th>定义</th> <th>状态码</th> <th>描述</th>
	</tr>
	<tr>
	<td><code>#define EX_OK</code></td> <td>0</td>
	<td>successful termination</td>
	</tr>
	<tr>
	<td><code>#define EX__BASE</code></td> <td>64</td>
	<td>base value for error messages</td>
	</tr>
	<tr>
	<td><code>#define EX_USAGE</code></td> <td>64</td>
	<td>command line usage error</td>
	</tr>
	<tr>
	<td><code>#define EX_DATAERR</code></td> <td>65</td>
	<td>data format error</td>
	</tr>
	<tr>
	<td><code>#define EX_NOINPUT</code></td> <td>66</td>
	<td>cannot open input</td>
	</tr>
	<tr>
	<td><code>#define EX_NOUSER</code></td> <td>67</td>
	<td>addressee unknown</td>
	</tr>
	<tr>
	<td><code>#define EX_NOHOST </code></td> <td>68</td>
	<td> host name unknown</td>
	</tr>
	<tr>
	<td><code>#define EX_UNAVAILABLE</code></td> <td>69</td>
	<td>service unavailable</td>
	</tr>
	<tr>
	<td><code>#define EX_SOFTWARE</code></td> <td>70</td>
	<td>internal software error</td>
	</tr>
	<tr>
	<td><code>#define EX_OSERR </code></td> <td>71</td>
	<td>system error (e.g., can't fork)</td>
	</tr>
	<tr>
	<td><code>#define EX_OSFILE</code></td> <td>72</td>
	<td>critical OS file missing</td>
	</tr>
	<tr>
	<td><code>#define EX_CANTCREAT</code></td> <td>73</td>
	<td>can't create (user) output file</td>
	</tr>
	<tr>
	<td><code>#define EX_IOERR</code></td> <td>74</td>
	<td>input/output error</td>
	</tr>
	<tr>
	<td><code>#define EX_TEMPFAIL</code></td> <td>75</td>
	<td>temp failure; user is invited to retry</td>
	</tr>
	<tr>
	<td><code>#define EX_PROTOCOL</code></td> <td>76</td>
	<td>remote error in protocol</td>
	</tr>
	<tr>
	<td><code>#define EX_NOPERM </code></td> <td>77</td>
	<td>permission denied</td>
	</tr>
	<tr>
	<td><code>#define EX_CONFIG</code></td> <td>78</td>
	<td>configuration error</td>
	</tr>
	<tr>
	<td><code>#define EX__MAX 78</code></td> <td>78</td>
	<td>maximum listed value</td>
		</tr>
</table>



## 状态码参考

更多状态码含义可参考以下表格：
<table>
    <tr>
        <th>状态码</th>
        <th>含义</th>
        <th>示例</th>
        <th>描述</th>
    </tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Catchall for general errors</td>
<td>let "var1 = 1/0"</td>
<td>Miscellaneous errors, such as <span>"divide by zero"</span> and other impermissible operations</td>
</tr>
<tr>
<td>2</td>
<td>Misuse of shell builtins (according to Bash documentation)</td>
<td>empty_function() {}</td>
<td><a>Missing keyword</a> or command</td>
</tr>
<tr>
 <td>126</td>
<td>Command invoked cannot execute</td>
<td>/dev/null</td>
<td>Permission problem or command is not an executable</td>
</tr>
        <tr>
            <td>127</td>
            <td><span>"command not found"</span></td>
            <td>illegal_command</td>
            <td>Possible problem with <tt>$PATH</tt> or a typo</td>
        </tr>
        <tr>
            <td>128</td>
            <td>Invalid argument to <a> exit</a></td>
            <td>exit 3.14159</td>
            <td><strong>exit</strong> takes only integer args in therange<span>0 - 255</span> (seefirst footnote)</td>
        </tr>
        <tr>
            <td>128+n</td>
            <td>Fatal error signal <span>"n"</span></td>
            <td><em>kill -9</em> <tt> $PPID</tt> of script</td>
            <td><tt><strong>$?</strong></tt> returns<span>137</span> (128 + 9)</td>
        </tr>
        <tr>
            <td>130</td>
            <td>Script terminated by Control-C</td>
            <td><em>Ctl-C</em></td>
            <td>Control-C is fatal error signal <span> 2</span>, (130 = 128 + 2, see above)</td>
        </tr>
        <tr>
            <td>255*</td>
            <td>Exit status out of range</td>
            <td>exit <span>-1</span></td>
            <td><strong>exit</strong> takes only integer args in the
                range<span>0 - 255</span></td>
        </tr>
    </tbody>
</table>
