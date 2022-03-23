import psutil
from rich import print, repr, print_json
# let's print CPU information
print("="*10, "CPU Info", "="*10)
def get_processor():

    proc = {}

    proc['Physical cores']= psutil.cpu_count(logical=False)
    proc['Total cores']= psutil.cpu_count(logical=True)

    cpufreq = psutil.cpu_freq()

    proc['Max Frequency']= f'{cpufreq.max:.2f}Mhz'
    proc['Min Frequency']= f'{cpufreq.min:.2f}Mhz'
    proc['Current Frequency']= f'{cpufreq.current:.2f}Mhz'

    proc['cores']=[]

    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        proc['cores'].append(percentage)

    proc['Total Usage']= f'{psutil.cpu_percent()}%'
    
    return proc


print(get_processor())
#print(core_usage)

#print(f"Total CPU Usage: {psutil.cpu_percent()}%")