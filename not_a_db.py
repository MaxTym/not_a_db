from sys import argv
import csv

class NotDataBase:


    def __init__(self, data_filename="not_a_db.db"):
        self.data_filename = data_filename
        self.data = []
        with open(self.data_filename, "r") as f:
            for line in f:
                self.data.append(line.strip())

    def __getitem__(self, index):
        return self.data[index]

    def add(self, new_item):
        self.data.append(new_item)
        self._save()

    def remove(self, index):
        try:
            index = int(index)
        except:
            pass
        if isinstance(index, int):
            self.data.pop(index)
        else:
            if index in self.data:
                self.data.pop(self.data.index(index))
        self._save()

    def clear(self):
        self.data = []
        self._save()

    def _save(self):
        with open(self.data_filename, "w") as f:
            for d in self.data:
                f.write(d)
                f.write("\n")


def read_data():
        user_data = []
        with open ('not_a_db.db') as f:
            reader = csv.DictReader(f, fieldnames=['user_name', 'password', 'full name', 'pn'], delimiter=',')
            for row in reader:
                user_data.append(row)
            return user_data


def check_login(user_login):
        for i in read_data():
            if i['user_name'] == user_login:
                password = input("Enter a password: ")
                if i['password'] == password:
                    return True


def main():
    db = NotDataBase()
    while True:
        user_login = input("Enter your login: ")
        if check_login(user_login):
            print("yes")
            choice = input("To see a db enter '1'\nTo add something enter '2'\nTo remove something enter '3'")
            if choice == '1':
                for k, v in enumerate(db):
                    if (v.split(',')[0]) == user_login:
                        print(v.split(',')[2:])
                        continue
            elif choice == '2':
                new_user = ''
                add_user_name = input("Enter a user_name: ")
                new_user += add_user_name + ','
                add_password = input("Enter a password: ")
                new_user += add_password + ','
                add_full_name = input("Enter a full name: ")
                new_user += add_full_name + ','
                add_pn = input("Enter a phone number: ")
                new_user += add_pn + ','
                db.add(new_user)
                
            elif choice == '3':
                index = input("Enter a number of line to remove: ")
                db.remove(index)
        else:
            print("wrong login")






if __name__ == "__main__":
    main()
