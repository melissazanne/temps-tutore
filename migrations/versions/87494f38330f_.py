"""empty message

Revision ID: 87494f38330f
Revises: b12d23c66127
Create Date: 2021-07-14 13:20:54.642210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87494f38330f'
down_revision = 'b12d23c66127'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('manager',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=200), nullable=False),
    sa.Column('prenom', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=200), nullable=False),
    sa.Column('fin', sa.DateTime(), nullable=True),
    sa.Column('debut', sa.DateTime(), nullable=True),
    sa.Column('classe_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['classe_id'], ['classe.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session')
    op.drop_table('manager')
    op.drop_table('classe')
    # ### end Alembic commands ###