from sys import exit
from random import randint


prompt = "> "


class Scene(object):

    def enter(self):
        """
        Play out scene and return next_scene name.
        :return: next_scene_name
        """
        raise NotImplementedError("You need to override this method!")


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        load_next = True

        current_scene_name = ""
        while load_next:
            if current_scene_name in ("death", "finished"):
                load_next = False

            next_scene_name = current_scene.enter()

            current_scene = self.scene_map.next_scene(next_scene_name)
            current_scene_name = next_scene_name


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print self.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.  You are the " \
              "last surviving member and your last mission is to get the neutron destruct bomb from the Weapons " \
              "Armory, put it in the bridge, and blow the ship up after getting into an escape pod. " \
              "\n" \
              "You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly " \
              "skin, dark grimy teeth, and evil clown costume flowing around his hate filled body. He's blocking the " \
              "door to the Armory and about to pull a weapon to blast you. " \
              "\n" \
              "What do you do? " \
              "\n" \
              "Shoot at him, dodge his shot, scream for your life, beg for your life, drop on the floor " \
              "and play dead, convince it you are on its side, or tell a joke?"

        action = raw_input(prompt)

        if "shoot" in action:
            print "Quick on the draw you yank out your blaster and fire it at the Gothon. His clown costume is " \
                  "flowing and moving around his body, which throws off your aim. Your laser hits his costume but " \
                  "misses him entirely. This completely ruins his brand new costume his mother bought him, which " \
                  "makes him fly into an insane rage and blast you repeatedly in the face until you are dead. Then " \
                  "he eats you."

            return "death"

        elif "dodge" in action:
            print "Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a " \
                  "laser past your head. In the middle of your artful dodge your foot slips and you bang your head " \
                  "on the metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on " \
                  "your head and eats you."

            return "death"

        elif "scream" in action:
            print "Your screaming disorients the Gothon. With renewed confidence, you run up to him. You are so " \
                  "focused on it that you don't notice the body of your crewmate on the floor. You trip over their " \
                  "body and slam into the Gothon. Annoyed, it throws you off, jumps on you, and starts eating your "\
                  "face off."

            return "death"

        elif "beg" in action:
            print "You beg for your life like no one ever has before. The Gothon walks up to you, stares into your " \
                  "eyes and screams. It grabs you by your throat and throws you against the wall. It then starts " \
                  "feasting on you."

            return "death"

        elif "play dead" in action:
            print "You drop immediately on the floor and pretend to be dead. The Gothon walks up to you and kicks " \
                  "you. Thankfully you took acting lessons last week while everyone else was taking survival " \
                  "lessons so you are an expert actor and the Gothon believes you are dead so it leaves . " \
                  "You decied to wait a minute or two before moving in case it comes back. Not 30 seconds later, the " \
                  "door opens again. Good thing you didn't move! Except...he brought other Gothons back. Apparently " \
                  "you are their dinner!"

            return "death"

        elif "joke" in action:
            print "Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke " \
                  "you know: Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The " \
                  "Gothon stops, tries not to laugh, then busts out laughing and can't move. While he's laughing " \
                  "you run up and shoot him square in the head putting him down, then jump through the Weapon " \
                  "Armory door."

            return "laser_weapon_armory"

        else:
            print "Just as you are about to {action}, you black out. You forgot to eat for the past few days! You " \
                  "wake up just as the Gothons are about to start feasting on you.".format(action=action)

            return "death"


class LaserWeaponArmory(Scene):

    KEYPAD_PROMPT = "[keypad]> "

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might " \
              "be hiding. It's dead quiet, too quiet. You stand up and run to the far side of the room and find the " \
              "neutron bomb in its container. There's a keypad lock on the box and you need the code to get the " \
              "bomb out. If you get the code wrong 10 times then the lock closes forever and you can't get the " \
              "bomb. The code is 3 digits."

        code = "{0}{1}{2}".format(randint(0, 9), randint(0, 9), randint(0, 9))
        code = int(code)

        guess = raw_input(self.KEYPAD_PROMPT)

        locked = True

        guesses = 0
        while locked and guesses < 10:
            if "cheat" in guess:
                break

            not_num = True
            while not_num:
                try:
                    guess = int(guess)
                except ValueError:
                    print "That's not a number! Try again"
                    guess = raw_input(self.KEYPAD_PROMPT)
                else:
                    not_num = False

            guesses += 1

            if guess == code:
                locked = False

            elif guess > code:
                print "BZZZZZEDDD!" \
                      "\n" \
                      "Hmm...that feels too high."

                guess = raw_input(self.KEYPAD_PROMPT)

            elif guess < code:
                print "BZZZZZEDDD!" \
                      "\n" \
                      "Hmm...that feels too low."

                guess = raw_input(self.KEYPAD_PROMPT)

        if not locked:
            print "The container clicks open and the seal breaks, letting gas out. You grab the neutron bomb and " \
                  "run as fast as you can to the bridge where you must place it in the right spot."

            return "the_bridge"

        else:
            print "The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is " \
                  "fused together. You decide to sit there, and finally the Gothons blow up the ship from their " \
                  "ship and you die."

            return "death"


class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the netron destruct bomb under your arm and surprise 5 Gothons who " \
              "are trying to take control of the ship. Each of them has an even uglier clown costume than the last. " \
              "They haven't pulled their weapons out yet, as they see the active bomb under your arm and don't want " \
              "to set it off."

        action = raw_input(prompt)

        if "throw" in action:
            print "In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as " \
                  "you drop it a Gothon shoots you right in the back killing you. As you die you see another Gothon " \
                  "frantically try to disarm the bomb. You die knowing they will probably blow up when it goes off."

            return "death"

        elif "place" in action:
            print "You point your blaster at the bomb under your arm and the Gothons put their hands up and start " \
                  "to sweat. You inch backward to the door, open it, and then carefully place the bomb on the floor, " \
                  "pointing your blaster at it. You then jump back through the door, punch the close button " \
                  "and blast the lock so the Gothons can't get out. Now that the bomb is placed you run to the " \
                  "escape pod to get off this tin can."

            return "escape_pod"

        else:
            print "You start to {action}, but you drop the bomb. As soon as it hits the floor, it goes off. You look " \
                  "up and see the Gothons' terrified faces as you are engulfed in the blast."

            return "death"


class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to the escape pod before the whole ship " \
              "explodes. It seems like hardly any Gothons are on the ship, so your run is clear of interference. " \
              "You get to the chamber with the escape pods, and now need to pick one to take. Some of them could " \
              "be damaged but you don't have time to look. There's 5 pods, which one do you take?"

        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")

        not_num = True
        while not_num:
            if "cheat" in guess:
                break

            try:
                guess = int(guess)
            except ValueError:
                print "That's not a number! Try again"
                guess = raw_input("[pod #]> ")
            else:
                not_num = False

        if "cheat" in guess or guess == good_pod:
            print "You jump into pod %s and hit the eject button. The pod easily slides out into space heading to " \
                  "the planet below. As it flies to the planet, you look back and see your ship implode then " \
                  "explode like a bright star, taking out the Gothon ship at the same time. You won!"

            return "finished"

        else:
            print "You jump into pod {num} and hit the eject button. The pod escapes out into the void of space, " \
                  "then implodes as the hull ruptures, crushing your body into jam jelly.".format(num=guess)

            return "death"


class Finished(Scene):

    def enter(self):
        print "You won! Good job."

        exit()


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
