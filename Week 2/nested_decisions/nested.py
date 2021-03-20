book_cover = input("What type of cover does the book have? ( Soft or Hard )\n")

if ( book_cover == 'soft'):
    book_type = input("Is the book perfect-bound?\n")
    if ( book_type == 'yes'):
        print("Soft cover, perfect bound books are very popular!")
    elif ( book_type == 'no'): 
        print("Soft covers with coils or stitches are great for short books")
elif ( book_cover == 'hard'):
    print("Books with hard covers can be more expensive!")