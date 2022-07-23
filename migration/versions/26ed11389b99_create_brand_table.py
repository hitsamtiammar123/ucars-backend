"""create brand table

Revision ID: 26ed11389b99
Revises: 
Create Date: 2022-07-24 03:33:05.508684

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy.schema as schema
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '26ed11389b99'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(schema.CreateSequence(schema.Sequence('brand_id_seq'))),
    op.create_table(
        'brand',
        sa.Column('id', sa.Integer, primary_key = True, server_default = sa.text("nextval('brand_id_seq'::regclass)")),
        sa.Column('name', sa.String(100), nullable = False),
        sa.Column('description', sa.TEXT, nullable = True),
        sa.Column('image_url', sa.TEXT),
        sa.Column('status', sa.Boolean),
        sa.Column('updated_at', sa.DateTime, server_default=func.now(), server_onupdate=func.now()),
        sa.Column('created_at', sa.DateTime, server_default=func.now())  
    )


def downgrade() -> None:
    op.drop_column('brand', 'id')
    op.drop_table('brand')
    op.execute(schema.DropSequence(schema.Sequence("brand_id_seq")))
