#!/bin/env python
# _*_ coding: utf-8 _*_

from kubernetes import client, config
from openpyxl import Workbook, load_workbook
import time

config.load_kube_config(config_file="d:/python_projects/inspection/config")

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

# event = v1.list_event_for_all_namespaces().items[0]
print(v1.list_event_for_all_namespaces().items)

#   config_dict=yaml.load(f),
# Traceback (most recent call last):
#   File "D:/python_projects/inspection/test.py", line 65, in <module>
#     print(v1.list_event_for_all_namespaces().items[0])
# IndexError: list index out of range


# if __name__ == '__main__':
    # # 加载现有excel文件（必须是xlsx后缀）
    # path = "C:\\Users\\Administrator\\Desktop\\test.xlsx"
    # book = load_workbook(path)
    #
    # # 获取所有sheet名称
    # print(book.get_sheet_names())

    # # 激活某个sheet(获取该sheet的index，然后将index赋值给active)
    # sheet1 = book.get_sheet_by_name("5月19日")
    # book.active = book.get_index(sheet1)
    # 打印当前的活动的sheet
    # print(book.active)

    # 复制sheet
    # book.copy_worksheet(book.active)
    # active_sheet = book.active


    # # 向单元格中写入数据并保存
    # active_sheet['D6'] = "测试"
    # active_sheet['B16'] = "19:00  测试  问题：打法胜多负少发送给\n顶格换行\n  换行空两格（中文换行）"
    # book.save(path)