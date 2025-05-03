[load_balancer]
${lb_ip}

[masters]
%{ for ip in master_ips ~}
${ip}
%{ endfor ~}

[workers]
%{ for ip in worker_ips ~}
${ip}
%{ endfor ~}

[all:vars]
ansible_user=osadmin
ansible_ssh_private_key_file=../keys/admin_id_rsa