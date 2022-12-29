"""Initial Migration

Revision ID: a4098101f6f9
Revises: 
Create Date: 2022-12-28 22:39:00.957695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4098101f6f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('email', sa.VARCHAR(length=80),
                              autoincrement=False, nullable=False),
                    sa.Column('password', sa.VARCHAR(length=256),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='user_pkey'),
                    sa.UniqueConstraint('email', name='user_email_key'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')

    # ### end Alembic commands ###
