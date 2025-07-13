import tabula
import  pandas as pd

tables = tabula.read_pdf(
    'eregli_rapor.pdf',
    pages='all',
    multiple_tables=True,
    lattice=True,
    stream=True,
    guess=True,
    pandas_options={'header': None}
)

for table in tables:
    print(table)