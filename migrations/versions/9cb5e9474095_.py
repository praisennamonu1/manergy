"""empty message

Revision ID: 9cb5e9474095
Revises: 6151f9f03122
Create Date: 2023-05-18 15:12:27.491776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cb5e9474095'
down_revision = '6151f9f03122'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('achievements',
    sa.Column('user_id', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('desc', sa.String(length=128), nullable=True),
    sa.Column('id', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('slugname', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('videos',
    sa.Column('user_id', sa.String(length=128), nullable=True),
    sa.Column('thumbnail', sa.String(length=256), nullable=False),
    sa.Column('url', sa.String(length=256), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('desc', sa.String(length=512), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('keyword', sa.String(length=32), nullable=True),
    sa.Column('id', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('slugname', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_table('feedbacks',
    sa.Column('user_id', sa.String(length=128), nullable=False),
    sa.Column('task_id', sa.String(length=128), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=256), nullable=True),
    sa.Column('id', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('slugname', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedbacks')
    op.drop_table('videos')
    op.drop_table('achievements')
    # ### end Alembic commands ###