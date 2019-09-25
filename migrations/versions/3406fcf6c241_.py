"""empty message

Revision ID: 3406fcf6c241
Revises: 
Create Date: 2019-09-25 22:49:53.938976

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3406fcf6c241'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hasil', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('result')
    # ### end Alembic commands ###
