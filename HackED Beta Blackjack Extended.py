import pygame as pg
import random as rnd
from pygame.locals import *

# Global variables for easy changes
screen_width =1200
screen_height = 900
timer = None
window = None
fps = 30
bg = pg.Color(0, 120, 0)

# creating list of all cards
suits = ["club", "dia", "heart", "spade"]
royalty = ["j", "q", "k"]
cards = []
card_val = []

for suit in suits:
	ace_card = "a" + "_" + suit
	cards.append(ace_card)
	for card_num in range (2, 11):
		card = str(card_num) + "_" + suit
		cards.append(card)
	for royal in royalty:
		card = str(royal) + "_" + suit
		cards.append(card)


class button():
	def __init__(self, color, x,y,width,height, text=''):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text

	def draw(self,win,outline=None):
		#Call this method to draw the button on the screen
		if outline:
			pg.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

		pg.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

		if self.text != '':
			font = pg.font.SysFont('cambria', 60)
			text = font.render(self.text, 1, (0,0,0))
			win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

	def over(self,pos):
		#Pos is the mouse position or a tuple of (x,y) coordinates
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True

		return False

def setup():
	img_call_list = []
	return img_call_list


def card_deal():
	dealt_cards = [None] * 10
	loop_cond = True
	while loop_cond:
		for card in range(len(dealt_cards)):
			dealt_cards[card] = rnd.randint(0,51)
			for i in range(52):
				if dealt_cards.count(i) > 1:
					loop_cond = True
					break
				else:
					loop_cond = False
	return dealt_cards


def card_img(dealt_cards, img_call_list):
	
	# Changing from card index values to actual cards
	for card in range(len(dealt_cards)):
		dealt_cards[card] = cards[dealt_cards[card]]
		card_val.append(dealt_cards[card][0])
		img_call_list.append("cards/" + dealt_cards[card] + ".png")
		img_call_list[card] = pg.image.load(img_call_list[card])
	for value in range(len(card_val)):
		card_val[value] = str(card_val[value])
		if card_val[value] == '1':
			card_val[value] = '10'
		if card_val[value] in royalty:
			card_val[value] = '10'
		if card_val[value].isalpha() is False:
			card_val[value] = int(card_val[value])
	return img_call_list, card_val


def play():
	# PyGame initialization
	pg.init()
	timer = pg.time.Clock()
	window = pg.display.set_mode((screen_width, screen_height))
	pg.display.set_caption("HackED Beta Blackjack 404")

	img_call_list, card_val = card_img(card_deal(), setup())
	hit_button = button((0,255,0), 0, 475, 225, 100,'HIT')
	stand_button = button((0,255,0), 225, 475, 225, 100,'STAND')
	quit_button = button((0,255,0), 975, 475, 225, 100, 'QUIT')
	bust_button = button((0,255,0), 400, 350, 400, 100, 'BUST! RETRY?')

	# Game Loop
	hit_list = [False] * 3 # haha hitlist
	finish = False
	stand = False
	hit_num = 0
	bust = False
	p_score = 0

	if card_val[0] == card_val[1] == 'a':
		p_score = 12
	elif card_val[0] == 'a':
		p_score = 11 + card_val[1]
	elif card_val[1] == 'a':
		p_score = 11 + card_val[0]
	else:
		p_score = card_val[0] + card_val[1]

	while finish == False:
		window.fill(bg)
		hit_button.draw(window, (0,0,0))
		stand_button.draw(window, (0,0,0))
		quit_button.draw(window, (0,0,0))
		
		window.blit(img_call_list[0], (0,575))
		window.blit(img_call_list[1], (225,575))
		window.blit(pg.image.load("cards/back.png"), (975,0))
		window.blit(img_call_list[3], (750,0))

		for event in pg.event.get():
			if bust is False:
				pos = pg.mouse.get_pos()
				if event.type == QUIT:
					finish = True
				if event.type == pg.MOUSEBUTTONDOWN:
					if hit_button.over(pos) and (hit_num != 3) and (not stand):
						hit_list[hit_num] = True
						if card_val[4+hit_num] == 'a':
							p_score += 11
							if p_score > 21:
								p_score -= 10
								if p_score > 21:
									bust = True
						else:
							p_score += card_val[4 + hit_num]
						if (card_val[0] or card_val[1]) == 'a':
							if p_score > 21:
								p_score -= 10
						if p_score > 21:
							bust = True
						hit_num += 1
					elif stand_button.over(pos):
						stand = True
						window.blit(img_call_list[2], (975,0))

					elif quit_button.over(pos):
						finish = True
					elif (hit_num == 3) or stand:
						hit_button.color = (128,128,128)

				if event.type == pg.MOUSEMOTION:
					if hit_button.over(pos) and (stand is False) and (hit_num != 3):
						hit_button.color = (255,0,0)
					elif (hit_num == 3) or stand:
						hit_button.color = (128,128,128)
					else:
						hit_button.color = (0,255,0)

					if stand_button.over(pos) and (not stand):
						stand_button.color = (255,0,0)
					elif stand:
						stand_button.color = (128,128,128)
					else:
						stand_button.color = (0,255,0)

					if quit_button.over(pos):
						quit_button.color = (255,0,0)
					else:
						quit_button.color = (0,255,0)

			if bust is True:
				hit_button.color = (128,128,128)
				stand_button.color = (128,128,128)
				pos = pg.mouse.get_pos()
				bust_button.draw(window, (0,0,0))

				if event.type == QUIT:
					finish = True

				if event.type == pg.MOUSEBUTTONDOWN:
					if quit_button.over(pos):
						finish = True
					if bust_button.over(pos):
						play()

				if event.type == pg.MOUSEMOTION:
					if quit_button.over(pos):
						quit_button.color = (255,0,0)
					else: 
						quit_button.color = (0,255,0)
					if bust_button.over(pos):
						bust_button.color = (255,0,0)
					else:
						bust_button.color = (0,255,0)
			for i in range(len(hit_list)):
				if hit_list[i]:
					window.blit(img_call_list[4 + i], (450 + 225*i,575))
			if stand:
				window.blit(img_call_list[2], (975,0))
			
			pg.display.update()
			timer.tick(fps)

	pg.display.quit()
	pg.quit()


if __name__ == "__main__":
	play()



