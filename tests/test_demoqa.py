from pages.registration_page import RegistrationPage
from data.user import User


def test_registration_form():
    registration_page = RegistrationPage()
    user = User(
        first_name="firstName",
        last_name="lastName",
        email="test@gmail.com",
        gender="Female",
        mobile="7777777777",
        date_of_birth=["29", "July", "1991"],
        subjects="Computer Science",
        hobbies="Sports",
        photo="rig.jpg",
        current_address="Current Address",
        state="Haryana",
        city="Karnal",
    )

    registration_page.open()
    registration_page.fill_form(user)
    registration_page.submit_form()
    registration_page.should_registered_user_info_with(user)