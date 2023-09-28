from random import randint, choice as rc
from faker import Faker
from app import app
from models import db, Game, Review, User

genres = [
    "Platformer", "Shooter", "Fighting", "Stealth", "Survival", "Rhythm", "Survival Horror", "Metroidvania", "Text-Based", "Visual Novel",
    "Tile-Matching", "Puzzle", "Action RPG", "MMORPG", "Tactical RPG", "JRPG", "Life Simulator", "Vehicle Simulator", "Tower Defense",
    "Turn-Based Strategy", "Racing", "Sports", "Party", "Trivia", "Sandbox"
]

platforms = [
    "PC", "PlayStation 5", "Xbox Series X", "Nintendo Switch", "PlayStation 4", "Xbox One", "Nintendo 3DS", "Wii U", "PlayStation Vita", "Xbox 360", "PlayStation 3",
]

fake = Faker()
fake.seed(12345)  # For reproducibility

with app.app_context():
    db.create_all()

    for _ in range(10):
        user = User(name=fake.name())
        db.session.add(user)

    for _ in range(50):
        game = Game(
            title=fake.unique.word().capitalize(),
            genre=rc(genres),
            platform=rc(platforms),
            price=randint(10, 60),
        )

        for _ in range(randint(0, 10)):
            review = Review(
                score=randint(1, 10),
                comment=fake.paragraph(),
                user=rc(User.query.all())
            )
            game.reviews.append(review)

        db.session.add(game)

    db.session.commit()
