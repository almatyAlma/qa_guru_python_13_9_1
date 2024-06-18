import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: str
    subjects: str
    hobbies: list
    photo: str
    path: str
    current_address: str
    state: str
    city: str


