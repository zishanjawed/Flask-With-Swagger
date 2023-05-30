from flask import  render_template



# """
#     creating the application instance using Connexion rather than Flask. 
#     Internally, the Flask app is still created, but it now has additional functionality added to it.
# """
# app = connexion.App(__name__, specification_dir="./")
# """
#     app instance creation includes the parameter specification_dir in line 9.
#     This tells Connexion which directory to look in for its configuration file.
#      In this case, it’s the same directory that you run app.py from
# """
# app.add_api("swagger.yml")


import config
from models import Person

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)