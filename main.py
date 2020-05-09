import json

def main():
    '''
    This is the main fucntion where the code going to be called
    all loads and dumps happens here

    :return: None
    '''
    # TODO: json loads

    try:
        long_term_target = json.loads(open("./Database/long_term_target.json"))
    except:
        long_term_target = {1:"test", 2:"test2"}
        print("Error in loading")


    print("Hello World")
    print("Testing shortcut")
    for x in long_term_target:
        print(str(x)+". "+long_term_target[x])

    # TODO: json dumps

main()