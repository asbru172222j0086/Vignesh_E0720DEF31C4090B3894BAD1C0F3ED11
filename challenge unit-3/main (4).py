def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices

products = ["smart watch", "Air pods", "mobile phone", "smart watch", "charger", "smart watch"]
target = "smart watch"
target2 = "apple"
result = linearSearchProduct(products, target)
print(result)                            