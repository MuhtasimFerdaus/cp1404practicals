"""
Email storage
Estimate: 30 minutes
Actual:   32 minutes
"""
def main():
    email_to_name = {}

    email = input("Email: ").strip()
    while email:
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("y", ""):
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    print("\nStored User Information:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


if __name__ == "__main__":
    main()
