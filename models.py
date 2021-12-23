from peewee import *
import datetime

'''psql_db = PostgresqlDatabase('BankStructure', user='postgres',
                                              password='forest123ry',
                                              host='localhost',
                                              port='5432')'''
'''psql_db = PostgresqlDatabase('BankStructure', user='manager',
                                              password='1234',
                                              host='localhost',
                                              port='5432')
psql_db.connect(reuse_if_open=True)
print(psql_db)'''
db = Proxy()  # Create a proxy for our db.
#db = PostgresqlDatabase(None)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        #database = psql_db
        #database = database_proxy
        database = db

class Regions(BaseModel):
    name = CharField(max_length=100)
    director_id = IntegerField()
    population = IntegerField(constraints=[Check('population >= 0')])
    number_of_companies = IntegerField(constraints=[Check('number_of_companies >= 0')])


class Districts(BaseModel):
    name = CharField(max_length=100)
    region_id = ForeignKeyField(Regions, backref='districts')
    administrator_id = IntegerField()
    population = IntegerField(constraints=[Check('population >= 0')])
    number_of_companies = IntegerField(constraints=[Check('number_of_companies >= 0')])

class Employers(BaseModel):
    name = CharField(max_length=100)
    age = IntegerField(constraints=[Check('age >= 18')])
    month_plan = IntegerField(constraints=[Check('month_plan >= 0')])
    login = CharField(max_length=50)
    password = CharField(max_length=50)
    #role = RoleField()
    role = CharField(max_length=50)

class Managers(BaseModel):
    employee_id = ForeignKeyField(Employers, backref='managers')
    district_id = ForeignKeyField(Districts, backref='managers')

class Companies(BaseModel):
    name = CharField(max_length=100, unique=True)
    region_id = ForeignKeyField(Regions, backref='companies')
    manager_id = ForeignKeyField(Managers, backref='companies')
    has_online = BooleanField(default=False)
    has_offline = BooleanField(default=False)

class T_Companies(BaseModel):
    name = CharField(max_length=100, unique=True)
    region_id = ForeignKeyField(Regions, backref='companies')
    manager_id = ForeignKeyField(Managers, backref='companies')
    has_online = BooleanField(default=False)
    has_offline = BooleanField(default=False)

class Deals(BaseModel):
    orderer_name = CharField(max_length=100)
    deal_sum = IntegerField(constraints=[Check('deal_sum >= 0')])
    deal_type = CharField(max_length=7)
    is_approved = BooleanField(default=False)
    deal_time = DateTimeField()

class T_Deals(BaseModel):
    orderer_name = CharField(max_length=100)
    deal_sum = IntegerField(constraints=[Check('deal_sum >= 0')])
    deal_type = CharField(max_length=7)
    is_approved = BooleanField(default=False)
    deal_time = DateTimeField()

class Directors(BaseModel):
    employee_id = ForeignKeyField(Employers, backref='directors')
    region_id = IntegerField()

class Administrators(BaseModel):
    employee_id = ForeignKeyField(Employers, backref='administrators')
    director_id = ForeignKeyField(Directors, backref='administrators')
    district_id = ForeignKeyField(Districts, backref='administrators')

class CompanyDeal(BaseModel):
    company_id = ForeignKeyField(Companies, backref='company_deal')
    deal_id = ForeignKeyField(Deals, backref='company_deal')

class T_CompanyDeal(BaseModel):
    company_id = ForeignKeyField(Companies, backref='company_deal')
    deal_id = ForeignKeyField(Deals, backref='company_deal')
