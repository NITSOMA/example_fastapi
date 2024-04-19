"""create post table

Revision ID: a3419bc0c464
Revises: 
Create Date: 2024-04-16 13:31:09.988138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3419bc0c464'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# upgrade make table or make changes in already exist table
def upgrade() -> None:
    # first create_tavle takes name of the columns and then sqlalchemy
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True), 
                    sa.Column("title", sa.String(), nullable=False))

# roll back we put all the logic to drop table
def downgrade() -> None:
    op.drop_table('posts')
