"""Added a WeightLog model in database

Revision ID: 76eb4d91fe9d
Revises: 
Create Date: 2025-03-17 22:39:06.931913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76eb4d91fe9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weight_log')
    op.drop_table('exercise_log')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=20), nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('exercise_log',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('exercise', sa.VARCHAR(length=50), nullable=False),
    sa.Column('sets', sa.INTEGER(), nullable=False),
    sa.Column('reps', sa.INTEGER(), nullable=False),
    sa.Column('weight', sa.FLOAT(), nullable=False),
    sa.Column('rpe', sa.INTEGER(), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weight_log',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('weight', sa.FLOAT(), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
