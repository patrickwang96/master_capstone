
 # faketty () {
 #     script -qefc "$(printf "%q " "$@")" /dev/null
 # }
 # faketty /var/task/llcbench/cachebench/cachebench -w -d1 -x1 -m10 -e1 |ts '[%Y-%m-%d %H:%M:%.S]'
 # stdbuf -i0 -o0 -e0 /var/task/llcbench/cachebench/cachebench -w -d5 -x1 -m32 -e1 | ts '[%Y-%m-%d %H:%M:%.S]'
 # stdbuf -i0 -o0 -e0 /var/task/llcbench/cachebench/cachebench -w -d5 -x1 -m32 -e1 | ts '[%Y-%m-%d %H:%M:%.S]'
 stdbuf -i0 -o0 -e0 /var/task/llcbench/cachebench/cachebench -w -d5 -x1 -m31 -e1 | ts '[%Y-%m-%d %H:%M:%.S]'
 # stdbuf -i0 -o0 -e0 /var/task/llcbench/cachebench/cachebench -w -d1 -x1 -m10 -e1 | ts '[%Y-%m-%d %H:%M:%.S]'
