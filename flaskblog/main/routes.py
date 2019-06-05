from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


##@app.route("/pagename") helps create a new route that can be access by adding /pagename at the end of address
##def pagename():
##    return "the webpage content"
##since it is to messy to input the whole html webpage here so we use render_template to return the html file
##render_template("filename", variables=variables) the file should be in  ./templates directory, variables are info you want to access in this page

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('home-temp.html', posts = posts)

@main.route("/about")
def about():
    return render_template('about-temp.html', title = 'About')



