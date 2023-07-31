
from PRODUCTManager.models import OfferList
import random
import array

def GENERATEOFFERCODE(target):
    # maximum length of password needed
    # this can be changed to suit your password length
    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_OFFERCODE = rand_digit + rand_upper + rand_lower
    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(10):
        temp_OFFERCODE = temp_OFFERCODE + random.choice(COMBINED_LIST)
        # convert temporary password into array and shuffle to
        # prEVENT it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_OFFERCODE_list = array.array('u', temp_OFFERCODE)
        random.shuffle(temp_OFFERCODE_list)

    # traverse the temporary password array and append the chars
    # to form the password
    genrateOFFERCODE = ""
    for x in temp_OFFERCODE_list:
            genrateOFFERCODE = genrateOFFERCODE + x

    if OfferList.objects.filter(product_id=target, Code=genrateOFFERCODE).exists():
        return GENERATEOFFERCODE()
    return genrateOFFERCODE




