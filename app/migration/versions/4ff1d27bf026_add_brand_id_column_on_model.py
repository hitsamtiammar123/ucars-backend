"""add brand_id column on model

Revision ID: 4ff1d27bf026
Revises: 44bbf4d8d33b
Create Date: 2022-07-24 04:18:13.134988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ff1d27bf026'
down_revision = '44bbf4d8d33b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('model', sa.Column('brand_id', sa.Integer, sa.ForeignKey('brand.id') )),


def downgrade() -> None:
    op.drop_constraint('model_brand_id_fkey', 'model')
    op.drop_column('model', 'brand_id')
