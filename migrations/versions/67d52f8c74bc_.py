"""empty message

Revision ID: 67d52f8c74bc
Revises: None
Create Date: 2016-02-20 21:37:08.214805

"""

# revision identifiers, used by Alembic.
revision = '67d52f8c74bc'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('company')
    op.add_column('posts', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'users', ['author_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'author_id')
    op.create_table('company',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('address', sa.CHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('salary', sa.REAL(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'company_pkey')
    )
    op.drop_table('users')
    ### end Alembic commands ###
