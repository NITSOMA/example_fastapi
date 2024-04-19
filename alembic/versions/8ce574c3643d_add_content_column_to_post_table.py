"""add content column to post table

Revision ID: 8ce574c3643d
Revises: a3419bc0c464
Create Date: 2024-04-18 21:25:25.402831

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ce574c3643d'
down_revision: Union[str, None] = 'a3419bc0c464'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
    
