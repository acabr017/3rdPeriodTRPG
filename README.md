# 3rdPeriodTRPG
This is the repo for my 3rd period's text based rpg game. Each file belongs to a particular student, working on a feature of the text based game. 

			Fantasy
Enemies/Player - Cabrera
	- Unique
		- Making a bunch of different kinds of enemies
			-Unique attributes
				-HP
				-Def
				-Str
				-Weaknesses
				-Loot
	- Area-dependent
	- Player:
	EXAMPLE:
		- Give them the choice between:
			1. Fighter
				~ High HP/def/Str
				~ low MP/agility
				~ Middle accuracy
						10,	8 , 7, 5, 4, 3	
						Str, def, HP, dex, luck int
			2. Mage
				~ High MP/Accuracy/Agility
				~ Low HP/Str
				~ Middle def
						10,	8 , 7, 5, 4, 3	
						int, dex, luck, def, hp, str
						
			3. Ranger
				~ High Accuracy,Agility,Str
				~ Low def/hp
				~ Middling mp
						10,	8 , 7, 5, 4, 3	
						Dex, luck, wisdom,def, str, hp,
						
	Skills/Attributes
	- Strength - how hard the user can hit, if they hit
	- Accuracy - how likely the user can hit
	- Defence - how much damage an attack to the user does, if it hits
	- Agility - how likely the user can dodge an incoming attack
	- HP - how much health the user has
	- MP - how much mana the user has to cast spells/spells stronger
	- Spells?
	- In future: combat skills
	- levels
		- every level they gain N amount of skill points.
		- Skill progression will be class based
		6,4,3,2,1,1
	- exp
		- Enemy/Puzzle based? 
			def exp_calculator(enemy):
				if enemy = "goblin" -> exp + 20
				elif enemy = "bugbear" -> exp + 60
	= Story person should be able to call (a) functions(s) to create and implement the enemies/player
	= must use functions/classes to implement these behaviours
	* Standardize the attributes
Items - Alejandro
	- Unique items:
		- weapons
			- distinct bonuses/attributes
			- damage attributes
			- accuracy attributes
			- elemental attribute *
			- melee/ranged/magic
		- armour
			- distinct bonuses/attributes
			- Def attributes
			- hp attributes
			- elemental attributes
			- offensive? 
			- set bonuses
		- potions
			-hp
			-mp
			-stat increasing/decreasing potions
			-poisons
	= callable functions that define the attributes when called 
	= integrate with inventory/combast/skills
	= must use functions/classes to implement these behaviours
	
Inventory - Chris
	- Add/Remove
	- Use them
	- Fixed? Expandable?
	- See entire inventory
		- specific items
			- show attributes
	= must use functions/classes to implement these behaviours

	
Combat
	- Turn based
	- RNG crits
		- Formula for crits that depends on: STR, ACC, MP
	- Misses
	- run away
		- consequences
	- item use
	- menu
	- status effects
	- damage calculations/ keeping track
	- special attacks
	- health bar/mana bar
	- death?
	

Story/Map-design - David
	- on paper: map
		- NO LINEAR GAMES
		- map should have all the connections to areas/rooms
		- user choice to go forward/back *
	- implement enemies/items/puzzles
	- main menu
	- restarting game
	- dealing with death/winning?
		- new life + ?
	- early exit
	

			

