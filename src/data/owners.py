class Owner:
    registered_date = None
    name = None
    email = None

    snake_ids = []
    cage_ids = []

    meta = {
        'db_alias': 'core',
        'collection': 'owners'
    }
