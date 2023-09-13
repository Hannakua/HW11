"""Init

Revision ID: 2193b1c299ac
Revises: 
Create Date: 2023-09-11 22:31:49.378813

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2193b1c299ac'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.Column('birth', sa.Date(), nullable=True),
    sa.Column('otherinform', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contacts_email'), 'contacts', ['email'], unique=True)
    op.create_index(op.f('ix_contacts_firstname'), 'contacts', ['firstname'], unique=False)
    op.create_index(op.f('ix_contacts_id'), 'contacts', ['id'], unique=False)
    op.create_index(op.f('ix_contacts_lastname'), 'contacts', ['lastname'], unique=False)
    op.create_index(op.f('ix_contacts_phone'), 'contacts', ['phone'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contacts_phone'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_lastname'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_id'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_firstname'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_email'), table_name='contacts')
    op.drop_table('contacts')
    # ### end Alembic commands ###