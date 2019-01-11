import matplotlib.pyplot as plt

################
###   VARS   ###
################

m = 2**64-1           # Maximum Supply, usually 2**64 - 1
u = 10**9             # How many atomic units form one coin (10**decimals)
premine = 0.15        # Premine, in percent. Example: 0.15 or 15%
blocktime = 30        # Blocktime in seconds
blockheight = 1000    # Calculate reward till this blockheight.
emission_factor = 21  # Emission Factor, can be found in src/cryptnote_config.h or src/config/CryptoNoteConfig.h

################
###   CODE   ###
################

# Do not change unless you know what you're doing

blocktime = blocktime/86400 # Blocktime in Days
reward = [int(premine*m)]   # Reward of First block (premine)
supply = [int(premine*m)]   # Supply after First block (premine)
x = [blocktime]             # Time of first Block

for j in range(blockheight):
	s = supply[-1]
	r = (m-s)>>emission_factor
	if r < u:
		r = u
	reward.append(r)
	supply.append(s+r)
	x.append(x[-1]+blocktime)

plt.close()
plt.subplot(211)
for i in range(len(reward)):
	reward[i] = reward[i]/u
for i in range(len(supply)):
	supply[i] = supply[i]/(m)
plt.title('Blockreward (in Coins)')
plt.plot(x[1:],reward[1:])
plt.subplot(212)
plt.title('Total Supply (in %)')
plt.plot(x[1:],supply[1:])
plt.show(block=False)
input()
