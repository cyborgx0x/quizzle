"""init table

Revision ID: e67ec10c3fe2
Revises: 
Create Date: 2020-06-12 08:50:21.445988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e67ec10c3fe2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('engine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_title', sa.Unicode(length=300), nullable=True),
    sa.Column('post_content', sa.Text(), nullable=True),
    sa.Column('post_date_gmt', sa.DateTime(), nullable=True),
    sa.Column('post_excerpt', sa.Unicode(length=200), nullable=True),
    sa.Column('original_link', sa.Unicode(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_engine_post_date_gmt'), 'engine', ['post_date_gmt'], unique=False)
    op.create_table('url_lib',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('website_name', sa.String(length=100), nullable=True),
    sa.Column('website_url', sa.String(length=100), nullable=True),
    sa.Column('website_title_tag', sa.String(length=100), nullable=True),
    sa.Column('website_body_tag', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.Unicode(length=50), nullable=True),
    sa.Column('last_name', sa.Unicode(length=50), nullable=True),
    sa.Column('user_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('url_lib')
    op.drop_index(op.f('ix_engine_post_date_gmt'), table_name='engine')
    op.drop_table('engine')
    # ### end Alembic commands ###
