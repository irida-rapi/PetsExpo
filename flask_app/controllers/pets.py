from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.pet import Pet
from flask_app.models.user import User
from flask import flash

@app.route("/pets/new")
def fill_pet_form():
    if 'user_id' not in session:
        return redirect("/logOut")
    data = {
            'user_id': session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template("newPet.html", loggedUser = user)

@app.route('/create_pet', methods=['POST'])
def createPet():
    if 'user_id' not in session:
        return redirect('/logOut')

    if not Pet.validate_pet(request.form):
        flash('Something went wrong!', 'newPet')
        return redirect(request.referrer)

    data = {
        'name' : request.form['name'],
        'origin' : request.form['origin'],
        'type' : request.form['type'],
        'user_id' : session['user_id']
    }
    Pet.create_pet(data)
    return redirect('/dashboard')

@app.route('/pets/<int:id>')
def display_each_pet(id):
    if 'user_id' not in session:
        return redirect('/logOut')
    data = {
        'pet_id' : id,
        'user_id' : session['user_id']
    }
    pet = Pet.get_pet_by_id(data)
    user = User.get_user_by_id(data)
    users = Pet.get_all_pet_info(data)
    if not session['user_id'] == pet['user_id']:
        return render_template("petViewer.html", pets = pet, loggedUser = user, users = users)
    return render_template("pet.html", pets = pet, loggedUser = user, users = users)

@app.route('/update_pet/<int:id>', methods=['POST'])
def update_pet(id):
    if 'user_id' not in session:
        return redirect('/logOut')

    if not Pet.validate_update(request.form):
        return redirect(request.referrer)

    data = { 
        'pet_id' : id,
        'name' : request.form['name'],
        'origin' : request.form['origin'],
        'type' : request.form['type'],
    }
    pet = Pet.get_pet_by_id(data)
    Pet.update_pet(data)
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def deletePet(id):
    if 'user_id' not in session:
        return redirect('/logOut')
    data = {
        'pet_id': id,
    }
    pet = Pet.get_pet_by_id(data)
    Pet.deletePet(data)
    return redirect('/dashboard')

