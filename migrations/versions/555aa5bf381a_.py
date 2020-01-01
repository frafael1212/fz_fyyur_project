"""empty message

Revision ID: 555aa5bf381a
Revises: 0cece2d1d1bc
Create Date: 2019-12-31 18:39:39.864309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '555aa5bf381a'
down_revision = '0cece2d1d1bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'start_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('start_time', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
