from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.app_context().push()

if __name__ == "__main__":
    app.run()