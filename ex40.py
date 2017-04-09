class Song(object):
	
	math = 3
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
	def do_some_math(self):
		return self.lyrics ** 3
			
happy_bday = Song(["Happy Birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They are rally around the family", "With pockets full of shells"])

no_pasa_nada = Song(['No pasa nada', 'No pasaaaaa nada', 'ohhh oh oooh'])

tryout = ['send someone to love me', 'in pouring rain', 'through this pain']

betterman = Song(tryout)
mathp = Song(2)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
no_pasa_nada.sing_me_a_song()
betterman.sing_me_a_song()

print mathp.do_some_math()
print mathp.math

mathp.math = 8

print betterman.math, mathp.math
