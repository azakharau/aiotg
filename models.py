import sqlalchemy as sa

metadata = sa.MetaData()

category = sa.Table('category', metadata,

                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('name', sa.String(255)),
                    sa.Column('is_base', sa.Boolean, default=False),
                    sa.Column('aliases', sa.ARRAY(sa.String)),
                    sa.Column('created', sa.TIMESTAMP, nullable=False),
                    sa.Column('updated', sa.TIMESTAMP, nullable=False)
                    )

expense = sa.Table('expense', metadata,

                   sa.Column('id', sa.Integer, primary_key=True),
                   sa.Column('category', sa.Integer,
                             sa.ForeignKey("category.id")),
                   sa.Column('value', sa.DECIMAL, nullable=True),
                   sa.Column('created', sa.TIMESTAMP, nullable=False),
                   sa.Column('updated', sa.TIMESTAMP, nullable=False)
                   )

user = sa.Table('user', metadata,

                sa.Column('id', sa.Integer, primary_key=True),
                sa.Column('first_name', sa.String, nullable=True),
                sa.Column('second_name', sa.String, nullable=True),
                sa.Column('username', sa.String),
                sa.Column('tg_id', sa.String, nullable=True),
                sa.Column('created', sa.TIMESTAMP, nullable=False),
                sa.Column('updated', sa.TIMESTAMP, nullable=False)
                )
