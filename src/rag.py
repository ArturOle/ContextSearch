from context_search import context_search

cs = context_search.ContextSearch()
cs.submit(["E:\DokumentyUstawy\D19970553Lj.pdf"])
print(cs.retrive('Młodociany przestępca', 5))
