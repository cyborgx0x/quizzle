"""new

Revision ID: e5cf3b77d549
Revises: e67ec10c3fe2
Create Date: 2020-06-12 08:57:38.409985

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e5cf3b77d549'
down_revision = 'e67ec10c3fe2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quizbank',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=True),
    sa.Column('solution', sa.Text(), nullable=True),
    sa.Column('other_answer', sa.Text(), nullable=True),
    sa.Column('hint', sa.Text(), nullable=True),
    sa.Column('full_solution', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('url_lib')
    op.drop_index('ix_engine_post_date_gmt', table_name='engine')
    op.drop_table('engine')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('last_name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('user_name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('engine',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('post_title', mysql.VARCHAR(length=300), nullable=True),
    sa.Column('post_content', mysql.TEXT(), nullable=True),
    sa.Column('post_date_gmt', mysql.DATETIME(), nullable=True),
    sa.Column('post_excerpt', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('original_link', mysql.VARCHAR(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_engine_post_date_gmt', 'engine', ['post_date_gmt'], unique=False)
    op.create_table('url_lib',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('website_name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('website_url', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('website_title_tag', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('website_body_tag', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('quizbank')
    # ### end Alembic commands ###
