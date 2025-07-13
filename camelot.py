import camelot

lattice_tables = camelot.read_pdf('eregli_rapor.pdf',pages='all',flavor='lattice',suppress_stdout=False)
stream_tables = camelot.read_pdf('eregli_rapor.pdf',pages='all',flavor='stream',suppress_stdout=False)

for table in lattice_tables:
    print('lattice_table')
    print(table.df)

for table in stream_tables:
    print('stream_tables')
    print(table.df)


