import re
import os
import operator
import subprocess

k_free_mem = 0
k_free_cores = 1
k_used_cores = 2

k_node = 0
k_max = 3
k_njobs = 4
k_mem = 11

mem_free_dict = {}
result_dict = {}


def beginBlock(text):
    print("{:-^30}".format(text))


def endBlock():
    print()


def error(text):
    print()
    print("-" * 40)
    print("{:^40}".format(text))
    print("-" * 40)


def balance(need_memory):
    with open("/home/alex/tmp_file", "r") as f:
        out_1 = f.read()
    with open("/home/alex/tmp_file2", "r") as f:
        out_2 = f.read()

    lsload_result = re.sub(' +', ' ', out_1).split("\n")[1:-1]
    bhosts_result = re.sub(' +', ' ', out_2).split("\n")[1:-1]
    for line in lsload_result:
        if not any(deprecated in line for deprecated in ["unavail", "bmk-x"]):
            splitted = re.sub(' +', ' ', line).replace("\n", "").split(" ")
            mem_free_dict[splitted[k_node]] = float(splitted[k_mem].replace("G", ""))
    for line in bhosts_result:
        if not any(deprecated in line for deprecated in ["unavail", "bmk-x"]):
            splitted = re.sub(' +', ' ', line).replace("\n", "").split(" ")
            if int(splitted[k_max]) - int(splitted[k_njobs]):
                mem_free_dict[ splitted[k_node] ] = [ mem_free_dict[ splitted[k_node] ],
                                                      int(splitted[k_max]) - int(splitted[k_njobs]),
                                                      int(splitted[k_max]) - int(splitted[k_njobs])
                                                      ]
            else:
                del( mem_free_dict[ splitted[k_node] ] )

    sum_cores = sum(elems[1] for k, elems in mem_free_dict.items())
    sum_mem = sum(elems[0] for k, elems in mem_free_dict.items())
    gb_per_core = need_memory / sum_cores

    beginBlock("Information")
    print("Total free CPU (cores): {}".format(sum_cores))
    print("Total free RAM (GB)   : {:.2f}".format(sum_mem))
    print("Necessary RAM (GB)    : {:.2f}".format(need_memory))
    if sum_mem <= need_memory:
        print("Status:")
        error("Not enough memory")
        return
    else:
        print("OK")
    endBlock()

    corrected = True
    while corrected:
        corrected = False
        gb_per_core = need_memory / sum(elems[k_used_cores] for k, elems in mem_free_dict.items())
        for k, v in sorted(mem_free_dict.items(), key=lambda x: (x[1][1], x[1][0])):
            node_info = mem_free_dict[k]
            if node_info[k_used_cores] * gb_per_core >= node_info[k_free_mem]:
                node_info[k_used_cores] -= 1
                corrected = True
        if sum(elems[k_used_cores] for k, elems in mem_free_dict.items()) < 25:
            error("Too small cores")
            return

    beginBlock("After balancing")
    print("GB per MPI: {:.2f} \n".format(gb_per_core))
    print("{:23} {:<9} {:<9} {:<9} {:<9}".format("Node", "Free MEM", "Used MEM", "Free CPU", "Used CPU"))
    for k,v in sorted(mem_free_dict.items(), key=lambda x: (x[1][2], x[1][0])):
        print("{:23} {:<9.2f} {:<9.2f} {:<9} {:<9}".format(k,
                                                           v[k_free_mem],
                                                           v[k_used_cores] * gb_per_core,
                                                           v[k_free_cores],
                                                           v[k_used_cores]))
    endBlock()
    total_cores_used = sum(elems[k_used_cores] for k, elems in mem_free_dict.items())
    print(total_cores_used)

balance(467.6)
