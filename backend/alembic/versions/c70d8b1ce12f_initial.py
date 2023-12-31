"""Initial

Revision ID: c70d8b1ce12f
Revises: 
Create Date: 2023-11-08 08:37:28.697911

"""
from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy


# revision identifiers, used by Alembic.
revision = "c70d8b1ce12f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "grade",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("grade_name", sa.String(), nullable=False),
        sa.Column("grade_level", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_grade_grade_name"), "grade", ["grade_name"], unique=False)
    op.create_table(
        "office",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("office_name", sa.String(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_office_office_name"), "office", ["office_name"], unique=False
    )
    op.create_table(
        "task_reference",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("task_name", sa.String(), nullable=False),
        sa.Column("priority", sa.Integer(), nullable=False),
        sa.Column(
            "execution_time",
            sa.Integer(),
            nullable=False,
            comment="Execution time in seconds",
        ),
        sa.Column("min_employee_level", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_task_reference_task_name"),
        "task_reference",
        ["task_name"],
        unique=False,
    )
    op.create_table(
        "user",
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.Column("surname", sa.String(length=50), nullable=False),
        sa.Column("login", sa.String(length=32), nullable=False),
        sa.Column("phone", sa.Integer(), nullable=True),
        sa.Column("birth_date", sa.DateTime(timezone=True), nullable=True),
        sa.Column("is_admin", sa.Boolean(), server_default="false", nullable=False),
        sa.Column("is_editor", sa.Boolean(), server_default="false", nullable=False),
        sa.Column(
            "created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("id", fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_index(op.f("ix_user_login"), "user", ["login"], unique=True)
    op.create_index(op.f("ix_user_name"), "user", ["name"], unique=False)
    op.create_index(op.f("ix_user_phone"), "user", ["phone"], unique=True)
    op.create_table(
        "condition",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("task_id", sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(["task_id"], ["task_reference.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "employee_reference",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("employee_name", sa.String(), nullable=False),
        sa.Column("grade_id", sa.BigInteger(), nullable=False),
        sa.Column("office_id", sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(["grade_id"], ["grade.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["office_id"], ["office.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_employee_reference_employee_name"),
        "employee_reference",
        ["employee_name"],
        unique=False,
    )
    op.create_table(
        "task_distribution",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("task_id", sa.BigInteger(), nullable=False),
        sa.Column("employee_id", sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(
            ["employee_id"], ["employee_reference.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["task_id"], ["task_reference.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("task_distribution")
    op.drop_index(
        op.f("ix_employee_reference_employee_name"), table_name="employee_reference"
    )
    op.drop_table("employee_reference")
    op.drop_table("condition")
    op.drop_index(op.f("ix_user_phone"), table_name="user")
    op.drop_index(op.f("ix_user_name"), table_name="user")
    op.drop_index(op.f("ix_user_login"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    op.drop_index(op.f("ix_task_reference_task_name"), table_name="task_reference")
    op.drop_table("task_reference")
    op.drop_index(op.f("ix_office_office_name"), table_name="office")
    op.drop_table("office")
    op.drop_index(op.f("ix_grade_grade_name"), table_name="grade")
    op.drop_table("grade")
    # ### end Alembic commands ###
