app = Flask(__name__)

#Model--------------------------------------------------------------------

class Utente(db.Model):
    id = db.Model(db.Integer, primary_key=True)
    nome = db.Model(db.String(80), nullable=False)
    email = db.Model(db.String(80), nullable=False)
    password = db.Model(db.String(80), nullable=False)
    cakeday = db.Model(db.Date, nullable=False)
    karma = db.Model(db.Integer, default=0)

class Post(db.Model):
    id = db.Model(db.Integer, primary_key=True)
    data = db.Model(db.Data, nullable=False)
    upvote = db.Model(db.Integer, default=0)
    idUtente = db.Model(db.Integer, db.foreignKey('Utente.id'), nullable=False)
    idSub = db.Model(db.Integer, db.foreignKey('Subrabbit.id'), nullable=False)
    utente = db.relationship('Utente')
    sub = db.relationship('Subrabbit')

class Immagine(db.Model):
    id = db.Model(db.Integer, primary_key=True)
    percorso = db.Model(db.String(80), nullable=False)
    tipo = db.Model(db.Enum('Post', 'Subrabbit', 'Avatar'), nullable=False)
    idPost = db.Model(db.Integer, db.foreignKey('Post.id'), nullable=False)
    idSub = db.Model(db.Integer, db.foreignKey('Subrabbit.id'), nullable=False)
    idAvatar = db.Model(db.Integer, db.foreignKey('Avatar.id'), nullable=False)
    post = db.relationship('Post')
    sub = db.relationship('Subrabbit')
    avatar = db.relationship('Avatar')

class Follow(db.Model):
    idUtente = db.Model(db.Integer, primary_key=True, db.foreignKey('Utente.id'), nullable=False)
    idSeguito = db.Model(db.Integer, primary_key=True, db.foreignKey('Utente.id'), nullable=False)
    data = db.Model(db.Data, nullable=False)
    utente1 = db.relationship('Utente')
    utente2 = db.relationship('Utente')

class Join(db.Model):
    idUtente = db.Model(db.Integer, primary_key=True, db.foreignKey('Utente.id'), nullable=False)
    idSub = db.Model(db.Integer, primary_key=True, db.foreignKey('Subrabbit.id'), nullable=False)
    data = db.Model(db.Data, nullable=False)
    utente = db.relationship('Utente')
    sub = db.relationship('Subrabbit')

class Subrabbit(db.Model):
    id = db.Model(db.Integer, primary_key=True)
    nome = db.Model(db.String(80), nullable=False)
    descrizione = db.Model(db.String(200), nullable=False)

class Avatar(db.Model):
    id = db.Model(db.Integer, primary_key=True)
    idUtente = db.Model(db.Integer, db.foreignKey('Utente.id'), nullable=False)
    utente = db.relationship('Utente')

#Control-----------------------------------------------------------------