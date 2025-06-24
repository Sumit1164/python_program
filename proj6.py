import random
def generate_story():
    subjects = ["A boy", "A girl", "A dog", "A cat", "An alien"]
    verbs = ["found", "lost", "saw", "met", "helped"]
    objects = ["a treasure", "a friend", "a mysterious object", "a monster", "a spaceship"]
    places = ["in the forest", "on the beach", "in the city", "in space", "in a haunted house"]

    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object_ = random.choice(objects)
    place = random.choice(places)

    story = f"{subject} {verb} {object_} {place}."
    return story
if __name__ == "__main__":
    print("Welcome to the Story Teller!")
    print("Here is your story:")
    print(generate_story())