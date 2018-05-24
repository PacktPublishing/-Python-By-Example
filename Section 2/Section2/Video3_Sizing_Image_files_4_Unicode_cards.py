'''
Created on Apr 27, 2018
https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
https://www.branah.com/unicode-converter
https://en.wikipedia.org/wiki/UTF-16
@author: Burkhard A. Meier
'''




Unicode_playing_cards = {
'ACE OF SPADES':   [u'\0001F0A1', 'Ace_of_spades', u'\ud83c\udca1', 'black', 0, 0],   # ... card color, row, col
'TWO OF SPADES':   [u'\0001F0A2', '2_of_spades', u'\ud83c\udca2', 'black', 0, 0],
'THREE OF SPADES': [u'\0001F0A3', '3_of_spades', u'\ud83c\udca3', 'black', 0, 0],
'FOUR OF SPADES':  [u'\0001F0A4', '4_of_spades', u'\ud83c\udca4', 'black', 0, 0],
'FIVE OF SPADES':  [u'\0001F0A5', '5_of_spades', u'\ud83c\udca5', 'black', 0, 0],
'SIX OF SPADES':   [u'\0001F0A6', '6_of_spades', u'\ud83c\udca6', 'black', 0, 0],
'SEVEN OF SPADES': [u'\0001F0A7', '7_of_spades', u'\ud83c\udca7', 'black', 0, 0],
'EIGHT OF SPADES': [u'\0001F0A8', '8_of_spades', u'\ud83c\udca8', 'black', 0, 0],
'NINE OF SPADES':  [u'\0001F0A9', '9_of_spades', u'\ud83c\udca9', 'black', 0, 0],
'TEN OF SPADES':   [u'\0001F0AA', '10_of_spades', u'\ud83c\udcaa', 'black', 0, 0],
'JACK OF SPADES':  [u'\0001F0AB', 'Jack_of_spades', u'\ud83c\udcab', 'black', 0, 0],
'QUEEN OF SPADES': [u'\0001F0AD', 'Queen_of_spades', u'\ud83c\udcad', 'black', 0, 0],
'KING OF SPADES':  [u'\0001F0AE', 'King_of_spades', u'\ud83c\udcae', 'black', 0, 0],

'ACE OF HEARTS':   [u'\0001F0B1', 'Ace_of_hearts', u'\ud83c\udcb1', 'red', 0, 0],
'TWO OF HEARTS':   [u'\0001F0B2', '2_of_hearts', u'\ud83c\udcb2', 'red', 0, 0],
'THREE OF HEARTS': [u'\0001F0B3', '3_of_hearts', u'\ud83c\udcb3', 'red', 0, 0],
'FOUR OF HEARTS':  [u'\0001F0B4', '4_of_hearts', u'\ud83c\udcb4', 'red', 0, 0],
'FIVE OF HEARTS':  [u'\0001F0B5', '5_of_hearts', u'\ud83c\udcb5', 'red', 0, 0],
'SIX OF HEARTS':   [u'\0001F0B6', '6_of_hearts', u'\ud83c\udcb6', 'red', 0, 0],
'SEVEN OF HEARTS': [u'\0001F0B7', '7_of_hearts', u'\ud83c\udcb7', 'red', 0, 0],
'EIGHT OF HEARTS': [u'\0001F0B8', '8_of_hearts', u'\ud83c\udcb8', 'red', 0, 0],
'NINE OF HEARTS':  [u'\0001F0B9', '9_of_hearts', u'\ud83c\udcb9', 'red', 0, 0],
'TEN OF HEARTS':   [u'\0001F0BA', '10_of_hearts', u'\ud83c\udcba', 'red', 0, 0],
'JACK OF HEARTS':  [u'\0001F0BB', 'Jack_of_hearts', u'\ud83c\udcbb', 'red', 0, 0],
'QUEEN OF HEARTS': [u'\0001F0BD', 'Queen_of_hearts', u'\ud83c\udcbd', 'red', 0, 0],
'KING OF HEARTS':  [u'\0001F0BE', 'King_of_hearts', u'\ud83c\udcbe', 'red', 0, 0],

'ACE OF DIAMONDS':   [u'\0001F0C1', 'Ace_of_diamonds', u'\ud83c\udcc1', 'red', 0, 0],
'TWO OF DIAMONDS':   [u'\0001F0C2', '2_of_diamonds', u'\ud83c\udcc2', 'red', 0, 0],
'THREE OF DIAMONDS': [u'\0001F0C3', '3_of_diamonds', u'\ud83c\udcc3', 'red', 0, 0],
'FOUR OF DIAMONDS':  [u'\0001F0C4', '4_of_diamonds', u'\ud83c\udcc4', 'red', 0, 0],
'FIVE OF DIAMONDS':  [u'\0001F0C5', '5_of_diamonds', u'\ud83c\udcc5', 'red', 0, 0],
'SIX OF DIAMONDS':   [u'\0001F0C6', '6_of_diamonds', u'\ud83c\udcc6', 'red', 0, 0],
'SEVEN OF DIAMONDS': [u'\0001F0C7', '7_of_diamonds', u'\ud83c\udcc7', 'red', 0, 0],
'EIGHT OF DIAMONDS': [u'\0001F0C8', '8_of_diamonds', u'\ud83c\udcc8', 'red', 0, 0],
'NINE OF DIAMONDS':  [u'\0001F0C9', '9_of_diamonds', u'\ud83c\udcc9', 'red', 0, 0],
'TEN OF DIAMONDS':   [u'\0001F0CA', '10_of_diamonds', u'\ud83c\udcca', 'red', 0, 0],
'JACK OF DIAMONDS':  [u'\0001F0CB', 'Jack_of_diamonds', u'\ud83c\udccb', 'red', 0, 0],
'QUEEN OF DIAMONDS': [u'\0001F0CD', 'Queen_of_diamonds', u'\ud83c\udccd', 'red', 0, 0],
'KING OF DIAMONDS':  [u'\0001F0CE', 'King_of_diamonds', u'\ud83c\udcce', 'red', 0, 0],
 
'ACE OF CLUBS':   [u'\0001F0D1', 'Ace_of_clubs', u'\ud83c\udcd1', 'black', 0, 0],
'TWO OF CLUBS':   [u'\0001F0D2', '2_of_clubs', u'\ud83c\udcd2', 'black', 0, 0],
'THREE OF CLUBS': [u'\0001F0D3', '3_of_clubs', u'\ud83c\udcd3', 'black', 0, 0],
'FOUR OF CLUBS':  [u'\0001F0D4', '4_of_clubs', u'\ud83c\udcd4', 'black', 0, 0],
'FIVE OF CLUBS':  [u'\0001F0D5', '5_of_clubs', u'\ud83c\udcd5', 'black', 0, 0],
'SIX OF CLUBS':   [u'\0001F0D6', '6_of_clubs', u'\ud83c\udcd6', 'black', 0, 0],
'SEVEN OF CLUBS': [u'\0001F0D7', '7_of_clubs', u'\ud83c\udcd7', 'black', 0, 0],
'EIGHT OF CLUBS': [u'\0001F0D8', '8_of_clubs', u'\ud83c\udcd8', 'black', 0, 0],
'NINE OF CLUBS':  [u'\0001F0D9', '9_of_clubs', u'\ud83c\udcd9', 'black', 0, 0],
'TEN OF CLUBS':   [u'\0001F0DA', '10_of_clubs', u'\ud83c\udcda', 'black', 0, 0],
'JACK OF CLUBS':  [u'\0001F0DB', 'Jack_of_clubs', u'\ud83c\udcdb', 'black', 0, 0],
'QUEEN OF CLUBS': [u'\0001F0DD', 'Queen_of_clubs', u'\ud83c\udcdd', 'black', 0, 0],
'KING OF CLUBS':  [u'\0001F0DE', 'King_of_clubs', u'\ud83c\udcde', 'black', 0, 0],

'PLAYING CARD BACK': [u'\0001F0A0', 'Back_of_card', u'\ud83c\udca0', 'black', 0, 0]
}


if __name__ == "__main__":
    for key, value in Unicode_playing_cards.items():
        print(value[1])











