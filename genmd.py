#!/usr/bin/env python
# coding: utf-8


import sys
import json
import codecs

filename = sys.argv[1]
with codecs.open(filename, "r", "utf-8") as f:
    products = json.load(f)

title_template = "### {} - {}"

print "# Sem Carboidrato"
print
print "## Índice"

print
for product in sorted(products, key=lambda p: p['name']):
    title = title_template.format(product["name"].encode("utf-8"), product["portion"].encode("utf-8"))
    slug = title.lower().replace("#", "").strip().replace(" ", "-").replace("%", "")
    print "* [{}](#{})".format(product["name"].encode("utf-8"), slug)

print
print "## Produtos"

for product in sorted(products, key=lambda p: p['name']):
    print
    print "### {} - {}".format(product["name"].encode("utf-8"), product["portion"].encode("utf-8"))

    nutrients = product['nutrients']
    name_length = len(sorted(nutrients.keys(), key=len)[-1]) + 8  # bold markup for carb
    value_length = len(sorted(nutrients.values(), key=len)[-1]) + 8

    row_template = "| {:%s} | {:%s} |" % (name_length, value_length)

    print
    print row_template.format(u"Nutriente", u"Qtd")
    print row_template.format(u"-" * name_length, u"-" * value_length)

    carb = nutrients.pop('carboidratos', '0g')
    print row_template.format('**Carboidrato**', "**{}**".format(carb))

    for nutrient in sorted(nutrients):
        print row_template.format(nutrient.title().encode("utf-8"), nutrients[nutrient].encode("utf-8"))

    print
