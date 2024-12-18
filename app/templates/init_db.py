from app import app, db
from app.models import Category, Recipe



def init_db():
    with app.app_context():
        db.create_all()

        if Category.query.count()== 0:
            categories = ["Entrées","Plats de principaux","Desserts", "Boissons"]

            for cat_name in categories:
                cat = Category(name=cat_name)
                db.session.add(cat)

            dessert_cat = Category(name="Desserts")
            db.session.add(dessert_cat)
            db.session.commit()

            test_recipe = Recipe(
                title ="Gâteau au chocolat", 
                description = 'Un délicieux gâteau au chocolat facile à faire',
                prep_time = 45,
                ingredients ="""200g de chocolat noir
                            200g de beurre
                            200g de sucre
                            4 oeufs
                            100g de farine""",
                instructions = """1. Préchauffer le four à 180 °C
                            2.Faire fondre le chocolat et le beurre""",
                category =dessert_cat,
            )
            db.session.add(test_recipe)
            db.session.commit()

            print('Base de donnée initialisée avec succès')
        else:
            print('les catégories existent déjà')
            