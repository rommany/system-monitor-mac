import psutil

from rich.table import Table
from rich.console import Console
from rich import box

console = Console()
table = Table(title='Partitions',box=box.MINIMAL)
table.add_column('device')
table.add_column('fstype')
table.add_column('mountpoint')


for p in psutil.disk_partitions():
    table.add_row(p.device,p.fstype,p.mountpoint)

#with console.capture() as cap:
console.print(table)
