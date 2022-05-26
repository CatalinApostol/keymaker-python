import math

def shift_characters(word, shift):
    """
    shift_characters('abby', 5)
    'fggd'
    """
    return ''.join(chr((ord(char) - 97 + shift) % 26 + 97) for char in word)
                

def pad_up_to(word, shift, n):
    """
    >>> pad_up_to('abb', 5, 11)
    'abbfggkllpq'
    """
    chara=''
    chara+=word
    while len(chara) <n:
        word=shift_characters(word, shift)
        chara+=word  
    return chara[:n]


def abc_mirror(word):
    """
    >>> abc_mirror('abcd')
    'zyxw'
    """
    new_word=''
    for char in word:
        new_word += chr(122-(ord(char)-97))
    return new_word
    


def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    my_list=[]
    for char in word2:
        shift = ord(char) - 97
        my_list.append(shift_characters(word1, shift))
    return my_list

def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """
    my_string=''
    word=''
    for j in range(len(matrix[0])):
        if j%2==0:
            for i in range(len(matrix)):
                word=matrix[i]
                my_string+=word[j]
        else:
            for i  in range(len(matrix)-1,-1,-1):
                word=matrix[i]
                my_string+=word[j]
    return my_string


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    return word[-n:] + word[:-n]


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    i=0
    new_word=''
    for i in range(len(word)):
        result =math.sqrt(i)
        if result - int(result) ==0:
            new_word+=word[i]
    return new_word
        


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    flag=0
    new_word=''
    initial=0
    while initial < len(word):
        if flag ==0:
            for i in range(block_length):
                new_word+=word[initial]
                initial +=1
                if initial== len(word):
                    break
                
            flag = 1
        elif flag == 1:
            initial += block_length
            flag =0
    return new_word

        
        


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    new_word=word[:n]
    return new_word[n:] + new_word[:n-1]


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    # name = input("Enter your name! ").lower()
    # print(f'Your key: {hash_it(name)}')
    #print(shift_characters('abby',5))
    #print(pad_up_to('abb', 5, 11))
    #print(abc_mirror('abcd'))
    #print(create_matrix('mamas','papas'))
    #print(zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl']))
    #print(rotate_right('abcdefgh', 3))
    #print(get_square_index_chars('abcdefghijklm'))
    #print(remove_odd_blocks('abcdefghijklm', 3))
    print(reduce_to_fixed('abcdefghijklm', 6))