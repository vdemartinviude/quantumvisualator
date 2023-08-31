import time
from rich.progress import Progress
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import IntPrompt
from rich.table import Table
import numpy as np


MdTitle = """
# Quantum RSA Key Break
## Comparando o tempo para quebra de chaves RSA entre computação clássica e quântica.
"""

console = Console()
console.clear()
md = Markdown(MdTitle)
console.print(md)
console.line()

bits = IntPrompt.ask("Informe o número de bits na chave")
n = 2**bits
nf = np.float128(n)
print ('Há {:,} possibilidades com {:,} bits'.format(n,bits))

classicaloperations = np.ceil(np.exp(np.power(np.log2(nf),1/3)*np.power(np.log2(np.log2(nf)),2/3)))
quantumoperations = np.ceil(np.power(np.log2(nf),3)*np.log2(np.log2(nf))*np.log2(np.log2(np.log2(nf))))

daysclassical = np.ceil(classicaloperations / 1000000 / 3600 / 24)
quantumdays = np.ceil(quantumoperations / 1000 / 3600 / 24)

console.line(1)

table = Table(title="Cálculo de complexidade")
table.add_column("Bits",justify="right")
table.add_column("Operações clássicas",justify="right")
table.add_column("Operações quânticas",justify="right")
table.add_column("Dias clássicos",justify="right")
table.add_column("Dias quânticos",justify="right")

table.add_row('{:,}'.format(bits),'{:,.0f}'.format(classicaloperations),'{:,.0f}'.format(quantumoperations),'{:,.0f}'.format(daysclassical),'{:,.0f}'.format(quantumdays))
console.print(table)

console.line(3)

with Progress() as progress:
    task1 = progress.add_task("[red]Classical Computing", total = daysclassical)
    task2 = progress.add_task("[cyan]Quantum Computing",total = quantumdays)
    while not progress.finished:
        progress.update(task1,advance=1)
        progress.update(task2,advance=1)
        time.sleep(1)

