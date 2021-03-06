from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SelectField, DateField
from wtforms.widgets.html5 import DateInput
from wtforms.validators import InputRequired


class AddCall(Form):
    """docstring for AddCall"""
    date_dn = DateField('date_dn', validators=[InputRequired()])
    franchise = SelectField('franchise', choices=[('A&E','A&E'),
                                                  ('Allied','Allied'),
                                                  ('Astro Llantas','Astro Llantas'),
                                                  ('Bauer','Bauer'),
                                                  ('Belisle','Belisle'),
                                                  ('Big L','Big L'),
                                                  ('Bill Williams','Bill Williams'),
                                                  ('Canyon','Canyon'),
                                                  ('Colony','Colony'),
                                                  ('De Lago','De Lago'),
                                                  ('DEGA-Sabinas','DEGA-Sabinas'),
                                                  ('Fleet','Fleet'),
                                                  ('Highlands','Highlands'),
                                                  ('InterCity','InterCity'),
                                                  ('Jacks','Jacks'),
                                                  ('Llantas Royal','Llantas Royal'),
                                                  ('Mil Neumaticos','Mil Neumaticos'),
                                                  ('MRT','MRT'),
                                                  ('MTI','MTI'),
                                                  ('Multillantas','Multillantas'),
                                                  ('New England Truck Tire','New England Truck Tire'),
                                                  ('Ozarko','Ozarko'),
                                                  ('Paisa','Paisa'),
                                                  ('Phelps','Phelps'),
                                                  ('Raben','Raben'),
                                                  ('Radial Llantas','Radial Llantas'),
                                                  ('Ren-Atec','Ren-Atec'),
                                                  ('Renollan','Renollan'),
                                                  ('Robert Bernard','Robert Bernard'),
                                                  ('Sam Autos','Sam Autos'),
                                                  ('STTC','STTC'),
                                                  ('Shrader','Shrader'),
                                                  ('Smetzer','Smetzer'),
                                                  ('Snider','Snider'),
                                                  ('Strouhal','Strouhal'),
                                                  ('Superior','Superior'),
                                                  ('Tampico Sales','Tampico Sales'),
                                                  ('TCI','TCI'),
                                                  ('Tecnicentro','Tecnicentro'),
                                                  ('Tiremaster','Tiremaster'),
                                                  ('Treads West','Treads West'),
                                                  ('T&W','T&W'),
                                                  ('Valley','Valley'),
                                                  ('Ziegler','Ziegler')], validators=[InputRequired()])
    location = SelectField('location', choices=[('Denver', 'Denver'),
                                                ('Chihuahua', 'Chihuahua'),
                                                ('Omaha','Omaha'),
                                                ('Mexico City', 'Mexico City'),
                                                ('Cedar Rapids', 'Cedar Rapids'),
                                                ('Des Moines', 'Des Moines'),
                                                ('Durand', 'Durand'),
                                                ('Indianapolis','Indianapolis'),
                                                ('Romeoville','Romeoville'),
                                                ('St_Paul', 'St_Paul'),
                                                ('Waukesha','Waukesha'),
                                                ('St_Augustine', 'St_Augustine'),
                                                ('St_Jerome', 'St_Jerome'),
                                                ('Midland','Midland'),
                                                ('Corona','Corona'),
                                                ('Harrisonburg','Harrisonburg'),
                                                ('Edenton','Edenton'),
                                                ('Aguascalientes', 'Aguascalientes'),
                                                ('Sabinas Hidalgo','Sabinas Hidalgo'),
                                                ('Dartmouth','Dartmouth'),
                                                ('Carlisle','Carlisle'),
                                                ('Elizibeth City', 'Elizibeth City'),
                                                ('Boise','Boise'),
                                                ('Logan','Logan'),
                                                ('Salt Lake City','Salt Lake City'),
                                                ('Fresno','Fresno'),
                                                ('Phoenix','Phoenix'),
                                                ('Culican','Culican'),
                                                ('Monterry','Monterry'),
                                                ('Duncan','Duncan'),
                                                ('Grand Rapids','Grand Rapids'),
                                                ('Queretero','Queretero'),
                                                ('Sanford','Sanford'),
                                                ('Pottsville','Pottsville'),
                                                ('West Plains','West Plains'),
                                                ('Cordoba','Cordoba'),
                                                ('Seattle','Seattle'),
                                                ('Evansville','Evansville'),
                                                ('Guadalajara','Guadalajara'),
                                                ('Villahermosa','Villahermosa'),
                                                ('Hermosillo','Hermosillo'),
                                                ('Toluca','Toluca'),
                                                ('Merida','Merida'),
                                                ('Torreon','Torreon'),
                                                ('Bethlehem','Bethlehem'),
                                                ('Millbury','Millbury'),
                                                ('York','York'),
                                                ('Melvindale','Melvindale'),
                                                ('Wooster','Wooster'),
                                                ('Bluffton','Bluffton'),
                                                ('Ellenwood','Ellenwood'),
                                                ('Greensboro','Greensboro'),
                                                ('Houston','Houston'),
                                                ('Pelzer','Pelzer'),
                                                ('Statesville','Statesville'),
                                                ('Hungerford','Hungerford'),
                                                ('Salem','Salem'),
                                                ('Tampico','Tampico'),
                                                ('Antioch','Antioch'),
                                                ('Birmingham','Birmingham'),
                                                ('Fontana','Fontana'),
                                                ('Hudson','Hudson'),
                                                ('Jacksonville','Jacksonville'),
                                                ('Kansas City','Kansas City'),
                                                ('Lancaster','Lancaster'),
                                                ('Pemberville','Pemberville'),
                                                ('Richland','Richland'),
                                                ('Tiajuana','Tiajuana'),
                                                ('Brampton','Brampton'),
                                                ('Ingersol','Ingersol'),
                                                ('Edmonton','Edmonton'),
                                                ('Langley','Langley'),
                                                ('Oklahoma City','Oklahoma City'),
                                                ('San Antonio','San Antonio'),
                                                ('Charleroi','Charleroi'),
                                                ('Massillon','Massillon'),
                                                ('Monroe','Monroe')],validators=[InputRequired()])

    machine = SelectField('franchise machine', choices = [('autoclave', 'autoclave'),
                                                           ('buffer','buffer'),
                                                           ('pm builder','pm builder'),
                                                           ('cm builder', 'cm builder'),
                                                           ('press', 'press'),
                                                           ('cia_1_2', 'cia_1_2'),
                                                           ('cia_3', 'cia_3'),
                                                           ('xray', 'xray'),
                                                           ('NDT', 'NDT'),
                                                           ('final', 'final')], validators=[InputRequired()])
    status = TextAreaField('status', validators=[InputRequired()])
    date_up = DateField('date_up', validators=[InputRequired()])
    tech = SelectField('technician', choices = [( 'Jay Bailey','Jay Bailey'),
                                                ( 'Marshal Barton', 'Marshal Barton'),
                                                ('Johnny Corn', 'Johnny Corn'),
                                                ('Keith Finley', 'Keith Finley'),
                                                ('Pablo Murphy', 'Pablo Murphy'),
                                                ('Alan Schmeelk', 'Alan Schmeelk'),
                                                ('John Simpson', 'John Simpson'),
                                                ('John Steele', 'John Steele'),
                                                ('Bobby Springman', 'Bobby Springman'),
                                                ('David Tucker', 'David Tucker')], validators=[InputRequired()])
    
   


class SelectReport(Form):
    """doc string for SelectReport"""
    report_type = SelectField('report_type', choices = [('all','all_calls'),
                                                        ('shop','by_shop_num'),
                                                        ('franchise','by_franchise'),
                                                        ('machine','by_machine'),
                                                        ('most','by_most_calls'),
                                                        ('downtime','by_downtime'),
                                                        ('callcount', 'by_num_call')], validators=[InputRequired()])


class SelectShop(Form):
    """docstring for SelectShop"""
    shop = SelectField('plant_num', choices = [('121','A & E-Denver' ),
                                                ('182','Agencia Llantera-Chihuahua' ),
                                                ('116','Allied-Omaha' ),
                                                ('163','Astro Llantas-Mexico City'),
                                                ('127','Bauer-Cedar Rapids'),
                                                ('128','Bauer-Des Moines'),
                                                ('131','Bauer-Durand'),
                                                ('130','Bauer-Indianapolis'),
                                                ('150','Bauer-Romeoville'),
                                                ('129','Bauer-St_Paul'),
                                                ('142','Bauer-Waukesha'),
                                                ('189','Belisle-St_Augustine'),
                                                ('144','Belisle-St_Jerome'),
                                                ('184','Bill Williams'),
                                                ('187','Canyon-Corona'),
                                                ('134','Big L-Harrisonburg'),
                                                ('190','Colony-Edenton'),
                                                ('165','De Lago-AguasCalientes'),
                                                ('161','DEGA-Sabinas Hidalgo'),
                                                ('146','Fleet-Dartmouth'),
                                                ('135','Highlands-Carlisle'),
                                                ('132','InterCity-Elizabeth'),
                                                ('117','Jacks-Boise'),
                                                ('119','Jacks-Logan'),
                                                ('118','Jacks-SLC'),
                                                ('197','Jacks-Fresno'),
                                                ('164','Jacks-Phoenix'),
                                                ('169','Llantas Royal-Culican'),
                                                ('153','Mil Neumaticos-Mexico City'),
                                                ('156','Mil Neumaticos-Monterrey'),
                                                ('101','MRT-Duncan'),
                                                ('137','MTI-Grand Rapids'),
                                                ('148','Multillantas Nieto-Queretaro'),
                                                ('186','New England Truck Tire-Sanford'),
                                                ('167','Ozarko-Pottsville'),
                                                ('140','Ozarko-West Plains'),
                                                ('151','Paisa-Cordoba'),
                                                ('133','Phelps-Seattle'),
                                                ('168','Raben Tire-Evansville'),
                                                ('162','Radial Llantas-Guadalajara'),
                                                ('178','Radial Llantas-Villahermosa'),
                                                ('157','Ren-Atec - Hermosillo'),
                                                ('171','Renollan - Toluca'),
                                                ('138','Robert Bernard - St_Paul'),
                                                ('199','Radial Llantas - Merida'),
                                                ('183','Sam Autos - Torreon'),
                                                ('175','STTC - Bethlehem'),
                                                ('196','STTC - Millbury'),
                                                ('176','STTC - York'),
                                                ('177','Shrader - Melvindale'),
                                                ('107','Smetzer Tire - Wooster'),
                                                ('194','Snider - Bluffton'),
                                                ('191','Snider - Ellenwood'),
                                                ('198','Snider - Greensboro'),
                                                ('193','Snider - Houston'),
                                                ('195','Snider - Pelzer'),
                                                ('192','Snider - Statesville'),
                                                ('158','Strouhal - Hungerford'),
                                                ('136','Superior - Salem'),
                                                ('179','Tampico Sales - Tampico'),
                                                ('152','TCI - Antioch'),
                                                ('166','TCI - Birmingham'),
                                                ('122','TCI - Fontana'),
                                                ('123','TCI - Hudson'),
                                                ('124','TC1 - Jacksonville'),
                                                ('115','TCI - Kansas City'),
                                                ('145','TCI - Lancaster'),
                                                ('106','TCI - Pemberville'),
                                                ('111','TCI - Richland'),
                                                ('170','Tecnicentro Royal - Tiajuana'),
                                                ('185','Tiremaster - Brampton'),
                                                ('149','Tiremaster - Ingersol'),
                                                ('159','Treads West - Edmonton'),
                                                ('172','Treads West - Langley'),
                                                ('200','TW - Oklahoma City'),
                                                ('201','TW - San Antonio'),
                                                ('180','Valley Tire - Charleroi'),
                                                ('108','Ziegler - Massillon'),
                                                ('173','Ziegler - Monroe')],  validators=[InputRequired()])


class SelectFranchise(Form):
    """docstring for SelectFranchise"""
    franchise = SelectField('franchise', choices=[('A&E','A&E'),
                                                  ('Allied','Allied'),
                                                  ('Astro Llantas','Astro Llantas'),
                                                  ('Bauer','Bauer'),
                                                  ('Belisle','Belisle'),
                                                  ('Big L','Big L'),
                                                  ('Bill Williams','Bill Williams'),
                                                  ('Canyon','Canyon'),
                                                  ('Colony','Colony'),
                                                  ('De Lago','De Lago'),
                                                  ('DEGA-Sabinas','DEGA-Sabinas'),
                                                  ('Fleet','Fleet'),
                                                  ('Highlands','Highlands'),
                                                  ('InterCity','InterCity'),
                                                  ('Jacks','Jacks'),
                                                  ('Llantas Royal','Llantas Royal'),
                                                  ('Mil Neumaticos','Mil Neumaticos'),
                                                  ('MRT','MRT'),
                                                  ('MTI','MTI'),
                                                  ('Multillantas','Multillantas'),
                                                  ('New England Truck Tire','New England Truck Tire'),
                                                  ('Ozarko','Ozarko'),
                                                  ('Paisa','Paisa'),
                                                  ('Phelps','Phelps'),
                                                  ('Raben','Raben'),
                                                  ('Radial Llantas','Radial Llantas'),
                                                  ('Ren-Atec','Ren-Atec'),
                                                  ('Renollan','Renollan'),
                                                  ('Robert Bernard','Robert Bernard'),
                                                  ('Sam Autos','Sam Autos'),
                                                  ('STTC','STTC'),
                                                  ('Shrader','Shrader'),
                                                  ('Smetzer','Smetzer'),
                                                  ('Snider','Snider'),
                                                  ('Strouhal','Strouhal'),
                                                  ('Superior','Superior'),
                                                  ('Tampico Sales','Tampico Sales'),
                                                  ('TCI','TCI'),
                                                  ('Tecnicentro','Tecnicentro'),
                                                  ('Tiremaster','Tiremaster'),
                                                  ('Treads West','Treads West'),
                                                  ('T&W','T&W'),
                                                  ('Valley','Valley'),
                                                  ('Ziegler','Ziegler')], validators=[InputRequired()])
        
class SelectMachine(Form):
    """docstring for SelectMachine"""
    machine = SelectField('machine', choices = [('autoclave','autoclave'),
                                                 ('buffer','buffer'),
                                                 ('pm builder','pm builder'),
                                                 ('cm builder','cm builder'),
                                                 ('press','press'),
                                                 ('cia_1_2','cia_1_2'),
                                                 ('cia_3','cia_3'),
                                                 ('xray','xray'),
                                                 ('ndt','ndt'),
                                                 ('final','final')], validators=[InputRequired()])