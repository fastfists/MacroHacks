"""empty message

Revision ID: 7a1944a6e5a8
Revises: 74b7d403c717
Create Date: 2020-06-27 15:05:48.568458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a1944a6e5a8'
down_revision = '74b7d403c717'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('liked_account_id', sa.Integer(), nullable=True),
    sa.Column('current_account', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['current_account'], ['user.id'], ),
    sa.ForeignKeyConstraint(['liked_account_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    # ### end Alembic commands ###
