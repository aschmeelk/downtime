from app import app, db, admin
from flask import render_template, g, redirect, url_for, flash
from app.forms import AddCall, SelectReport, SelectShop, SelectFranchise, SelectMachine                       
from app.models import Calls
from flask.ext.admin.contrib.sqla import ModelView


# Admin views for modifying records
# need to make this available via log in only.
admin.add_view(ModelView(Calls, db.session))


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	calls = Calls.query.order_by('date_dn desc').all()
	return render_template('index.html', calls = calls)


@app.route('/calls', methods=['GET', 'POST'])
def addcall():
    form = AddCall()
    # #add logic to insert data into the database.
    # 	redirect('/')
    if form.validate_on_submit():
        new_call = Calls(date_dn = form.date_dn.data,
        	
        			franchise = form.franchise.data,
        			location = form.location.data,
        		
        			machine = form.machine.data,
        			
        			status = form.status.data,
                    date_up = form.date_up.data,
                    tech = form.tech.data
        			) 
        db.session.add(new_call)
        db.session.commit()
        flash('data committed!')
    	return redirect(url_for('index'))
    return render_template('calls.html', form=form)

# @app.route('/reports', methods=['GET','POST'])
# def reports():
#     form = SelectReport()
#     if form.validate_on_submit():       
#         if form.report_type.data == 'all':
#             return redirect(url_for('all'))
#         elif form.report_type.data == 'shop':
#             return redirect(url_for('shop'))
#         elif form.report_type.data == 'franchise':
#             return redirect(url_for('franchise'))
#         elif form.report_type.data == 'machine':
#             return redirect(url_for('machine'))
#         elif form.report_type.data == 'most':
#             return redirect(url_for('most'))
#         elif form.report_type.data == 'downtime':
#             return redirect(url_for('downtime'))
#         elif form.report_type.data == 'callcount':
#             return redirect(url_for('callcount'))

#     return render_template('reports.html', form=form)


# @app.route('/all', methods=['GET','POST'])
# def all():
#     calls = Calls.query.order_by('date desc').all()
#     return render_template('all.html', calls=calls)


# @app.route('/shop', methods=['GET','POST'])
# def shop():
#     form = SelectShop()
#     shop_num = form.shop.data
#     if form.validate_on_submit():
#         return redirect(url_for('by_num', shop_num=shop_num))
#     return render_template('shop.html', form = form)

# @app.route('/most', methods=['GET','POST'])
# def most():
#     most_calls = Calls.query.order_by('franchise','location').all()
#     return render_template('most.html', calls=most_calls)

# @app.route('/downtime', methods=['GET','POST'])
# def downtime():
#     most_downtime = Calls.query.order_by('downtime desc').all()
#     return render_template('downtime.html', calls = most_downtime)

# @app.route('/by_num/<shop_num>', methods = ['GET','POST'])
# def by_num(shop_num):
#     lst = Calls.query.filter_by(plant_num=shop_num).all()
#     return render_template('by_num.html', shop=shop_num, calls=lst)


# @app.route('/franchise', methods=['GET','POST'])
# def franchise():
#     form = SelectFranchise()
#     franchise = form.franchise.data
#     if form.validate_on_submit():
#         return redirect(url_for('by_franchise', franchise=franchise))
#     return render_template('franchise.html', form=form)


# @app.route('/by_franchise/<franchise>', methods=['GET','POST'])
# def by_franchise(franchise):
#     lst = Calls.query.filter_by(franchise = franchise).all()
#     return render_template('by_franchise.html',franchise=franchise, calls=lst)

# @app.route('/machine', methods=['GET','POST'])
# def machine():
#     form = SelectMachine()
#     machine = form.machine.data
#     if form.validate_on_submit():
#         return redirect(url_for('by_machine', machine = machine))
#     return render_template('machine.html', form = form)


# @app.route('/by_machine/<machine>', methods=['GET','POST'])
# def by_machine(machine):
#     lst = Calls.query.filter_by(machine = machine).all()
#     return render_template('by_machine.html', machine=machine, calls=lst)


# @app.route('/callcount', methods=['GET','POST'])
# def callcount():
#     #Create a list of all franchises that have called
#     frn_lst = db.session.query(Calls.franchise).distinct().all()
#     plt_lst = db.session.query(Calls.location).distinct().all()
#     #Initialize dictionary to hold franchise and count
#     frn = {}
#     plnt = {}

#     for x in frn_lst:
#         #load franchise count into temp. variable
#         r = db.session.query(Calls).filter(Calls.franchise.like('%s' %x)).count()
#         #load franchise, count into the dictionary
#         frn.update({x:r})

#     for num in plt_lst:
#         #load franchise count into temp. variable
#         r = db.session.query(Calls).filter(Calls.location.like('%s' %num)).count()
#         #load franchise, count into the dictionary
#         plnt.update({num:r})


#     return render_template('callcount.html', frn = frn, plnt = plnt)

#         