soup = input('soup:')
meal = input('meal:')
vegan = ['vegetables','mushroom','mashed potatoes']
non_vegan = ['seafood','burger','grilled chicken']
if soup and meal in vegan:
    print('she loves vegetables')
elif soup and meal in non_vegan:
    print('she hates vegatables')
else:
    print('she neither hate nor love vegetables')