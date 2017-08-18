"""Period added to submission

Revision ID: d11668d40499
Revises: 0ca342e59e09
Create Date: 2017-08-18 23:30:10.770974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd11668d40499'
down_revision = '0ca342e59e09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fund_submission', sa.Column('period', sa.String(length=45), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('fund_submission', 'period')
    # ### end Alembic commands ###
