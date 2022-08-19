""" AUTOMATICALLY COMMENTED OUT BY FaaSET 
@FaaSET.cloud_function(platform="AWS Docker Debian", config={"memory": 259})
"""

def yourFunction(request, context): 
    import subprocess, datetime, time

    from SAAF import Inspector
    inspector = Inspector()
    inspector.inspectAll()
    
#     command = "/var/task/llcbench/cachebench/cachebench -w -d1 -x1 -m20 -e1"

    command = "sleep 4m" 
#     command = "stdbuf -i0 -o0 -e0 /var/task/llcbench/cachebench/cachebench -w -d1 -x1 -m10 -e1 | ts '[%Y-%m-%d %H:%M:%.S]'"
    start_time = float(request['start_time'])
    print("start time is: {}".format(start_time))
    
    now = datetime.datetime.now().timestamp()
    if start_time >= now:
        time.sleep(start_time - now)
        
    output = subprocess.check_output(command.split()).decode('ascii')

#     inspector.addAttribute("cache_bench_metric", output)
    inspector.inspectAllDeltas()
    return inspector.finish()
