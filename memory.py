import psutil
from rich import print, repr, print_json

svmem = psutil.virtual_memory()
swap = psutil.swap_memory()

def get_size(val):
    return val/1024/1024/1024


def memory():
    vmem = {}
    vmem['total']=svmem.total
    vmem['available']=svmem.available
    vmem['used']=svmem.used
    vmem['percent']=svmem.percent
    vmem['wired']=svmem.wired
    vmem['free']=svmem.free
    vmem['inactive']=svmem.inactive

    smem = {}
    smem['total']=swap.total
    smem['used']=swap.used
    smem['percent']=swap.percent
    smem['free']=swap.free

    mem = {}
    mem['virtual'] = vmem
    mem['swap'] = smem
    
    return mem

print(memory())

