
import csv
import smtplib
from flask import Flask, render_template, request, Response, flash, redirect



app = Flask(__name__)


@app.route('/')
def get_homepage():
    return render_template('index.html')
    
@app.route('/<string:page_name>')
def get_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/contact_submit', methods=['POST', 'GET'])
def contact_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        # email = data["email"]
        # subject = data["subject"]
        # message = data["message"]

        # my_email = 'Fentonalf@gmail.com'
        # mail_from = email
        # mail_subject = subject
        # mail_message = f'''
        # From: {mail_from}
        # To: {mail_subject}
        # Subject: {subject}
        # {message}
        # '''
        # server = smtplib.SMTP('http://127.0.0.1:8000/')
        # server.sendmail(mail_from, my_email, mail_subject, mail_message)
        # server.quit
        return redirect('thankyou.html')
    else:
        flash("Something went wrong, please try again")




if __name__ == "__main__":
    app.run()
