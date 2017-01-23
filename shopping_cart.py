#!/usr/bin/env python
# -*- coding:utf-8 -*-


#商品信息--名称、单价
product_list = [
    ["iphone", 6000],
    ["PC", 3000],
    ["book", 60],
    ["bike", 800]]


#用户信息- 帐号、密码、余额
with open("history.txt", "r", encoding="utf-8") as f1:
    user_dict = f1.readline().strip().split("|")
    if len(user_dict) > 2:
        balance = int(user_dict[2])
        user_dict.pop()
        user_dict.append(balance)


shopping_list = []


#显示商品信息
def show_product():
    print("商品信息".center(50, '-'))
    for i in range(len(product_list)):
        print("%s  %s  %s" % (i+1, product_list[i][0], product_list[i][1]))
    print("end".center(50, '-'))


#购物历史信息
def print_shopping_history():
    with open("history.txt", "r", encoding="utf-8") as f1:
        print("购物历史信息".center(50, '-'))
        f1.readline()
        for line in f1.readlines():
            print(line.strip())
        print("end".center(50, '-'))


#保存购物信息
def write_shopping_history():
    with open("history.txt", "a+", encoding="utf-8") as f1:
        for i in range(len(shopping_list)):
            f1.write(str(shopping_list[i]))
            f1.write("\n")


#显示购物信息
def print_shopping_information():
    print("购物清单".center(50, '-'))
    for index, item in enumerate(shopping_list):
        print(index+1, item)
    print("end".center(50, '-'))


def user_information_save():
    monkey = str(user_dict[-1])
    user_dict.pop()
    user_dict.append(monkey)
    repl = "|".join(user_dict)
    with open("history.txt", "w+", encoding="utf-8") as f1:
        f1.readline()
        all_text = f1.readlines()
        f1.write(repl)
        f1.write("\n")
        for line in all_text:
            f1.write(line)


def main():

    username = input("Enter your name:")
    password = input("Enter your password:")

    if username == user_dict[0] and password == user_dict[1]:
        print(("Welcome %s Coming here!" % username).center(50, '-'))
        if len(user_dict) == 2:
            salary = int(input("Enter salary: "))
            user_dict.append(salary)
    else:
        print("\033[0;31m")
        print("\tusername or password is wrong!")
        print("\033[0m")
        exit()

    while True:
        show_product()
        choose = input(">>")
        if choose.isdigit():
            choose = int(choose)
            if choose > len(product_list) or choose < 1:
                print("\t请输入正确的选择")
            elif user_dict[2] < product_list[choose-1][1]:
                print("\033[0;31m")
                print("\t余额：%s" % user_dict[2])
                print("\t余额不足，购买该商品！")
                print("\033[0m")
            else:
                shopping_list.append(product_list[choose-1])
                user_dict[2] -= product_list[choose-1][1]
                print("\033[0;31m")
                print("\t商品已加入购物车")
                print("\t余额：%s" % user_dict[2])
                print("\033[0m")
        elif choose == 'h':
            print_shopping_history()
        elif choose == 'q':
            print_shopping_information()
            print("\033[0;31m")
            print("\t余额：%s" % user_dict[2])
            print("\033[0m")
            user_information_save()
            write_shopping_history()
            break
        else:
            continue


if __name__ == '__main__':
    main()