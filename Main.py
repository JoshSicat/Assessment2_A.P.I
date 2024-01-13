import requests

response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')
cocktails = response.json() ['drinks'] [0]
print(cocktails)

#the names or type of drinks 
name = cocktails['strDrink']
glass = cocktails['strGlass']
alcohol = cocktails['strAlcoholic']
instructions = cocktails['strInstructions']

print(f"Name: {name}")
print(f"Glass: {glass}")
if alcohol == "Alcoholic":
    print(f"Alcoholic: Yes")
else:
    print(f"Alcoholic: No")
print(f"Intructions: {instructions}")

