from . import recipes_blueprint
from flask import render_template, abort


breakfast_recipes_names = ['pancakes', 'acai_bowl', 'honey_bran_muffins', 'breakfast_scramble',
                           'pumpkin_donuts', 'waffles', 'omelette']
dinner_recipes_names = ['steak_fajitas', 'ground_beef_tacos', 'pizza', 'sweet_fire_chicken', 'tri_tip']
baked_goods_recipes_names = ['bagels', 'french_bread', 'pitas', 'irish_soda_bread']
side_dishes_recipes_names = ['sweet_potatoes', 'spanish_rice', 'jasmine_rice']
dessert_recipes_names = ['brownies', 'chocolate_chip_cookies', 'linzer_cookies', 'sugar_cookies']
smoothies_recipes_names = ['berry_smoothie', 'chocolate_milk_shake']


@recipes_blueprint.route('/')
def recipes():
    return render_template('recipes/recipes.html')


@recipes_blueprint.route('/breakfast/')
def breakfast_recipes():
    return render_template('recipes/breakfast.html')


@recipes_blueprint.route('/breakfast/<recipe_name>/')
def breakfast_recipe(recipe_name):
    if recipe_name not in breakfast_recipes_names:
        abort(404)

    return render_template(f'recipes/{recipe_name}.html')


@recipes_blueprint.route('/dinner/')
def dinner_recipes():
    return render_template('recipes/dinner.html')


@recipes_blueprint.route('/dinner/<recipe_name>/')
def dinner_recipe(recipe_name):
    if recipe_name not in dinner_recipes_names:
        abort(404)

    return render_template(f'recipes/{recipe_name}.html')


@recipes_blueprint.route('/baked_goods/')
def baked_goods_recipes():
    return render_template('recipes/baked_goods.html')


@recipes_blueprint.route('/baked_goods/<recipe_name>/')
def baked_goods_recipe(recipe_name):
    if recipe_name not in baked_goods_recipes_names:
        abort(404)

    return render_template(f'recipes/{recipe_name}.html')


@recipes_blueprint.route('/side_dishes/')
def side_dishes_recipes():
    return render_template('recipes/side_dishes.html')


@recipes_blueprint.route('/side_dishes/<recipe_name>/')
def side_dishes_recipe(recipe_name):
    if recipe_name not in side_dishes_recipes_names:
        abort(404)

    return render_template(f'recipes/{recipe_name}.html')


@recipes_blueprint.route('/dessert/')
def dessert_recipes():
    return render_template('recipes/dessert.html')


@recipes_blueprint.route('/dessert/<recipe_name>/')
def dessert_recipe(recipe_name):
    if recipe_name not in dessert_recipes_names:
        abort(404)

    return render_template(f'recipes/{recipe_name}.html')


@recipes_blueprint.route('/smoothies/')
def smoothies_recipes():
    return render_template('recipes/smoothies.html')


@recipes_blueprint.route('/smoothies/<recipe_name>/')
def smoothies_recipe(recipe_name):
    if recipe_name not in smoothies_recipes_names:
        abort(404)

    return render_template(f'recipes/{recipe_name}.html')
