import tkinter as tk
from tkinter import messagebox
import random
import time

# templates of words for the typing test
templates = [
    ["cat", "dog", "sky", "book", "table", "apple", "happy", "mouse", "chair", "quick",
     "light", "power", "smile", "truck", "grape", "clock", "brush", "cloud", "ocean", "dance",
     "bread", "dream", "stone", "green", "house", "tiger", "music", "storm", "world", "radio",
     "tree", "fire", "moon", "laugh", "phone", "river", "sugar", "paint", "snake", "pencil",
     "island", "button", "coffee", "flower", "orange", "shadow", "camera", "window", "pillow",
     "basket", "desert", "beauty", "soccer", "jacket", "energy", "forest", "writer", "wizard",
     "lemon", "mirror", "market", "planet", "action", "dollar", "rocket", "galaxy", "garden",
     "candle", "silver", "paper", "needle", "carpet", "butter", "dinner", "magic", "engine",
     "animal", "bottle", "magnet", "blanket", "ticket", "helmet", "handle", "anchor", "puzzle",
     "number", "ladder", "driver", "cookie", "hammer", "castle", "dragon", "painter", "mirror",
     "window", "camera", "storm", "engine", "castle", "forest", "market", "jacket", "soccer",
     "blanket", "candle", "rock", "shield", "marker", "river", "smile", "ocean", "flower",
     "planet", "wizard", "energy", "market", "painter", "basket", "ticket", "puzzle", "carpet",
     "candle", "silver", "anchor", "window", "lemon", "action", "beauty", "pillow", "button",
     "planet", "dragon", "galaxy", "rocket", "shadow", "butter", "cloud", "dinner", "puzzle",
     "helmet", "ladder", "soccer", "mirror", "blanket", "anchor", "ticket", "bottle", "driver",
     "market", "camera", "engine", "castle", "forest", "rock", "shield", "rocket", "marker",
     "river", "smile", "ocean", "lemon", "mirror", "planet", "wizard", "rock", "ticket",
     "driver", "rocket", "basket", "blanket", "ticket", "flower", "garden", "shadow", "butter",
     "cloud", "candle", "carpet", "button", "market", "planet", "wizard", "storm", "soccer",
     "camera", "planet", "mirror", "rock", "cloud", "castle", "energy", "button", "driver",
     "ticket", "rocket", "soccer", "jacket", "basket", "blanket", "candle", "storm", "castle",
     "planet", "energy", "cloud", "wizard", "garden", "flower", "mirror", "ticket", "button",
     "rock", "planet", "anchor", "shield", "cloud", "rocket", "soccer", "energy", "blanket",
     "wizard", "storm", "driver", "garden", "ladder", "camera", "soccer", "planet", "forest",
     "basket", "ticket", "engine", "market", "puzzle", "rocket", "mirror", "lemon", "flower",
     "painter", "planet", "cloud", "rock", "anchor", "candle", "jacket", "wizard", "camera",
     "ticket", "storm", "planet", "rock", "carpet", "basket", "puzzle", "soccer", "planet",
     "driver", "mirror", "planet", "rocket", "soccer", "blanket", "cloud", "anchor", "market",
     "ticket", "mirror", "storm", "carpet", "soccer", "rock", "painter", "planet", "forest",
     "basket", "energy", "pillow", "camera", "ticket", "cloud", "garden", "planet", "mirror",
     "basket", "planet", "ladder", "wizard", "storm", "flower", "mirror", "cloud", "market",
     "basket", "ticket", "planet", "blanket", "candle", "wizard", "rock", "cloud", "soccer",
     "planet", "storm", "painter", "rock", "candle", "anchor", "pillow", "basket", "blanket",
     "planet", "wizard", "ladder", "cloud", "camera", "storm", "planet", "rock", "cloud",
     "basket", "ticket", "wizard", "planet", "carpet", "basket", "ladder", "soccer", "rocket"],  # template 1
#########
    ["zebra", "ghost", "light", "apple", "beach", "straw", "mountain", "pencil", "yacht", "violin",
     "breeze", "quartz", "camera", "kiwi", "grape", "tulip", "vortex", "eagle", "forest", "garden",
     "python", "safari", "cloud", "galaxy", "radio", "flame", "shadow", "island", "button", "castle",
     "oyster", "whale", "carpet", "cookie", "engine", "whisk", "lemon", "snow", "donkey", "paper",
     "river", "puzzle", "window", "parrot", "rabbit", "kiwi", "soccer", "violet", "planet", "cloud",
     "elephant", "ticket", "rocket", "pillow", "wizard", "cactus", "zipper", "panda", "tractor", "crown",
     "lion", "peach", "bridge", "laser", "flask", "pebble", "butter", "quill", "honey", "pencil",
     "coffee", "dollar", "smile", "flute", "jungle", "parade", "skate", "orange", "butterfly", "castle",
     "jacket", "gold", "falcon", "school", "light", "stone", "train", "painter", "cloud", "turkey",
     "lamp", "banana", "glove", "pearl", "shadow", "ring", "apple", "river", "storm", "spider",
     "bicycle", "spoon", "fire", "balloon", "canoe", "quilt", "button", "anchor", "snow", "basketball",
     "camera", "hammer", "sweater", "blanket", "torch", "onion", "ladder", "drum", "potato", "soccer",
     "crystal", "grill", "planet", "mirror", "thumb", "lantern", "pencil", "clown", "rocket", "spider",
     "whistle", "pillow", "monkey", "globe", "ocean", "window", "tiger", "market", "motor", "castle",
     "river", "fork", "table", "bottle", "snowflake", "clover", "wallet", "flower", "key", "moon",
     "balloon", "zipper", "robot", "rocket", "cliff", "sheep", "peach", "flamingo", "soccer", "clock",
     "pencil", "kangaroo", "guitar", "quartz", "mirror", "river", "garden", "ladder", "spade", "tomato",
     "bridge", "camera", "magnet", "kiwi", "ball", "pepper", "fire", "basket", "piano", "mountain",
     "paper", "giraffe", "quilt", "mirror", "dollar", "planet", "engine", "snow", "flower", "crab",
     "castle", "volcano", "hat", "snowman", "wizard", "leopard", "strawberry", "fork", "river",
     "train", "drum", "soccer", "cloud", "camera", "pillow", "soccer", "chair", "sunset", "rocket",
     "bridge", "cookie", "sunshine", "engine", "forest", "garden", "flute", "spider", "fire", "mirror",
     "pebble", "flower", "storm", "hat", "garden", "bicycle", "banana", "drum", "snowflake", "paint",
     "parrot", "lizard", "kettle", "planet", "ferry", "apple", "wizard", "lemon", "rain", "boat",
     "garden", "rocket", "camera", "snowman", "planet", "tractor", "moon", "candle", "lighthouse",
     "rocket", "fire", "volcano", "sunset", "snow", "shadow", "butter", "wind", "stone", "mirror",
     "crown", "stream", "keyboard", "garden", "elephant", "quill", "laptop", "spider", "moon", "pillow",
     "castle", "banana", "trumpet", "fire", "rose", "skate", "guitar", "planet", "train", "coin",
     "ribbon", "snowman", "glove", "basket", "butterfly", "pebble", "tiger", "lemon", "pillow",
     "planet", "rainbow", "drum", "paint", "spider", "castle", "moon", "sunset", "soccer", "basket",
     "window", "quartz", "mirror", "rocket", "flower", "planet", "cloud", "storm", "engine", "fire",
     "garden", "window", "breeze", "train", "river", "spider", "pencil", "button", "rocket", "planet"],  # template 2
########
    ["sword", "jelly", "towel", "fox", "umbrella", "skull", "eagle", "cave", "lioness", "rope",
     "beetle", "cherry", "hedgehog", "scooter", "kite", "tent", "bush", "fern", "compass", "tiger",
     "cloudy", "avocado", "helicopter", "vase", "leaf", "sketch", "blossom", "gate", "waterfall",
     "plum", "hatchet", "drizzle", "fountain", "dolphin", "swim", "goggles", "helmet", "jeep",
     "broom", "starfish", "kangaroo", "lantern", "mango", "mist", "beacon", "diamond", "foxglove",
     "plough", "steamboat", "swallow", "unicorn", "velvet", "creek", "tractor", "violin", "nest",
     "napkin", "whisker", "lily", "mushroom", "mirrorball", "beehive", "iguana", "bubble", "bonsai",
     "chisel", "marble", "postcard", "vine", "owl", "yarn", "hammerhead", "tigerlily", "cork",
     "raccoon", "marathon", "reptile", "galleon", "ant", "bulldozer", "lichen", "piano", "keychain",
     "spine", "dagger", "mule", "iris", "macaroni", "whirlpool", "wrinkle", "zucchini", "iceberg",
     "jigsaw", "tricycle", "heather", "canoe", "binoculars", "torchlight", "alligator", "wolf",
     "iguana", "badge", "dice", "tornado", "tractor", "clay", "tarantula", "dart", "iguana", "lighthouse",
     "pineapple", "parasol", "stingray", "toucan", "apricot", "chasm", "gem", "blossom", "vulture",
     "wagon", "zipper", "trumpet", "beehive", "volleyball", "reindeer", "moth", "haystack", "beaker",
     "cauldron", "albatross", "pelican", "bison", "airship", "dock", "harp", "net", "rug", "strawberry",
     "treetop", "vineyard", "lantern", "seed", "wings", "hedge", "cuckoo", "harmonica", "easel", "lizard",
     "otter", "lobster", "gravy", "reef", "ice", "spoonful", "cliffside", "quartz", "peacock", "badger",
     "diary", "soap", "sundial", "tray", "sail", "thunder", "axle", "icecream", "yoke", "seedling",
     "wig", "ladle", "motorcycle", "raven", "orchid", "sunbeam", "badminton", "coat", "blender",
     "grapefruit", "seal", "banjo", "freckle", "chimney", "hatchet", "antelope", "sunflower", "melon",
     "trolley", "stadium", "ember", "jackal", "spindle", "nail", "ivory", "blacksmith", "tarpon",
     "pelican", "shrimp", "strudel", "cinnamon", "pot", "garland", "reed", "flipper", "clam",
     "postcard", "seaweed", "plough", "tuna", "clocktower", "partridge", "hive", "longboat",
     "willow", "cotton", "maple", "pebble", "dune", "panther", "mustard", "wildcat", "autumn",
     "bell", "thermos", "drill", "parchment", "thistle", "acorn", "thyme", "horizon", "zipline",
     "guitar", "puffin", "dahlia", "toolbox", "bass", "nugget", "root", "shears", "peppercorn",
     "beard", "sled", "gnome", "daisy", "birch", "tentacle", "windmill", "parka", "kiwifruit",
     "footbridge", "chimera", "driftwood", "koala", "crater", "newt", "mongoose", "cedar",
     "leech", "cartwheel", "bamboo", "glacier", "bronco", "plover", "helmet", "radish", "clover",
     "seagull", "canvas", "pickaxe", "manta", "swirl", "papaya", "carousel", "spiderweb",
     "toucan", "ivy", "ginger", "cricket", "pod", "ribbon", "amethyst", "camper", "icicle",
     "milestone", "stoat", "twilight", "geyser", "flint", "turnip", "yeti", "peppermint",
     "lichen", "sparrow", "coral", "limestone", "copper", "whale", "mangrove", "popcorn",
     "robin", "coral", "hummingbird", "sunlight", "baboon", "slug", "spark", "raindrop",
     "icicle", "wing", "forestfire", "moss", "basil", "marigold", "meadow", "spade",
     "seashell", "puffball", "shore", "orchid", "harbor", "gull", "lily", "seaweed",
     "kelp", "seaplane", "reed", "scallop", "goldfinch", "sunrise", "woodpecker", "froth"],  # template 3
########
    ["arrow", "bacon", "carrot", "denim", "easel", "fiddle", "grill", "hammock", "ink", "jar",
     "keypad", "laptop", "mittens", "notebook", "owl", "pancake", "quiver", "raft", "snowball",
     "torch", "urchin", "vacuum", "whip", "xylophone", "yogurt", "zeppelin", "armadillo", "barn",
     "chimney", "door", "engine", "fountain", "grapevine", "hay", "iron", "jug", "kettle", "ladder",
     "mantle", "nail", "oak", "peach", "quilt", "rope", "sailboat", "tank", "umbrella", "van",
     "wheel", "xylophone", "yacht", "zipper", "alarm", "bicycle", "cupboard", "dock", "eraser",
     "fossil", "globe", "hose", "ice", "jug", "kale", "leaf", "mug", "nectar", "oven", "pasta",
     "quicksand", "rose", "sugar", "tractor", "umbrella", "vinegar", "window", "axe", "bench",
     "cactus", "dove", "emu", "flamingo", "guitar", "helicopter", "ivory", "joker", "kite",
     "lantern", "magnet", "net", "onion", "paint", "quilt", "reel", "sock", "tent", "utensil",
     "vulture", "wagon", "yarn", "zeppelin", "arch", "box", "clamp", "dolphin", "egg", "fox",
     "gorilla", "honey", "inkwell", "jackal", "kangaroo", "ladle", "magpie", "nest", "orange",
     "porcupine", "quartz", "racquet", "scissors", "thorn", "underwear", "vacation", "wolf",
     "yolk", "zenith", "anvil", "beehive", "creek", "dust", "eagle", "frog", "gravy", "hat",
     "ivy", "jewel", "knot", "lily", "minnow", "noose", "oyster", "plank", "quill", "rabbit",
     "sand", "top", "umbrella", "vial", "whisker", "xylophone", "yo-yo", "zephyr", "ant",
     "bird", "crate", "doll", "eel", "feather", "goblet", "horn", "iceberg", "jug", "knapsack",
     "lamp", "map", "net", "oar", "peg", "quote", "river", "seed", "twig", "urchin", "vine",
     "wasp", "xenon", "yam", "zebra", "anchor", "barrel", "cliff", "dagger", "earth", "fire",
     "grain", "hoop", "ink", "jet", "knife", "lizard", "moon", "newt", "owl", "pit", "quail",
     "rain", "stone", "toad", "urn", "viper", "worm", "x-ray", "year", "zoo", "avocado",
     "bat", "cobweb", "dune", "eggplant", "fig", "garlic", "hammer", "ice", "jar", "kite",
     "leaf", "melon", "night", "orange", "pie", "quiver", "rope", "salt", "tree", "up",
     "vase", "wall", "xylophone", "yeti", "zigzag", "airplane", "brick", "crate", "duck",
     "elbow", "fern", "garden", "hen", "island", "jug", "kale", "ladle", "mask", "nut",
     "onion", "pitcher", "quote", "reed", "shell", "tail", "urn", "volcano", "wheel",
     "xenon", "yarn", "zip", "anemone", "bead", "chain", "dime", "eraser", "fish", "glove",
     "hook", "ink", "jar", "kite", "lemon", "mango", "net", "owl", "parrot", "quicksilver",
     "rope", "shield", "tailor", "utensil", "vase", "wheel", "x-ray", "yolk", "zipper",
     "apron", "bucket", "cup", "drill", "elephant", "frog", "giant", "harp", "island",
     "jelly", "key", "lawn", "match", "needle", "orchard", "pebble", "quill", "raft",
     "sword", "trap", "umbrella", "violet", "whale", "xylophone", "yoyo", "zeppelin"],  # template 4
#######
    ["abacus", "backpack", "candle", "daisy", "eclipse", "fiddle", "goblin", "hazelnut", "igloo", "jigsaw",
     "kitchen", "lantern", "mango", "nectar", "octopus", "pyramid", "quicksand", "raincoat", "satellite",
     "teapot", "umbrella", "vortex", "watermelon", "xylophone", "yellow", "zucchini", "almond", "banana",
     "catfish", "dartboard", "elephant", "firefly", "grapefruit", "horizon", "insect", "jellyfish", "koala",
     "lobster", "mushroom", "nectarine", "ostrich", "pebble", "quail", "rosebud", "sail", "tornado",
     "underwater", "violet", "walnut", "yacht", "zebra", "amethyst", "broomstick", "crane", "dandelion",
     "emerald", "feather", "gondola", "hummingbird", "ivy", "jackal", "kettle", "lighthouse", "motorboat",
     "napkin", "orchid", "penguin", "quicksilver", "raven", "saxophone", "telephone", "uranium", "vanilla",
     "wave", "xylophone", "yoyo", "zeppelin", "arctic", "blueberry", "caramel", "doughnut", "elephant",
     "fireplace", "glacier", "honeycomb", "indigo", "jacket", "kite", "lotus", "mistletoe", "navy", "olive",
     "peacock", "quartz", "rainbow", "sandcastle", "tulip", "umpire", "viper", "whirlpool", "xylophone",
     "yarn", "zephyr", "antler", "balloon", "compass", "drumstick", "espresso", "fern", "gorilla", "hammock",
     "icicle", "jet", "knight", "lava", "moose", "noodle", "orange", "penny", "quiver", "riverbank", "scarecrow",
     "train", "umbrella", "volcano", "weasel", "xenon", "yew", "zucchini", "archer", "bonfire", "clover",
     "dragonfly", "ember", "foxglove", "goblet", "hedgehog", "iceberg", "jeep", "koi", "log", "muffin", "nutmeg",
     "oak", "plankton", "quasar", "rock", "sandstone", "trumpet", "urchin", "vulture", "woodpecker", "xenon",
     "yo-yo", "zenith", "albatross", "butterfly", "cocoon", "dewdrop", "eggplant", "fossil", "gazelle", "heron",
     "iguana", "joker", "kangaroo", "leopard", "mountain", "nettle", "ox", "parakeet", "quagmire", "rattlesnake",
     "sailboat", "thorn", "ulcer", "vineyard", "willow", "xylophone", "yogurt", "zipline", "anchor", "beetle",
     "coral", "donut", "elm", "fiddlehead", "goose", "hornet", "igloo", "jalapeno", "koala", "lightning",
     "mulberry", "nightshade", "owl", "palm", "quokka", "rhinoceros", "spatula", "toadstool", "upholstery",
     "vine", "wasp", "xenon", "yeti", "zircon", "apple", "bridge", "crow", "dolphin", "eleven", "falcon", "gecko",
     "hermit", "iris", "jump", "kangaroo", "lobster", "moth", "nebula", "opal", "piano", "quartz", "raindrop",
     "starfish", "tiger", "ultraviolet", "vine", "waterfall", "xerox", "yawn", "zeppelin", "ant", "birch",
     "clam", "diamond", "egg", "frog", "guitar", "hippopotamus", "icicle", "jungle", "koala", "lion", "moon",
     "nest", "otter", "pumpkin", "quartz", "rock", "seagull", "turtle", "umbrella", "violin", "wolf", "xylophone",
     "yellow", "zebra", "acorn", "blizzard", "carrot", "dragon", "eel", "fiddle", "geode", "hibiscus", "iguana",
     "joker", "kangaroo", "lily", "mango", "nectar", "osprey", "pinecone", "quail", "raccoon", "swan", "tree",
     "unicorn", "velvet", "walrus", "xylophone", "yogurt", "zephyr", "ankle", "bison", "crystal", "driftwood",
     "egg", "fire", "giant", "honey", "ice", "jar", "kiwi", "lamb", "moose", "nebula", "olive", "pencil",
     "quartz", "rattlesnake", "shell", "tulip", "umbrella", "volcano", "wombat", "xenon", "yak", "zebra"]
    ,  # template 5
]


# number of words to display at a time (3 lines of words)
WORDS_TO_DISPLAY = 15
words_index = 0  # to keep track of word positions

# function to calculate typing speed
def calculate_speed():
    global end_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time / 60
    correct_count = len(typed_word_history)

    wpm = correct_count / elapsed_minutes
    typing_input.unbind("<space>")  # Unbind the spacebar to prevent further input
    messagebox.showinfo("Result", f"Typing Speed: {wpm:.2f} WPM")
    start_button.config(state=tk.NORMAL)  # enable the start button again after test

# function to update the timer
def update_timer(seconds_left):
    if seconds_left > 0:
        timer_label.config(text=f"Time left: {seconds_left}s")
        root.after(1000, update_timer, seconds_left - 1)  # update every second
    else:
        calculate_speed()

# function to display the next set of words
def display_words():
    test_text.config(state=tk.NORMAL)
    test_text.delete("1.0", tk.END)
    test_text.insert(tk.END, " ".join(current_words))  # display the current set of words
    test_text.config(state=tk.DISABLED)

# function to flash the correct or incorrect word for 1 second before removing it
def flash_word(typed_word, word_start_index, word_end_index):
    global current_word

    if typed_word == current_word:  # correct word
        test_text.tag_add("correct", word_start_index, word_end_index)
        test_text.tag_config("correct", background="lime")  # highlight correct word in neon green
        typed_word_history.append(current_word)  # store the correct word
    else:  # incorrect word
        test_text.tag_add("incorrect", word_start_index, word_end_index)
        test_text.tag_config("incorrect", background="red")  # highlight incorrect word in red

    # Wait for 1 second before removing the word and updating the list
    root.after(1000, remove_typed_word)

# function to remove the typed word after flashing and display the next word
def remove_typed_word():
    global words_index, current_word
    current_words.pop(0)  # remove the first word (the one just typed)
    next_word = random.choice(random_template)  # select the next random word
    current_words.append(next_word)  # append it to the end to keep 15 words displayed
    current_word = current_words[0]  # update the current word to the new first word

    # Reset the words_index to highlight the next word correctly
    words_index = 0
    display_words()  # update the displayed words

# function to check the typed word and flash the correct/incorrect word for 1 second
def check_word(event):
    global words_index, current_word
    typed_word = typing_input.get().strip()  # get the word typed by the user
    typing_input.delete(0, tk.END)  # clear the input box for the next word

    # Get the index for where to apply the tag (highlight)
    word_start_index = f"1.{words_index}"
    word_end_index = f"1.{words_index + len(current_word)}"

    # Flash the word with red or green for 1 second
    flash_word(typed_word, word_start_index, word_end_index)

# function to start the test
def start_test():
    global start_time, random_template, typed_word_history, current_words, current_word, words_index
    start_time = time.time()

    random_template = random.choice(templates)  # randomly choose a word template
    typed_word_history = []  # to track correct words typed by the user

    current_words = random.sample(random_template, WORDS_TO_DISPLAY)  # randomly pick 15 words
    current_word = current_words[0]  # set the first word to type
    words_index = 0  # reset word index for highlighting

    start_button.config(state=tk.DISABLED)
    display_words()  # display the first set of words
    typing_input.focus_set()  # set focus to the typing input box
    typing_input.bind("<space>", check_word)  # bind spacebar to check word
    update_timer(60)  # start the 60-second countdown

# setting up the tkinter window
root = tk.Tk()
root.geometry("1152x648")
root.title("Speed Typing App")

# defining the color theme
root.configure(bg="#FFFACD")  # light yellow color

# text area for displaying the word template
test_text = tk.Text(root, height=5, width=90, bg="blue", fg="white", font=("Helvetica", 16))
test_text.pack(pady=20)
test_text.config(state=tk.DISABLED)

# entry widget for typing
typing_input = tk.Entry(root, width=30, bg="white", fg="black", font=("Helvetica", 24))
typing_input.pack(pady=20)

# start button
start_button = tk.Button(root, text="Start Test", command=start_test, bg="green", fg="white", font=("Helvetica", 16))
start_button.pack(pady=20)

# timer label to show the remaining time in purple
timer_label = tk.Label(root, text="Time left: 60s", bg="#FFFACD", fg="purple", font=("Helvetica", 16))
timer_label.pack(pady=10)

# run the tkinter main loop
root.mainloop()