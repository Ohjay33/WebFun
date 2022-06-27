# model/validation #
from flask import flash
class Burger:
    # Other Burger methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_burger(burger):
        is_valid = True # we assume this is true
        if len(burger['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(burger['bun']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if int(burger['calories']) < 200:
            flash("Calories must be 200 or greater.")
            is_valid = False
        if len(burger['meat']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        return is_valid




# controller/   validation
    from flask_app.models.burger import Burger
@app.route('/create', methods=['POST'])
def create_burger():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not Burger.validate_burger(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    Burger.save(request.form)
    return redirect("/burgers")

# HTML/validation
{% with messages = get_flashed_messages() %}     <!-- declare a variable called messages -->
    {% if messages %}                            <!-- check if there are any messages -->
        {% for message in messages %}            <!-- loop through the messages -->
            <p>{{message}}</p>                   <!-- display each message in a paragraph tag -->
        {% endfor %}
    {% endif %}
{% endwith %}

