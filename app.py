"""Adopt application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


connect_db(app)
# db.create_all()

@app.route('/')
def list_pets():
    """Show list of pets with name, photo (if added) and availability."""

    all_pets = Pet.query.all()

    return render_template('home.html', all_pets=all_pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add pet form; handle adding"""

    form = PetForm()

    if form.validate_on_submit():

        print('')
        print('-------- ADD PET POST ROUTE --------')
        print('')


        print('')
        print('************* FORM DATA *************')
        print(form.data)
        print('')
        print(form.name.data)
        print(form.species.data)
        print(form.image_url.data)
        print(form.age.data)
        print(form.notes.data)
        print(form.available.data)
        print('*************************************')
        print('')

        name = form.name.data
        species = form.species.data
        image_url = form.image_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name, species=species, image_url=image_url, age=age, notes=notes, available=available)

        print('')
        print('************* PET OBJECT *************')
        print(new_pet)
        print('**************************************')
        print('')

        db.session.add(new_pet)
        db.session.commit()

        flash(f'Added {name} who is a {species} and available: {available}')
        return redirect('/')
    else:

        print('')
        print('-------- ADD PET GET ROUTE --------')
        print('')

        print('')
        print('*************** FORM ERRORS ***************')
        print(form.errors)
        print('*******************************************')
        print('')

        return render_template('add-pet-form.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_edit_pet(pet_id):

    form = PetForm()

    # get the current pet being viewed
    curr_pet = Pet.query.get_or_404(pet_id)

    # to add data from our pet entry to the form, we pass the pet object to the AddPetForm
    form = PetForm(obj=curr_pet)

    if form.validate_on_submit():

        print('')
        print('-------- EDIT PET POST ROUTE --------')
        print('')

        name = form.name.data
        image_url = form.image_url.data
        notes = form.notes.data
        available = form.available.data

        curr_pet.image_url = image_url
        curr_pet.notes = notes
        curr_pet.available = available

        print('')
        print('************* NEW PET OBJECT ************')
        print(curr_pet)
        print('*************************')
        print('')

        # the below line wasn't in the class for Editing/Updating forms, do we need this , or can we just commit?
        # db.session.add(curr_pet)
        db.session.commit()

        flash(f'Edited {name}!')
        return redirect('/')
    else:
        print('')
        print('-------- EDIT PET GET ROUTE --------')
        print('')

        print('')
        print('************* FORM ERRORS ************')
        print(form.errors)
        print('**************************************')
        print('')

        return render_template('edit-pet-form.html', curr_pet=curr_pet, form=form)