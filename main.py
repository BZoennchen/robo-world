
import roboworld as rw

def example():
    text= """############
#----LL----#
#----------#
#----R-----#
#-O--------#"""
    world = rw.str_to_world(text)
    fig = world.show(scale=0.3)
    fig.savefig('./world-str-to-world.png')
    robo = world.robo

if __name__ == "__main__":
    example()