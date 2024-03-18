from random import choice as rc

from faker import Faker

from app import app
from models import db, Author, Post

fake = Faker()

with app.app_context():
    Author.query.delete()
    Post.query.delete()

    used_names = set()  # Keep track of used names

    authors = []
    for n in range(25):
        while True:
            name = fake.name()
            if name not in used_names:  # Check if the name is unique
                used_names.add(name)  # Add the name to the set of used names
                break
        author = Author(name=name, phone_number='1324543333')
        authors.append(author)

    db.session.add_all(authors)

    posts = []
    for n in range(25):
        post = Post(title='Secret banana', content='This is the content Secret' * 50, category='Fiction',
                    summary="Summary Secret")
        posts.append(post)

    db.session.add_all(posts)

    db.session.commit()
