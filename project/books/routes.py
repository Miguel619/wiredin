from . import books_blueprint
from flask import render_template, abort


torah = ['Genesis', 'Exodus', 'Leviticus', 'Numbers','Deuteronomy']
neviim = ['Joshua', 'Judges', 'Samuel', 'Kings', 'Isaiah' , 'Jeremiah', 'Ezekiel',
            'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah' , 'Nahum', 
            'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi']
baked_goods_recipes_names = ['bagels', 'french_bread', 'pitas', 'irish_soda_bread']
side_dishes_recipes_names = ['sweet_potatoes', 'spanish_rice', 'jasmine_rice']
dessert_recipes_names = ['brownies', 'chocolate_chip_cookies', 'linzer_cookies', 'sugar_cookies']
smoothies_recipes_names = ['berry_smoothie', 'chocolate_milk_shake']


@books_blueprint.route('/')
def books():
    return render_template('books/books.html')


@books_blueprint.route('/torah/')
def torah_books():
    return render_template('books/torah.html')


@books_blueprint.route('/torah/<book_name>/')
def torah_book(book_name):
    if book_name not in torah:
        abort(404)

    return render_template(f'torah/{book_name}.html')


@books_blueprint.route('/neviim/')
def neviim_books():
    return render_template('books/Neviim.html')


@books_blueprint.route('/neviim/<book_name>/')
def neviim_book(book_name):
    if book_name not in neviim:
        abort(404)

    return render_template(f'neviim/{book_name}.html')


@books_blueprint.route('/baked_goods/')
def baked_goods_recipes():
    return render_template('books/baked_goods.html')


@books_blueprint.route('/baked_goods/<book_name>/')
def baked_goods_recipe(book_name):
    if book_name not in baked_goods_recipes_names:
        abort(404)

    return render_template(f'books/{book_name}.html')


@books_blueprint.route('/side_dishes/')
def side_dishes_recipes():
    return render_template('books/side_dishes.html')


@books_blueprint.route('/side_dishes/<book_name>/')
def side_dishes_recipe(book_name):
    if book_name not in side_dishes_recipes_names:
        abort(404)

    return render_template(f'books/{book_name}.html')


@books_blueprint.route('/dessert/')
def dessert_recipes():
    return render_template('books/dessert.html')


@books_blueprint.route('/dessert/<book_name>/')
def dessert_recipe(book_name):
    if book_name not in dessert_recipes_names:
        abort(404)

    return render_template(f'books/{book_name}.html')


@books_blueprint.route('/smoothies/')
def smoothies_recipes():
    return render_template('books/smoothies.html')


@books_blueprint.route('/smoothies/<book_name>/')
def smoothies_recipe(book_name):
    if book_name not in smoothies_recipes_names:
        abort(404)

    return render_template(f'books/{book_name}.html')
