import numpy as np
import csv
import pandas as pd
import sklearn

from sklearn.neighbors import NearestNeighbors
from flask import Flask, render_template, url_for
from forms import SubmitForm
app = Flask(__name__)
app.config['SECRET_KEY']='6efa5941e2b4b5a9912c11bfe3cd98d1'



def setpost(mpg,cyl,hp,gr,sit):
    cars=pd.read_csv('mtcars.csv')
    cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
    cars.head()

    x=cars.iloc[:,[1,2,4,6,10]]
    x[0:5]

    nbrs=NearestNeighbors(n_neighbors=1).fit(x)

    t=[mpg,cyl,hp,sit,gr]

    result1=nbrs.kneighbors([t])
    array1=np.asarray(result1)
    num2=array1[1]
    num2=num2.astype(int)
    num2=num2+1
    return result(num2)


@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    form=SubmitForm()
    if form.validate_on_submit():
        hp=int(form.horsepower.data)
        mpg=int(form.mileage.data)
        sit=float(form.seats.data)
        cyl=int(form.cylinders.data)
        gr=int(form.gears.data)
        
        return setpost(mpg,cyl,hp,gr,sit)
    
    return render_template('home.html', title='Home',form = form)


@app.route('/result')
def result(num2):
    num1=num2
    with open('mtcars.csv','r') as carfile:
        csv_reader=csv.reader(carfile)
        line_count=2
        for row in csv_reader:
            if line_count==num1:
                
                posts=[{'title':row[0],
                            'horsepower':row[4],
                            'cylinders':row[2],
                            'mileage':row[1],
                            'manual':'Automatic',
                            'gears':row[10],
                            'seats':row[6]}]

                        
                line_count= line_count + 1
            else:
                line_count= line_count + 1
    return render_template('newresult.html',posts=posts)


if __name__ == '__main__':
        app.run(debug=True)

                    

