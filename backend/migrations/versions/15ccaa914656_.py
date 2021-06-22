"""empty message

Revision ID: 15ccaa914656
Revises: e2a4feeee4f6
Create Date: 2021-06-17 23:31:34.841252

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '15ccaa914656'
down_revision = 'e2a4feeee4f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', mysql.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###
