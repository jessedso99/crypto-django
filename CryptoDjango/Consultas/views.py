from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests as rqts

def home(request):
  print('testeee2')
#   # data = {}
#   # data['transacoes'] = ['t1', 't2', 't3']
#   # data['now']= datetime.datetime.now()
#   # return render(request, 'Consultas/home.html', data)
#   data = {}
#   data['username'] = request.GET['username']
#   return render(request, 'Consultas/home.html', data) #{'username': username}
  return render(request, 'Consultas/home.html') #{'username': username}


def home_0(request):
  now= datetime.datetime.now()
  html= "<html><body>Agora é %s</html></body>" %now
  return HttpResponse(html)

def some_view(request):
  vars1= {}
  vars1["tokens1"]= []
  vars1["tokensTop10"]= []
  
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map?CMC_PRO_API_KEY=af649c3a-de4f-43e4-86ad-f802c0dc6e5d&listing_status=active&sort=cmc_rank'#&limit=100'
  response = rqts.get(url) 
  list_tokenMap = response.json().get("data")#.get("BTC").keys())#.get("BTC").get("name"))
  vars1["x"]=1
  for i in list_tokenMap:
    vars1["tokens1"].append(i["symbol"])

  vars1["tokensTop10"]= vars1["tokens1"][0:10]
  return render(request, 'Consultas/home.html', vars1)

def teste2(request):
  data = {}
  data["y"]= request.POST['tecnologias']
  if data["y"] == "":
    data["y"] = "BTC"
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?CMC_PRO_API_KEY=af649c3a-de4f-43e4-86ad-f802c0dc6e5d&symbol=%s' %data["y"]
  response = rqts.get(url) 
  data["x"]= round(response.json().get("data").get(data["y"]).get('quote').get('USD').get('price'), 4)
  data["z"]= response.json().get("data").get(data["y"]).get("name")

  url_logo_desc = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?CMC_PRO_API_KEY=af649c3a-de4f-43e4-86ad-f802c0dc6e5d&symbol=%s' %data["y"]
  response = rqts.get(url_logo_desc) 
  data["logo"]= (response.json().get("data").get(data["y"]))[0]["logo"]
  data["desc"]= (response.json().get("data").get(data["y"]))[0]["description"]

  data['now']= datetime.datetime.now()

  #html= "<html><body>Sua mensagem: %s</html></body>" %y
  #return HttpResponse(html)
  return render(request, 'Consultas/result.html', data)
