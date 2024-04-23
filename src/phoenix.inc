

***    
*** BUILD OPTIONS
***

	.ifdef	RELEASE
    OPT_DISABLE_BG_LAYER=0            | LEAVE AT 0!!!
    OPT_DISABLE_FG_LAYER=0            | LEAVE AT 0!!!
    OPT_START_SCORE=0                 | LEAVE AT 0!!!
	OPT_SKIP_INTRO=0                  | LEAVE AT 0!!!
	.else
	
    * hardware options
    OPT_DISABLE_BG_LAYER=0
    OPT_DISABLE_FG_LAYER=0
  
	* permanent cheats/hacks to test game
 	OPT_SKIP_INTRO=0
    * score is BCD format???
	* all options are zeroed for release
    OPT_START_SCORE=0x0
	.endif
	
***
*** end of BUILD OPTIONS
***




* sound ordinals



	.equ	SHOT_SND,                      0
	.equ	SHOT_BOUNCES_1_SND,                          1
	.equ	SHOT_BOUNCES_2_SND,                     2
	.equ	SHIELD_SND,                      3
	.equ	EXPLOSION_SND,               4
	.equ	BIRD_SHOT_SND,                      5
	.equ	ATTACK_LOOP_SND,                    6
	.equ	VULTURE_SHOT_SND,              7
	.equ	VULTURE_BACK_1_SND,              8
	.equ	VULTURE_BACK_2_SND,              9
	.equ	BOSS_SND,              10
	.equ	BOSS_SHIELD_SHOT_1,              11
	.equ	BOSS_SHIELD_SHOT_2,              12
	.equ	START_MUSIC_SND,              13
	.equ	BOSS_END_MUSIC_SND,              14




    
