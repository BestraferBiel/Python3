#!/usr/bin/env python3
import requests



response = requests.get("https://httpbin.org/basic-auth/foo/bar",auth=("foo","bar"))
print(response.status_code)
print(response.content)


#otro ejemplo
cokies = {"sesion_id":"123456789"}
response = requests.get("https://httpbin.org/cookies",cookies=cokies)

print(response.content)


#otro ejemplo con envio de archivos

url = "https://httpbin.org/post"
files = {"file":open("D:\Python3\Curso_Python3.0\lista.txt","rb")}
response = requests.post(url,files=files)
print(response.content)

#como arrastar una cookie de una pagina a otra usando request y session

s = requests.Session()
repuesta = s.get("https://httpbin.org/cookies/set/sessioncookie/123456789")
resuesta = s.get("https://httpbin.org/cookies")
print(repuesta.content)
print(repuesta.text) #imprime el contenido de la pagina

#ejemplo para obtener el historial de urls visitadas
s = requests.Session()  
s.get("https://github.com")

response = s.get("http://github.com")  
 
for request in response.history:
    print(request.url)