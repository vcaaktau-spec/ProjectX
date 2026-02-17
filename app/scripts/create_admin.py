from app.db.session import SessionLocal
from app.models.user import User
from app.models.company import Company
from app.core.security import get_password_hash
import app.models


def create_admin():
    db = SessionLocal()

    # создаём компанию
    company = Company(name="VCA Test Company")
    db.add(company)
    db.commit()
    db.refresh(company)

    # создаём пользователя
    user = User(
        company_id=company.id,
        email="admin@test.com",
        password_hash=get_password_hash("admin123"),
        role="owner"
    )

    db.add(user)
    db.commit()

    print("Admin created:")
    print("Email: admin@test.com")
    print("Password: admin123")


if __name__ == "__main__":
    create_admin()
