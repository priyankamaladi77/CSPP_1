'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
def clean_string(string):
    '''remove the special characters'''
    string = string.ascii_letters + string.digit + ' '
    return(string)

def main():
    '''clean the string'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
