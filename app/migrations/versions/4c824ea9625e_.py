"""empty message

Revision ID: 4c824ea9625e
Revises: e9f3f8be5b27
Create Date: 2018-04-09 14:42:33.263647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c824ea9625e'
down_revision = 'e9f3f8be5b27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('add_time', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_product_add_time'), 'product', ['add_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_add_time'), table_name='product')
    op.drop_column('product', 'add_time')
    # ### end Alembic commands ###