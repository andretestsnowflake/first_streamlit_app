import networkx as nx
G=nx.from_pandas_edgelist(df,
                          source='Source',
                          target='Target',
                          edge_attr='weight')
