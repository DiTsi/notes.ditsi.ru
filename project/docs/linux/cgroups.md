# cgroups

## Limit process memory (from [here](https://unix.stackexchange.com/questions/44985/limit-memory-usage-for-a-single-linux-process))

Another way to limit this is to use Linux's control groups. This is especially useful if you want to limit a process's (or group of processes') allocation of physical memory distinctly from virtual memory. For example:

```bash
cgcreate -g memory:myGroup
echo 500M > /sys/fs/cgroup/memory/myGroup/memory.limit_in_bytes
echo 5G > /sys/fs/cgroup/memory/myGroup/memory.memsw.limit_in_bytes
```
will create a control group named `myGroup`, cap the set of processes run under `myGroup` up to 500 MB of physical memory with `memory.limit_in_bytes` and up to 5000 MB of physical and swap memory together with `memory.memsw.limit_in_bytes`. More info about these options can be found here: [https://access.redhat.com/documentation/en-us/red\_hat\_enterprise\_linux/6/html/resource\_management\_guide/sec-memory](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/sec-memory)

To run a process under the control group:

```bash
cgexec -g memory:myGroup pdftoppm
```
> Note that on a modern Ubuntu distribution this example requires installing the `cgroup-bin` package and editing `/etc/default/grub` to change `GRUB_CMDLINE_LINUX_DEFAULT` to: `GRUB_CMDLINE_LINUX_DEFAULT="cgroup_enable=memory swapaccount=1"`

</div></div>and then running `sudo update-grub` and rebooting to boot with the new kernel boot parameters.