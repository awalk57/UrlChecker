"""initial migration

Revision ID: 40d93154b9f2
Revises: None
Create Date: 2015-09-15 14:42:42.976381

"""

# revision identifiers, used by Alembic.
revision = '40d93154b9f2'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_roles_default', table_name='roles')
    op.create_unique_constraint(None, 'roles', ['name'])
    op.drop_column('roles', 'default')
    op.drop_column('roles', 'permissions')
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    op.add_column('roles', sa.Column('permissions', sa.INTEGER(), nullable=True))
    op.add_column('roles', sa.Column('default', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'roles', type_='unique')
    op.create_index('ix_roles_default', 'roles', ['default'], unique=1)
    ### end Alembic commands ###
