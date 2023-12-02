from flask import Flask, render_template, request
from trip_helper import location_search, combined_location_info

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/location_list', methods=['GET', 'POST'])
def location_list():
    locations = []
    if request.method == 'POST':
        query = request.form['query']
        category = request.form.get('category')
        locations = location_search(query, category)

    return render_template('location_list.html', locations=locations)


@app.route('/location_details/<location_id>')
def location_details(location_id):
    combined_info = combined_location_info(location_id, category=None)

    if combined_info == "No details found for the given location ID.":
        return render_template('no_details.html')

    return render_template('location_details.html', details=combined_info)


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
