from blogpost import app, db
from blogpost.models import User, Post

if __name__ == '__main__':
    app.run(debug=True)
