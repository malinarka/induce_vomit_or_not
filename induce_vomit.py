# Ett program som ska hjälpa kliniker eller djurägare att avgöra om en hund 
# behöver kräkas då den ätit choklad.

print("Choklad innehåller substansen teobromin som är giftig för hund.")
print("Vit choklad innehåller väldigt lite eller ingen teobromin alls. Mjölkchoklad innehåller ca 2 mg teobromin per gram choklad. Mörk choklad innehåller ca 5-15 mg teobromin per gram choklad. Kliniska symtom kan uppkomma då hunden har ätit mer än 20 mg teobromin per kg kroppsvikt. En hund som ätit stora mängder vit choklad kan bli sjuk av andra orsaker än teobrominförgiftning.")
print("Nedan fyller du i din hunds storlek och ungefär hur mycket choklad den fått i sig.")

hundens_vikt = float(input("Hundens vikt i kg: "))

mängd_vit_choklad = float(input("Mängd vit choklad i gram: "))
mängd_mjölkchoklad = float(input("Mängd mjölkchoklad i gram: "))
mängd_mörk_choklad = float(input("Mängd mörk choklad i gram: ")) 

teobromin_vit_choklad = 0
teobromin_mjölkchoklad = mängd_mjölkchoklad * 2
teobromin_mörk_choklad = mängd_mörk_choklad * 15

total_teobromin = teobromin_vit_choklad + teobromin_mjölkchoklad + teobromin_mörk_choklad

toxisk_dos = hundens_vikt * 20

if total_teobromin < toxisk_dos:
    print("Hunden behöver inte åka till veterinären för att framkalla kräkning men man bör ändå hålla koll på om hunden får symtom på förgiftning.")
elif total_teobromin >= toxisk_dos:
    print("Kontakta veterinär för att framkalla kräkning så fort som möjligt.")

print("Symtom på chokladförgiftning: Kommer som regel efter 4-24 timmar. Kräkningar, buksmärtor, törst, inkontinens, skakighet, rastlöshet, riklig saliverig och hjärtklappning är vanligt. Vid större mängder kan allvarligare symptom eller dödsfall inträffa.")

