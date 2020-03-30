"""init

Revision ID: 9d081c9da26f
Revises: 
Create Date: 2020-03-30 17:17:53.690154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d081c9da26f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dept_name', sa.String(length=64), nullable=True),
    sa.Column('building', sa.String(length=64), nullable=True),
    sa.Column('budget', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dept_name')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('dept_name', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['dept_name'], ['departments.dept_name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    op.drop_table('departments')
    # ### end Alembic commands ###
