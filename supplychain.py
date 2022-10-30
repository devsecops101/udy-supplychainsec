from lxml.etree import fromstring, XMLParser
import requests

parser = XMLParser(ns_clean=True, recover=True, encoding='utf-8')

response = requests.get('http://www.google.com')