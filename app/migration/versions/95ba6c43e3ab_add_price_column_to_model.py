"""add price column to model

Revision ID: 95ba6c43e3ab
Revises: 4ff1d27bf026
Create Date: 2022-07-24 18:34:50.694564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95ba6c43e3ab'
down_revision = '4ff1d27bf026'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.add_column('model', sa.Column('price', sa.DECIMAL )),


def downgrade() -> None:
    op.drop_column('model','price')
