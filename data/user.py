import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: list
    subjects: str
    hobbies: str
    photo: str
    current_address: str
    state: str
    city: str


