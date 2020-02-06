"""
Add new DeletedRepository tracking table.

Revision ID: 4fd6b8463eb2
Revises: 34c8ef052ec9
Create Date: 2019-12-22 14:58:34.375692
"""

# revision identifiers, used by Alembic.
revision = "4fd6b8463eb2"
down_revision = "34c8ef052ec9"

from alembic import op as original_op
from data.migrations.progress import ProgressWrapper
import sqlalchemy as sa


def upgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "deletedrepository",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("repository_id", sa.Integer(), nullable=False),
        sa.Column("marked", sa.DateTime(), nullable=False),
        sa.Column("original_name", sa.String(length=255), nullable=False),
        sa.Column("queue_id", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(
            ["repository_id"],
            ["repository.id"],
            name=op.f("fk_deletedrepository_repository_id_repository"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_deletedrepository")),
    )
    op.create_index(
        "deletedrepository_original_name", "deletedrepository", ["original_name"], unique=False
    )
    op.create_index("deletedrepository_queue_id", "deletedrepository", ["queue_id"], unique=False)
    op.create_index(
        "deletedrepository_repository_id", "deletedrepository", ["repository_id"], unique=True
    )
    # ### end Alembic commands ###


def downgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("deletedrepository")
    # ### end Alembic commands ###
