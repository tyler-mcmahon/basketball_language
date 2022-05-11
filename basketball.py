from lark import Lark
import sys

my_grammar = """
?start: statement			
?statement: expression+
?expression: play
?play: name + action + "."    
name: NAME + NAME
action: rebound
      | make
      | miss
      | steal
      | block
      | turnover
      | fouls
      | assist
assist: "assist"
rebound: "rebound" + category
make: "makes" + attempt
miss: "misses" + attempt
steal: "steal"
block: "block"
turnover: "turnover"
?category: offensive | defensive
offensive: "offensive" -> oreb
defensive: "defensive" -> dreb
?attempt: twopointer | threepointer | freethrow
twopointer: "two pointer"
threepointer: "three pointer"
freethrow: "free throw"
fouls: "foul" 
%import common.NUMBER
%import common.WS
%ignore WS
%import common.CNAME -> NAME
 """   
def boxscore(t, env):
	global makeormiss
	global twoorthree
	if t.data == 'statement':
		for child in t.children:
			boxscore(child, env)
	elif t.data == 'play':
		for child in t.children:
			boxscore(child, env)
	elif t.data == 'name':
		if t.children[0] + ' ' +t.children[1] not in env:
			global name
			name = t.children[0] + ' ' +t.children[1]
			env[name] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		else:
			name = t.children[0] + ' ' +t.children[1]
	elif t.data == 'action':
		for child in t.children:
			#print(child)
			boxscore(child, env)
	elif t.data == 'assist':
		env[name][12] += 1	#+1 assist
	elif t.data == 'steal':
		env[name][13] += 1	#+1 steal
	elif t.data == 'block':
		env[name][14] += 1	#+1 block
	elif t.data == 'turnover':
		env[name][15] += 1	#+1 TO			
	elif t.data == 'fouls':
		env[name][16] += 1	#+1 foul
	elif t.data == 'rebound':
		for child in t.children:
			boxscore(child, env)
	elif t.data == 'dreb':
		env[name][10] += 1	#+1 DREB
		env[name][11] += 1	#+1 REB
	elif t.data == 'oreb':
		env[name][9] += 1	#+1 OREB
		env[name][11] += 1	#+1 REB	
	elif t.data == 'make':
		makeormiss = 'make'
		for child in t.children:
			boxscore(child, env)
	elif t.data == 'miss':
		makeormiss = 'miss'
		for child in t.children:
			boxscore(child, env)			
	elif t.data == 'twopointer' or t.data == 'threepointer' or t.data == 'freethrow':
		if makeormiss == 'make':
			if t.data == 'twopointer':
				env[name][17] += 2	#Make +2 pts
				env[name][0] += 1	#Make +1 FGM
				env[name][1] += 1	#Make +1 FGA
				env[name][2] = round(env[name][0] / env[name][0] * 100,1) #FG%
			elif t.data == 'freethrow':
				env[name][17] += 1	#Make +1 pts
				env[name][6] += 1	#Make +1 FTM
				env[name][7] += 1	#Make +1 FTA
				env[name][8] = round(env[name][6] / env[name][7] * 100,1)	#FT%
			else:
				env[name][17] += 3	#Make +3 pts
				env[name][3] += 1	#Make +1 3PM
				env[name][4] += 1	#Make +1 3PA
				env[name][5] = round(env[name][3] / env[name][4] * 100, 1)	#3PT%
				env[name][0] += 1		#Make +1 FGM
				env[name][1] += 1		#Make +1 FGA
				env[name][2] = round(env[name][0] / env[name][1] * 100,1) #FG%
		else:
			if t.data == 'twopointer':
				env[name][1] += 1	#Make +1 FGA
				env[name][2] = round(env[name][0] / env[name][1] * 100,1) #FG%
			elif t.data == 'freethrow':
				env[name][7] += 1	#Make +1 FTA
				env[name][8] = round(env[name][6] / env[name][7] * 100,1)	#FT%
			else:
				env[name][4] += 1	#Make +1 3PA
				env[name][5] = round(env[name][3] / env[name][4] * 100, 1)	#3PT%
				env[name][1] += 1		#Make +1 FGA
				env[name][2] = round(env[name][0] / env[name][1] * 100,1) #FG%
	else:
		return "error" 

parser = Lark(my_grammar)
with open(sys.argv[1], 'r') as f:
	contents = f.read()

parse_tree = parser.parse(contents)
#print(parse_tree.pretty())
env = {
}
boxscore(parse_tree, env)
print('FGM  FGA  FG%  3PM  3PA  3PT%  FTM  FTA  FT%  OREB  DREB  REB  AST  STL  BLK  TO  PF  PTS')
for name in env:
	print(name, env[name])
