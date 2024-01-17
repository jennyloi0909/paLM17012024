from flask import Flask,request,render_template
import google.generativeai as palm

app = Flask(__name__)
palm.configure(api_key="AIzaSyDKf9wGDZFs0XLHFwq1Y1tk5C_wK6NnwbQ")
model = {"model": "models/chat-bison-001"}

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        print(q)
        r = palm.chat(
            **model,
            messages=q
            )
        return (render_template("index.html", r=r.last))
    else:
        return(render_template("index.html", result = "waiting for question...."))
    
if __name__ == "__main__":
    app.run()
