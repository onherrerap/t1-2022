"""empty message

Revision ID: df3a775a9518
Revises: 
Create Date: 2022-02-07 10:42:52.020548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df3a775a9518'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conferences',
    sa.Column('conference_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('fhoto_id', sa.Integer(), nullable=True),
    sa.Column('remarks', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('conference_id'),
    sa.UniqueConstraint('fhoto_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('equipments',
    sa.Column('equipment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('num', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('equipment_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('conference_equipments',
    sa.Column('conference_equipments_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('conference_id', sa.Integer(), nullable=False),
    sa.Column('equipment_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['conference_id'], ['conferences.conference_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipments.equipment_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('conference_equipments_id')
    )
    op.create_table('registers',
    sa.Column('register_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('passwd', sa.String(length=30), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('register_id')
    )
    op.create_table('reserves',
    sa.Column('reserve_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('register_id', sa.Integer(), nullable=False),
    sa.Column('conference_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=30), nullable=False),
    sa.Column('time', sa.String(length=30), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('purpose', sa.String(length=100), nullable=True),
    sa.Column('remarks', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['conference_id'], ['conferences.conference_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['register_id'], ['registers.register_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('reserve_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reserves')
    op.drop_table('registers')
    op.drop_table('conference_equipments')
    op.drop_table('users')
    op.drop_table('equipments')
    op.drop_table('conferences')
    # ### end Alembic commands ###
