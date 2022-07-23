"""create model table

Revision ID: 44bbf4d8d33b
Revises: 26ed11389b99
Create Date: 2022-07-24 03:47:09.324390

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy.schema as schema
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = '44bbf4d8d33b'
down_revision = '26ed11389b99'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(schema.CreateSequence(schema.Sequence('model_id_seq'))),
    op.create_table(
        'model',
        sa.Column('id', sa.Integer, primary_key = True, server_default = sa.text("nextval('model_id_seq'::regclass)")),
        sa.Column('name', sa.String(100), nullable = False),
        sa.Column('description', sa.TEXT, nullable = True),
        sa.Column('image_url', sa.TEXT),
        sa.Column('status', sa.Boolean),
        sa.Column('updated_at', sa.DateTime, server_default=func.now(), server_onupdate=func.now()),
        sa.Column('created_at', sa.DateTime, server_default=func.now())   
    )


def downgrade() -> None:
    op.drop_column('model', 'id')
    op.drop_table('model')
    op.execute(schema.DropSequence(schema.Sequence("model_id_seq")))
