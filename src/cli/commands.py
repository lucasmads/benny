from auth import AuthService
from user_manager import UserManager
from role_manager import RoleManager
from services.access_service import AccessService
from statistics import Statistics

from cli.prompts import (
    username,
    role,
    permission
)


users = UserManager()
roles = RoleManager()
access = AccessService()
stats = Statistics()
auth = AuthService()


def execute(choice):

    if choice == "1":

        data = users.all()

        print()

        if not data:

            print("No users found.")
            return

        for user in data:

            print(
                f"{user['username']} "
                f"({user['role']})"
            )

    elif choice == "2":

        user = username()
        user_role = role()

        if users.create(
            user,
            user_role
        ):

            print("User created.")

        else:

            print("User already exists.")

    elif choice == "3":

        data = roles.all()

        print()

        if not data:

            print("No roles found.")
            return

        for item in data:

            print(
                f"{item['name']} "
                f"-> {len(item['permissions'])} permissions"
            )

    elif choice == "4":

        role_name = role()

        if roles.create(role_name):

            print("Role created.")

        else:

            print("Role already exists.")

    elif choice == "5":

        user = username()
        perm = permission()

        access.check(
            user,
            perm
        )

    elif choice == "6":

        stats.print_summary()

    else:

        print("Unknown option.")
