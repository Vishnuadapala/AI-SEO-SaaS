from flask import Blueprint, render_template, request
from .seo_service import generate_seo_content

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        topic = request.form.get("topic")
        result = generate_seo_content(topic)

    return render_template("index.html", result=result)