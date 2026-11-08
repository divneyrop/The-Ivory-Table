from django.shortcuts import render

CATEGORIES = [
    {
        'name': 'Africa',
        'tagline': 'Swahili coast and East African spice',
        'items': [
            {'course': 'Starter', 'name': 'Spiced Beef Croquettes', 'price': '1,100',
             'image': 'Spiced-Beef-Croquettes.jpg',
             'description': 'Crisp golden croquettes of slow-cooked beef scented with berbere, served with a rich dark sauce.',
             'ingredients': ['Minced beef', 'Potato', 'Onion', 'Garlic', 'Berbere spice', 'Breadcrumbs', 'Egg', 'Pickled beetroot'],
             'tags': ['Spicy']},
            {'course': 'Main', 'name': 'Swahili Coconut Prawn Curry', 'price': '2,900',
             'image': 'Swahili Coconut Prawn Curry.jpg',
             'description': 'Prawns simmered in coconut milk with turmeric and chilli, served with steamed rice and crispy onions.',
             'ingredients': ['Prawns', 'Coconut milk', 'Tomato', 'Ginger', 'Garlic', 'Turmeric', 'Curry leaves', 'Chilli', 'Lime', 'Coriander', 'Rice'],
             'tags': ['Gluten-free']},
        ],
    },
    {
        'name': 'Asia',
        'tagline': 'Thai, Indian and Southeast Asian flavours',
        'items': [
            {'course': 'Starter', 'name': 'Coconut-Chilli Prawns', 'price': '1,300',
             'image': 'Coconut-Chilli-Prawns.jpg',
             'description': 'Crisp coconut-crusted prawns on skewers, served over a golden squash purée.',
             'ingredients': ['Prawns', 'Coconut flakes', 'Breadcrumbs', 'Red chilli', 'Butternut squash', 'Garlic', 'Edible flowers'],
             'tags': ['Spicy']},
            {'course': 'Main', 'name': 'Roasted Cauliflower Steak', 'price': '1,900',
             'image': 'Roasted Cauliflower Steak.jpg',
             'description': 'Charred cauliflower steaks on red pepper sauce with a fresh herb sauce and pomegranate.',
             'ingredients': ['Cauliflower', 'Roasted red pepper', 'Parsley', 'Coriander', 'Garlic', 'Lemon', 'Olive oil', 'Pomegranate'],
             'tags': ['Vegan', 'Gluten-free']},
        ],
    },
    {
        'name': 'Europe',
        'tagline': 'Italian and French classics',
        'items': [
            {'course': 'Starter', 'name': 'Heirloom Tomato & Burrata', 'price': '1,400',
             'image': 'Heirloom-Tomato&Burrata.jpg',
             'description': 'Colourful heirloom tomatoes around creamy burrata, finished with basil and olive oil.',
             'ingredients': ['Heirloom tomatoes', 'Burrata', 'Basil', 'Olive oil', 'Balsamic vinegar', 'Sea salt', 'Black pepper'],
             'tags': ['Vegetarian', 'Gluten-free']},
            {'course': 'Main', 'name': 'Wild Mushroom Risotto', 'price': '2,200',
             'image': 'Wild Mushroom Risotto.jpg',
             'description': 'Creamy risotto topped with wild mushrooms, shaved parmesan and edible flowers.',
             'ingredients': ['Arborio rice', 'Wild mushrooms', 'Parmesan', 'White wine', 'Shallot', 'Butter', 'Vegetable stock', 'Edible flowers'],
             'tags': ['Vegetarian', 'Gluten-free']},
        ],
    },
    {
        'name': 'Oceania',
        'tagline': 'Australia and New Zealand',
        'items': [
            {'course': 'Main', 'name': 'Slow-Braised Lamb Shank', 'price': '3,200',
             'image': 'Slow-Braised Lamb Shank.jpg',
             'description': 'Lamb shank braised for hours in red wine and rosemary, served on creamy mash.',
             'ingredients': ['Lamb shank', 'Red wine', 'Rosemary', 'Thyme', 'Garlic', 'Onion', 'Potato', 'Cream'],
             'tags': ['Gluten-free']},
            {'course': 'Dessert', 'name': 'Mango & Passion Pavlova', 'price': '950',
             'image': 'Mango & Passion Pavlova.jpg',
             'description': 'A crisp meringue nest with whipped cream, mango, kiwi and passion fruit.',
             'ingredients': ['Egg whites', 'Caster sugar', 'Cornflour', 'Cream', 'Mango', 'Kiwi', 'Passion fruit'],
             'tags': ['Vegetarian', 'Gluten-free']},
        ],
    },
    {
        'name': 'South America',
        'tagline': 'Argentina, Peru and Brazil',
        'items': [
            {'course': 'Main', 'name': 'Charcoal-Grilled Beef Fillet', 'price': '3,400',
             'image': 'Charcoal-Grilled Beef Fillet.jpg',
             'description': 'Beef fillet grilled over charcoal, served on creamy mash with a dark berry sauce.',
             'ingredients': ['Beef fillet', 'Potato', 'Butter', 'Cream', 'Blackcurrant', 'Red wine', 'Micro herbs', 'Sea salt'],
             'tags': ['Gluten-free']},
            {'course': 'Dessert', 'name': 'Dark Chocolate Fondant', 'price': '1,000',
             'image': 'Dark Chocolate Fondant.jpg',
             'description': 'A warm Brazilian-cacao chocolate cake with a molten centre, vanilla ice cream and a caramel tuile.',
             'ingredients': ['Dark chocolate', 'Butter', 'Eggs', 'Sugar', 'Flour', 'Vanilla ice cream', 'Berry coulis'],
             'tags': ['Vegetarian']},
        ],
    },
    {
        'name': 'North America',
        'tagline': 'Pacific coast and American classics',
        'items': [
            {'course': 'Main', 'name': 'Pan-Seared Salmon', 'price': '2,800',
             'image': 'Pan-Seared Salmon.jpg',
             'description': 'Crisp-skinned salmon with grilled asparagus, roasted tomato and charred lemon.',
             'ingredients': ['Salmon fillet', 'Asparagus', 'Tomato', 'Lemon', 'Olive oil', 'Micro herbs', 'Sea salt'],
             'tags': ['Gluten-free']},
            {'course': 'Dessert', 'name': 'Coffee Crème Brûlée', 'price': '950',
             'image': 'Kenyan Coffee Crème Brûlée.jpg',
             'description': 'Silky coffee custard under a crackling caramel crust, with ice cream and a caramel tuile.',
             'ingredients': ['Double cream', 'Egg yolks', 'Coffee', 'Sugar', 'Vanilla', 'Biscuit crumb'],
             'tags': ['Vegetarian']},
        ],
    },
]


def menu(request):
    return render(request, 'menu.html', {'categories': CATEGORIES})