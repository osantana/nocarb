#!/usr/bin/env python


from __future__ import unicode_literals

import sys
import json

filename = sys.argv[1]
with open(filename) as f:
    products = json.load(f)

print "# No Carbs"

for product in products:
    print
    print "## {} - {}".format(product["name"], product["portion"])

    nutrients = product['nutrients']
    name_length = len(sorted(nutrients.keys(), key=len)[-1])
    value_length = len(sorted(nutrients.values(), key=len)[-1])

    row_template = "| {:%s} | {:%s} |" % (name_length, value_length)

    print
    print row_template.format("Nutrient", "Qty")
    print row_template.format("-" * name_length, "-" * value_length)

    carb = nutrients.pop('carboidratos', '0g')
    for nutrient in nutrients:
        print row_template.format(nutrient.title(), nutrients[nutrient])

    print
