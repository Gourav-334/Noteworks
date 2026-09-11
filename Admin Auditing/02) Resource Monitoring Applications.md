# $\fbox{Chapter 2: RESOURCE MONITORING APPLICATIONS}$





## **Topic - 1: Task Manager**

### <u>About</u>

- It is mainly about knowing usage information.


### <u>Shortcut</u>

```cmd
Ctrl + Shift + Esc
```


### <u>Monitored Features</u>

- CPU & GPU usage
- Disk & memory
- Network
- Processes & services
- Startup applications



## **Topic - 2: Resource Monitor**

### <u>About</u>

- Similar to *Task Manager* but more detailed.
- It very specifically specializes in showing which processes are running which operations.
- Operations like *read*, *write*, etc.
- Expect to know about running threads also.


### <u>Shortcut Command</u>

```cmd
resmon.exe
```



## **Topic - 3: Performance Monitor**

### <u>About</u>

- Traditional *Windows* tool for performance monitoring.
- Unlike *Task Manager*, certain form of performance type can be chosen to know.
- These performances are about processor, memory, and disk.
- It shows plot over time when chosen.
- Includes past data, not just current ones.

```
utilization
 100% │             ╭─╮
      │       ╭─────╯ ╰──╮
  50% │───────╯           ╰──
      │
   0% └────────────────────────► time
```


### <u>Performance Counters</u>

```
Processor
 ├── % Processor Time
 ├── % User Time
 └── % Privileged Time

Memory
 ├── Available MBytes
 ├── Pages/sec
 └── Committed Bytes

PhysicalDisk
 ├── Disk Reads/sec
 ├── Disk Writes/sec
 └── Avg. Disk Queue Length
```



## **Topic - 4: Windows CLI**

### <u>Task List</u>

```cmd
tasklist
```


### <u>Task Kill</u>

```cmd
taskkill /PID <p_id>
```



## **Topic - 5: PowerShell**

### <u>About Feature</u>

- Contains important information related to usage.
- **For example -** CPU, memory, processes, threads, executables, etc.


### <u>Command</u>

```powershell
Get-Process                 # Running processes
Get-Process explorer        # Example
```



## **Topic - 6: Summary**

| Application         | When To Use                  |
| :------------------ | :--------------------------- |
| Task Manager        | Basic usage details          |
| Resource Monitor    | Processes & threads details  |
| Performance Monitor | Performance & usage timeline |
| Windows CLI         | Command-line interface       |
| PowerShell          | Command-line interface       |

>**<u>NOTE</u>:**
>There are other more detailed tools too, like *Process Explorer* & *Process Monitor (`procmon`)*.

---
