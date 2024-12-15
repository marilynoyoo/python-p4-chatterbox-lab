"""create messages table

Revision ID: 943be89f2743
Revises: a4664a7ad55c
Create Date: 2024-12-13 13:30:17.507670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '943be89f2743'
down_revision = 'a4664a7ad55c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('messages', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.alter_column('messages', 'body',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column('messages', 'username',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('messages', 'username',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('messages', 'body',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.drop_column('messages', 'updated_at')
    op.drop_column('messages', 'created_at')
    # ### end Alembic commands ###
