"""empty message

Revision ID: 7944ed16acd6
Revises: 4d238dec0fa4
Create Date: 2019-12-13 16:33:40.913517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7944ed16acd6'
down_revision = '4d238dec0fa4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('song_id', sa.Integer(), nullable=True))
    op.drop_index('ix_answer_answer', table_name='answer')
    op.create_foreign_key(None, 'answer', 'song', ['song_id'], ['id'])
    op.drop_index('ix_song_answer', table_name='song')
    op.drop_column('song', 'answer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('song', sa.Column('answer', sa.VARCHAR(length=120), nullable=True))
    op.create_index('ix_song_answer', 'song', ['answer'], unique=1)
    op.drop_constraint(None, 'answer', type_='foreignkey')
    op.create_index('ix_answer_answer', 'answer', ['answer'], unique=1)
    op.drop_column('answer', 'song_id')
    # ### end Alembic commands ###
