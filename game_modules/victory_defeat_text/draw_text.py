import pygame
import game_modules.__settings__ as m_settings
import game_modules.main_screen as m_screen 


pygame.font.init()

font = pygame.font.SysFont('corbel', 60)
main_title_font = pygame.font.SysFont('impact', 140)
lower_title_font = pygame.font.SysFont('impact', 40)
text_color = (255, 0, 0)

text_victory = font.render("Victory!", True, text_color)
victory_cord_tuple = (315, 370)

text_defeat = font.render("You lost!", True, text_color)
defeat_cord_tuple = (310, 370)


title_text = main_title_font.render("ARCANOID", True, text_color)
title_lower_text = lower_title_font.render("game", True, text_color)

main_title_cord_tuple = (120, 25)
lower_title_cord_tuple = (360, 165)


"""
'comicsansms' 'impact'

# 'arial', 'arialblack', 'bahnschrift', 'calibri', 'cambria', 'cambriamath', 'candara', 'comicsansms', 
'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi',
'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole',
'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhenghei', 'microsoftjhengheiui',
'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyahei', 'microsoftyaheiui',
'microsoftyibaiti', 'mingliuextb', 'pmingliuextb', 'mingliuhkscsextb', 'mongolianbaiti', 'msgothic', 'msuigothic',
'mspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets',
'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold',
'segoeuisemilight', 'segoeuisymbol', 'simsun', 'nsimsun', 'simsunextb', 'sitkasmall', 'sitkatext', 'sitkasubheading',
'sitkaheading', 'sitkadisplay', 'sitkabanner', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana',
'webdings', 'wingdings', 'yugothic', 'yugothicuisemibold', 'yugothicui', 'yugothicmedium', 'yugothicuiregular', 'yugothicregular',
'yugothicuisemilight', 'holomdl2assets' 

"""