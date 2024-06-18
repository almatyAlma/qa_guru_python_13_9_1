from selene import browser, have, command
import resourses
from data.user import User


class RegistrationPage:

    def __init__(self):
        self.registered_user_data = (
            browser.element(".modal-content").element("table").all("tr").all("td").even
        )
        self.month_of_birth = browser.element(".react-datepicker__month-select")

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, first_name):
        browser.element("#firstName").type(first_name)
        return self

    def fill_last_name(self, last_name):
        browser.element("#lastName").type(last_name)
        return self

    def fill_email(self, email):
        browser.element("#userEmail").type(email)
        return self

    def select_gender(self, gender):
        browser.element(f"[name=gender][value={gender}]+label").click()
        return self

    def fill_mobile(self, mobile):
        browser.element("#userNumber").type(mobile)
        return self

    def fill_date_of_birth(self, day, month, year):
        browser.element("#dateOfBirthInput").click()
        self.month_of_birth.click()
        self.month_of_birth.all("option").element_by(have.exact_text(month)).click()
        browser.element(".react-datepicker__year-select").send_keys(year)
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

    def fill_subjects(self, subject):
        browser.element("#subjectsInput").type(subject).press_enter()
        return self

    def fill_hobbies(self, hobbies):
        browser.all("[for^=hobbies-checkbox]").element_by(have.text(hobbies)).click()
        return self

    def upload_picture(self, path, photo):
        browser.element("#uploadPicture").send_keys(resourses.path(photo))
        return self

    def fill_current_address(self, address):
        browser.element("#currentAddress").type(address).perform(
            command.js.scroll_into_view
        )
        return self

    def fill_state(self, name):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_city(self, city):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(city)
        ).click()
        return self

    def submit_form(self):
        browser.element("#submit").press_enter()
        return self

    def fill_form(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_mobile(user.mobile)
        self.fill_date_of_birth(*user.date_of_birth)
        self.fill_subjects(user.subjects)
        self.fill_hobbies(user.hobbies)
        self.upload_picture(user.photo)
        self.fill_current_address(user.current_address)
        self.fill_state(user.state)
        self.fill_city(user.city)

    def should_registered_user_info_with(self, user: User):
        browser.element(".modal-content").element("table").all("tr").all(
            "td"
        ).even.should(
            have.exact_texts(
                f"{user.first_name} {user.last_name}",
                user.email,
                user.gender,
                user.mobile,
                f"{user.date_of_birth[0]} {user.date_of_birth[1]},{user.date_of_birth[2]}",
                user.subjects,
                user.hobbies,
                user.photo,
                user.current_address,
                f"{user.state} {user.city}",
            )
        )