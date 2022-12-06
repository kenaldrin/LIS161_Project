from flask import Flask
from data import pets

app = Flask(__name__)

@app.route('/')
def index():
    return """<h1>Adopt a Pet!</h1> 
                <p>Browse through the links below to find your new furry friend:</p>
                <ul>
                    <li><a href="/animals/dogs">Dogs</a></li>
                    <li><a href="/animals/cats">Cats</a></li>
                    <li><a href="/animals/rabbits">Rabbits</a></li>
                </ul>
    """

@app.route('/animals/<pet_type>')
def animals(pet_type): 
    html = "<h1>List of {}</h1>".format(pet_type)
   
    html += "<ul>"
    
    #Step 16: enumerate loop and turn list into a link
    for i, pet in enumerate(pets[pet_type]): 
        html += "<li><a href='/animals/{a}/{b}'>{c}</a></li>".format(a=pet_type, b=i, c=pet["name"])

    html += "</ul>"

    return html


#Step 13: Define function and route
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id] #Step 14: Access list in dictionary

    #Step 15: Return pet name
    #Step 17: Return pet img, description, breed, and age
    return f""" <h1>{pet['name']}</h1> 
                <img src={pet['url']} alt='alt text'>
                <p>{pet['description']}</p>
                <ul>
                    <li>{pet['breed']}</li>
                    <li>{pet['age']}</li>
                </ul>
    """


if __name__ == "__main__":
    app.run(debug=True)