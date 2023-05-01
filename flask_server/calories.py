from app import app, mongo

#ruta sa fie in functie de user id
@app.route('/calories', methods=['GET', 'POST'])
def test():
    return "Successful CONN"

if __name__ == "__main__":
    app.run(host="0.0.0.0")