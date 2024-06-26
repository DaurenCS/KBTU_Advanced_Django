"""migrations

Revision ID: a9e85dba63b1
Revises: 04c140ccfbfa
Create Date: 2024-05-05 17:31:40.010252

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9e85dba63b1'
down_revision: Union[str, None] = '04c140ccfbfa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('orders', 'created_at',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('orders', 'created_at',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
