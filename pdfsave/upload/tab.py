import json
import tabula
from .models import Transactions, Upload
# from .models import Transactions
from django.conf import settings

filepath = settings.MEDIA_ROOT


# k = list()
def savetodb():
    data = tabula.read_pdf(filepath + "/data.pdf", output_format="json", pages="all")
    if Transactions.objects.filter(ReceiptNo=data[0]['data'][1][0]['text']):
            print("Breaking")
            Upload.objects.all().delete()
            return False
    for t in range(len(data)):
        
            
        h = [data[t]['data'][0][a]['text'] for a in range(10)]
        # print(Transactions.objects.filter(ReceiptNo=data[0]['data'][1][0]['text']))
        g = [[data[t]['data'][b][a]['text'] for b in range(1, len(data[t]['data']))] for a in range(len(data[t]['data'][0]))]
        d = {x: list(y) for x, y in zip(h, zip(g))}
        print("here")
        try:
            for a in range(len(d['Receipt No.'][0])):
                Transactions.objects.create(
                    ReceiptNo = d['Receipt No.'][0][a],
                    CompletionTime = d['Completion\rTime'][0][a],
                    Details = d['Details'][0][a],
                    PaidIn = d['Paid In'][0][a],
                    Withdrawn = d['Withdrawn'][0][a],
                    Balance = d['Balance'][0][a]
                )
                Upload.objects.all().delete()
            

        except Exception as t:
            print(t)
            return False
    return True
#     k.append(d)
# print(type(k))
# res = dict()
# tr = []
# for dict in k:
#         for list in dict:
#             if list in res:
#                 res[list] += (dict[list])
#                 tr.append(res)
#             else:
#                 res[list] = dict[list]
#                 tr.append(res)

# # tr = []

# tr1 = {}
# for dict in tr:
#         for list in dict:
#             if list in tr1:
#                 tr1[list] += (dict[list])
#             else:
#                 tr1[list] = dict[list]