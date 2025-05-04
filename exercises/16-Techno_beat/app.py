def lyrics_generator(lst):
    aux = ""
    count = 0

    for i in lst:
        if i == 0:
           aux += "Boom "
           count = 0

        elif i == 1:
            aux += "Drop the bass "
            count += 1

            if count == 3:
                aux += "!!!Break the bass!!! "
                count += 0

    return aux


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
