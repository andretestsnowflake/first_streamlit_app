import networkx as nx
G=nx_from_pandas_edgelist(df,
                          source='Source',
                          target='Target',
                          edge_attr='weight')
