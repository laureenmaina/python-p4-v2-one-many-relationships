"""add foreign key to Review

Revision ID: 3298e122d722
Revises: efdc46795454
Create Date: 2024-06-27 19:57:47.725063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3298e122d722'
down_revision = 'efdc46795454'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_reviews_employee_id_employees', 'employees', ['employee_id'], ['id'])

def downgrade():
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')