# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def camelcase(sentence):
    title_case = sentence.title()
    upper_title_case = title_case.replace(''," ")

    return upper_title_case[1:0].lower() + upper_title_case[1:]

def banner():
    message = 'Amazing camel sentence'
    star = '*'* len(message)
    print(f'\n{star} \n{message} \n{star}')
def main():
    sentence = input('enter a sentence')
    output = camelcase(sentence)
    print(output)

if__name__ = '__main__'
main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
