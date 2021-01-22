import json
import tabula
# from .models import Transactions
# from django.conf import settings

# filepath = settings.MEDIA_ROOT

data = tabula.read_pdf(
    "/home/mathew/project/japhweb/pdfsave/media/test.pdf", output_format="json", pages="all")
k = list()
for t in range(len(data)):
    h = [data[t]['data'][0][a]['text'] for a in range(10)]
    g = [[data[t]['data'][b][a]['text'] for b in range(1, 20)] for a in range(10)]
    d = {x: list(y) for x, y in zip(h, zip(g))}
    k.append(d)
print(type(k))
res = dict()
tr = []
for dict in k:
        for list in dict:
            if list in res:
                res[list] += (dict[list])
                tr.append(res)
            else:
                res[list] = dict[list]
                tr.append(res)

# tr = []

tr1 = {}
for dict in tr:
        for list in dict:
            if list in tr1:
                tr1[list] += (dict[list])
            else:
                tr1[list] = dict[list]

with open('kip.json', 'w') as file:
	json.dump(tr1, file)
