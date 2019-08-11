import os
from datetime import datetime

from mcp import db
from mcp.users.models import User, Role, UserRoles


def Reset():
    if os.path.exists('mcp/site.db'):
        os.system('rm mcp/site.db')
    if os.path.exists('migrations/'):
        os.system('rm -r migrations/versions/*')
    else:
        os.system('flask db init')
    os.system('flask db migrate')
    os.system('flask db upgrade')

    test_users = ['Cameron Alsop',
                  'Leonard Black',
                  'Trevor Wilkins',
                  'Emily Hughes',
                  'Steven Butler',
                  'Samantha Clarkson',
                  'Stephanie Allan',
                  'Lauren Davies',
                  'Jake Hodges',
                  'Joe Ferguson',
                  'Jan Lawrence',
                  'Joe Langdon',
                  'Benjamin Martin',
                  'Alan Greene',
                  'Lauren Burgess',
                  'Ian Avery',
                  'Dominic Powell',
                  'Anthony North',
                  'James Gibson',
                  'Joshua Simpson', ]

    for user in test_users:
        fn = user.split(' ')[0]
        ln = user.split(' ')[1]
        e = f"testuser+{fn}.{ln}@makeict.org"
        u = User(first_name=fn, last_name=ln, email=e, username=f"{fn}.{ln}",
                 email_confirmed_at=datetime.utcnow())
        db.session.add(u)

    admin_role = Role(name='admin')
    db.session.add(admin_role)

    admin = User(first_name="Ryan", last_name="Fisher",
                 email="testuser+admin@makeict.org", username="Ryan_Admin",
                 email_confirmed_at=datetime.utcnow(), roles=[admin_role])
    db.session.add(admin)

    db.session.commit()
