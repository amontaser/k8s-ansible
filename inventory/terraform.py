#!/usr/bin/env python3
# inventory/terraform.py
import json
import subprocess

tf_output = subprocess.check_output(["terraform", "output", "-json"])
data = json.loads(tf_output)

inventory = {
    "load_balancer": {"hosts": [data["load_balancer_ip"]["value"]]},
    "masters": {"hosts": data["master_ips"]["value"]},
    "workers": {"hosts": data["worker_ips"]["value"]},
    "_meta": {"hostvars": {}}
}

print(json.dumps(inventory))