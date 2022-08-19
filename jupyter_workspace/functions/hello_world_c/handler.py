""" AUTOMATICALLY COMMENTED OUT BY FaaSET 
@FaaSET.cloud_function(platform="AWS Docker Debian", config={"memory": 259})
"""

def yourFunction(request, context): 
    import subprocess

    from SAAF import Inspector
    inspector = Inspector()
    inspector.inspectAll()
    
    command = "./stream.10M"
    metric_outputs = list()
    for x in range(20):
        output = subprocess.check_output(command.split()).decode('ascii')
        data = output.split('\n')[23:27]
        metric = list(map(lambda i: list(map(float, i.split()[1:])), data))
        metric_outputs.append(metric)
    inspector.addAttribute("stream_metric", metric_outputs)
    inspector.inspectAllDeltas()
    return inspector.finish()
