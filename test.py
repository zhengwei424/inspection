#!/bin/env python
# _*_ coding: utf-8 _*_

import os
from kubernetes import client, config
import tokens
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from openpyxl import Workbook, load_workbook
import time


class GetAllSources(object):
    def __init__(self):
        pass

    def auth(self, mode, kubeconfig_file=None, **kwargs):
        if mode is 'kubeconfig':
            if os.path.isfile(kubeconfig_file):
                config.load_kube_config(config_file=kubeconfig_file)
        elif mode is 'token':
            if isinstance(kwargs.get('kwargs').get('token'), str):
                configuration = client.Configuration()
                configuration.host = kwargs.get('kwargs').get('host')
                configuration.api_key = {'authorization': 'Bearer ' + kwargs.get('kwargs').get('token')}
                configuration.verify_ssl = False
                client.Configuration.set_default(configuration)
                # 禁用安全请求警告
                disable_warnings(InsecureRequestWarning)
        else:
            print("Please set the authentication mode: kubeconfig or token")


test = GetAllSources()
# test.auth(mode='kubeconfig', kubeconfig_file='config')
test.auth(mode='token', kwargs=tokens.production_envs[0])

# 创建v1对象
v1 = client.CoreV1Api()
# 创建apps/v1对象
rs1 = client.AppsV1beta1Api()
# 创建extensions/v1对象
rs2 = client.ExtensionsV1beta1Api()

# 创建batch/v1对象
rs3 = client.BatchV1Api()

# 创建batch/v1beta1对象
rs4 = client.BatchV1beta1Api()

# 获取node节点数
nodes_num = len(v1.list_node().items)
# 获取pod数量
pods_num = len(v1.list_pod_for_all_namespaces().items)
# 获取service数量
svc_num = len(v1.list_service_for_all_namespaces().items)
# 获取configmap数量
cm_num = len(v1.list_config_map_for_all_namespaces().items)

# 获取secret数量
secret_num = len(v1.list_secret_for_all_namespaces().items)

# 获取statefuSet数量
statefulset_num = len(rs1.list_stateful_set_for_all_namespaces().items)

# 获取deployment数量
deploy_num = len(rs2.list_deployment_for_all_namespaces().items)

# 获取daemonSet数量
ds_num = len(rs2.list_daemon_set_for_all_namespaces().items)

# 获取replicationController数量
rc_num = len(v1.list_replication_controller_for_all_namespaces().items)

# 获取replicationSet数量
rs_num = len(rs2.list_replica_set_for_all_namespaces().items)

# 获取Job数量
job_num = len(rs3.list_job_for_all_namespaces().items)

# 获取CronJob数量
cronjob_num = len(rs4.list_cron_job_for_all_namespaces().items)

# 控制器总数
total_num = cronjob_num + job_num + deploy_num + ds_num + statefulset_num + rc_num + rs_num

# for pod in v1.list_pod_for_all_namespaces().items:
#     if pod.metadata.name == "pi-85hhr":
#         print(pod)

event = v1.list_event_for_all_namespaces().items[0]

pods = []
pod_events = [{'name': '', 'events': []}, ]

for event in v1.list_event_for_all_namespaces().items:
    if event.involved_object.kind == 'Pod':
        if event.involved_object.name not in pods:
            pods.append(event.involved_object.name)

for i in range(len(pods)):
    pod_events[i]['name'] = pods[i]
    print(type(pod_events[i]['events']))
    # for event in v1.list_event_for_all_namespaces().items:
    #     a = []
    #     if event.involved_object.kind == 'Pod' and event.involved_object.name == pods[i]:
    #         a.append(event.message)
    # pod_events[i]['events'] = a
# if event.involved_object.name in pods:
#     pod_events[index]['name'] = event.involved_object.name
#     pod_events[index]['events'].append(event.message)

print(pods)
print(pod_events)

# if __name__ == '__main__':
#     # 加载现有excel文件（必须是xlsx后缀）
#     path = "C:\\Users\\Administrator\\Desktop\\test.xlsx"
#     book = load_workbook(path)
#
#     # 获取所有sheet名称
#     print(book.get_sheet_names())
#
#     # 激活某个sheet(获取该sheet的index，然后将index赋值给active)
#     sheet1 = book.get_sheet_by_name("5月19日")
#     book.active = book.get_index(sheet1)
#     # 打印当前的活动的sheet
#     print(book.active)
#
#     # 复制sheet
#     book.copy_worksheet(book.active)
#     active_sheet = book.active
#
#
#     # 向单元格中写入数据并保存
#     active_sheet['D6'] = "测试"
#     active_sheet['B16'] = "19:00  测试  问题：打法胜多负少发送给\n顶格换行\n  换行空两格（中文换行）"
#     book.save(path)
