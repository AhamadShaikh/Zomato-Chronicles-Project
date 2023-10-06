from flask import Flask, request, render_template,redirect

app = Flask(__name__)

data = {}

@app.route("/create", methods=['GET', 'POST'])
def create_entry():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data[key] = value
        return redirect("/")
    return render_template('create.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
            return redirect('/')
    return render_template('delete.html')


@app.route("/",methods=['GET', 'POST'])
def read_entries():
    return render_template("read.html",data=data)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        if key in data:
            data[key] = value
            return redirect('/')
    return render_template('update.html')


if __name__ == "__main__":
    app.run(debug=True)