"""empty message

Revision ID: 2223d53ce2c8
Revises: 87ece975e53b
Create Date: 2018-04-02 15:42:12.945106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2223d53ce2c8'
down_revision = '87ece975e53b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('stock', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'stock')
    # ### end Alembic commands ###