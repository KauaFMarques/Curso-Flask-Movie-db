import urllib.request, json

url="https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=44271fcf35be9f198059a3ece4aa58ce"

resposta=urllib.request.urlopen(url)

dados=resposta.read()

jsondata=json.loads(dados)

print(jsondata['results'])