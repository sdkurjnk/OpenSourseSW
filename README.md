# 오픈소스 과제 3

#### 1. top
현재 OS의 상태를 나타내주는 CLI 어플리케이션.

메모리 사용량, CPU 사용량 등을 보여준다.

실시간으로 업데이트하여 실시간에 근접한 내용을 보여준다.

사용 가능한 옵션

* -d <초> : 업데이트 주기 설정

* -n <횟수> : 업데이트 횟수 지정 후 종료

* -u <사용자> : 특정 사용자의 프로세스만 출력

* -p <PID> : 특정 PID만 모니터링하여 출력

* -b : 배치 모드 (출력 결과를 파일로 저장하거나 파이프 처리 시 사용)

```bash
top - 17:12:22 up 1 min,  1 user,  load average: 0.00, 0.00, 0.00
Tasks:  23 total,   1 running,  22 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni, 99.8 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :  15744.2 total,  14914.9 free,    534.3 used,    490.6 buff/cache
MiB Swap:   4096.0 total,   4096.0 free,      0.0 used.  15210.0 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
      1 root      20   0   21816  12124   9180 S   0.0   0.1   0:00.35 systemd
      2 root      20   0    3060   1920   1792 S   0.0   0.0   0:00.00 init-systemd(Ub
      6 root      20   0    3076   1792   1792 S   0.0   0.0   0:00.00 init
     52 root      19  -1   42124  15620  14724 S   0.0   0.1   0:00.10 systemd-journal
     98 root      20   0   25264   6400   4864 S   0.0   0.0   0:00.07 systemd-udevd
    108 systemd+  20   0   21452  12288  10368 S   0.0   0.1   0:00.05 systemd-resolve
    117 systemd+  20   0   91020   7680   6784 S   0.0   0.0   0:00.02 systemd-timesyn
    165 root      20   0    4236   2560   2432 S   0.0   0.0   0:00.00 cron
    166 message+  20   0    9536   4864   4480 S   0.0   0.0   0:00.04 dbus-daemon
    179 root      20   0   18148   8320   7424 S   0.0   0.1   0:00.03 systemd-logind
    182 root      20   0 1756096  11776  10112 S   0.0   0.1   0:00.05 wsl-pro-service
    197 root      20   0    3160   1920   1792 S   0.0   0.0   0:00.00 agetty
    202 syslog    20   0  222508   5376   4352 S   0.0   0.0   0:00.03 rsyslogd
    205 root      20   0    3116   1792   1664 S   0.0   0.0   0:00.00 agetty
    211 root      20   0  107020  22528  13184 S   0.0   0.1   0:00.07 unattended-upgr
    301 root      20   0    3064    896    896 S   0.0   0.0   0:00.00 SessionLeader
    302 root      20   0    3080   1152   1024 S   0.0   0.0   0:00.01 Relay(303)
```

#### 2. ps
Process State의 약자.

현재 실행 중인 프로세스와 상태를 출력한다.

사용할 수 있는 옵션

* -e 또는 -A : 모든 프로세스 출력

* -f : 풀 포맷 출력

* -u <사용자> : 특정 사용자의 프로세스만 출력

* -x : 터미널 없이 실행 중인 프로세스까지 출력

* -o : 출력할 항목 지정

```bash
sdkurjnk@BOOK-P85075HF94:~$ ps
    PID TTY          TIME CMD
    303 pts/0    00:00:00 bash
    518 pts/0    00:00:00 top
    569 pts/0    00:00:00 ps
```

#### 3. jobs
실행 중인 백그라운드 프로세스를 출력한다.

사용할 수 있는 옵션

* -i : 프로젝트 ID와 함계 jobs 목록을 출력한다.

* -n : 마지막으로 알림 이후 변경된 jobs만 출력한다.

* -p : jobs의 프로세스 ID만 출력한다.

* -r : 실행 중인 jobs만 출력한다.

* -s : 중지된 jobs만 출력한다.

```bash
sdkurjnk@BOOK-P85075HF94:~$ jobs
[1]+  Stopped                 top
```

#### 4. kill
실행 중인 프로세스를 종료한다.

```bash
kill -9 12314
```
프로세스 12314를 강제종료
