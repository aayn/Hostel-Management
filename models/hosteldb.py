from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=False,signature=False)

auth.settings.extra_fields['auth_user']= [
    Field('address'),
    Field('city'),
    Field('zip'),
    Field('phone')]

db.define_table('lugin',
                Field('username', requires=IS_EMAIL()),
                Field('password', requires=CRYPT()))

db.define_table('student',
                Field('first_name', requires=IS_NOT_EMPTY()),
                Field('last_name', requires=IS_NOT_EMPTY()),
                Field('father_name'),
                Field('room_number', requires=IS_NOT_EMPTY()),
                Field('email_id', requires=[IS_NOT_EMPTY(), IS_EMAIL()]),
                Field('password', 'password', requires=[IS_STRONG(), CRYPT()]),
                Field('phone_number', 'integer', requires=IS_NOT_EMPTY()),
                Field('name_of_local_guardian'),
                Field('phone_number_of_local_guardian'),
                Field('address_of_local_guardian', 'text')
                )
