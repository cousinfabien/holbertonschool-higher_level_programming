#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Rendu de la page d'accueil."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Rendu de la page à propos."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Rendu de la page de contact."""
    return render_template('contact.html')

if __name__ == '__main__':
    # On lance le serveur sur le port 5000 avec le mode debug activé
    app.run(debug=True, port=5000)
