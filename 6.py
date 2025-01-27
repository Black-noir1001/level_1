def count_word(string):
    count = 1
    sr = list(string)
    for i in range(len(sr)) :
        if sr[i] == " " :
            count += 1
    print(count)
count_word("hi si loka goka")