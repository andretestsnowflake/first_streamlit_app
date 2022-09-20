import streamlit
from pyvis.network import network
net=network(notebook=True)
net.from_nx(G)
net.show("example.html")
