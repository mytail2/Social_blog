"""empty message

Revision ID: 788576410251
Revises: 3c47f26c8918
Create Date: 2018-03-17 15:23:49.638128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '788576410251'
down_revision = '3c47f26c8918'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirm', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    op.drop_column('users', 'confirm')
    # ### end Alembic commands ###
