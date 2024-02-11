#!/usr/bin/env python3
from mitmproxy import http



def response(packet):
    content_type = packet.response.headers.get("content-type", "")

    try:
         if "image" in content_type:
             url = packet.request.url
             extension = content_type.split("/")[-1]# split me quedo con el ultimo elemento de la lista
             if extension == "jpeg":
                 extension = "jpg"

         filename = f"images/{url.replace("/","_").replace(":","_")}.{extension}"
         image_data = packet.response.content
         with open(filename, "wb") as image:
             image.write(image_data)
             print(f"[+] Downloaded {url} to {filename}")      


    except:
        pass