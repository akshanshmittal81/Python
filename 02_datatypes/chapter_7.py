masala_spices=("cardamom","cloves","cinamon")
(spice1,spice2,spice3)=masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio,cardamon_ratio = 2,1 
print(f"Ratio is G: {ginger_ratio} and C : {cardamon_ratio}" )
ginger_ratio , cardamon_ratio = cardamon_ratio , ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C : {cardamon_ratio}" )

# membership

print(f"Is ginger in masala spices ? {'ginger'in masala_spices}")
print(f"Is cinamon in masala spices ? {'cinamon'in masala_spices}")
