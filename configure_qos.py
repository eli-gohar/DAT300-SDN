#!/bin/bash
# Author: Aitor Martin Rodriguez (University of Stavanger)

# Usage:
# ./configure_qos.sh <interface_name> <total_link_bandwidth > <q0_minrate> <q0_maxrate> <q1_minrate> <q1_maxrate> 

import sys, os

if len(sys.argv) != 7:
    print("Usage:\n ./configure_qos.sh <interface_name> <total_link_bandwidth> <q0_minrate> <q0_maxrate> <q1_minrate> <q1_maxrate>")
    print("Bandwidth and queue rate values must be given in Mbit/s")
else:
    interface_name = sys.argv[1]
    bandwidth = float(sys.argv[2])
    q0_minrate = float(sys.argv[3])
    q0_maxrate = float(sys.argv[4])
    q1_minrate = float(sys.argv[5])
    q1_maxrate = float(sys.argv[6])

    if interface_name != "":
        command = "sudo ovs-vsctl -- set Port %s qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=%s queues=0=@q0,1=@q1 -- --id=@q0 create Queue other-config:min-rate=%s other-config:max-rate=%s -- --id=@q1 create Queue other-config:min-rate=%s other-config:max-rate=%s" %(interface_name, int(bandwidth*1e6), int(q0_minrate*1e6), int(q0_maxrate*1e6), int(q1_minrate*1e6), int(q1_maxrate*1e6))
        ret = os.system(command)
        if ret == 0:
            print("QoS configuration applied to interface %s" % interface_name)
            print(f"Total Link Bandwidth: {bandwidth:.0f} Mbps")
            print(f"Queue 0 Min Rate: {q0_minrate:.0f} Mbps")
            print(f"Queue 0 Max Rate: {q0_maxrate:.0f} Mbps")
            print(f"Queue 1 Min Rate: {q1_minrate:.0f} Mbps")
            print(f"Queue 1 Max Rate: {q1_maxrate:.0f} Mbps")
        else:
            print("Error applying queue configuration. Please verify that the interface name is valid.")
            print("You can run \"ip link show\" to see the list of interfaces.")
    else:
        print("Please write a valid interface name")