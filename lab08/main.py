from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from retriever import get_apod

app = Flask(__name__)

@app.route('/')
def home():
    apod_data = get_apod()  
    return render_template('home.html', apod=apod_data)

@app.route('/history', methods=['GET', 'POST'])
def history():
    error_message = None
    apod_data = None

    if request.method == 'POST':
        date_input = request.form['date']
        try:
            date_obj = datetime.strptime(date_input, '%Y-%m-%d')
            if date_obj > datetime.now():
                error_message = "Date cannot be in the future. Please try again."
            elif date_obj < datetime(1995, 6, 16):
                error_message = "Date cannot be before June 16, 1995. Please try again."
            else:
                apod_data = get_apod(date=date_input)
        except ValueError:
            error_message = "Invalid date format. Please use YYYY-MM-DD."

    return render_template('history.html', apod=apod_data, error=error_message)
if __name__ == '__main__':
    app.run(debug=True)
