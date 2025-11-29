essential_spices={"cardamon","ginger","cinnamon"}
optional_spices={"cloves","ginger","black pepper"}


all_spices =essential_spices| optional_spices
print(f"All spices:{all_spices}")
comomon=essential_spices & optional_spices
print(f"common {comomon}")

only_in_essential=essential_spices-optional_spices
print(f"only in essential spices: {only_in_essential}")
print(optional_spices)
print(f"Is 'cloves' in essential  {'cloves'in optional_spices}" )
