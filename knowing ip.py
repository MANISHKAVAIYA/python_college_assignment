from urllib.request import urlopen
import re


url = "http://checkip.dyndns.com/"
response = urlopen(url)
data = response.read().decode("utf-8")

ip_pattern = re.compile(r"(\d{1,3}\.){3}\d{1,3}")
ip_address = ip_pattern.search(data).group()


print(ip_address)
