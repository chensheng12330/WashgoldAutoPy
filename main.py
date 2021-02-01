# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from core_action import action_tool as act


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # adb_utils.tap(0, 0)
    # action_tool.tapWithRand(20, 20)
    act.tapWithRand(20, 20)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
