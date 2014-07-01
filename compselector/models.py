from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Champ(models.Model):
	name = models.CharField(max_length=32)
	attack_range = models.CharField(max_length=6)
	ranged = models.BooleanField()
	mov_speed = models.CharField(max_length=6)
	cost_type = models.CharField(max_length=32)
	# cost type
	#	{ mana, health, energy, free, fury, heat, etc }
	# list skills
	#	{ Passive, Q, W, E, R }
	# list aspect ratings

	def __unicode__(self):
		return u'%s\n' % (self.name)

class Skill(models.Model):
	champ = models.ForeignKey(Champ)
	name = models.CharField(max_length=32)
	SKILL_TYPE = (
		('Passive', 'Passive'),
		('Q', 'Q'),
		('W', 'W'),
		('E', 'E'),
		('R', 'R'),
	)
	key = models.CharField(max_length=7, choices=SKILL_TYPE)
	cost = models.IntegerField(max_length=6)
	range = models.IntegerField(max_length=6)
	cool_down = models.IntegerField(max_length=6)
	# list tags

	def __unicode__(self):
		return u'%s\n' % (self.name)

class Type(models.Model):
	name = models.CharField(max_length=64)
	# Types - Last updated 6/30
	#	Damage
	#		AD, AP, buff_dps
	#	Crowd Control
	#		airborne, blind, entangle, root, forced_action, polymorph, silence, slow
	#		stun, suppression, flee, knock_up, knock_down, knock_aside, taunt, fear
	#	Mobility
	#		dash, buff_mov, gap_closer, jump
	#	Sustain
	#		heal, cost_sustain, buff_tank, shield
	#	Utility
	#		aura, vision, trap, interrupt, disengage, main_init, follow_up_init, dunk,
	#		resets, stealth, global, DoT, aa_reset, hook, applies_on_hit, zoning, AoE,
	#		can_hit_structure, 
	#	Target Type
	#		auto_target, targeted, skillshot, self

	def __unicode__(self):
		return u'%s\n' % (self.name)

class Tag(models.Model):
	skill = models.ForeignKey(Skill)
	type = models.ForeignKey(Type)

	def __unicode__(self):
		return u'%s - %s\n' % (self.skill, self.type)

class AspectCategory(models.Model):
	name = models.CharField(max_length=64)
	# Categories - Last updated 6/30
	#	teamfight (5v5, 4v4), skirmish (3v3, 2v2), duel (1v1)
	# 	early, mid, late
	#	poke, burst

	def __unicode__(self):
		return u'%s' % (self.name)

class Aspect(models.Model):
	champ = models.ForeignKey(Champ)
	name = models.ForeignKey(AspectCategory)
	# each user can vote a value between 0 and 1
	value = models.FloatField()
	# each user can only vote once
	total = models.BigIntegerField()

	def __unicode__(self):
		return u'%s, %s - %0.2f\n, %d votes' % (self.champ, self.name, self.value/float(self.total), self.total)

class ChampRating(models.Model):
	user   = models.ForeignKey(User)
	aspect = models.ForeignKey(Aspect)
	value  = models.FloatField()

	def __unicode__(self):
		return u'%0.2f - %s' % (self.value, self.aspect)

class Lolcomp(models.Model):
	# time first suggested
	date = models.DateTimeField(auto_now=True)

	# JSON list of champs, in alphabetical order
	comp = models.TextField(max_length=200)

	# badge rating: { lolcomp OP, good, noob }
	num_op   = models.BigIntegerField()		# Yellow
	num_good = models.BigIntegerField()		# Green
	num_noob = models.BigIntegerField()		# Red

	# list comments

	def __unicode__(self):
		return u'%s' % (self.comp)

class Comment(models.Model):
	lolcomp = models.ForeignKey(Lolcomp)
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now=True)
	text = models.TextField(max_length=200)

	# comment ranking system, top 2 rated then by newest
	vote_up   = models.IntegerField()
	vote_down = models.IntegerField()

	def __unicode__(self):
		return u'%0.2f - %s' % (self.vote_up/float(self.vote_down), self.text)

class CompRating(models.Model):
	user    = models.ForeignKey(User)
	lolcomp = models.ForeignKey(Lolcomp)
	RATING_TYPE = (
		('lolcomp_op', 'lolComp OP'),
		('good', 'Good'),
		('noob', 'Noob'),
	)
	value   = models.CharField(max_length=10, choices=RATING_TYPE)

	def __unicode__(self):
		return u'%s - %s' % (self.value, self.lolcomp)

class Profile(models.Model):
	user = models.ForeignKey(User)

	# list champ ratings

	# list lolComp ratings

	# list comments

	# Mark will personally add each verified pro
	pro  = models.BooleanField()

	# JSON list of honors, in alphabetical order
	honors = models.TextField(max_length=200)

	def __unicode__(self):
		return u'%s - Pro: %s' % (self.user, self.pro)


