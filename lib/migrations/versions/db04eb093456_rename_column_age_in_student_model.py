"""Rename column age in Student model

Revision ID: db04eb093456
Revises: 7cdda15af9d2
Create Date: 2023-12-07 20:12:28.517517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db04eb093456'
down_revision = '7cdda15af9d2'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.alter_column('scholars', 'grade', new_column_name='age')


def downgrade() -> None:
     op.alter_column('scholars', 'age', new_column_name='grade')
