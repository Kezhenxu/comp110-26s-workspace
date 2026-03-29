rsvp_list: list[str] = ["Enrico", "Yun"]


def has_rsvped(rsvped: list[str], friend: str) -> bool:
    idx: int = 0
    while idx < len(rsvped):
        if rsvped[idx] == friend:
            return True
        idx += 1
    return False


def not_yet_rsvped(rsvped: list[str], invited: list[str]) -> list[str]:
    not_rsvped_list: list[str] = []
    index: int = 0

    while index < len(invited):

        friend: str = invited[index]

        if not has_rsvped(rsvped, friend):
            not_rsvped_list.append(friend)

        index += 1

    return not_rsvped_list
