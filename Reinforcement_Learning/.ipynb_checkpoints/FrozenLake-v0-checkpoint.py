import gym
from gym.envs.registration import register
import sys, tty, termios


### python arrow keyin
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            
        return ch
    
inkey = _Getch()

#MACROS
LEFT  = 0
DOWN  = 1
RIGHT = 2
UP    = 3

#Key mapping
arrow_keys = {
    '\x1b[A' : UP,
    '\x1b[B' : DOWN,
    '\x1b[C' : RIGHT,
    '\x1b[D' : LEFT
}


env = gym.make('FrozenLake-v0')
env.reset()
env.render() #Show the initial board

while True:
    #Choose an action from keyboard
    key = inkey()
    if key not in arrow_keys.keys():
        print("Game aborted!")
        break
        
    action = arrow_keys[key]
    state, reward, done, info = env.step(action)
    env.render() #Show the board after action
    print("State :", state, "Action :", action, "Reward :", reward, "info :", info)
    print()
    
    if done:
        print("Finished with reward", reward)
        break