"""добавили признак публикации

Revision ID: a72104cf4111
Revises: 
Create Date: 2024-03-11 19:42:14.496864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from data import db_session
from data.news import News
from data.users import User

# revision identifiers, used by Alembic.
revision: str = 'a72104cf4111'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('is_published', sa.Boolean(),
                                    nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'is_published')
    # ### end Alembic commands ###
