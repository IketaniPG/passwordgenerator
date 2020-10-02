from flask import Flask, render_template, request
from forms import forms
from random import choice
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_KEY_HERE'

def passgeneratorfunction(passLength):
    value = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(passLength):
        password += choice(value)
    return password

@app.route('/', methods=['GET', 'POST'])
def passGenerator():
    form = forms.PassGenerator()
    if form.is_submitted():
        result = request.form
        
        def resultado():
            for value in result.items():
                return int(value[1])

        return render_template('generated.html', password=passgeneratorfunction(resultado()))
    return render_template('generator.html', form=form)

if __name__ == '__main__':
    app.run()
