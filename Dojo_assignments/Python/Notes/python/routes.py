# Passing Data to Html
<!--  # import statements, maybe some other routes -->
@app.route('/success')
def success():

return "success
app.run(debug=True) should be the very last statement!



# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name



    # <!--  # for a route '/users/____/____', two parameters in the url get passed as username and id -->

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

# Rendering data on a template
<h3 > My Flask Template < /h3 >
<p > Phrase: {{phrase}} < /p >
<p > Times: {{times}} < /p >

{ % for x in range(0, times): % }
<p > {{phrase}} < /p >
{% endfor % }

{% if phrase == "hello" % }
<p > The phrase says hello < /p >
{% endif % }



# Retrieving and displaying data
@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)


    <h1>All My Friends</h1>
{% for one_friend in all_friends %}
<p>First Name:{{one_friend.first_name}}</p>
<p>Last Name: {{one_friend.last_name}}</p>
<p>Occupation: {{one_friend.occupation}}</p>
<hr>
{% endfor %}


