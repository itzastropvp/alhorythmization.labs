def format_adress(city, street, house, apartment=None):
    if apartment == None:
     return f"м. {city}, вул. {street}, буд. {house}"
    else:
        return f"м. {city}, вул. {street}, буд. {house}, кв. {apartment}"
print(format_adress("Київ", "Хрещатик", "1", "24"))